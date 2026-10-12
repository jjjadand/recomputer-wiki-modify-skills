#!/usr/bin/env python3
"""Audit Seeed Jetson reComputer MD/MDX pages for shared-template invariants."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


DOC_SUFFIXES = {".md", ".mdx"}
FRONTMATTER_RE = re.compile(r"^---\r?\n(.*?)\r?\n---(?:\r?\n|$)", re.S)
FIELD_RE_TEMPLATE = r"^{field}:\s*(.+?)\s*$"
IMAGE_RE = re.compile(r"<img\b([^>]*)>", re.I | re.S)
LINK_RE = re.compile(r"<a\b([^>]*)>", re.I | re.S)
ATTR_RE_TEMPLATE = r"\b{name}\s*=\s*([\"'])(.*?)\1"
PLACEHOLDER_RE = re.compile(r"\{\{[A-Z0-9_]+\}\}")


@dataclass
class Finding:
    severity: str
    path: str
    line: int
    message: str


def line_of(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def attr(fragment: str, name: str) -> str | None:
    match = re.search(ATTR_RE_TEMPLATE.format(name=re.escape(name)), fragment, re.I | re.S)
    return match.group(2).strip() if match else None


def frontmatter_value(frontmatter: str, field: str) -> str | None:
    match = re.search(FIELD_RE_TEMPLATE.format(field=re.escape(field)), frontmatter, re.M)
    if not match:
        return None
    return match.group(1).strip().strip("\"'")


def collect_docs(inputs: Iterable[str]) -> list[Path]:
    docs: set[Path] = set()
    for raw in inputs:
        path = Path(raw).resolve()
        if not path.exists():
            raise FileNotFoundError(raw)
        if path.is_file():
            if path.suffix.lower() in DOC_SUFFIXES:
                docs.add(path)
        else:
            docs.update(
                candidate.resolve()
                for candidate in path.rglob("*")
                if candidate.is_file()
                and candidate.suffix.lower() in DOC_SUFFIXES
                and "_bk" not in candidate.stem
            )
    return sorted(docs)


def audit_doc(path: Path) -> tuple[list[Finding], str | None]:
    text = path.read_text(encoding="utf-8", errors="replace")
    display_path = str(path)
    findings: list[Finding] = []

    def add(severity: str, message: str, offset: int = 0) -> None:
        findings.append(Finding(severity, display_path, line_of(text, offset), message))

    frontmatter_match = FRONTMATTER_RE.match(text)
    if not frontmatter_match:
        add("error", "Missing or malformed YAML frontmatter.")
        return findings, None

    frontmatter = frontmatter_match.group(1)
    required = ("description", "title", "image", "slug", "last_update", "createdAt", "updatedAt", "url")
    for field in required:
        if not re.search(rf"^{re.escape(field)}:\s*", frontmatter, re.M):
            add("warning", f"Frontmatter is missing `{field}`.")

    slug = frontmatter_value(frontmatter, "slug")
    url = frontmatter_value(frontmatter, "url")
    if slug:
        if not slug.startswith("/jetson/recomputer_"):
            add("warning", "Canonical slug does not use the `/jetson/recomputer_<family>/...` namespace.")
        expected_url = "https://wiki.seeedstudio.com" + slug.rstrip("/") + "/"
        if url and url != expected_url:
            add("error", f"Frontmatter URL does not match slug; expected `{expected_url}`.")

    placeholder = PLACEHOLDER_RE.search(text)
    if placeholder:
        add("error", f"Unresolved template token `{placeholder.group(0)}`.", placeholder.start())

    class_match = re.search(r"\bclass=(?:[\"']|\{)", text)
    if class_match:
        add("warning", "Use `className` instead of `class` in MDX/JSX.", class_match.start())

    if "JetsonProductDocNav" not in text:
        add("warning", "Shared `JetsonProductDocNav` is not used.")
    if "@site/src/data/jetson/productDocNavigation" not in text:
        add("warning", "Family navigation is not imported from the centralized data file.")

    for match in IMAGE_RE.finditer(text):
        image_alt = attr(match.group(1), "alt")
        if image_alt is None:
            add("warning", "Image is missing an `alt` attribute.", match.start())
        elif image_alt.strip().lower() in {"", "image", "img", "photo", "picture"}:
            add("warning", "Image alt text is empty or generic.", match.start())

    for match in LINK_RE.finditer(text):
        attributes = match.group(1)
        href = attr(attributes, "href") or ""
        external = href.startswith(("http://", "https://", "//"))
        if external and attr(attributes, "target") == "_blank":
            rel = attr(attributes, "rel") or ""
            rel_tokens = set(rel.split())
            if not {"noopener", "noreferrer"}.issubset(rel_tokens):
                add("warning", "External `_blank` link should use `rel=\"noopener noreferrer\"`.", match.start())

    title = frontmatter_value(frontmatter, "title") or ""
    getting_started = "getting started" in title.lower() or "getting_start" in path.stem.lower()
    if getting_started:
        if 'className="jetson-product-page"' not in text:
            add("error", "Getting Started page is missing the `jetson-product-page` wrapper.")
        class_requirements = {
            "jetson-product-hero": "product hero",
            "jetson-product-fact-grid": "fact grid",
            "jetson-product-feature-grid": "feature grid",
            "jetson-product-table-wrap": "responsive specification table",
            "jetson-product-hardware-gallery": "hardware gallery",
            "jetson-product-step-flow": "numbered flash workflow",
            "jetson-product-application-grid": "application collection",
            "jetson-product-resource-grid": "resource collection",
        }
        for class_name, label in class_requirements.items():
            if class_name not in text:
                add("warning", f"Getting Started page is missing the shared {label} (`{class_name}`).")

        required_headings = (
            "Specifications",
            "Hardware Overview",
            "Flash JetPack",
            "Applications",
            "Resources",
            "Tech Support & Product Discussion",
        )
        for heading in required_headings:
            if not re.search(rf"^##\s+{re.escape(heading)}\s*$", text, re.M | re.I):
                add("warning", f"Getting Started page is missing the `{heading}` section.")

        covers = re.findall(
            r'<a\s+className="jetson-product-application-cover"\s+href="([^"]+)"', text
        )
        titles = re.findall(r"<h3>\s*<a\s+href=\"([^\"]+)\"", text)
        if covers and titles and covers != titles:
            add("error", "Application cover and title routes are inconsistent.")

    return findings, slug


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", help="Markdown files or product-family directories")
    parser.add_argument("--strict", action="store_true", help="Return non-zero when warnings exist")
    parser.add_argument("--json", action="store_true", dest="as_json", help="Emit JSON")
    args = parser.parse_args()

    try:
        docs = collect_docs(args.paths)
    except FileNotFoundError as exc:
        print(f"error: path does not exist: {exc}", file=sys.stderr)
        return 2

    if not docs:
        print("error: no Markdown or MDX documents found", file=sys.stderr)
        return 2

    findings: list[Finding] = []
    slugs: dict[str, Path] = {}
    for doc in docs:
        doc_findings, slug = audit_doc(doc)
        findings.extend(doc_findings)
        if slug:
            if slug in slugs:
                findings.append(
                    Finding("error", str(doc), 1, f"Duplicate slug also used by `{slugs[slug]}`: `{slug}`.")
                )
            else:
                slugs[slug] = doc

    counts = {
        "documents": len(docs),
        "errors": sum(item.severity == "error" for item in findings),
        "warnings": sum(item.severity == "warning" for item in findings),
    }

    if args.as_json:
        print(json.dumps({"summary": counts, "findings": [asdict(item) for item in findings]}, indent=2))
    else:
        for item in findings:
            print(f"{item.severity.upper():7} {item.path}:{item.line} {item.message}")
        print(
            f"Audited {counts['documents']} document(s): "
            f"{counts['errors']} error(s), {counts['warnings']} warning(s)."
        )

    if counts["errors"] or (args.strict and counts["warnings"]):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

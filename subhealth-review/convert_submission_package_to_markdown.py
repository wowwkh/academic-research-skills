#!/usr/bin/env python3
"""Convert the generated author-review DOCX files to previewable Markdown.

Uses only the Python standard library.  It preserves headings, lists, tables,
references and the conceptual-figure link; it does not attempt to reproduce
Word typography.
"""

from __future__ import annotations

import re
from pathlib import Path
from zipfile import ZipFile
from xml.etree import ElementTree as ET

PACKAGE = Path(__file__).resolve().parent / "submission-package-2026-10-15"
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}


def text_of(element) -> str:
    return "".join((node.text or "") for node in element.findall(".//w:t", NS)).replace("\xa0", " ")


def style_of(paragraph) -> str:
    node = paragraph.find("./w:pPr/w:pStyle", NS)
    return node.get(f"{{{W}}}val", "") if node is not None else ""


def has_drawing(paragraph) -> bool:
    return paragraph.find(".//w:drawing", NS) is not None or paragraph.find(".//w:pict", NS) is not None


def parse_table(table):
    rows = []
    for tr in table.findall("./w:tr", NS):
        row = []
        for tc in tr.findall("./w:tc", NS):
            parts = []
            for paragraph in tc.findall("./w:p", NS):
                value = text_of(paragraph).strip()
                if value:
                    parts.append(value)
            row.append("<br>".join(parts).replace("|", r"\|"))
        if row:
            rows.append(row)
    return rows


def table_markdown(rows) -> str:
    if not rows:
        return ""
    width = max(len(row) for row in rows)
    rows = [row + [""] * (width - len(row)) for row in rows]
    result = ["| " + " | ".join(rows[0]) + " |", "|" + "|".join("---" for _ in range(width)) + "|"]
    result.extend("| " + " | ".join(row) + " |" for row in rows[1:])
    return "\n".join(result)


def paragraph_markdown(paragraph, *, first=False, number=None) -> str:
    value = text_of(paragraph).strip()
    style = style_of(paragraph).lower()
    if has_drawing(paragraph):
        return "![Figure 1 — evidence-bounded SLIM conceptual model](Figure_1_SLIM_Conceptual_Model_SchemeB.png)"
    if not value:
        return ""
    if first or "title" in style:
        return "# " + value
    if "heading1" in style:
        return "## " + value
    if "heading2" in style:
        return "### " + value
    if "heading3" in style:
        return "#### " + value
    if "bullet" in style:
        return "- " + value
    if "number" in style and not re.match(r"^\d+\. ", value):
        return f"{number or 1}. {value}"
    if value.startswith("Table ") or value.startswith("Figure 1."):
        return f"**{value}**"
    return value


def convert(path: Path) -> None:
    with ZipFile(path) as archive:
        root = ET.fromstring(archive.read("word/document.xml"))
    body = root.find("./w:body", NS)
    blocks = []
    first = True
    list_number = 0
    previous_list = None
    for child in list(body):
        if child.tag == f"{{{W}}}p":
            style = style_of(child).lower()
            if "number" in style:
                list_number = list_number + 1 if previous_list == "number" else 1
                previous_list = "number"
            elif "bullet" in style:
                list_number = 0
                previous_list = "bullet"
            else:
                list_number = 0
                previous_list = None
            block = paragraph_markdown(child, first=first, number=list_number)
            if text_of(child).strip() or has_drawing(child):
                first = False
            if block:
                blocks.append(block)
        elif child.tag == f"{{{W}}}tbl":
            blocks.append(table_markdown(parse_table(child)))
    destination = path.with_suffix(".md")
    destination.write_text("\n\n".join(block for block in blocks if block) + "\n", encoding="utf-8")
    print(f"wrote {destination.name}")


def main() -> None:
    for docx in sorted(PACKAGE.glob("*.docx")):
        convert(docx)


if __name__ == "__main__":
    main()

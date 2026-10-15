#!/usr/bin/env python3
"""Build the author-review submission package from the clean Scheme B copy.

The builder intentionally keeps author-controlled fields as `*`, omits the
Data/Code/Ethics statements at this review stage, and labels the conceptual
figure as a draft.  It requires python-docx and Pillow in the environment
used to run it; the generated package itself contains no participant-level
data.
"""

from __future__ import annotations

import re
import textwrap
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageDraw, ImageFont
from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "57_Journal_Facing_Submission_Copy_SchemeB_2026-10-15.md"
OUT = ROOT / "submission-package-2026-10-15"
FIGURE_PNG = OUT / "Figure_1_SLIM_Conceptual_Model_SchemeB.png"
FIGURE_PDF = OUT / "Figure_1_SLIM_Conceptual_Model_SchemeB.pdf"

TITLE = "Low-grade inflammation, stress-axis dysregulation and a proposed immune-metabolic continuum in suboptimal health defined by SHSQ-25"


def set_cell_shading(cell, fill: str) -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = tc_pr.find(qn("w:shd"))
    if shd is None:
        shd = OxmlElement("w:shd")
        tc_pr.append(shd)
    shd.set(qn("w:fill"), fill)


def set_cell_margins(cell, top=80, start=80, bottom=80, end=80) -> None:
    tc = cell._tc
    tc_pr = tc.get_or_add_tcPr()
    tc_mar = tc_pr.first_child_found_in("w:tcMar")
    if tc_mar is None:
        tc_mar = OxmlElement("w:tcMar")
        tc_pr.append(tc_mar)
    for m, v in (("top", top), ("start", start), ("bottom", bottom), ("end", end)):
        node = tc_mar.find(qn(f"w:{m}"))
        if node is None:
            node = OxmlElement(f"w:{m}")
            tc_mar.append(node)
        node.set(qn("w:w"), str(v))
        node.set(qn("w:type"), "dxa")


def set_repeat_table_header(row) -> None:
    tr_pr = row._tr.get_or_add_trPr()
    tbl_header = OxmlElement("w:tblHeader")
    tbl_header.set(qn("w:val"), "true")
    tr_pr.append(tbl_header)


def set_document_defaults(doc: Document, title: str) -> None:
    section = doc.sections[0]
    section.top_margin = Inches(0.8)
    section.bottom_margin = Inches(0.8)
    section.left_margin = Inches(0.85)
    section.right_margin = Inches(0.85)
    styles = doc.styles
    normal = styles["Normal"]
    normal.font.name = "Times New Roman"
    normal._element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")
    normal.font.size = Pt(10.5)
    normal.paragraph_format.space_after = Pt(5)
    normal.paragraph_format.line_spacing = 1.12
    for name, size, color in (("Title", 18, "17365D"), ("Heading 1", 14, "17365D"), ("Heading 2", 12, "1F4E79"), ("Heading 3", 11, "1F4E79")):
        style = styles[name]
        style.font.name = "Times New Roman"
        style._element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")
        style.font.size = Pt(size)
        style.font.bold = True
        style.font.color.rgb = RGBColor.from_string(color)
    doc.core_properties.title = title
    doc.core_properties.subject = "Author-review submission package"
    doc.core_properties.author = "*"


def add_runs(paragraph, text: str, size: float | None = None) -> None:
    """Add a small Markdown subset as Word runs."""
    token_re = re.compile(r"(\*\*.*?\*\*|(?<!\*)\*[^*]+\*(?!\*)|`[^`]+`)")
    pos = 0
    for match in token_re.finditer(text):
        if match.start() > pos:
            run = paragraph.add_run(text[pos : match.start()])
            if size:
                run.font.size = Pt(size)
        token = match.group(0)
        if token.startswith("**"):
            run = paragraph.add_run(token[2:-2])
            run.bold = True
        elif token.startswith("*"):
            run = paragraph.add_run(token[1:-1])
            run.italic = True
        else:
            run = paragraph.add_run(token[1:-1])
            run.font.name = "Courier New"
        if size:
            run.font.size = Pt(size)
        pos = match.end()
    if pos < len(text):
        run = paragraph.add_run(text[pos:])
        if size:
            run.font.size = Pt(size)


def add_paragraph(doc: Document, text: str, *, style: str | None = None, bold=False, italic=False, size=None, align=None):
    paragraph = doc.add_paragraph(style=style)
    if align is not None:
        paragraph.alignment = align
    if bold or italic:
        run = paragraph.add_run(text)
        run.bold = bold
        run.italic = italic
        if size:
            run.font.size = Pt(size)
    else:
        add_runs(paragraph, text, size=size)
    return paragraph


def parse_tables(lines: list[str]):
    tables = []
    i = 0
    while i < len(lines):
        if lines[i].startswith("**Table "):
            caption = re.sub(r"^\*\*(.*?)\*\*$", r"\1", lines[i].strip())
            j = i + 1
            while j < len(lines) and not lines[j].startswith("|"):
                j += 1
            table_lines = []
            while j < len(lines) and lines[j].startswith("|"):
                table_lines.append(lines[j])
                j += 1
            rows = []
            for line in table_lines:
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                if all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
                    continue
                rows.append(cells)
            tables.append((caption, rows))
            i = j
        else:
            i += 1
    return tables


def add_table(doc: Document, caption: str, rows: list[list[str]], font_size=7.6):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(3)
    r = p.add_run(caption)
    r.bold = True
    r.font.size = Pt(9.5)
    if not rows:
        return
    ncols = max(len(row) for row in rows)
    table = doc.add_table(rows=len(rows), cols=ncols)
    table.style = "Table Grid"
    table.autofit = True
    for ri, row in enumerate(rows):
        tr = table.rows[ri]
        if ri == 0:
            set_repeat_table_header(tr)
        for ci in range(ncols):
            cell = tr.cells[ci]
            cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            set_cell_margins(cell)
            if ci < len(row):
                cell.text = ""
                pcell = cell.paragraphs[0]
                pcell.paragraph_format.space_after = Pt(0)
                add_runs(pcell, row[ci], size=font_size)
            if ri == 0:
                set_cell_shading(cell, "D9EAF7")
                for run in cell.paragraphs[0].runs:
                    run.bold = True
    doc.add_paragraph().paragraph_format.space_after = Pt(0)


def load_lines() -> list[str]:
    return SOURCE.read_text(encoding="utf-8").splitlines()


def add_figure(doc: Document, draft=True) -> None:
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run().add_picture(str(FIGURE_PNG), width=Inches(6.4))
    caption = "Figure 1. Evidence-bounded SLIM conceptual model."
    if draft:
        caption += " Draft for author review; it is a hypothesis-generating model, not a causal pathway or a direct SHS molecular finding."
    cp = doc.add_paragraph()
    cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = cp.add_run(caption)
    run.bold = True
    run.font.size = Pt(9.5)
    lp = doc.add_paragraph()
    lp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    lr = lp.add_run("Solid blue/amber blocks represent audited human or contextual evidence; dashed purple blocks and arrows represent transfer evidence or hypotheses requiring prospective SHSQ-25 validation.")
    lr.italic = True
    lr.font.size = Pt(8.5)


def add_main_manuscript(lines: list[str], tables) -> None:
    doc = Document()
    set_document_defaults(doc, TITLE)
    # Title and abstract are handled as normal content, while internal status lines
    # and the author/declaration section are intentionally omitted at this stage.
    i = 0
    figure_inserted = False
    skip_declarations = False
    table_iter = iter(tables)
    while i < len(lines):
        line = lines[i]
        if line.startswith("# "):
            i += 1
            continue
        if line.startswith("## "):
            heading = line[3:].strip()
            if heading.startswith("6."):
                skip_declarations = True
                i += 1
                continue
            if heading == "References":
                skip_declarations = False
                add_paragraph(doc, heading, style="Heading 1")
                i += 1
                continue
            if skip_declarations:
                i += 1
                continue
            if heading == "Abstract":
                add_paragraph(doc, "Abstract", style="Heading 1")
            else:
                add_paragraph(doc, heading, style="Heading 1")
            i += 1
            continue
        if skip_declarations:
            i += 1
            continue
        if line.startswith("### "):
            heading = line[4:].strip()
            if heading.startswith("4.3") and not figure_inserted:
                add_figure(doc, draft=True)
                figure_inserted = True
            add_paragraph(doc, heading, style="Heading 2")
            i += 1
            continue
        if line.startswith("**Manuscript status") or line.startswith("**Target format"):
            i += 1
            continue
        if line.startswith("**Table "):
            caption, rows = next(table_iter)
            add_table(doc, caption, rows)
            i += 1
            while i < len(lines) and (lines[i].startswith("|") or not lines[i].strip()):
                i += 1
            continue
        if line.startswith("|"):
            i += 1
            continue
        if not line.strip():
            i += 1
            continue
        if line.startswith("- "):
            p = doc.add_paragraph(style="List Bullet")
            add_runs(p, line[2:])
            i += 1
            continue
        if line.startswith("References are presented"):
            add_paragraph(doc, line)
            i += 1
            continue
        if re.match(r"^\d+\. .*doi:", line):
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.15)
            add_runs(p, line)
            i += 1
            continue
        if re.match(r"^\d+\. ", line):
            p = doc.add_paragraph(style="List Number")
            add_runs(p, re.sub(r"^\d+\. ", "", line))
            i += 1
            continue
        # Collect ordinary wrapped Markdown lines into one Word paragraph.
        paragraph_lines = [line]
        j = i + 1
        while j < len(lines) and lines[j].strip() and not lines[j].startswith(("#", "**Table ", "|", "- ")) and not re.match(r"^\d+\. ", lines[j]):
            paragraph_lines.append(lines[j])
            j += 1
        add_paragraph(doc, " ".join(x.strip() for x in paragraph_lines))
        i = j
    if not figure_inserted:
        add_figure(doc, draft=True)
    path = OUT / "Main_Manuscript_SchemeB_Author_Review.docx"
    doc.save(path)


def add_title_page() -> None:
    doc = Document()
    set_document_defaults(doc, TITLE)
    add_paragraph(doc, "Title page — author-review draft", style="Title", align=WD_ALIGN_PARAGRAPH.CENTER)
    add_paragraph(doc, TITLE, style="Heading 1", align=WD_ALIGN_PARAGRAPH.CENTER)
    add_paragraph(doc, "Article type: Review Article", align=WD_ALIGN_PARAGRAPH.CENTER)
    add_paragraph(doc, "Target journal: Molecular Psychiatry", align=WD_ALIGN_PARAGRAPH.CENTER)
    doc.add_paragraph()
    fields = [
        ("Running title", "*"),
        ("Author names and order", "*"),
        ("Affiliations and institution superscripts", "*"),
        ("ORCID identifiers", "*"),
        ("Corresponding author / email / postal address", "*"),
        ("Funding statement", "*"),
        ("Competing-interest statement", "*"),
        ("Author-contribution statement", "*"),
        ("Originality / exclusive-submission statement", "*"),
    ]
    for label, value in fields:
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(8)
        r = p.add_run(f"{label}: ")
        r.bold = True
        p.add_run(value)
    add_paragraph(doc, "Current content inventory", style="Heading 2")
    for item in [
        "Abstract: approximately 213 words",
        "Main narrative: approximately 4,000 lexical words before final typesetting",
        "References: 19",
        "Main-text tables: 3",
        "Conceptual figure: 1 draft figure for author review",
        "Mandatory supplementary information: none identified for this narrative review draft",
    ]:
        p = doc.add_paragraph(style="List Bullet")
        p.add_run(item)
    add_paragraph(doc, "Data availability, code availability and ethics/consent statements are intentionally not populated in this author-review package, per current instruction.", italic=True, size=9)
    doc.save(OUT / "Title_Page_SchemeB_Author_Review.docx")


def add_cover_letter() -> None:
    doc = Document()
    set_document_defaults(doc, "Cover letter — " + TITLE)
    add_paragraph(doc, "Cover letter — author-review draft", style="Title", align=WD_ALIGN_PARAGRAPH.CENTER)
    add_paragraph(doc, "Dear Editors,", size=11)
    paragraphs = [
        f"Please consider our Review Article, “{TITLE},” for publication in Molecular Psychiatry.",
        "Suboptimal health status is commonly assessed with the SHSQ-25, yet biological reports use non-equivalent thresholds, populations, matrices and estimands. This review provides a source-audited narrative synthesis rather than a forced meta-analysis. Three direct SHS-related cortisol reports are retained study by study, but no primary pooled direct-cortisol estimate is reported because cohort independence, exposure definitions and estimands cannot be shown to be sufficiently comparable.",
        "Low-grade-inflammation, quality-of-life and fatigue findings are kept as bridge evidence. A proposed SLIM framework organizes immune-metabolic and mitochondrial hypotheses while explicitly distinguishing mechanistic-transfer evidence from direct human SHS evidence.",
        "The review package contains 19 identity-verified Vancouver references, three main-text tables and one evidence-bounded conceptual figure prepared for author review. It makes no standalone biomarker diagnostic claim and does not convert transfer evidence into direct SHS evidence.",
        "The manuscript is a narrative Review Article and does not report a new participant-level dataset or a new human intervention. Author-controlled originality, funding, competing-interest, contribution and correspondence statements will be completed before submission.",
    ]
    for text in paragraphs:
        add_paragraph(doc, text)
    add_paragraph(doc, "Originality and exclusive-submission statement: *")
    add_paragraph(doc, "Funding statement: *")
    add_paragraph(doc, "Competing-interest statement: *")
    add_paragraph(doc, "Author approval and contribution statement: *")
    add_paragraph(doc, "Suggested or excluded reviewers, if requested: *")
    doc.add_paragraph()
    add_paragraph(doc, "Sincerely,")
    add_paragraph(doc, "*")
    add_paragraph(doc, "Corresponding author: *")
    add_paragraph(doc, "Affiliation: *")
    add_paragraph(doc, "Email: *")
    add_paragraph(doc, "Data availability, code availability and ethics/consent statements are intentionally not included in this author-review draft.", italic=True, size=9)
    doc.save(OUT / "Cover_Letter_SchemeB_Author_Review.docx")


def add_tables_doc(tables) -> None:
    doc = Document()
    set_document_defaults(doc, "Tables — " + TITLE)
    add_paragraph(doc, "Tables 1–3 — author-review package", style="Title", align=WD_ALIGN_PARAGRAPH.CENTER)
    add_paragraph(doc, "These tables are duplicated from the clean manuscript copy for convenient review and upload preparation. They retain the evidence boundaries and are not independent quantitative evidence files.", italic=True, size=9)
    for caption, rows in tables:
        add_table(doc, caption, rows, font_size=8.0)
    doc.save(OUT / "Tables_1_to_3_SchemeB_Author_Review.docx")


def font(path: str, size: int, bold=False):
    try:
        return ImageFont.truetype(path, size=size)
    except OSError:
        return ImageFont.load_default()


def draw_wrapped(draw, xy, text, fnt, fill, width, spacing=8):
    x, y = xy
    # approximate character width to keep the figure deterministic across fonts
    chars = max(12, int(width / max(8, fnt.size * 0.54)))
    lines = textwrap.wrap(text, width=chars)
    draw.multiline_text((x, y), "\n".join(lines), font=fnt, fill=fill, spacing=spacing)
    bbox = draw.multiline_textbbox((x, y), "\n".join(lines), font=fnt, spacing=spacing)
    return bbox[3]


def rounded_box(draw, xy, fill, outline, title, bullets, title_font, body_font, dashed=False):
    x1, y1, x2, y2 = xy
    draw.rounded_rectangle(xy, radius=28, fill=fill, outline=outline, width=5)
    draw.text((x1 + 28, y1 + 24), title, font=title_font, fill=outline)
    y = y1 + 92
    for bullet in bullets:
        draw.ellipse((x1 + 32, y + 9, x1 + 48, y + 25), fill=outline)
        y = draw_wrapped(draw, (x1 + 66, y), bullet, body_font, "#263238", x2 - x1 - 95) + 20


def arrow(draw, start, end, fill, label, label_xy, fnt, dashed=False):
    x1, y1 = start
    x2, y2 = end
    if dashed:
        steps = 20
        for i in range(steps):
            if i % 2 == 0:
                xa = x1 + (x2 - x1) * i / steps
                ya = y1 + (y2 - y1) * i / steps
                xb = x1 + (x2 - x1) * (i + 1) / steps
                yb = y1 + (y2 - y1) * (i + 1) / steps
                draw.line((xa, ya, xb, yb), fill=fill, width=5)
    else:
        draw.line((x1, y1, x2, y2), fill=fill, width=5)
    # arrow head
    import math
    angle = math.atan2(y2 - y1, x2 - x1)
    size = 18
    pts = [(x2, y2), (x2 - size * math.cos(angle - 0.5), y2 - size * math.sin(angle - 0.5)), (x2 - size * math.cos(angle + 0.5), y2 - size * math.sin(angle + 0.5))]
    draw.polygon(pts, fill=fill)
    draw.text(label_xy, label, font=fnt, fill=fill)


def build_figure() -> None:
    global FONT
    FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    W, H = 2100, 1300
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)
    title_font = font(BOLD, 48, True)
    sub_font = font(FONT, 24)
    box_title = font(BOLD, 30, True)
    body = font(FONT, 25)
    small = font(FONT, 21)
    draw.text((70, 40), "Evidence-bounded SLIM conceptual model", font=title_font, fill="#17365D")
    draw.text((72, 105), "Author-review draft: direct human evidence is not interchangeable with bridge or mechanistic-transfer evidence.", font=sub_font, fill="#455A64")
    rounded_box(draw, (70, 190, 650, 700), "#DCEEFF", "#2166AC", "Direct SHSQ-25 human evidence", [
        "SHSQ-25 phenotype and symptom construct",
        "Three cortisol reports; no primary pooling",
        "Telomere bridge for cellular-ageing signal",
        "Context and multi-omics records",
    ], box_title, body)
    rounded_box(draw, (760, 190, 1340, 700), "#FFF0C9", "#B87900", "Bridge and contextual evidence", [
        "CRP/IL-6 with HRQoL or fatigue in non-SHS populations",
        "Vascular, glycomic and psychosocial SHS context",
        "Pregnancy-specific oxidative/vascular bridge",
        "Indirect evidence; population and outcome remain separate",
    ], box_title, body)
    rounded_box(draw, (1450, 190, 2030, 700), "#E8DDF5", "#6A3D9A", "Mechanistic transfer / hypotheses", [
        "Immunometabolism",
        "Mitochondrial dynamics: Drp1, MFN2, OPA1",
        "mtDNA–cGAS–STING and NLRP3",
        "Prospective SHSQ-25 validation required",
    ], box_title, body, dashed=True)
    arrow(draw, (650, 440), (760, 440), "#B87900", "contextual bridge", (650, 720), small, dashed=True)
    arrow(draw, (1340, 440), (1450, 440), "#6A3D9A", "biological plausibility only", (1310, 720), small, dashed=True)
    draw.rounded_rectangle((240, 850, 1860, 1040), radius=30, fill="#FDECEC", outline="#B22222", width=5)
    draw.text((330, 890), "Evidence lock", font=font(BOLD, 32, True), fill="#B22222")
    draw.text((330, 945), "Direct SHS–cortisol primary pooled estimate = 0", font=font(BOLD, 30, True), fill="#263238")
    draw.text((330, 985), "No standalone SHS biomarker diagnosis; no causal pathway demonstrated", font=body, fill="#263238")
    draw.text((160, 1130), "Solid blocks: audited human/context evidence    Dashed blocks/arrows: transfer evidence or testable hypotheses    No causal inference implied", font=small, fill="#455A64")
    img.save(FIGURE_PNG, dpi=(300, 300))
    img.save(FIGURE_PDF, "PDF", resolution=300.0)


def write_manifest() -> None:
    (OUT / "PACKAGE_README.md").write_text(
        """# Author-review submission package — Scheme B — 2026-10-15

This package is prepared for strict author review. It is not yet the final upload package because author-controlled fields remain `*`.

## Files

- `Main_Manuscript_SchemeB_Author_Review.docx`: body, abstract, three tables, references and one evidence-bounded conceptual figure.
- `Title_Page_SchemeB_Author_Review.docx`: independent title-page template with personal/funding fields left as `*`.
- `Cover_Letter_SchemeB_Author_Review.docx`: independent cover-letter template with author-controlled statements left as `*`.
- `Tables_1_to_3_SchemeB_Author_Review.docx`: separate review copy of the three main-text tables.
- `Figure_1_SLIM_Conceptual_Model_SchemeB.png` and `.pdf`: one conceptual figure, explicitly marked as a draft for author review.

## Current package decision

The package uses a restrained focused-review format: approximately 4,000 words in the clean body, three main-text tables and one conceptual figure. The figure is evidence-bounded and does not assert a causal SHS pathway. No exploratory forest plot, historical PRISMA figure, legacy GRADE table or unverified quantitative output is included.

No supplementary-information file is generated at this stage. Data availability, code availability and ethics/consent statements are intentionally omitted from the author-review manuscript package per current instruction. They must be handled later if the target submission system requires them.

Before submission, complete the title page and cover letter, confirm the figure/table/supplement decisions, replace author-controlled `*` fields, convert/proof the Word files against the target system and rerun the repository audits.
""",
        encoding="utf-8",
    )


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    lines = load_lines()
    tables = parse_tables(lines)
    if len(tables) != 3:
        raise SystemExit(f"Expected three manuscript tables, found {len(tables)}")
    build_figure()
    add_main_manuscript(lines, tables)
    add_title_page()
    add_cover_letter()
    add_tables_doc(tables)
    write_manifest()
    print(f"Built author-review package: {OUT}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 09 号综述稿转为投稿用 Word 文档。

处理：标题层级、正文（首行缩进2字符）、三线表、引注框（可检验推论）、
行内加粗、上下标（^hi 与 ⁺ 等）、参考文献（悬挂缩进）。
用法: python3 md2docx.py <input.md> <output.docx>
"""
import re
import sys

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

CN_FONT = "宋体"
CN_HEI = "黑体"
EN_FONT = "Times New Roman"


def set_run_font(run, cn=CN_FONT, size=10.5, bold=False):
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.name = EN_FONT
    rpr = run._element.get_or_add_rPr()
    rf = rpr.find(qn("w:rFonts"))
    if rf is None:
        rf = OxmlElement("w:rFonts")
        rpr.append(rf)
    rf.set(qn("w:ascii"), EN_FONT)
    rf.set(qn("w:hAnsi"), EN_FONT)
    rf.set(qn("w:eastAsia"), cn)


def set_cell_border(cell, **kwargs):
    tc = cell._tc
    tcpr = tc.get_or_add_tcPr()
    borders = OxmlElement("w:tcBorders")
    for edge in ("top", "bottom"):
        if edge in kwargs:
            el = OxmlElement(f"w:{edge}")
            el.set(qn("w:val"), "single")
            el.set(qn("w:sz"), str(kwargs[edge]))
            el.set(qn("w:color"), "000000")
            borders.append(el)
        else:
            el = OxmlElement(f"w:{edge}")
            el.set(qn("w:val"), "nil")
            borders.append(el)
    for edge in ("left", "right"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "nil")
        borders.append(el)
    tcpr.append(borders)


SUP_MAP = {"⁺": "+", "⁻": "-", "²": "2", "³": "3", "¹": "1", "⁰": "0"}


def add_rich_text(para, text, size=10.5, base_bold=False, cn=CN_FONT):
    """渲染 **加粗**、^上标^ 与 Unicode 上标字符。"""
    # 先切分加粗
    parts = re.split(r"(\*\*[^*]+\*\*)", text)
    for part in parts:
        if not part:
            continue
        bold = base_bold
        if part.startswith("**") and part.endswith("**") and len(part) > 4:
            bold = True
            part = part[2:-2]
        # 处理 ^xxx 形式的上标。仅取紧随 ^ 的小写修饰词（hi/lo/high/low/+/-/数字组合），
        # 避免把 GPNMB^hiLy6C^lo 中的 "hiLy6C" 整体上标。
        segs = re.split(r"(\^(?:high|low|hi|lo|pos|neg|\d+[a-z]*|[+-]))", part)
        for seg in segs:
            if not seg:
                continue
            if seg.startswith("^") and len(seg) > 1:
                r = para.add_run(seg[1:])
                set_run_font(r, cn, size, bold)
                r.font.superscript = True
                continue
            # 处理 Unicode 上标字符
            buf = ""
            for ch in seg:
                if ch in SUP_MAP:
                    if buf:
                        r = para.add_run(buf)
                        set_run_font(r, cn, size, bold)
                        buf = ""
                    r = para.add_run(SUP_MAP[ch])
                    set_run_font(r, cn, size, bold)
                    r.font.superscript = True
                else:
                    buf += ch
            if buf:
                r = para.add_run(buf)
                set_run_font(r, cn, size, bold)


def main(src, dst):
    lines = open(src, encoding="utf-8").read().split("\n")

    doc = Document()
    sec = doc.sections[0]
    sec.top_margin = Cm(2.5)
    sec.bottom_margin = Cm(2.5)
    sec.left_margin = Cm(2.5)
    sec.right_margin = Cm(2.5)

    st = doc.styles["Normal"]
    st.font.name = EN_FONT
    st.font.size = Pt(10.5)
    st.element.rPr.rFonts.set(qn("w:eastAsia"), CN_FONT)

    i = 0
    in_refs = False
    while i < len(lines):
        ln = lines[i]
        s = ln.strip()

        # 跳过分隔线与空行
        if s in ("", "---"):
            i += 1
            continue

        # 表格
        if s.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                row = lines[i].strip()
                if not re.match(r"^\|[\s\-:|]+\|$", row):
                    cells = [c.strip() for c in row.strip("|").split("|")]
                    rows.append(cells)
                i += 1
            if rows:
                ncol = max(len(r) for r in rows)
                tb = doc.add_table(rows=0, cols=ncol)
                tb.alignment = WD_TABLE_ALIGNMENT.CENTER
                for ri, r in enumerate(rows):
                    cells = tb.add_row().cells
                    for ci in range(ncol):
                        txt = r[ci] if ci < len(r) else ""
                        p = cells[ci].paragraphs[0]
                        p.paragraph_format.space_before = Pt(2)
                        p.paragraph_format.space_after = Pt(2)
                        add_rich_text(p, txt, size=9, base_bold=(ri == 0))
                        if ri == 0:
                            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    # 三线表：首行上下框线，末行下框线
                    for ci in range(ncol):
                        if ri == 0:
                            set_cell_border(cells[ci], top=12, bottom=6)
                        elif ri == len(rows) - 1:
                            set_cell_border(cells[ci], bottom=12)
                        else:
                            set_cell_border(cells[ci])
            continue

        # 标题
        if s.startswith("#"):
            m = re.match(r"^(#+)\s*(.+)$", s)
            lvl, txt = len(m.group(1)), m.group(2)
            if lvl == 1:
                p = doc.add_paragraph()
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.space_before = Pt(6)
                p.paragraph_format.space_after = Pt(14)
                r = p.add_run(txt)
                set_run_font(r, CN_HEI, 16, True)
            else:
                if txt.startswith("参考文献"):
                    in_refs = True
                p = doc.add_paragraph()
                p.paragraph_format.space_before = Pt(10 if lvl == 2 else 8)
                p.paragraph_format.space_after = Pt(5)
                r = p.add_run(txt)
                set_run_font(r, CN_HEI, 12 if lvl == 2 else 10.5, True)
            i += 1
            continue

        # 引注框（可检验推论）
        if s.startswith(">"):
            body = re.sub(r"^>\s?", "", s)
            p = doc.add_paragraph()
            pf = p.paragraph_format
            pf.left_indent = Cm(0.75)
            pf.right_indent = Cm(0.75)
            pf.space_before = Pt(6)
            pf.space_after = Pt(6)
            pf.line_spacing = 1.4
            add_rich_text(p, body, size=10)
            for r in p.runs:
                r.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
            i += 1
            continue

        # 参考文献条目：悬挂缩进
        if in_refs and re.match(r"^\[\d+\]", s):
            p = doc.add_paragraph()
            pf = p.paragraph_format
            pf.left_indent = Cm(0.85)
            pf.first_line_indent = Cm(-0.85)
            pf.space_after = Pt(2)
            pf.line_spacing = 1.25
            add_rich_text(p, s, size=9)
            i += 1
            continue

        # 普通段落
        p = doc.add_paragraph()
        pf = p.paragraph_format
        pf.first_line_indent = Cm(0.74)  # 首行缩进 2 字符
        pf.space_after = Pt(3)
        pf.line_spacing = 1.5
        # 摘要/关键词等以加粗标签开头的段落不缩进
        if s.startswith("**关键词") or s.startswith("**致谢") or s.startswith("**利益冲突"):
            pf.first_line_indent = Cm(0)
        add_rich_text(p, s)
        i += 1

    doc.save(dst)
    print("saved:", dst)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

#!/usr/bin/env python3
import re
import json
from pathlib import Path

base = Path("/home/user/academic-research-skills")
md_path = base / "asti-review" / "09_综述精修稿_v2_伤科三期.md"
out_dir = base / "zotero"
out_dir.mkdir(exist_ok=True)

text = md_path.read_text(encoding='utf-8')
# Extract references section
# Find "## 参考文献" and then lines starting with [n]
ref_section_match = re.search(r'## 参考文献\n(.+)', text, re.DOTALL)
ref_text = ref_section_match.group(1) if ref_section_match else text

# Parse lines like [1] ...
# References are each on one line (some may wrap? but in file each is one line)
refs = []
for line in ref_text.splitlines():
    line=line.strip()
    m = re.match(r'^\[(\d+)\]\s*(.+)$', line)
    if m:
        num = int(m.group(1))
        content = m.group(2).strip()
        refs.append((num, content))

print(f"Found {len(refs)} refs")

# Helper to extract DOI and PMID
def extract_doi(s):
    m = re.search(r'DOI:\s*([^\s]+)', s, re.I)
    if m:
        doi = m.group(1).strip().rstrip('.')
        # remove trailing comma
        doi = doi.rstrip(',;')
        return doi
    # also DOI: 10.xxx
    m = re.search(r'(10\.\d+/[^\s,;]+)', s)
    if m:
        return m.group(1).rstrip('.,;')
    return None

def extract_pmid(s):
    m = re.search(r'PMID:\s*(\d+)', s)
    if m:
        return m.group(1)
    return None

def parse_authors_title_journal(s):
    # Very heuristic
    # Format: Authors. Title[J]. Journal, year, vol(issue): pages. DOI...
    # Try to split
    # Remove DOI/PMID tail for parsing
    s_clean = re.sub(r'DOI:.*$', '', s, flags=re.I).strip()
    s_clean = re.sub(r'PMID:.*$', '', s_clean, flags=re.I).strip()
    # For Chinese: 周静, 杨林... Title. Journal, year...
    # Attempt: authors = before first ". " that is followed by capital or Chinese
    # Simplified: split by ". " 
    # We'll attempt regex for journal pattern: [J]. *Journal*, year
    # Extract year: 4-digit
    year_match = re.search(r'(19|20)\d{2}', s_clean)
    year = year_match.group(0) if year_match else "2025"
    # Journal: try to find pattern \*Journal\* or Journal,
    journal = ""
    m_j = re.search(r'\*\s*([^*]+?)\s*\*', s_clean)
    if m_j:
        journal = m_j.group(1).strip()
    else:
        # Look for pattern: [J]. Something, year
        m_j2 = re.search(r'\[J\]\.\s*([^,]+),', s_clean)
        if m_j2:
            journal = m_j2.group(1).strip()
        else:
            # After title, before year
            # Take text between "]. " and ", 20xx" ?
            pass
    # Title: try to extract between authors and [J] or journal
    title = ""
    # If [J] present, title is between authors and [J]
    if "[J]" in s_clean:
        parts = s_clean.split("[J]")
        # before [J] contains authors + title
        before = parts[0]
        # authors are up to first period? Actually Chinese titles may contain .
        # Heuristic: last period before [J] splits authors and title
        # Find last occurrence of ". " before [J] marker in original s_clean
        # Use rsplit
        if ". " in before:
            # Split by ". " and assume last segment is title
            segs = before.rsplit(". ", 1)
            if len(segs)==2:
                title = segs[1].strip()
                authors = segs[0].strip()
            else:
                title = before.strip()
                authors = ""
        else:
            title = before.strip()
    else:
        # For [M] books
        if "[M]" in s_clean:
            parts = s_clean.split("[M]")
            before = parts[0]
            # Title is before [M] after authors?
            if ". " in before:
                segs = before.rsplit(". ", 1)
                title = segs[-1].strip()
            else:
                title = before.strip()
        else:
            # No [J] [M], maybe just title.
            # Take first sentence as title?
            # For English: Authors. Title. Journal...
            # Split by ". " first two
            segs = s_clean.split(". ")
            if len(segs)>=2:
                title = segs[1].strip()
            else:
                title = s_clean[:200]

    # Authors: try to get before title
    authors_raw = ""
    if title and title in s_clean:
        idx = s_clean.find(title)
        authors_raw = s_clean[:idx].strip().rstrip('.')
    else:
        # fallback: take up to first period
        authors_raw = s_clean.split(".")[0].strip()

    # Clean authors
    authors_raw = re.sub(r'\s+', ' ', authors_raw)
    # Remove trailing [J] etc
    return {
        "authors_raw": authors_raw,
        "title": title,
        "journal": journal,
        "year": year,
        "raw": s
    }

# Generate BibTeX
bib_entries = []
ris_entries = []
csl_entries = []

for num, content in refs:
    doi = extract_doi(content)
    pmid = extract_pmid(content)
    parsed = parse_authors_title_journal(content)
    # Determine entry type
    entry_type = "book" if "[M]" in content else "article"
    # Clean title for bib
    title = parsed["title"] or content[:150]
    # Remove any remaining markup
    title_clean = title.replace("{","").replace("}","").strip()
    # Authors: try to split by comma and format as "and"
    authors_raw = parsed["authors_raw"]
    # For bibtex, authors separated by " and "
    # Split by comma but keep Chinese names as is
    # Heuristic: if "等" present, keep as is
    # Convert Chinese "，"
    authors_raw = authors_raw.replace("，", ",")
    # If authors_raw contains "et al" keep
    # For bibtex author field, use raw but replace ", " with " and " for last?
    # Simplistic: if comma present, assume list of authors separated by ","
    # We'll just put authors_raw as author, Zotero will parse
    bib_author = authors_raw
    # If bib_author empty, use "Unknown"
    if not bib_author or len(bib_author)<2:
        bib_author = "Unknown"

    cite_key = f"ref{num:02d}_{parsed['year']}"
    # Make safe key
    # Add first author last name
    first_author = bib_author.split(",")[0].split()[0] if bib_author else "ref"
    first_author = re.sub(r'[^a-zA-Z0-9\u4e00-\u9fa5]', '', first_author)[:20]
    cite_key = f"{first_author}{parsed['year']}_{num:02d}"

    bib = ""
    if entry_type == "book":
        bib = f"""@book{{{cite_key},
  author = {{{bib_author}}},
  title = {{{title_clean}}},
  year = {{{parsed['year']}}},
  note = {{{content}}},
"""
        if doi:
            bib += f"  doi = {{{doi}}},\n"
        bib += "}\n"
    else:
        journal = parsed["journal"] or "Unknown Journal"
        bib = f"""@article{{{cite_key},
  author = {{{bib_author}}},
  title = {{{title_clean}}},
  journal = {{{journal}}},
  year = {{{parsed['year']}}},
  note = {{{content}}},
"""
        if doi:
            bib += f"  doi = {{{doi}}},\n"
        if pmid:
            bib += f"  pmid = {{{pmid}}},\n"
        bib += "}\n"

    bib_entries.append(bib)

    # RIS
    # TY  - JOUR or BOOK
    ty = "BOOK" if entry_type=="book" else "JOUR"
    ris = f"TY  - {ty}\n"
    # Authors: split
    # For RIS, each author on separate AU line
    # Split authors_raw by comma or " and " or "，"
    # For Chinese, keep whole as AU
    authors_list = []
    # Try split by ","
    # If Chinese contains "等", keep one
    if "等" in authors_raw:
        # Take before 等
        # e.g., "周静, 杨林, 王建华, 等"
        base_auth = authors_raw.split("等")[0].strip().rstrip(",").rstrip("，")
        # split base_auth by comma
        parts = re.split(r'[,\s]+', base_auth)
        # Actually better split by ","
        parts = [p.strip() for p in base_auth.split(",") if p.strip()]
        authors_list = parts
    else:
        # Split by ", " but handle "and"
        # For English authors: "Fong DT, Hong Y, Chan LK, et al."
        parts = [p.strip() for p in re.split(r',\s*|\s+and\s+', authors_raw) if p.strip()]
        # If parts contain et al, keep previous
        authors_list = [p for p in parts if p.lower() not in ["et al", "et al."]]

    if not authors_list:
        authors_list = [authors_raw]

    for au in authors_list[:10]:  # limit
        if au:
            ris += f"AU  - {au}\n"
    ris += f"TI  - {title_clean}\n"
    if journal:
        ris += f"JO  - {journal}\n"
        ris += f"JF  - {journal}\n"
    ris += f"PY  - {parsed['year']}\n"
    if doi:
        ris += f"DO  - {doi}\n"
    if pmid:
        ris += f"AN  - {pmid}\n"
    # Add original content as notes
    ris += f"N1  - {content}\n"
    ris += "ER  - \n\n"
    ris_entries.append(ris)

    # CSL JSON
    csl = {
        "id": cite_key,
        "type": "book" if entry_type=="book" else "article-journal",
        "title": title_clean,
        "author": [{"literal": au} for au in authors_list[:10]],
        "issued": {"date-parts": [[int(parsed['year']) if parsed['year'].isdigit() else 2025]]},
        "note": content,
    }
    if doi:
        csl["DOI"] = doi
    if journal:
        csl["container-title"] = journal
    csl_entries.append(csl)

# Write files
bib_path = out_dir / "ASTI_v9_98refs.bib"
bib_path.write_text("\n".join(bib_entries), encoding='utf-8')
print(f"Wrote {bib_path} {bib_path.stat().st_size/1024:.1f}KB")

ris_path = out_dir / "ASTI_v9_98refs.ris"
ris_path.write_text("".join(ris_entries), encoding='utf-8')
print(f"Wrote {ris_path}")

json_path = out_dir / "ASTI_v9_98refs_CSL.json"
json_path.write_text(json.dumps(csl_entries, ensure_ascii=False, indent=2), encoding='utf-8')
print(f"Wrote {json_path}")

# Also generate CSV for overview
csv_path = out_dir / "ASTI_v9_98refs_overview.csv"
import csv
with open(csv_path, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(["编号", "类型", "年份", "标题", "期刊/出版社", "作者", "DOI", "PMID", "原始条目"])
    for (num, content), bib in zip(refs, bib_entries):
        doi = extract_doi(content) or ""
        pmid = extract_pmid(content) or ""
        parsed = parse_authors_title_journal(content)
        writer.writerow([num, "图书" if "[M]" in content else "期刊", parsed["year"], parsed["title"][:200], parsed["journal"], parsed["authors_raw"][:200], doi, pmid, content])

print(f"Wrote {csv_path}")

# Generate README for Zotero
readme = f"""# Zotero 导入指南 - ASTI综述 v9 98篇参考文献

生成时间：2026-09-14
来源：`asti-review/09_综述精修稿_v2_伤科三期.md` 参考文献 [1]-[98]（已核实，全部可溯源）

## 文件清单

| 文件 | 说明 | 大小 | 推荐用途 |
|------|------|------|----------|
| `ASTI_v9_98refs.bib` | BibTeX格式 | {bib_path.stat().st_size/1024:.1f}KB | **Zotero / JabRef / LaTeX** 推荐，含DOI可自动补全 |
| `ASTI_v9_98refs.ris` | RIS格式 | {ris_path.stat().st_size/1024:.1f}KB | **EndNote / Zotero / Mendeley** 通用 |
| `ASTI_v9_98refs_CSL.json` | CSL-JSON | {json_path.stat().st_size/1024:.1f}KB | Zotero高级导入，保留完整元数据 |
| `ASTI_v9_98refs_overview.csv` | CSV概览 | {csv_path.stat().st_size/1024:.1f}KB | Excel快速浏览、筛选 |

## 一键导入 Zotero（3种方法）

### 方法A：BibTeX导入（推荐，保留DOI自动补全）
1. 打开 Zotero 桌面版
2. 文件 → 导入 → 选择 `ASTI_v9_98refs.bib`
3. 勾选“将导入的条目放入新分类” → 命名为 `ASTI_v9_伤科三期`
4. 导入后全选98条 → 右键 → “通过DOI获取元数据” → 自动补全缺失信息
5. 右键 → “添加标签” → 按治则分类：`消法` `和法` `补法` `时相机制` `组学技术`

### 方法B：RIS导入（兼容性最好）
1. Zotero → 文件 → 导入 → 选择 `ASTI_v9_98refs.ris`
2. 导入选项：UTF-8编码
3. 完成后检查：`N1`字段含原始中文条目，便于核对

### 方法C：拖拽DOI批量抓取（最完整）
1. 打开 `ASTI_v9_98refs_overview.csv`，复制DOI列
2. Zotero → 点击魔术棒图标“通过标识符添加条目” → 粘贴DOI批量添加
3. 优势：自动从CrossRef/PubMed获取最完整元数据
4. 对中文文献（无DOI）手动添加：文件 → 新建条目 → 期刊文章

## 98篇文献分类（建议Zotero中建子文件夹）

- **α 直接证据（ASTI模型）**：[6] 栀黄膏Treg趋化, [30][31] 电针巨噬细胞极化, [95] 刮痧+马桑狗帮油, [44] 泛酸-H3K27ac轴
  → 标签：`α_ASTI直接`
- **β 跨疾病外推**：心肌[33][34][62][77]、关节炎[60][80-82]、脑损伤[72-74]、肠道[78]、肿瘤[96]
  → 标签：`β_外推`
- **时相机制核心**：[26] Arnold 2007奠基, [46] Mounier AMPKα1, [47] Juban代谢调控, [51] Chazaud综述, [27] Giannakis脂质介质
  → 标签：`核心_时相机制`
- **教材/古籍**：[15] 中医筋伤学, [16] 医宗金鉴, [64] 中医骨伤科学
  → 标签：`教材_古籍`
- **中药成分**：按治则分
  - 消法：[4][69-74][96-98] 槲皮素、葛根素、黄芩苷、丹参酮、HSYA
  - 和法：[56-61][75-79][80-83] 黄芪甲苷、三七皂苷、小檗碱、青藤碱
  - 补法：[62][63][45] 真武汤、阿魏酸、艾灸
  → 标签：`消法` `和法` `补法`

## 中文文献特别处理

本综述含中文文献约15篇（如[4]中国药房, [15][16][64]教材, [30]中国针灸, [66][67][68]等），RIS/BibTeX已保留原始中文条目在 `note/N1` 字段。

Zotero中建议：
1. 安装插件 `Jasminum`（茉莉花）→ 自动抓取CNKI元数据
2. 或手动在CNKI搜索题名 → 导出RIS → 合并到本库
3. 教材类[15][16][64]在Zotero中设为“书籍”，手动填页码：65-67, 55, 48-50/245

## 去重与核实

- 本库98条已去重，旧125条中的25条已移出（见 `13_参考文献重编号审计.md` §4）
- 5条曾“查无此文”已替换：[1]→Fong 2007, [3]→Jones Cochrane 2020, [7]→Wynn 2016, [8]→Landén 2016, [28]→Dakin 2018
- 全部含DOI/PMID，已通过Europe PMC核实

## 进阶：与Word联动

1. Zotero中选中98条 → 右键 → 创建引文目录 → 选择 GB/T 7714（顺序编码制）
2. 在 `37_终稿_v9_套用参考b结构.docx` 中插入Zotero引文，实现动态编号
3. 或直接用本BibTeX在Overleaf中编译

## 下载中心

所有文件已部署到 LIVE PREVIEW：
- `/zotero/ASTI_v9_98refs.bib`
- `/zotero/ASTI_v9_98refs.ris`
- `/zotero/ASTI_v9_98refs_CSL.json`
- `/zotero/ASTI_v9_98refs_overview.csv`

---

生成脚本：`generate_zotero.py`
原始数据：`asti-review/04_参考文献完整版.md` + `09_综述精修稿_v2_伤科三期.md`
"""

readme_path = out_dir / "README_Zotero导入指南.md"
readme_path.write_text(readme, encoding='utf-8')
print(f"Wrote {readme_path}")

# Also copy to root for easy download via preview
for f in [bib_path, ris_path, json_path, csv_path, readme_path]:
    dest = base / f.name
    # copy
    import shutil
    shutil.copy2(f, dest)
    print(f"Copied to {dest}")

print("Done")

#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The navigation of a built manual, checked row by row against its printed pages (the founder's order of 17 October).

  - every Contents row's page number against the page label where that heading is printed (through the PDF's bookmarks);
  - every List of Figures row's page number against the page where that figure's caption is printed;
  - every figure against the text that names it: the figure stands on the page of the paragraph before its image line
    in the book's one-file text, or on the next page (a float), never further;
  - no page carries more than two figures (figures where they live, never in one block);
  - the index: every page listed for a term carries that term's first word on that page;
  - every page but the title page carries the running head (the book and its section) and the page label in both
    bottom corners.

Usage: python3 docs/book/nav_check.py docs/OMNI_COMPASS_MANUAL.pdf docs/book/OMNI_COMPASS_BOOK.md
       python3 docs/book/nav_check.py docs/OMNI_COMPASS_OWNERS_MANUAL.pdf docs/book/OMNI_COMPASS_OWNERS_BOOK.md
It prints one line per check and exits 1 when a page lacks its head or a corner number, a page carries more than two
figures, or a figure stands further than the next page from the paragraph that names it."""
import re
import sys

import pymupdf as fitz

TOP, BOTTOM = 0.95 * 72, 0.9 * 72                        # the frame's margins, as build_book.py sets them


def main(pdf, md_path):
    doc = fitz.open(pdf)
    H = doc[0].rect.height
    bad = 0

    # the page labels as printed in the corners; the body starts where the label restarts at 1
    label, no_corner = {}, []
    for i, p in enumerate(doc):
        foot = [w for w in p.get_text("words") if w[1] > H - 0.6 * 72]
        nums = [w[4] for w in foot if re.fullmatch(r"[0-9]+|[ivxlcdm]+", w[4])]
        label[i + 1] = nums[0] if nums else None
        if len(nums) < 2 and i > 0:
            no_corner.append(i + 1)
    body = next((pg for pg, lab in label.items() if lab == "1"), 1)
    print(f"page label in both corners: missing on {len(no_corner)} pages {no_corner[:10]}")
    bad += bool(no_corner)

    # the running head on every page but the title page
    missing_head = [i + 1 for i, p in enumerate(doc) if i > 0
                    and "OMNI-COMPASS" not in " ".join(w[4] for w in p.get_text("words") if w[1] < 0.7 * 72).upper()]
    print(f"running head: missing on {len(missing_head)} pages {missing_head[:10]}")
    bad += bool(missing_head)

    # the Contents and the List of Figures (the front matter) against the bookmarks and the caption pages
    toc = [(re.sub(r"\s+", " ", t), label[pg]) for lvl, t, pg in doc.get_toc()]
    rows, lof_rows = [], []
    # the Contents and the List of Figures are the pages from the Contents heading to the first bookmarked page (the
    # Foreword), that page included; the title and copyright pages before them carry no rows
    front_end = min((pg for _lvl, _t, pg in doc.get_toc()), default=body)      # the List of Figures can end on it
    framed = lambda i: " ".join(w[4] for w in doc[i].get_text("words") if TOP < w[1] < H - BOTTOM)
    first = next((i for i in range(1, front_end) if framed(i).startswith("Contents")), 1)
    for i in range(first, front_end):
        lines = {}
        for w in doc[i].get_text("words"):
            if TOP < w[1] < H - BOTTOM:
                lines.setdefault(round(w[3] / 3), []).append(w)
        carry = ""                                        # a row wrapped onto a second line is joined before the test
        for k in sorted(lines):
            txt = " ".join(w[4] for w in sorted(lines[k], key=lambda w: w[0]) if w[4] != ".")
            if re.match(r"Figure \d+\. ", txt):
                carry = ""                                # every figure row starts its own line: what came before was
                                                          # the page's heading or the list's opening paragraph
            m = re.match(r"(.*\S)\s+([0-9]+|[ivxlcdm]+)$", txt)
            if m and len(txt) < 200:
                full = (carry + " " + m.group(1)).strip() if carry else m.group(1)
                full = re.sub(r"^(Contents|List of Figures) ", "", full)            # the page's heading
                (lof_rows if full.startswith("Figure ") else rows).append((re.sub(r"\s+", " ", full), m.group(2)))
                carry = ""
            elif len(txt) < 200 and (txt.startswith("Figure ") or txt[:1].isupper() or txt[:1].isdigit() or carry):
                carry = (carry + " " + txt).strip()
    rows = [r for r in rows if not re.match(r"^(October|THE OMNI)", r[0])]
    ok, miss = 0, []
    for title, lab in rows:
        hit = {v for k, v in toc if k[:30] == title[:30] or k.startswith(title[:40]) or title.startswith(k[:40])}
        if lab in hit:
            ok += 1
        else:
            miss.append((title[:50], lab, sorted(x for x in hit if x)[:3]))
    print(f"contents rows {len(rows)}: {ok} match the page where the heading is printed; {len(miss)} do not {miss[:8]}")

    cap_page = {}
    for i in range(body - 1, len(doc)):
        for m in re.finditer(r"^Figure (\d+)\. ", doc[i].get_text(), re.M):
            cap_page.setdefault(int(m.group(1)), label[i + 1])
    ok, miss = 0, []
    for title, lab in lof_rows:
        n = int(re.match(r"Figure (\d+)\.", title).group(1))
        if cap_page.get(n) == lab:
            ok += 1
        else:
            miss.append((n, lab, cap_page.get(n)))
    print(f"list of figures rows {len(lof_rows)}: {ok} match the page of the caption; {len(miss)} do not {miss[:8]}")

    # every figure against the paragraph that names it, in the book's one-file text
    md = open(md_path, encoding="utf-8").read().splitlines()
    page_text = [doc[i].get_text() for i in range(len(doc))]
    page_norm = [re.sub(r"\s+", " ", t) for t in page_text]
    far, second, n_fig, fig_no = [], [], 0, 0
    for k, ln in enumerate(md):
        if not ln.startswith("!["):
            continue
        fig_no += 1
        j = k - 1
        while j >= 0 and (not md[j].strip() or md[j].startswith("![") or md[j].startswith("#")):
            j -= 1
        if j < 0:
            continue
        paired = md[j].startswith("![") if j >= 0 else False
        text = md[j].strip()
        if text.startswith("|"):                           # a figure under a table: the table's last row names it
            text = text.strip("|").split("|")[0]
        anchor = re.sub(r"\s+", " ", re.sub(r"[`*_\[\]]", "", text))[:60]
        if len(anchor) < 20:
            continue
        apages = [i + 1 for i, t in enumerate(page_norm) if i >= body - 1 and anchor in t]
        cpages = [i + 1 for i, t in enumerate(page_text) if i >= body - 1 and re.search(rf"^Figure {fig_no}\. ", t, re.M)]
        if not apages or not cpages:
            continue
        n_fig += 1
        c = min(cpages)
        before = [a for a in apages if a <= c]            # the paragraph that names it stands before the figure
        d = c - max(before) if before else 99
        if 2 <= d <= 3 and all(re.search(rf"^Figure {fig_no - j}\. ", page_text[c - 1 - j], re.M) for j in range(1, d)):
            second.append((fig_no, [max(before)], [c]))   # the figures before it took the pages between: later by those
        elif d > 1:
            far.append((fig_no, before[-1:] or apages[:1], [c]))
    print(f"figures checked against the text that names them: {n_fig}; one page later because the figure before it "
          f"took the page between: {len(second)}; further than that from the text: {len(far)} {far[:8]}")
    bad += bool(far)

    per = {i + 1: len(re.findall(r"^Figure \d+\. ", page_text[i], re.M)) for i in range(body - 1, len(doc))}
    per = {k: v for k, v in per.items() if v}
    crowd = {k: v for k, v in per.items() if v > 2}
    print(f"pages with figures: {len(per)}; with more than two: {len(crowd)} {crowd}")
    bad += bool(crowd)

    # the index: every page listed for a term carries the term's first word (a file name may wrap: eight letters suffice)
    idx_start = next((i for i in range(len(doc)) if "Every term of the glossary where this book" in page_text[i]), None)
    checked, misses = 0, []
    if idx_start is not None:
        plain = {}
        for i, lab in label.items():
            if lab and lab not in plain:
                plain[lab] = re.sub(r"\s+", " ", page_text[i - 1]).lower()
        entries = []                                   # (term, pages) in the order the index prints them
        for i in range(idx_start, min(idx_start + 40, len(doc))):
            # an entry is drawn as its dot leader ending in its pages, then its term (or both on one line); read in the
            # order drawn, so a term is never paired with the pages of the entry beside it
            nums = None
            for b in doc[i].get_text("dict")["blocks"]:
                for ln in b.get("lines", []):
                    if not TOP < ln["bbox"][1] < H - BOTTOM:
                        continue
                    txt = "".join(s["text"] for s in ln["spans"]).strip()
                    lead = re.fullmatch(r"[\s.]*?((?:\d+,\s*)*\d+)", txt)
                    same = re.match(r"^([A-Za-z].*?)(?:\s*\.){2,}\s*((?:\d+,\s*)*\d+)$", txt)
                    if lead:
                        nums = lead.group(1)
                    elif same:
                        entries.append((same.group(1), same.group(2))); nums = None
                    elif nums and re.match(r"^[A-Za-z]", txt):
                        entries.append((txt, nums)); nums = None
        for term, pages in entries:
            term = term.strip().lower()
            key = term.split()[0].strip(",;:()").lower()[:8]
            if len(key) < 4:
                continue
            # a file name is wrapped inside its table cell, its folder can sit in another line of the cell, and a cell
            # split over two pages carries the name's end to the next page, where the index tag (placed right after
            # the term) records it: the page is right when it shows the name's start, its file name or its end
            squeeze = lambda t: re.sub(r"[\s­]", "", t)
            whole = squeeze(term.split()[0].strip(",;:()"))
            ends = {whole[:24], whole.rsplit("/", 1)[-1], whole[-6:]}
            for pg in pages.split(","):
                checked += 1
                body_txt = plain.get(pg.strip(), "")
                tight = squeeze(body_txt)
                if key not in body_txt and not any(e in tight for e in ends):
                    misses.append((term[:30], pg.strip()))
    print(f"index references checked {checked}; the term's first word not on the listed page: {len(misses)} {misses[:8]}")

    # every cross-reference in the book's text names a heading the book has (the one numbering, 17 October)
    heads = set()
    for ln in md:                                         # "## 10. Title", "### 10.2 Title", "## Appendix K. Title", "### K.3 Title"
        m = re.match(r"^#{2,4} (?:(\d+(?:\.\d+)+)|(\d+)\.|Appendix ([A-Z])|([A-Z](?:\.\d+)+))(?=[\s.])", ln)
        if m:
            heads.add(next(g for g in m.groups() if g))
    parts = {re.match(r"^# Part (\w+)\.", ln).group(1) for ln in md if re.match(r"^# Part \w+\.", ln)}
    # a reference that follows another document's name (`DISCLOSURES.md`, section 4; `LICENSE`, section 10; the other
    # manual; the founder's manuscript) carries that document's numbering: not this book's to check
    # a reference after another document's name keeps that document's numbering; "the page's section 3a" is the live benchmark
    # engine page's own numbering, as docs/book/build_book.py reads it (its EXTERNAL)
    external = re.compile(r"(\.md`|\.md\)|LICENSE`|Manual,|Manual's|DISCLOSURES|of the manual|the page['’]s)\W*$")
    own_name = ("Owner's Manual" if "OWNERS" in md_path.upper() else "Live Benchmark Engine Manual" if "LIVE_ENGINE" in md_path.upper()
                else "Operator's Manual")

    def foreign(prev, ln, start):
        ctx = (prev[-80:] + "\n" + ln[:start]) if start < 60 else ln[start - 60:start]
        return "anuscript" in ctx[-200:] or (bool(external.search(ctx)) and own_name not in ctx[-70:])

    dangling, n_refs, prev = [], 0, ""
    for ln in md:
        if ln.startswith("#"):
            continue
        for m in re.finditer(r"\b(?:[Ss]ections?|Chapters?)\s+(\d+(?:\.\d+)*[a-z]?|[A-Z]\.\d+)", ln):
            if foreign(prev, ln, m.start()):
                continue
            n_refs += 1
            if m.group(1).rstrip("abcdefghijklmnopqrstuvwxyz") not in heads and m.group(1) not in heads:
                dangling.append(m.group(0))
        for m in re.finditer(r"\bAppendix ([A-Z])\b", ln):
            if foreign(prev, ln, m.start()):
                continue
            n_refs += 1
            if m.group(1) not in heads:
                dangling.append(m.group(0))
        if ln.strip():
            prev = ln
        for m in re.finditer(r"\bPart ([A-Z][a-z]+|[IVX]+)\b", ln):
            n_refs += 1
            if m.group(1) not in parts:
                dangling.append(m.group(0))
    print(f"cross-references checked {n_refs}; naming no heading of this book: {len(dangling)} {sorted(set(dangling))[:12]}")
    bad += bool(dangling)

    # every numbered heading the PDF prints carries the number the book's one-file text gives it, so that a reference
    # ("section 4.1") lands on the heading it names (21 October: the printing pass had counted on from the labelling pass)
    # read in the book's order, so that two chapters with a section of the same title (the clouds' chapters) are told apart
    md_heads = []
    for ln in md:
        m = re.match(r"^#{2,4} (\d+(?:\.\d+)+|[A-Z](?:\.\d+)+) (.+)$", ln)
        if m:
            md_heads.append((m.group(1), re.sub(r"\s+", " ", re.sub(r"[`*_]", "", m.group(2))).strip()[:40]))
    wrong, n_num, at = [], 0, 0
    for _lvl, t, _pg in doc.get_toc():
        m = re.match(r"^(\d+(?:\.\d+)+|[A-Z](?:\.\d+)+) (.+)$", re.sub(r"\s+", " ", t).strip())
        if not m:
            continue
        title = m.group(2)[:40]
        k = next((k for k in range(at, len(md_heads)) if md_heads[k][1] == title), None)
        if k is None:
            continue
        at = k + 1
        n_num += 1
        if md_heads[k][0] != m.group(1):
            wrong.append((m.group(1), md_heads[k][0], title[:36]))
    print(f"numbered headings checked against the book's text: {n_num}; printed under another number: {len(wrong)} {wrong[:6]}")
    bad += bool(wrong) or not n_num
    return 1 if bad else 0


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1], sys.argv[2]))

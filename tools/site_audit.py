#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The graded audit of every page the company shows (the founder's order of 1 November, night: "a grading audit ... across
this whole website, every domain, every file, every sub file ... every page, every landing page, every text, every tone,
every document that's in their links, and make sure links are great").

Every page of the repository a reader can open (every Markdown and HTML file a clone carries, the raw receipts and the built
book's intermediate files aside, which are records and a build's output) is read and graded on what can be checked to the
letter:

- **the notice**: the legal notice at the top and the end, in the founder's wording (`tools/legal.py`);
- **the links**: every link to another page or file of the repository points at one that exists;
- **the anchors**: every link to a heading or an element (`#name`), on the same page or another, finds it (GitHub's own rule
  for a heading's name);
- **the outside links**: every link off the repository is written in full and secure (`https://`), never to a machine's own
  address;
- **the engine**: no page of the newest material calls an older engine the one that stands (`tools/layout_check.py`).

A page reads **A** with nothing found; **B** with an outside link that is not secure; **C** with an anchor that finds nothing;
**D** with a link to a page or file that does not exist; **F** without the notice, or calling an older engine the one that
stands. Each finding is written with its fix. The company's website (www.omni-compass.com) is built outside this repository;
its pages are graded here only when this machine can reach them, and a page that cannot be reached is said so, never graded.

    python3 tools/site_audit.py            writes docs/SITE_AUDIT.md and results/SITE_AUDIT.json
    python3 tools/site_audit.py --check    fails when any page reads below A
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
import unicodedata
from collections import Counter, OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))
from tools.legal import stamp, TOP  # noqa: E402
from tools import legal  # noqa: E402
import layout_check as LC  # noqa: E402

OUT_MD = ROOT / "docs" / "SITE_AUDIT.md"
OUT_JSON = ROOT / "results" / "SITE_AUDIT.json"
SKIP = ("results/live/raw/", "release/", "results/external_review/", "archive/")
BUILT = ("docs/book/OMNI_COMPASS_BOOK.md", "docs/book/OMNI_COMPASS_OWNERS_BOOK.md", "docs/book/OMNI_COMPASS_LIVE_ENGINE_BOOK.md")
GRADES = {"notice": "F", "engine": "F", "link": "D", "anchor": "C", "outside": "B"}
ORDER = "ABCDF"
MD_LINK = re.compile(r"(?<!\!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
MD_IMG = re.compile(r"\!\[[^\]]*\]\(([^)\s]+)\)")
HREF = re.compile(r"""(?:href|src)\s*=\s*["']([^"'<>{}$`]+)["']""", re.I)
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
EXPLICIT = re.compile(r"""<a\s+(?:[^>]*?\s)?(?:id|name)\s*=\s*["']([^"']+)["']""", re.I)
HTML_ID = re.compile(r"""\sid\s*=\s*["']([^"'<>{}$`]+)["']""", re.I)


def slug(text: str) -> str:
    """A heading's anchor as GitHub writes it: the text without its markup, lower case, every character that is not a
    letter, a mark, a number, an underscore, a space or a hyphen dropped, every space a hyphen."""
    t = re.sub(r"`([^`]*)`", r"\1", text)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    t = re.sub(r"<[^>]+>", "", t)
    t = t.replace("**", "").replace("__", "")
    t = re.sub(r"(?<!\w)[*_](.+?)[*_](?!\w)", r"\1", t)
    t = t.strip().lower()
    out = []
    for ch in t:
        cat = unicodedata.category(ch)
        if cat[0] in "LMN" or ch in "_- ":
            out.append("-" if ch == " " else ch)
    return "".join(out)


def anchors_md(text: str) -> set:
    """Every anchor a Markdown page offers: its headings (a repeated heading takes -1, -2 ...) and its explicit anchors."""
    seen, out, fence = Counter(), set(), False
    for ln in text.splitlines():
        if ln.lstrip().startswith("```"):
            fence = not fence
            continue
        if fence:
            continue
        m = HEADING.match(ln)
        if m:
            s = slug(m.group(2))
            out.add(s if not seen[s] else f"{s}-{seen[s]}")
            seen[s] += 1
    out |= set(EXPLICIT.findall(text))
    out |= set(HTML_ID.findall(text))
    return out


def anchors_html(text: str) -> set:
    return set(HTML_ID.findall(text)) | set(re.findall(r"""\sname\s*=\s*["']([^"']+)["']""", text, re.I))


def pages(files) -> list:
    return [p for p in files if p.endswith((".md", ".html")) and not p.startswith(SKIP) and p not in BUILT
            and (ROOT / p).is_file()]


def norm(base: Path, target: str) -> str:
    parts = []
    for x in Path((base / target).as_posix()).parts:
        if x == "..":
            parts = parts[:-1]
        elif x != ".":
            parts.append(x)
    return "/".join(parts)


def links_of(p: str, text: str) -> list:
    if p.endswith(".md"):
        body = LC.prose_only(text)
        return MD_LINK.findall(body) + MD_IMG.findall(body) + HREF.findall(body)
    body = re.sub(r"<script\b[^>]*>.*?</script>", "", text, flags=re.S | re.I)   # a script's strings are code, not links
    body = re.sub(r"<style\b[^>]*>.*?</style>", "", body, flags=re.S | re.I)
    return [html.unescape(x) for x in HREF.findall(body)]


def audit() -> dict:
    files = LC.tracked()
    present = set(files)
    dirs = {str(Path(f).parents[i]) for f in files for i in range(len(Path(f).parents) - 1)}
    raw = LC.raw_branch()
    if raw is None:
        dirs.add("results/live/raw")
    else:
        present |= set(raw)
        dirs |= {str(Path(f).parents[i]) for f in raw for i in range(len(Path(f).parents) - 1)}
    found = OrderedDict((p, []) for p in pages(files))
    cache = {}

    def offered(q: str):
        if q not in cache:
            f = ROOT / q
            try:
                t = f.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                t = ""
            cache[q] = anchors_md(t) if q.endswith(".md") else anchors_html(t) if q.endswith(".html") else None
        return cache[q]

    for line in legal.check():
        p, _, why = line.partition(": ")
        if p in found:
            found[p].append(("notice", why, "python3 tools/legal.py --fix"))
    for line in LC.stale_engine(list(found)):
        m = re.match(r"engine: ([^:]+):(\d+) (.*)", line)
        if m and m.group(1) in found:
            found[m.group(1)].append(("engine", f"line {m.group(2)}: {m.group(3)}", "name the engine that stands"))
    for p in found:
        text = (ROOT / p).read_text(encoding="utf-8", errors="ignore")
        base = Path(p).parent
        own = anchors_md(text) if p.endswith(".md") else anchors_html(text)
        for t in links_of(p, text):
            t = t.strip("<>")
            if not t or t.startswith(("javascript:", "data:", "tel:", "mailto:")):
                continue
            if "://" in t:
                if t.startswith("http://") and not re.match(r"http://(www\.)?w3\.org/", t):
                    found[p].append(("outside", f"{t[:120]} is not secure", "write it as https://"))
                if re.match(r"https?://(localhost|127\.0\.0\.1|0\.0\.0\.0)", t):
                    found[p].append(("outside", f"{t[:120]} points at a machine's own address", "link the page a reader can open"))
                continue
            if t.startswith("//") or t.startswith("/"):
                continue                                   # a site-absolute path is the site's own, not a file of this tree
            path, _, frag = t.partition("#")
            path = path.split("?")[0]
            if p.endswith(".md") and path and not any(c in path for c in "./") and not (ROOT / base / path).exists():
                continue                                   # a formula's argument read as a link (tools/layout_check.py's rule)
            if not path:
                if frag and frag not in own and not frag.startswith(("L", ":~:")):
                    found[p].append(("anchor", f"#{frag} finds no heading or element on this page", "point it at the heading's own name"))
                continue
            q = norm(base, path)
            if q not in present and q not in dirs:
                found[p].append(("link", f"{t[:120]} (no such file)", "point it at the file that exists, or remove it"))
                continue
            if frag and q in present and not re.fullmatch(r"L\d+(-L\d+)?", frag):
                got = offered(q)
                if got is not None and frag not in got:
                    found[p].append(("anchor", f"{t[:120]}: {q} has no #{frag}", "point it at the heading's own name"))
    graded = OrderedDict()
    for p, fs in found.items():
        g = max((GRADES[k] for k, *_ in fs), key=ORDER.index, default="A")
        graded[p] = {"grade": g, "findings": [{"kind": k, "what": w, "fix": f} for k, w, f in fs]}
    return graded


def audit_published(html_path: Path, files: list, url: str) -> dict:
    """A published copy of the live engine (a claude.ai artifact or any host), read from its saved HTML and the list of the
    files published beside it: the same rules as a repository page, plus the engine it names against the engine that stands
    and whether it carries the self-update (docs/engine/build_live_engine.py, the founder's order of 1 November)."""
    t = html_path.read_text(encoding="utf-8", errors="ignore")
    sys.path.insert(0, str(ROOT / "tools"))
    from omni_version import VERSIONS
    stands = "omni-" + next(iter(VERSIONS))
    body = re.sub(r"<script\b[^>]*>.*?</script>", "", t, flags=re.S | re.I)
    body = re.sub(r"<style\b[^>]*>.*?</style>", "", body, flags=re.S | re.I)
    ids = anchors_html(t)
    found = []
    if "The Omni-Compass LLC" not in t[:20000] or "© 2026" not in t[:20000]:
        found.append(("notice", "the notice does not open the page", "republish from the newest build"))
    tail = re.sub(r"<script\b[^>]*>.*?</script>", "", t[-60000:], flags=re.S | re.I)
    if "www.omni-compass.com" not in tail:
        found.append(("notice", "the notice does not close the page", "republish from the newest build"))
    for h in (html.unescape(x) for x in HREF.findall(body)):
        if h.startswith("#"):
            if h[1:] and h[1:] not in ids:
                found.append(("anchor", f"{h} finds no element on the page", "point it at the element's own id"))
        elif "://" in h:
            if h.startswith("http://"):
                found.append(("outside", f"{h[:120]} is not secure", "write it as https://"))
        elif not h.startswith(("mailto:", "tel:", "data:", "javascript:")) and h.split("#")[0].split("?")[0] not in files:
            found.append(("link", f"{h[:120]} is not among the files published with it", "publish the file, or remove the link"))
    named = sorted(set(re.findall(r'data-engine="(omni-v\d+)"', t)))
    if named != [stands]:
        found.append(("engine", f"it names {', '.join(named) or 'no engine'}; the engine that stands is {stands}",
                      "republish it from the newest build (docs/engine/build_live_engine.py)"))
    if "omniSelfUpdate" not in t:
        found.append(("engine", "it does not carry the self-update, so it keeps the build it was published with until it is "
                      "published again", "republish it from the newest build, which carries the self-update"))
    g = max((GRADES[k] for k, *_ in found), key=ORDER.index, default="A")
    return {"url": url, "grade": g, "engine": named, "self_update": "omniSelfUpdate" in t, "files": len(files),
            "findings": [{"kind": k, "what": w, "fix": f} for k, w, f in found]}


def page(graded: dict, site: dict) -> list:
    n = Counter(v["grade"] for v in graded.values())
    L = ["# The graded audit of every page", "", f"> {TOP}", "",
         "Written by `python3 tools/site_audit.py` from the pages themselves (the founder's order of 1 November): every page of "
         "the repository a reader can open, Markdown and HTML, read for its notice, its links, its anchors, its outside links and "
         "the engine it calls the one that stands. **A** nothing found; **B** an outside link that is not secure; **C** an anchor "
         "that finds nothing; **D** a link to a page or file that does not exist; **F** no notice, or an older engine called the "
         "one that stands. The raw receipts and the built books' intermediate files are records and a build's output, not pages, "
         "and are not graded. What cannot be checked to the letter (the tone, a sentence's clarity) is the referee's own reading "
         "and is not graded here.", "",
         "## The grades", "",
         f"**{len(graded):,} pages read: " + ", ".join(f"{g} {n.get(g, 0):,}" for g in ORDER) + ".**", "",
         "## The company's website", "", site["words"], ""]
    for pub in site.get("published") or []:
        L += [f"### {pub['grade']}: the live engine as published at {pub['url']}", "",
              f"Read from its saved page and the {pub['files']} files published beside it, by the same rules (engine named: "
              f"{', '.join(pub['engine']) or 'none'}; the self-update {'carried' if pub['self_update'] else 'not carried'}).", ""]
        L += [f"- **{f['kind']}**: {f['what']}. Fix: {f['fix']}." for f in pub["findings"]] or ["- Nothing found."]
        L.append("")
    low = [(p, v) for p, v in graded.items() if v["grade"] != "A"]
    L += ["## Every page below A, with its findings and their fixes", ""]
    if not low:
        L += ["None: every page reads A.", ""]
    for p, v in sorted(low, key=lambda kv: (-ORDER.index(kv[1]["grade"]), kv[0])):
        L += [f"### {v['grade']}: `{p}`", ""]
        for f in v["findings"]:
            L.append(f"- **{f['kind']}**: {f['what']}. Fix: {f['fix']}.")
        L.append("")
    L += ["## Every page that reads A", "", ", ".join(f"`{p}`" for p, v in graded.items() if v["grade"] == "A") + ".", ""]
    return L


SITE_WORDS = ("**www.omni-compass.com is not graded here**: this machine's network does not reach it (the session's network "
              "settings deny the host), so none of its pages, links or documents was read, and no grade is written for it. "
              "When the host is allowed, its every page and link is read by the same rules and graded on this page.")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--published", help="a published copy of the live engine, saved as HTML, to grade beside the repository")
    ap.add_argument("--files", default="", help="the files published beside it, comma-separated")
    ap.add_argument("--url", default="", help="where it is published")
    a = ap.parse_args(argv)
    graded = audit()
    low = {p: v for p, v in graded.items() if v["grade"] != "A"}
    if a.check:
        for p, v in low.items():
            for f in v["findings"]:
                print(f"{v['grade']} {p}: {f['kind']}: {f['what']}")
        print(f"site audit: {len(graded)} pages, {len(low)} below A: " + ("FAIL" if low else "PASS"))
        return 1 if low else 0
    site = {"reached": False, "words": SITE_WORDS, "published": []}
    if a.published:
        site["published"].append(audit_published(Path(a.published), [x for x in a.files.split(",") if x], a.url))
    elif OUT_JSON.exists():                                  # a published copy graded before stays on the page until read again
        site["published"] = (json.loads(OUT_JSON.read_text()).get("website") or {}).get("published") or []
    OUT_MD.write_text("\n".join(stamp(page(graded, site))) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps({"notice": legal.SHORT, "pages": graded, "website": site}, indent=1) + "\n", encoding="utf-8")
    n = Counter(v["grade"] for v in graded.values())
    print(f"{OUT_MD.relative_to(ROOT)}: {len(graded)} pages, " + ", ".join(f"{g} {n.get(g, 0)}" for g in ORDER))
    return 0


if __name__ == "__main__":
    sys.exit(main())

# © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

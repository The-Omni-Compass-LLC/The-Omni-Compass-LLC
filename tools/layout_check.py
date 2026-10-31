#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The repository stays lined up: run by verify.py on every release, so a push that leaves the tree out of line fails.

Checks:
  root      the root holds only the declared set (ROOT_ALLOWED): the front door, the license and IP papers, the
            build files. Anything else belongs under docs/, .github/ or a code folder.
  links     every relative link in every Markdown file points at a file or folder that exists.
  paths     every repository path a Markdown file names in backticks (`results/...`, `docs/...`, `tools/...`, ...)
            exists, so no page cites a file that has gone.
  orphans   every top-level entry of results/ is named by some page or program outside results/, so a result nothing
            uses falls off instead of piling up.
  engine    every page of the newest material that names the engine that stands names the newest one in
            tools/omni_version.py (VERSIONS, newest first), so no page is left calling an older engine the one that
            stands; the history, the receipts, the change log, each older engine's own page and the referees' reports (which quote
            the page they read, docs/engine/audit_*/) keep the words of their day.

  python3 tools/layout_check.py        (exit 0: lined up; exit 1: what is out of line, one line each)
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROOT_ALLOWED = {
    # the front door
    "README.md", "CHANGELOG.md", "CITATION.cff", "SECURITY.md",
    # a person's own system for the Monte Carlo 500 (the live engine's button, monte-carlo.yml)
    "systems",
    # the license and the intellectual property
    "LICENSE", "LICENSES", "NOTICE", "PATENTS.md", "TRADEMARKS.md", "THIRD_PARTY_NOTICES.md", "REUSE.toml",
    "DISCLOSURES.md", "LICENSING_FAQ.md", "ENTERPRISE_LICENSE.md", "CLAUDE.md",
    # the same rules for every AI assistant that reads this repository (Codex, Copilot, Gemini, Cursor)
    "AGENTS.md", "GEMINI.md", ".cursorrules", "llms.txt",   # llms.txt: read by AI crawlers at the root, the notice in it
    # build, verification and metadata
    "pyproject.toml", "requirements.txt", "requirements-lock.txt", "verify.py", "RELEASE_MANIFEST.json", "OMNI_V1.json", "OMNI_V2.json", "OMNI_V3.json", "OMNI_V5.json", "OMNI_V6.json", "OMNI_V7.json", "OMNI_V8.json", "OMNI_V9.json", "OMNI_V10.json", "OMNI_V11.json", "OMNI_V12.json", "OMNI_V13.json", "OMNI_V14.json", "OMNI_V15.json", "OMNI_V16.json", "OMNI_V17.json", "OMNI_V18.json", "OMNI_V19.json", "OMNI_V20.json", "OMNI_V21.json", "OMNI_V22.json", "OMNI_V23.json", "codemeta.json",
    "docker-compose.yml", ".gitignore", ".gitattributes", ".dockerignore", ".github", ".fossa.yml", ".snyk",
    # code and evidence
    "omnicompass", "omni_controller", "omni_orchestrator", "realms", "cpp", "tools", "scripts", "tests", "deploy", "fleet", "pilot",
    "k8s_controlplane", "k8s_fleet", "omnilab", "hardware", "benchmarks", "tuning", "reference", "fixtures", "sbom",
    "results", "docs", "release",
}
PATH_PREFIXES = ("results/", "docs/", "tools/", "scripts/", "realms/", "omnicompass/", "omni_controller/", "tests/",
                 ".github/", "deploy/", "tuning/", "cpp/")
LINK = re.compile(r"\]\(([^)\s#]+)(?:#[^)]*)?\)")
TICK = re.compile(r"`([A-Za-z0-9_.\-/]+)`")


def prose_only(text: str) -> str:
    """The page without its code: fenced blocks, indented code blocks and `inline code` carry no links, so an equation
    written with a bracket subscript, f[U](x), is not read as one."""
    out, fence = [], False
    for ln in text.split("\n"):
        if ln.lstrip().startswith("```"):
            fence = not fence
            continue
        if fence or (ln.startswith("    ") and not re.match(r"^\s*(-|\*|\d+\.) ", ln)):
            continue
        out.append(re.sub(r"`[^`]*`", "`", ln))
    return "\n".join(out)


STANDS = [re.compile(r"\b[Oo]mni[- ]v(\d+)\b\**`?\)?[^.;()]{0,25}\bstands\b(?! (?:as|for|with|in|at|beside))"),
          re.compile(r"stands on main[^.;]{0,20}[Oo]mni[- ]v(\d+)"),
          re.compile(r"\bthe (?:newest )?engine (?:on main|that stands)[^.;]{0,15}?\b[Oo]mni[- ]v(\d+)"),   # the first engine named after it
          re.compile(r"[Ee]ngine that stands[,:]?\s*\(?\**`?omni-v(\d+)")]


def stale_engine(files):
    """Pages of the newest material that call an older engine the one that stands."""
    sys.path.insert(0, str(ROOT / "tools"))
    from omni_version import VERSIONS                       # newest first
    newest = next(iter(VERSIONS)).lstrip("v")
    own_page = f"docs/OMNI_V{newest}.md"
    out = []
    for p in files:
        if p.startswith(("results/", "release/", "docs/history/", "archive/", "OMNI_V", "docs/engine/audit_")) or p in ("CHANGELOG.md", "RELEASE_MANIFEST.json") \
                or not p.endswith((".md", ".py", ".txt", ".yml", ".yaml", ".cff", ".toml")) \
                or (re.match(r"docs/OMNI_V\d+(_PLAN)?\.md$", p) and p != own_page):
            continue
        for i, ln in enumerate((ROOT / p).read_text(errors="ignore").splitlines(), 1):
            for pat in STANDS:
                for m in pat.finditer(ln):
                    if m.group(1) != newest:
                        out.append(f"engine: {p}:{i} calls omni-v{m.group(1)} the engine that stands (the newest is omni-v{newest})")
    return sorted(set(out))


def tracked():
    out = subprocess.run(["git", "-c", "safe.directory=*", "ls-files"], cwd=ROOT, capture_output=True, text=True).stdout
    return [p for p in out.splitlines() if p]


def raw_branch():
    """The raw receipts' files as the pages name them (results/live/raw/...), read from the branch raw's trees
    (scripts/raw_archive.sh fetch), or None when the branch is not fetched."""
    for ref in ("refs/remotes/origin/raw", "refs/heads/raw"):
        r = subprocess.run(["git", "-c", "safe.directory=*", "ls-tree", "-r", "--name-only", ref], cwd=ROOT,
                           capture_output=True, text=True)
        if r.returncode == 0 and r.stdout.strip():
            return ["results/live/raw/" + x for x in r.stdout.splitlines() if x]
    return None


def main():
    files = tracked()
    present = set(files)
    dirs = {str(Path(p).parents[i]) for p in files for i in range(len(Path(p).parents) - 1)}
    problems = []
    # a path a page names under results/live/raw/ is checked against the branch raw, where the receipts live (18 October)
    raw = raw_branch()
    if raw is None:
        problems.append("raw: the branch raw is not fetched, so the receipts' paths cannot be checked (bash scripts/raw_archive.sh fetch)")
        dirs.add("results/live/raw")
    else:
        present |= set(raw)
        dirs |= {str(Path(p).parents[i]) for p in raw for i in range(len(Path(p).parents) - 1)}
    for top in sorted({p.split("/")[0] for p in files}):
        if top not in ROOT_ALLOWED:
            problems.append(f"root: {top} is not in the declared root set (move it under docs/, .github/ or a code folder)")
    for p in files:
        if not p.endswith(".md") or p.startswith(("results/live/raw/", "release/", "results/external_review/")) \
                or p in ("docs/book/OMNI_COMPASS_BOOK.md", "docs/book/OMNI_COMPASS_OWNERS_BOOK.md"):            # quoted reviews; the book is built (build_book.py)
            continue
        text = (ROOT / p).read_text(errors="ignore")
        base = Path(p).parent
        for m in LINK.finditer(prose_only(text)):
            t = m.group(1)
            if "://" in t or t.startswith(("mailto:", "/")):
                continue
            if not any(c in t for c in "./") and not (ROOT / base / t).exists():
                continue                   # a formula's argument, u[req](k), read as a link: no file has neither a dot nor a slash
            q = (base / t).as_posix()
            q = str(Path(q)).replace("\\", "/")
            norm = Path(*[x for x in Path(q).parts])
            parts = []
            for x in norm.parts:
                if x == "..":
                    parts = parts[:-1]
                elif x != ".":
                    parts.append(x)
            q = "/".join(parts)
            if q and q not in present and q not in dirs:
                problems.append(f"link: {p} -> {t} (no such file)")
        for m in TICK.finditer(text):
            t = m.group(1).rstrip("/.")
            last = t.rsplit("/", 1)[-1]
            if "." in last and not re.search(r"\.(md|py|sh|json|csv|txt|yml|yaml|toml|cpp|hpp|h|pdf|png|jsonl|gz|zip|cff)$", last):
                continue                                         # a module attribute (pkg/module.name), not a file
            if t.startswith(PATH_PREFIXES) and "*" not in t and "<" not in t and "STAMP" not in t:
                if t not in present and t not in dirs:
                    problems.append(f"path: {p} names `{t}` (no such file)")
    corpus = "\n".join((ROOT / p).read_text(errors="ignore") for p in files
                       if not p.startswith(("results/", "release/")) and p != "RELEASE_MANIFEST.json"
                       and p not in ("docs/book/OMNI_COMPASS_BOOK.md", "docs/book/OMNI_COMPASS_OWNERS_BOOK.md") and p.endswith((".md", ".py", ".sh", ".yml", ".yaml", ".toml", ".json", ".txt")))
    for top in sorted({p.split("/")[1] for p in files if p.startswith("results/") and p.count("/") >= 1}):
        stem = top.rsplit(".", 1)[0] if "." in top else top
        if top.startswith("VERIFY_") or (f"results/{top}" not in corpus and f"results/{stem}" not in corpus and f'"{top}"' not in corpus
                                         and f"'{top}'" not in corpus and top not in corpus
                                         and not (re.sub(r"\d+$", "", top) != top and re.sub(r"\d+$", "", top) in corpus)):
            if not top.startswith("VERIFY_"):
                problems.append(f"orphan: results/{top} is named by no page or program (remove it, or cite it)")
    problems += stale_engine(files)
    for x in problems:
        print(x)
    print(f"layout: {len(problems)} out of line" if problems else "layout: lined up")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())

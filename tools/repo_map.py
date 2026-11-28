#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License or, for a pilot, a signed, paid pilot agreement. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The map of the repository: every file its map ID, its anchor, its owner, how it carries the owner's notice, its role and
the engine it belongs to (the founder's order of 28 November: "check every file, align, map everything so everything has
its map ID tag ... anchor it", each file named as the property of its owner).

A map ID is OC-<AREA>-<NNNNN> (OC-DOC-00042: the 42nd file of docs/). It is given once and never changes: a file keeps its
ID for as long as it lives, a new file takes the next number of its area, and a file that leaves the repository keeps its
ID in the register's retired list, so no ID is ever given twice. Each ID is an anchor on its area's page
(docs/map/<AREA>.md#oc-doc-00042), so any page, receipt or letter can point at one file by its ID.

  python3 tools/repo_map.py            give every tracked file its ID and write results/REPO_MAP.json and docs/map/
  python3 tools/repo_map.py --check    exit 1 if an ID is malformed or given twice, a file's ID moved, or the pages are not
                                       what the register gives; files added since the last write are counted, not failed
                                       (a bot's new page takes its ID at the next write)
"""
from __future__ import annotations

import argparse, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import legal  # noqa: E402

REGISTER = ROOT / "results" / "REPO_MAP.json"
PAGES = ROOT / "docs" / "map"
OWNER = "Dubra Software Inc. / The Omni-Compass LLC"
ROWS_PER_PAGE = 900
AREAS = {"": "ROOT", ".github": "GH", "docs": "DOC", "results": "RES", "tests": "TST", "tools": "TOOL", "tuning": "TUNE",
         "deploy": "DEP", "scripts": "SCR", "cpp": "CPP", "omnicompass": "ENG", "omni_controller": "CTL",
         "omni_orchestrator": "ORC", "realms": "RLM", "k8s_controlplane": "K8S", "fleet": "FLT", "omnilab": "LAB",
         "hardware": "HW", "benchmarks": "BEN", "pilot": "PIL", "k8s_fleet": "K8F", "systems": "SYS", "sbom": "SBOM",
         "release": "REL", "reference": "REF", "fixtures": "FIX", "LICENSES": "LIC"}
ID_RE = re.compile(r"^OC-[A-Z0-9]+-\d{5}$")
THIRD_PARTY = ("tests/third_party/", "fleet/traces/planetlab/", "k8s_controlplane/traces/planetlab/")


def area_of(path: str) -> str:
    top = path.split("/", 1)[0] if "/" in path else ""
    return AREAS.get(top) or re.sub(r"[^A-Z0-9]", "", top.upper())[:5] or "MISC"


def section_of(path: str) -> str:
    """The page a file is listed on: its area, and for docs/ and results/ the folder under it."""
    parts = path.split("/")
    if parts[0] in ("docs", "results") and len(parts) > 2:
        return f"{parts[0]}/{parts[1]}"
    return parts[0] if len(parts) > 1 else "(root)"


def tracked() -> list[str]:
    return [p for p in legal.tracked(ROOT) if "__pycache__" not in p]


ENGINE = None


def engine_files() -> dict:
    """The engine that stands and its fingerprinted files (tools/omni_version.py)."""
    global ENGINE
    if ENGINE is None:
        versions = sorted(ROOT.glob("OMNI_V*.json"), key=lambda p: int(re.sub(r"\D", "", p.stem) or 0))
        d = json.loads(versions[-1].read_text(encoding="utf-8"))
        ENGINE = (d.get("version") or versions[-1].stem.lower().replace("_", "-"), set(d.get("files") or {}))
    return ENGINE


def engine_of(path: str) -> str:
    name = path.rsplit("/", 1)[-1]
    standing, files = engine_files()
    if path in files:
        return f"{standing} engine file (fingerprinted)"
    m = re.match(r"^OMNI_V(\d+)\.(json|md)$", name)
    if m:
        return f"omni-v{m.group(1)}"
    m = re.match(r"^V(\d+)_", name) or re.search(r"(?:^|_)OMNI_V(\d+)(?:[._]|$)", name)
    if m and path.startswith(("results/", "docs/")):
        return f"omni-v{m.group(1)}"
    return ""


KIND_ROLE = {"log": "log", "jsonl": "log (JSON lines)", "err": "error log", "yaml": "configuration (YAML)",
             "yml": "configuration (YAML)", "webm": "video", "docx": "document (Word)", "xlsx": "spreadsheet",
             "pptx": "slides", "txt": "text", "py": "program (Python)", ".gitignore": "files git leaves out",
             ".gitattributes": "how git treats each kind of file", ".dockerignore": "files a container build leaves out",
             ".cursorrules": "instructions for an AI coding assistant, the notice first", ".snyk": "the Snyk scanner's settings",
             ".fossa.yml": "the FOSSA scanner's settings"}


def role_of(path: str) -> str:
    """What the file is, in its own words: a page's title, a program's first docstring line, a workflow's name."""
    p = ROOT / path
    name = path.rsplit("/", 1)[-1]
    suffix = name.rsplit(".", 1)[-1].lower() if "." in name else ""
    binary = {"pdf": "document (PDF)", "png": "image", "jpg": "image", "jpeg": "image", "gif": "image", "svg": "figure (SVG)",
              "zip": "archive", "gz": "archive", "parquet": "data (Parquet)", "woff2": "font", "ttf": "font", "mp3": "audio",
              "mp4": "video", "wav": "audio", "npz": "data (NumPy)", "npy": "data (NumPy)", "ico": "icon"}
    if suffix in binary:
        return binary[suffix]
    try:
        head = p.read_bytes()[:8192].decode("utf-8", errors="replace")
    except OSError:
        return ""
    role = ""
    if name in ("LICENSE", "NOTICE") or path.startswith("LICENSES/"):
        role = next((l.strip() for l in head.splitlines() if l.strip()), "")
    elif suffix == "md" or name == "README":
        m = re.search(r"^#{1,2} +(.+)$", head, re.M)
        role = m.group(1) if m else ""
    elif suffix == "py":
        m = re.search(r'^(?:[ \t]*#[^\n]*\n|[ \t]*\n|from __future__[^\n]*\n)*\s*[rubRUB]?("""|\'\'\')\s*(.+?)(?:\n\s*\n|\1)', head, re.S)
        role = m.group(2) if m else ""
    elif suffix in ("yml", "yaml"):
        m = re.search(r"^name:\s*(.+)$", head, re.M)
        role = ("workflow: " + m.group(1).strip().strip("'\"")) if (m and path.startswith(".github/workflows/")) else (m.group(1) if m else "")
    elif suffix == "html":
        m = re.search(r"<title>(.*?)</title>", head, re.S | re.I)
        role = ("page: " + m.group(1)) if m else "page (HTML)"
    elif suffix == "json":
        m = re.search(r'"(?:title|name|claim|benchmark)"\s*:\s*"([^"]{3,200})"', head)
        role = ("data: " + m.group(1)) if m else "data (JSON)"
    elif suffix in ("csv", "tsv"):
        role = "data table (" + suffix.upper() + ")"
    elif suffix in ("sh", "bash", "cpp", "hpp", "h", "c", "txt", "toml", "cfg", "ini", "js", "ts", "") or head.startswith("#!"):
        for line in head.splitlines():
            t = line.strip().lstrip("#/*; ").strip()
            low = t.lower()
            if not t or t.startswith("!") or any(k in low for k in ("spdx", "copyright", "evaluation and simulation",
                                                                         "enterprise license", "all patents", "see license")):
                continue
            role = t
            break
    role = re.sub(r"\s+", " ", role).strip()
    if not role:
        role = KIND_ROLE.get(suffix) or KIND_ROLE.get(name, "") or ("program (Python)" if suffix == "py" else "file")
    return role[:140] + ("…" if len(role) > 140 else "")


def carried(path: str, locked: set) -> tuple[str, str]:
    """(owner, how the file carries the owner's notice)."""
    if path.startswith(THIRD_PARTY):
        return "third party (its own authors)", "its own notice (REUSE.toml names its authors)"
    if path in locked:
        return OWNER, "locked by a fingerprint: its notice as it stood when sealed; REUSE.toml and the LICENSE"
    try:
        text = (ROOT / path).read_text(encoding="utf-8")[:4096]
    except (OSError, UnicodeDecodeError):
        text = None
    k = legal.kind(path, text)
    if text and "Evaluation and Simulation use only" in text and "Dubra Software Inc." in text:
        return OWNER, "the notice in the file"
    if k is None:
        return OWNER, "REUSE.toml and the LICENSE (a data or binary file)"
    return OWNER, "the notice in the file"


def load() -> dict:
    if REGISTER.exists():
        return json.loads(REGISTER.read_text(encoding="utf-8"))
    return {"owner": OWNER, "files": {}, "retired": {}}


def assign(reg: dict, paths: list[str]) -> dict:
    """Keep every ID already given; give each new file its area's next number; retire the IDs of files that left."""
    files, retired = reg.setdefault("files", {}), reg.setdefault("retired", {})
    used = {}
    for e in list(files.values()) + list(retired.values()):
        a, n = e["id"].rsplit("-", 1)
        used[a] = max(used.get(a, 0), int(n))
    live = set(paths)
    for path in [p for p in files if p not in live]:
        retired[path] = {"id": files.pop(path)["id"]}
    locked = legal.locked(ROOT)
    for path in sorted(paths):
        if path in files:
            e = files[path]
        else:
            a = "OC-" + area_of(path)
            used[a] = used.get(a, 0) + 1
            e = files[path] = {"id": f"{a}-{used[a]:05d}"}
            retired.pop(path, None)
        owner, how = carried(path, locked)
        e.update({"owner": owner, "notice": how, "role": role_of(path), "engine": engine_of(path)})
    reg["owner"] = OWNER
    reg["files"] = dict(sorted(files.items(), key=lambda kv: kv[1]["id"]))
    reg["retired"] = dict(sorted(retired.items(), key=lambda kv: kv[1]["id"]))
    return reg


def cell(s: str) -> str:
    return (s or "").replace("|", "\\|").replace("<", "&lt;").replace(">", "&gt;")


def slug(section: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "_", section).strip("_").upper() or "ROOT"


def pages(reg: dict) -> dict:
    """{page name: text}: the index and one page a section (cut into parts of ROWS_PER_PAGE rows)."""
    by = {}
    for path, e in reg["files"].items():
        by.setdefault(section_of(path), []).append((path, e))
    out, index = {}, []
    for section in sorted(by, key=lambda s: (s != "(root)", s.lower())):
        rows = sorted(by[section], key=lambda pe: pe[1]["id"])
        parts = [rows[i:i + ROWS_PER_PAGE] for i in range(0, len(rows), ROWS_PER_PAGE)]
        for k, part in enumerate(parts, 1):
            name = slug(section) + (f"_{k}" if len(parts) > 1 else "") + ".md"
            title = f"{section}" + (f", part {k} of {len(parts)}" if len(parts) > 1 else "")
            L = [f"# The map: {title}", "",
                 f"Every file below is the property of {OWNER} unless its row names a third party, and carries the owner's "
                 "notice as its row says. The ID is the file's map ID, given once and never changed; each is an anchor: "
                 f"`docs/map/{name}#<id in lower case>`. Written by `tools/repo_map.py` from `results/REPO_MAP.json`; back to "
                 "[the map's index](README.md).", "",
                 "| Map ID | File | What it is | Engine | Owner | How it carries the owner's notice |",
                 "|---|---|---|---|---|---|"]
            for path, e in part:
                L.append(f'| <a id="{e["id"].lower()}"></a>{e["id"]} | [`{cell(path)}`](../../{path.replace(" ", "%20")}) | '
                         f'{cell(e["role"])} | {cell(e["engine"])} | {cell(e["owner"])} | {cell(e["notice"])} |')
            out[name] = "\n".join(legal.stamp(L)) + "\n"
            index.append((title, name, len(part), part[0][1]["id"], part[-1][1]["id"]))
    n_files, n_ret = len(reg["files"]), len(reg["retired"])
    third = sum(1 for e in reg["files"].values() if e["owner"] != OWNER)
    eng = sum(1 for e in reg["files"].values() if "engine file" in e["engine"])
    L = ["# The map of the repository", "",
         f"Every file in this repository has a map ID, an anchor and its owner. **{n_files:,} files are mapped**: "
         f"{n_files - third:,} are the property of {OWNER} and its entities, {third:,} are third-party files that keep their own "
         f"authors' notices; {eng} are the engine's fingerprinted files. {n_ret:,} IDs are retired (their files left the "
         "repository; an ID is never given twice).", "",
         "**How to cite a file:** by its map ID, OC-<area>-<number> (for example OC-DOC-00042), linked as "
         "`docs/map/<page>.md#oc-doc-00042`. The register behind every page is `results/REPO_MAP.json`; "
         "`python3 tools/repo_map.py` gives each new file its ID and writes the pages again, and `--check` (run by `verify.py`) "
         "fails a push where an ID moved, was given twice, or a page differs from the register.", "",
         "**Use:** every file is evaluation and simulation use only. Any commercial use, commercialization, monetization, "
         "production use, redistribution or hosted service of any part of it requires a signed, paid Omni-Compass Enterprise "
         "License, or, for a pilot, a signed, paid pilot agreement for the systems and dates it names (`LICENSE`, sections 5 "
         "and 5.4; `docs/PILOT_PROTOCOL.md`).", "",
         "| Section | Page | Files | First ID | Last ID |", "|---|---|---:|---|---|"]
    for title, name, n, first, last in index:
        L.append(f"| {cell(title)} | [{name}]({name}) | {n:,} | {first} | {last} |")
    out["README.md"] = "\n".join(legal.stamp(L)) + "\n"
    return out


def check(reg_now: dict, reg_stored: dict) -> list[str]:
    bad = []
    ids = [e["id"] for e in list(reg_stored.get("files", {}).values()) + list(reg_stored.get("retired", {}).values())]
    bad += [f"malformed map ID {i}" for i in ids if not ID_RE.match(i)]
    dup = {i for i in ids if ids.count(i) > 1} if len(ids) != len(set(ids)) else set()
    bad += [f"map ID given twice: {i}" for i in sorted(dup)]
    want = pages(reg_stored)
    have = {p.name: p.read_text(encoding="utf-8") for p in PAGES.glob("*.md")} if PAGES.exists() else {}
    bad += [f"docs/map/{n} is not what the register gives" for n in sorted(want) if have.get(n) != want[n]]
    bad += [f"docs/map/{n} is no page of the register" for n in sorted(set(have) - set(want))]
    return bad


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    paths = tracked()
    stored = load()
    if a.check:
        bad = check(None, stored)
        new = [p for p in paths if p not in stored.get("files", {})]
        gone = [p for p in stored.get("files", {}) if p not in set(paths)]
        for b in bad[:20]:
            print("map:", b)
        print(f"repository map: {len(stored.get('files', {})):,} files mapped; {len(new)} added and {len(gone)} removed since "
              f"its last write" + ("" if not bad else f"; {len(bad)} problems"))
        return 1 if bad else 0
    reg = assign(stored, paths)
    REGISTER.write_text(json.dumps(reg, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    PAGES.mkdir(parents=True, exist_ok=True)
    want = pages(reg)
    for old in PAGES.glob("*.md"):
        if old.name not in want:
            old.unlink()
    for name, text in want.items():
        (PAGES / name).write_text(text, encoding="utf-8")
    print(f"repository map: {len(reg['files']):,} files mapped on {len(want)} pages; {len(reg['retired'])} IDs retired")
    return 0


if __name__ == "__main__":
    sys.exit(main())

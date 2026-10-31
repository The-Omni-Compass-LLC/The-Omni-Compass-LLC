# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The front page keeps itself current (the founder's order of 10 October 2026: the newest result is always at the front, and
the repository, not a person, moves it there).

Reads every archived live run under results/live/raw/run-<id>/ of the five live products (Redis, Kafka, PostgreSQL, MySQL,
MongoDB), groups the runs into sets of three by what they are (the product, the verdict's objective, the engine the run
carried, the workloads it ran), takes the three newest complete runs of each kind as A, B and C, and where that set is newer
than the table on the front page: moves the table whole into docs/history as the next numbered set, rebuilds it with the
product's own three-run tool, then rebuilds the index, the wiring page, the benefit sheet and the dossier, and writes one
line per rebuilt table into the README's latest block. Nothing is ever deleted: every superseded table is kept in history,
every raw file stays archived.

  python tools/front_page.py            # the plan only: what would be rebuilt, as JSON; nothing changes
  python tools/front_page.py --apply    # do it
  python tools/front_page.py --summary  # one line for a commit message

Run by the front-page workflow after every finished live run (.github/workflows/front-page.yml) and by hand after a pull."""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "results" / "live" / "raw"
LIVE = ROOT / "results" / "live"
HISTORY = ROOT / "docs" / "history"
STATE = LIVE / "FRONT_PAGE_STATE.json"
README = ROOT / "README.md"
BEGIN, END = "<!-- front-page:begin -->", "<!-- front-page:end -->"
# the other blocks the repository writes on its front page: the engine and the index now, every table by when it last
# changed, and the runs that just finished on GitHub
BLOCKS = ("status", "tables", "runs")
# workflows that are not benchmarks: their runs are housekeeping and never listed as results
NOT_BENCHMARKS = {"front-page", "archive-run", "verify", "reaggregate", "pod-report", "azure-inventory", "azure-quota",
                  "Push on main", "Code Quality: Push on main", "CodeQL", "Dependabot Updates", "Dependency Graph",
                  "pages-build-deployment"}

# the five live products: the artifact prefix the run's files carry, the table's base name, the three-run tool
PRODUCTS = {
    "redis": ("REDIS", "tools/redis_abc.py"),
    "kafka": ("KAFKA", "tools/kafka_abc.py"),
    "pgbench": ("PGBENCH", "tools/pgbench_abc.py"),
    "sysbench": ("SYSBENCH", "tools/sysbench_abc.py"),
    "ycsb": ("YCSB", "tools/ycsb_abc.py"),
}
AFTER = ["tools/omni_index.py", "tools/wiring_verdicts.py", "tools/benefit_sheet.py", "tools/whole_system.py", "tools/dossier.py",
         "tools/headline.py"]   # the composition and the answer at the top follow the tables too (27 October 2026)


def _run_id(d: Path):
    m = re.fullmatch(r"run-(\d+)", d.name)
    return int(m.group(1)) if m else None


def _find(obj, key, depth=0):
    """The first value of `key` anywhere inside a JSON document (the objective sits at the top of a Redis or Kafka workload
    record and inside each repetition's arm record of a database run; the engine sits in the workload summary)."""
    if depth > 6:
        return None
    if isinstance(obj, dict):
        if key in obj:
            return obj[key]
        for v in obj.values():
            r = _find(v, key, depth + 1)
            if r is not None:
                return r
    elif isinstance(obj, list):
        for v in obj[:50]:
            r = _find(v, key, depth + 1)
            if r is not None:
                return r
    return None


def describe(run_dir: Path):
    """What one archived run is: (product, objective, engine version, workloads, native) or None when it is not a complete
    live product run (no report directory, or no workload directory). The workloads are the run's own artifact directories
    (`<product>-<workload>`); the objective, the engine and the native arm's setting are read from the records inside them,
    wherever each product keeps them; a record that names none reads as the resource objective on the engine the table was
    built for, against the operator's setting. The native setting is part of what a run is (19 October): native exactly as
    the vendor ships it (`native: shipped`) and native at the operator's setting are two benchmarks, and three runs of one
    are never read with runs of the other."""
    product = None
    for p in PRODUCTS:
        if (run_dir / f"{p}-report").is_dir():
            product = p
            break
    if product is None:
        return None
    workloads, objective, engine, native = set(), None, None, None
    for sub in sorted(run_dir.iterdir()):
        if not sub.is_dir() or not sub.name.startswith(f"{product}-") or sub.name == f"{product}-report":
            continue
        workloads.add(sub.name[len(product) + 1:])
        if objective is not None and engine is not None and native is not None:
            continue
        for f in sorted(sub.rglob("*.json"))[:400]:
            try:
                d = json.loads(f.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                continue
            if objective is None:
                o = _find(d, "objective")
                if isinstance(o, str) and o:
                    objective = o
            if engine is None:
                e = _find(d, "engine")
                if isinstance(e, dict) and e.get("version"):
                    engine = str(e["version"])
                elif isinstance(e, str) and e.startswith("omni-v"):
                    engine = e
            if native is None:
                n = _find(d, "native")
                if n in ("shipped", "operator"):
                    native = n
            if objective is not None and engine is not None and native is not None:
                break
    if not workloads:
        return None
    return (product, objective or "resource", engine_version(engine or "omni-v3"), tuple(sorted(workloads)),
            native or "operator")


def engine_version(text):
    """The engine a record names, reduced to its version: "omni-v3 (digest b53d05449ee04c4b, 40 files)" is "omni-v3"; a record
    whose engine is not a declared version ("differs from v2: ...") reads "unversioned" and never joins a versioned set."""
    m = re.search(r"omni-v(\d+)", str(text or ""))
    return f"omni-v{m.group(1)}" if m else "unversioned"


def table_name(product, objective, engine, native="operator"):
    base = PRODUCTS[product][0]
    m = re.search(r"omni-v(\d+)", engine_version(engine))
    v = m.group(1) if m else "0"
    return (f"V{v}_{base}" + ("" if objective == "resource" else f"_{objective.upper().replace('-', '_')}")
            + ("_SHIPPED" if native == "shipped" else ""))


def plan(root: Path = ROOT):
    """Every table whose three newest complete runs differ from the runs it was last built from."""
    raw = root / "results" / "live" / "raw"
    state = {}
    sp = root / "results" / "live" / "FRONT_PAGE_STATE.json"
    if sp.exists():
        try:
            state = json.loads(sp.read_text(encoding="utf-8"))
        except ValueError:
            state = {}
    kinds = {}
    for d in sorted(raw.glob("run-*")) if raw.is_dir() else []:
        rid = _run_id(d)
        if rid is None:
            continue
        desc = describe(d)
        if desc is None:
            continue
        kinds.setdefault(desc, []).append(rid)
    out = []
    for (product, objective, engine, workloads, native), ids in sorted(kinds.items()):
        ids = sorted(ids)
        if len(ids) < 3:
            continue
        a, b, c = ids[-3:]
        name = table_name(product, objective, engine, native)
        built = state.get(name, {}).get("runs")
        table = root / "results" / "live" / f"{name}.md"
        if built == [a, b, c] and table.exists():
            continue
        out.append({"table": name, "product": product, "objective": objective, "engine": engine, "workloads": list(workloads),
                    "native": native, "runs": [a, b, c], "tool": PRODUCTS[product][1], "previous": built, "table_exists": table.exists()})
    return out


def engine_now(root: Path = ROOT) -> str:
    """The engine that stands in this checkout (tools/omni_version.py): omni-v5, or unversioned."""
    sys.path.insert(0, str(root))
    from tools import omni_version as ov
    return ov.version_of(ov.engine_files()) or "unversioned"


def next_history_name(name: str, history: Path = HISTORY):
    n = 1 + len(list(history.glob(f"{name}_set*.md")))
    return history / f"{name}_set{n}.md"


def apply(items, root: Path = ROOT):
    """Rebuild each planned table (the old one kept whole in docs/history), then the pages read from every table, then the
    README's latest lines. Returns the lines written."""
    py = sys.executable
    lines = []
    state = {}
    if STATE.exists():
        try:
            state = json.loads(STATE.read_text(encoding="utf-8"))
        except ValueError:
            state = {}
    for it in items:
        name = it["table"]
        table = LIVE / f"{name}.md"
        if table.exists():
            dest = next_history_name(name)
            HISTORY.mkdir(parents=True, exist_ok=True)
            kept, _ = _legal_normalize(table.read_text(encoding="utf-8"))           # kept whole, in the one notice's wording
            dest.write_text(kept, encoding="utf-8")
        dirs = [os.path.relpath(RAW / f"run-{r}", ROOT) for r in it["runs"]]
        r = subprocess.run([py, it["tool"], *dirs, "--out", os.path.relpath(table, ROOT)], capture_output=True, text=True,
                           cwd=ROOT)
        if r.returncode != 0:
            raise SystemExit(f"{it['tool']} failed on {name}: {(r.stdout + r.stderr)[-800:]}")
        summary = _plain_summary((r.stdout.strip().splitlines() or [""])[-1])
        state[name] = {"runs": it["runs"], "built": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
                       "engine": it["engine"], "objective": it["objective"], "summary": summary}
        if it["engine"] == engine_now(root):              # the front page shows the engine that stands; an older engine's
            lines.append(f"- {state[name]['built']}: `{name}` rebuilt from runs {it['runs'][0]}, {it['runs'][1]}, "  # table
                         f"{it['runs'][2]} ({it['product']}, the {it['objective']} objective"
                         + (", native as shipped" if it.get("native") == "shipped" else "") + f", {it['engine']}): {summary}")
    if items:
        STATE.write_text(json.dumps(state, indent=1, sort_keys=True) + "\n", encoding="utf-8")
        for tool in AFTER:
            r = subprocess.run([py, tool], capture_output=True, text=True, cwd=ROOT)
            if r.returncode != 0:
                raise SystemExit(f"{tool} failed: {(r.stdout + r.stderr)[-800:]}")
        write_readme(lines)
    return lines


def write_readme(lines, readme: Path = README, keep: int = 8):
    """The README's latest block: the newest lines first, at most `keep`, between the two markers. Without the markers the
    README is left alone (and said so)."""
    if not lines:
        return False
    s = readme.read_text(encoding="utf-8")
    if BEGIN not in s or END not in s:
        print("README has no front-page markers; the latest lines were not written", file=sys.stderr)
        return False
    head, rest = s.split(BEGIN, 1)
    old, tail = rest.split(END, 1)
    kept = [ln for ln in old.strip().splitlines() if ln.strip()]
    block = "\n".join(list(reversed(lines)) + kept)[:100000]
    block_lines = [ln for ln in block.splitlines() if ln.strip()][:keep]
    readme.write_text(head + BEGIN + "\n" + "\n".join(block_lines) + "\n" + END + tail, encoding="utf-8")
    return True


def _legal_normalize(text):
    sys.path.insert(0, str(ROOT))
    from tools.legal import normalize_markdown
    return normalize_markdown(text)


def _no_machine_path(text: str) -> str:
    """A line with any machine's checkout folder taken out (a GitHub runner's, or this repository's own)."""
    text = text.replace(str(ROOT) + "/", "")
    return re.sub(r"/home/runner/work/[^/\s]+/[^/\s]+/", "", text)


def _plain_summary(text: str) -> str:
    """A tool's last line without the file it wrote ("results/live/V3_YCSB.md: 4 untouched workloads; ..." reads "4 untouched
    workloads; ...") and without any machine's folder."""
    return re.sub(r"^\S+\.md:\s*", "", _no_machine_path(text).strip())[:240]


def _git(*args, root: Path = ROOT) -> str:
    return subprocess.run(["git", "-c", "safe.directory=*", *args], cwd=root, capture_output=True, text=True).stdout


def status_lines(root: Path = ROOT) -> list[str]:
    """The engine on main and the index now, read from the version tool and the index's own file."""
    sys.path.insert(0, str(root))
    from tools import omni_version as ov
    files = ov.engine_files()
    v, d = ov.version_of(files), ov.digest(files)[:16]
    pkg = re.search(r'^version = "([^"]+)"', (root / "pyproject.toml").read_text(encoding="utf-8"), re.M)
    nxt = ("Its default brain is **the max**: every muscle pushed to its own limit, never past it and never below native, "
           "the energy it takes shown as power given beside the work and the wear; the dial turns it down "
           "([`docs/OMNI_V5.md`](docs/OMNI_V5.md)).") if v == "omni-v5" else ""
    out = [f"- **Engine on main:** {v or 'unversioned (it differs from every frozen engine)'}, fingerprint `{d}` "
           f"({len(files)} files); package {pkg.group(1) if pkg else 'unknown'}. {nxt}".rstrip()]
    ix = root / "results" / "OMNI_INDEX.json"
    if ix.exists():
        idx = json.loads(ix.read_text(encoding="utf-8"))
        if idx.get("engine") == v:                          # only an index built on the engine that stands (no older one up front)
            out.append(f"- **The Omni index now:** {idx['headline_pct']:+.1f}% on the resource reading (work, speed, machines "
                       f"and energy) and {idx['service_headline_pct']:+.1f}% on the service reading (work and speed), real "
                       "machines, every test the same in all three of our runs ([`results/OMNI_INDEX.md`](results/OMNI_INDEX.md)).")
    return out


OLD_ENGINE = re.compile(r"(^|/)(V[0-4]_[^/]*\.md$|v[0-4][-_/])")
ENGINE_NOW = re.compile(r"omni-v5|Omni v5")


def current_table(p: str, root: Path = ROOT) -> bool:
    """A table of the engine that stands: it says it ran on omni-v5, and it is not named for or filed under an older
    engine (V1_, V3_, v3-...); the older tables stay in the repository as the road to 1.0, never in front."""
    if OLD_ENGINE.search(p):
        return False
    try:
        v = engine_now(root)
        number = re.search(r"omni-v(\d+)", v)
        if not number:
            return False
        pattern = re.compile(r"(?:omni-v|Omni v)" + number.group(1) + r"(?!\d)")
        return bool(pattern.search((root / p).read_text(encoding="utf-8", errors="ignore")[:4000]))
    except OSError:
        return False


def table_lines(root: Path = ROOT, n: int = 10) -> list[str]:
    """Every result table, newest first by the time it last changed (now, for one changed and not yet committed)."""
    present = [p for p in _git("ls-files", "--", "results", root=root).splitlines()
               if p.endswith(".md") and not p.startswith(("results/live/raw/", "results/external_review/"))
               and current_table(p, root)]
    present = [p for p in present if (root / p).is_file()]
    when = {}
    changed = {ln[3:].strip() for ln in _git("status", "--porcelain", "--", "results", root=root).splitlines() if len(ln) > 3}
    now = dt.datetime.now(dt.timezone.utc)
    for p in present:
        if p in changed:
            when[p] = now
    cur = None
    log = _git("log", "--format=@%cI\t%(trailers:key=Front-page-ignore,valueonly,separator=%x20)", "--name-only", "--",
               "results/*.md", ":(exclude)results/live/raw", root=root)
    for ln in log.splitlines():
        if ln.startswith("@"):
            stamp, _, ignore = ln[1:].partition("\t")
            cur = None if ignore.strip() else dt.datetime.fromisoformat(stamp.strip()).astimezone(dt.timezone.utc)
        elif ln.strip() and cur is not None and ln not in when:
            when[ln] = cur
    rows = sorted(((when[p], p) for p in present if p in when), reverse=True)[:n]
    out = ["| Last changed (UTC) | Table | Reading |", "|---|---|---|"]
    for t, p in rows:
        text = (root / p).read_text(encoding="utf-8", errors="ignore").splitlines()
        title = next((ln[2:].strip() for ln in text if ln.startswith("# ")), Path(p).stem)
        reading = next((ln.strip("* ").strip() for ln in reversed(text) if ln.startswith("**Across ")), "")
        out.append(f"| {t:%Y-%m-%d %H:%M} | [{title.replace('|', '/')}]({p}) | {reading.replace('|', '/')} |")
    return out


def run_lines(n: int = 10, pages: int = 4) -> list[str] | None:
    """The newest finished run of each benchmark workflow on GitHub, newest first (None when GitHub cannot be asked from
    here). Housekeeping workflows and GitHub's own dynamic runs are left out; a skipped run is not a run."""
    from tools.repo import NAME as repo   # the repository's name, written once
    out = ["| Finished (UTC) | Benchmark | Outcome | Run |", "|---|---|---|---|"]
    seen, asked, rows = set(), False, []
    for page in range(1, pages + 1):
        try:
            r = subprocess.run(["gh", "api", f"repos/{repo}/actions/runs?status=completed&per_page=100&page={page}"],
                               capture_output=True, text=True, timeout=60)
            runs = json.loads(r.stdout)["workflow_runs"] if r.returncode == 0 else None
        except (OSError, ValueError, KeyError, subprocess.TimeoutExpired):
            runs = None
        if runs is None:
            break
        asked = True
        for x in runs:
            path = str(x.get("path", ""))
            name = str(x.get("name", ""))
            if name.startswith(".github/workflows/"):              # a run of a file GitHub could not read is named by its path
                name = Path(name).stem
            if (name in NOT_BENCHMARKS or x.get("conclusion") in (None, "skipped") or not path.startswith(".github/workflows/")
                    or name in seen):
                continue
            seen.add(name)
            t = dt.datetime.fromisoformat(x["updated_at"].replace("Z", "+00:00"))
            rows.append((t, f"| {t:%Y-%m-%d %H:%M} | {name} | {x['conclusion']} | [{x['id']}]({x['html_url']}) |"))
        if len(runs) < 100 or len(rows) >= n:
            break
    return out + [r for _, r in sorted(rows, reverse=True)[:n]] if asked else None


def write_block(name: str, lines: list[str], readme: Path = README) -> bool:
    """Replaces what stands between `<!-- front-page:NAME:begin -->` and its end marker (a README without them is left alone)."""
    b, e = f"<!-- front-page:{name}:begin -->", f"<!-- front-page:{name}:end -->"
    s = readme.read_text(encoding="utf-8")
    if b not in s or e not in s:
        return False
    head, rest = s.split(b, 1)
    _, tail = rest.split(e, 1)
    new = head + b + "\n" + "\n".join(lines) + "\n" + e + tail
    if new != s:
        readme.write_text(new, encoding="utf-8")
    return True


def refresh(readme: Path = README) -> list[str]:
    """Writes the engine and index line, the newest tables and the runs that just finished; returns the blocks written."""
    done = []
    for name, lines in (("status", status_lines()), ("tables", table_lines()), ("runs", run_lines())):
        if lines is not None and write_block(name, lines, readme):
            done.append(name)
    # lines written before the paths were made relative keep no machine's folder either
    s = readme.read_text(encoding="utf-8")
    t = re.sub(r"\): (?:\S+/)?V\d+_[A-Z_]+\.md: ", "): ", _no_machine_path(s))
    if t != s:
        readme.write_text(t, encoding="utf-8")
    if STATE.exists():
        st = json.loads(STATE.read_text(encoding="utf-8"))
        for v in st.values():
            if isinstance(v, dict) and "summary" in v:
                v["summary"] = _plain_summary(v["summary"])
        new = json.dumps(st, indent=1, sort_keys=True) + "\n"
        if new != STATE.read_text(encoding="utf-8"):
            STATE.write_text(new, encoding="utf-8")
    return done


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--apply", action="store_true", help="rebuild what the plan names; without it, print the plan only")
    ap.add_argument("--summary", action="store_true", help="one line naming the tables the plan would rebuild")
    a = ap.parse_args(argv)
    items = plan()
    if a.summary:
        print(", ".join(it["table"] for it in items) if items else "nothing to rebuild")
        return 0
    if not a.apply:
        print(json.dumps(items, indent=1))
        return 0
    lines = apply(items)
    print("\n".join(lines) if lines else "nothing to rebuild: every table is built from its three newest runs")
    print("front page refreshed: " + ", ".join(refresh()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

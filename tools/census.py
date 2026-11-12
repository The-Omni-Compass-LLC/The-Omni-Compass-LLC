# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The census: every run GitHub holds, every file the branch raw holds, every table, the catalog and the website feed, read
from both ends (docs/CENSUS.md).

The founder's order of 11 November: "Go through it inside out, upside down, reverse, inverse, reverse engineer it all, make
confirm everything works and all databases are full blown wide open fully populated. If not, you spend more and build." It
reads forward (every run of every benchmark workflow GitHub recorded: did it finish, are its files on the branch raw, which
table counts it) and backward (every run a three-run table names: is its folder on raw), and it counts the archive itself
(folders, files, checksum lists, signatures, receipts), the engine that stands (what stands, carries or runs again on it),
the catalog (muscles, families, wiring, cards) and the website feed (numbers with receipts). Every gap is listed with what
fills it: a run whose files GitHub still holds is put on the archive's request list (.github/archive_request.txt), oldest
first, so it is saved before GitHub's retention ends.

  python3 tools/census.py                       write docs/CENSUS.md from results/CENSUS_RECORDS.json
  python3 tools/census.py --check               exit 1 when the page differs from the records
  python3 tools/census.py --refresh RUNS.json --raw-folders FOLDERS.txt --artifacts ART.json [--request]
                                                build the records again from a saved GitHub run list (one list a workflow),
                                                the branch raw's folder counts (name, files, checksum list, signed, receipt)
                                                and each unarchived run's files on GitHub; --request adds every unarchived run
                                                whose files GitHub still holds to .github/archive_request.txt
"""
from __future__ import annotations

import argparse
import csv
import glob
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
RECORDS, OUT = ROOT / "results" / "CENSUS_RECORDS.json", ROOT / "docs" / "CENSUS.md"
REQUEST = ROOT / ".github" / "archive_request.txt"
TABLE_DIRS = ("results/live", "results/orchestrator", "results/gpu")
# workflows whose runs hand their results in some other way than files to archive (they commit their records to main, or
# they hand in nothing by design); a run of these with no files on GitHub is not a gap
SELF_RECORDING = {"engine-runs.yml": "commits its record to main (the Python's runs and the core's Monte Carlo)",
                  "monte-carlo.yml": "commits its record to main",
                  "cpu-power.yml": "hands in its receipt as the run's summary and the record on main",
                  "kwok-scale.yml": "a model of a large cluster: its result is printed in the run and recorded on main",
                  "reproduce.yml": "rebuilds a published table from the archive; hands in nothing new"}


def _folder_id(name: str):
    m = re.fullmatch(r"(?:.*-)?run-(\d+)", name)
    return m.group(1) if m else None


def table_runs() -> dict:
    """Every run a three-run table names, from its record: {run id: [table, ...]}."""
    named = defaultdict(list)
    for d in TABLE_DIRS:
        for p in sorted((ROOT / d).glob("*.json")):
            if p.name.startswith(("AZURE_RUN", "RECIPES")):
                continue
            try:
                j = json.loads(p.read_text(encoding="utf-8"))
            except ValueError:
                continue
            runs = j.get("runs") if isinstance(j, dict) else None
            ids = []
            for r in runs if isinstance(runs, list) else []:      # a list of runs; some records keep a count under "runs"
                v = r if isinstance(r, (str, int)) else (r.get("run") or r.get("run_id") or r.get("github_run") or r.get("id")
                                                           if isinstance(r, dict) else None)
                if v is not None and re.fullmatch(r"\d{10,12}", str(v)):
                    ids.append(str(v))
            for i in ids:
                named[i].append(str(p.relative_to(ROOT)))
    return named


def refresh(runs_file: str, folders_file: str, art_file: str) -> dict:
    data = json.loads(Path(runs_file).read_text(encoding="utf-8"))
    folders, raw = {}, Counter()
    for ln in Path(folders_file).read_text(encoding="utf-8").splitlines():
        name, n, sums, signed, receipt = ln.split()
        raw["folders"] += 1
        raw["files"] += int(n)
        raw["checksums"] += int(sums)
        raw["signed"] += int(signed)
        raw["receipts"] += int(receipt)
        i = _folder_id(name)
        if i:
            folders[i] = name
    arts = {str(x[1]): x for x in json.loads(Path(art_file).read_text(encoding="utf-8"))} if art_file else {}
    named = table_runs()
    wfs, missing = {}, []
    for wf, v in sorted(data.items()):
        c = Counter((r.get("conclusion") or r.get("status")) for r in v["runs"])
        fin = [r for r in v["runs"] if r.get("conclusion") in ("success", "failure")]
        arch = [r for r in fin if str(r["id"]) in folders]
        row = {"runs": len(v["runs"]), "by_outcome": dict(sorted(c.items())), "finished": len(fin), "archived": len(arch),
               "with_files": 0, "with_files_bytes": 0, "no_files": 0, "unread": 0, "earliest_expiry": ""}
        for r in fin:
            if str(r["id"]) in folders:
                continue
            a = arts.get(str(r["id"]))
            if not a or a[4] is None:
                row["unread"] += 1
                continue
            n, size, expired, expires = a[4], a[5], a[6], a[7]
            if n and n > expired:
                row["with_files"] += 1
                row["with_files_bytes"] += size
                if expires and (not row["earliest_expiry"] or expires < row["earliest_expiry"]):
                    row["earliest_expiry"] = expires
                missing.append([wf, r["id"], r["created_at"], r["conclusion"], n, size, expires[:10]])
            else:
                row["no_files"] += 1
        wfs[wf] = row
    folder_ids = set(folders)
    not_on_raw = sorted([t, i] for i, ts in named.items() if i not in folder_ids for t in ts)
    missing.sort(key=lambda x: x[2])
    return {"read": "GitHub's own run records of every workflow that hands in files, read through GitHub's API on 11 November "
                    "2026, and the branch raw's tree read the same day",
            "workflows": wfs, "raw": dict(raw), "unarchived_with_files": missing,
            "tables": {"runs_named": len(named), "on_raw": len(set(named) & folder_ids), "not_on_raw": not_on_raw}}


def _catalog() -> dict:
    cat = list(csv.DictReader((ROOT / "realms" / "catalog_v5.csv").open(encoding="utf-8")))
    fams = {r["family_id"] for r in cat}
    wired = {r["family_id"] for r in csv.DictReader((ROOT / "docs" / "wiring_recipes.csv").open(encoding="utf-8"))}
    cards = {r["muscle_id"] for r in csv.DictReader((ROOT / "realms" / "muscle_cards_v5.csv").open(encoding="utf-8"))}
    return {"muscles": len(cat), "families": len(fams), "wired": len(fams & wired), "unwired": sorted(fams - wired),
            "cards": len(cards & {r["muscle_id"] for r in cat})}


def _carry() -> dict:
    j = json.loads((ROOT / "results" / "CARRY.json").read_text(encoding="utf-8"))
    return {"engine": j.get("engine_standing"), "counts": j.get("counts") or {}}


def _site() -> dict:
    j = json.loads((ROOT / "results" / "SITE_NUMBERS.json").read_text(encoding="utf-8"))
    return {"show": len(j.get("show") or []), "not_for_the_site": len(j.get("not_for_the_site") or [])}


def _mb(b: int) -> str:
    return f"{b / 1e9:,.1f} GB" if b >= 1e9 else f"{b / 1e6:,.0f} MB"


def render(rec: dict) -> str:
    from tools.legal import stamp
    w, raw = rec["workflows"], rec["raw"]
    tot = Counter()
    for v in w.values():
        tot.update(v["by_outcome"])
    fin = sum(v["finished"] for v in w.values())
    arch = sum(v["archived"] for v in w.values())
    wf_files = sum(v["with_files"] for v in w.values())
    wf_bytes = sum(v["with_files_bytes"] for v in w.values())
    nofiles = sum(v["no_files"] for v in w.values())
    unread = sum(v["unread"] for v in w.values())
    going = sum(tot[k] for k in ("in_progress", "queued", "pending", "waiting", "requested"))
    cat, car, site, t = _catalog(), _carry(), _site(), rec["tables"]
    expiries = [v["earliest_expiry"] for v in w.values() if v["earliest_expiry"]]
    lines = [
        "# The census: every run, every file, every table", "",
        "Read from both ends, from " + rec["read"] + ". Forward: every run GitHub recorded for the workflows that hand in "
        "files, whether it finished, whether its files are on the branch `raw`, which table counts it. Backward: every run a "
        "three-run table names, whether its folder is on `raw`. Written by `python3 tools/census.py` from "
        "`results/CENSUS_RECORDS.json`; `verify.py` fails a push where the page differs from its records. Counts, not "
        "readings: nothing here reads GAIN, STEADY or LOSS.", "",
        "## 1. The runs GitHub holds", "",
        f"{sum(v['runs'] for v in w.values()):,} runs of {len(w)} workflows. {tot['skipped']:,} were skipped: a push "
        "that changed no file the workflow watches, so it never started and nothing ran. "
        f"{tot['cancelled']:,} were cancelled (most waited behind a running set and never started). {fin:,} finished: "
        f"{tot['success']:,} succeeded and {tot['failure']:,} failed. {going} were still going when the records were read.", "",
        "## 2. The archive (the branch `raw`)", "",
        f"{raw['folders']:,} run folders holding {raw['files']:,} files. Every folder carries its checksum list "
        f"({raw['checksums']:,} of {raw['folders']:,}); {raw['signed']:,} lists are signed with GitHub's own identity "
        f"(Sigstore; the signing began on 26 October, and the folders before it carry the checksums alone); "
        f"{raw['receipts']:,} folders hold a paired receipt (`LIVE_REPS.json`), the rest the files their own test writes "
        "(the grid's squares, the organisms, the models).", "",
        "## 3. Every finished run and its files", "",
        f"Of the {fin:,} finished runs, {arch:,} have their folder on `raw` ({100 * arch / fin:.0f}%). Of the rest, "
        f"{wf_files:,} still have their files on GitHub ({_mb(wf_bytes)}"
        + (f"; the first of them expire on {min(expiries)[:10]}" if expiries else "")
        + "): every one is on the archive's request list, oldest first, and is copied to `raw` by "
        "`archive-run.yml` before GitHub lets it go. "
        f"{nofiles:,} handed in no files at all: a launch refused before anything ran, a set stopped at its login, or a "
        "workflow that records its result another way (named below)."
        + (f" {unread:,} could not be read when the records were taken; the next refresh reads them." if unread else ""), "",
        "| Workflow | Runs | Finished | On `raw` | Files still on GitHub, requested | No files handed in | How it records |",
        "|---|---:|---:|---:|---:|---:|---|"]
    for wf, v in sorted(w.items(), key=lambda x: -x[1]["finished"]):
        lines.append(f"| `{wf}` | {v['runs']:,} | {v['finished']:,} | {v['archived']:,} | {v['with_files']:,} | "
                     f"{v['no_files']:,} | {SELF_RECORDING.get(wf, 'its files, on `raw`')} |")
    nr = t["not_on_raw"]
    lines += ["", "## 4. Backward: every run a table names", "",
              f"The three-run tables' records name {t['runs_named']:,} runs; {t['on_raw']:,} have their folder on `raw`."
              + (" The rest, each requested for the archive:" if nr else " None is missing."), ""]
    for tb, i in nr:
        lines.append(f"- `{tb}`: run {i}")
    cc = car["counts"]
    lines += ["" if nr else "", "## 5. The engine that stands", "",
              f"On {car['engine']}: " + ", ".join(f"{v} {k}" for k, v in sorted(cc.items())) + " (`results/CARRY.md`: a "
              "benchmark stands when its three runs on this engine are tabled, carries when no file it runs changed since "
              "its last engine, and runs again otherwise; the conductor releases the reruns, A of every benchmark, then B, "
              "then C).", "",
              "## 6. The catalog", "",
              f"{cat['muscles']:,} muscles in {cat['families']} families (`realms/catalog_v5.csv`); {cat['wired']} of the "
              f"{cat['families']} families carry their physical wiring (`docs/wiring_recipes.csv`)"
              + (f", missing: {', '.join(cat['unwired'])}" if cat["unwired"] else "") + f"; {cat['cards']} muscles carry a "
              "card of their own (`realms/muscle_cards_v5.csv`, kept only where it won twice and never fell behind native), "
              "and every other muscle runs on the engine's setting.", "",
              "## 7. The website feed", "",
              f"`results/SITE_NUMBERS.json` holds {site['show']} numbers for the site and {site['not_for_the_site']} kept "
              "off it (each with the reason), every one with the record it is read from; "
              "`results/WEBSITE_SURFACE_CONTRACT.json` names which page may show which, and `verify.py` fails a push where "
              "either differs from its records.", ""]
    return "\n".join(stamp(lines)) + "\n"


def request(rec: dict) -> int:
    """Put every unarchived run whose files GitHub still holds on the archive's request list, oldest first, after the runs
    already asked for; a run already on the list is never written twice."""
    text = REQUEST.read_text(encoding="utf-8") if REQUEST.exists() else ""
    have = set(re.findall(r"\b\d{9,12}\b", text))
    new = [str(x[1]) for x in rec["unarchived_with_files"] if str(x[1]) not in have]
    new += [i for _, i in rec["tables"]["not_on_raw"] if i not in have and i not in new]
    if new:
        lines = [" ".join(new[k:k + 12]) for k in range(0, len(new), 12)]
        REQUEST.write_text(text.rstrip("\n") + "\n# the census of 11 November (tools/census.py): every finished run whose files "
                           "GitHub still holds and raw does not, oldest first\n" + "\n".join(lines) + "\n", encoding="utf-8")
    return len(new)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--refresh", default="")
    ap.add_argument("--raw-folders", default="")
    ap.add_argument("--artifacts", default="")
    ap.add_argument("--request", action="store_true")
    a = ap.parse_args(argv)
    if a.refresh:
        RECORDS.write_text(json.dumps(refresh(a.refresh, a.raw_folders, a.artifacts), indent=0) + "\n", encoding="utf-8")
    rec = json.loads(RECORDS.read_text(encoding="utf-8"))
    if a.request:
        print(f"archive request list: {request(rec)} runs added")
    md = render(rec)
    if a.check:
        ok = OUT.exists() and OUT.read_text(encoding="utf-8") == md
        print("census: docs/CENSUS.md is what its records give" if ok else
              "census: docs/CENSUS.md differs from its records: python3 tools/census.py")
        return 0 if ok else 1
    OUT.write_text(md, encoding="utf-8")
    print(f"docs/CENSUS.md written: {sum(v['finished'] for v in rec['workflows'].values()):,} finished runs, "
          f"{rec['raw']['folders']:,} folders on raw")
    return 0


if __name__ == "__main__":
    sys.exit(main())

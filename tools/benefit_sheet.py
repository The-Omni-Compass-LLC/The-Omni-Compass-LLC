#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The benefit sheet: one number per benchmark, its word (GAIN, STEADY or LOSS), and every change said in words.

The founder's orders of 9 and 13 October 2026: next to every benchmark, say whether Omni-Compass on top was a benefit to the
system and by how much, in one number whose sign always means the same thing, whatever the gauge measures; and say it in
GAIN, STEADY and LOSS, judged by what each gauge is for and never by the sign of its number (tools/readings.py, the key). So the
sign here is the system's own declared aims, gauge by gauge: plus is a GAIN; a minus is a LOSS on work, speed, misses or
failures, and power given on a resource spent (energy, machines, memory). The tables keep their raw signs (a response time
that fell reads "-65%" there); this sheet turns every one the same way round, and says each change in words: which way it
went (cut, down or up) and its word.

How the number is made, the same rule as the Omni index (tools/omni_index.py):

  every judged gauge becomes a ratio oriented so that above 1 is a GAIN against the gauge's declared aim (native / omni for a
  gauge that aims lower or is a resource spent, omni / native for one that aims higher); a gauge counts only where its reading is
  judged across our three runs, anything else (STEADY: inside the noise or the same; the runs disagree) counts as exactly 1; the number is the geometric mean of
  those ratios, minus one, in percent. For the tests inside the index the number IS the index's own resource reading of
  that test; for a stack with several workloads the stack's number is its index category. For the simulators and the
  organisms, which the index does not score, the same arithmetic runs over every judged gauge of their tables.

  "Benefit?" reads GAIN (gauges GAIN across our three runs, none LOSS or power given), GAIN, power given (a GAIN bought with a
  resource put in), GAIN AND LOSS (both; the number says which way the trade nets by this scoring), LOSS (a LOSS, no GAIN), power
  given (a resource put in, nothing gained), or STEADY (nothing moved 0.5% or more across our three runs).

  python3 tools/benefit_sheet.py            ->  docs/BENEFIT_SHEET.md, results/BENEFIT_SHEET.json
  python3 tools/benefit_sheet.py --check    ->  exit 1 if the committed files differ from what the tables give
"""
from __future__ import annotations

import datetime
import json
import math
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.legal import stamp as legal_stamp                       # noqa: E402
from tools.readings import with_own_runs, receipt_key, row_gain, landed, word as gel_word, aim as gel_aim, GAIN, STEADY, LOSS, GIVEN, GAIN_AND_LOSS, GAIN_GIVEN, reading_kind  # noqa: E402
from tools import omni_index                                       # noqa: E402
from tools import wiring_verdicts as wv                            # noqa: E402

LIVE = ROOT / "results" / "live"
OUT_MD = ROOT / "docs" / "BENEFIT_SHEET.md"
OUT_JSON = ROOT / "results" / "BENEFIT_SHEET.json"
# the Owner's Manual's own evidence table (section 3.5) is these rows, written here on every push so the book never quotes an
# engine's numbers after the next engine's tables land (27 October 2026: its hand-typed table still read omni-v10 and omni-v11)
MANUAL = ROOT / "docs" / "OMNI_COMPASS_OWNERS_MANUAL.md"
M_BEGIN, M_END = "<!-- the evidence, one row per benchmark (tools/benefit_sheet.py) -->", "<!-- end of the evidence -->"
ENGINE_RE = re.compile(r"\bomni-v(\d+)\b")


def has_commit(sha):
    """Whether this checkout holds the named commit (a shallow checkout, as GitHub's verify runs, does not)."""
    try:
        return subprocess.run(["git", "cat-file", "-e", f"{sha}^{{commit}}"], cwd=ROOT, capture_output=True,
                              timeout=60).returncode == 0
    except (OSError, subprocess.SubprocessError):
        return False


def recorded_engine(rel):
    """The engine the committed sheet records for a table, read where the commit it names was in the history."""
    try:
        rows = json.loads(OUT_JSON.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return "not named"
    rows = rows.get("rows", []) if isinstance(rows, dict) else rows
    return next((r.get("engine") or "not named" for r in rows if r.get("file") == rel), "not named")


def stated_engines(p: Path) -> set:
    """The engines a table states for its own runs: its run table's Engine column, else its JSON's "engine" field; empty when
    it states neither. Only these are read where they exist, so an engine a table names in passing (the drone swarms' table
    names omni-v12 as the engine before whose runs its preregistration's amendment was written) is never filed as an engine
    it ran on (27 October 2026: the sheet had filed that table under "omni-v12 and omni-v21")."""
    found = set()
    try:
        lines = p.read_text(encoding="utf-8").splitlines()
    except OSError:
        lines = []
    for i, ln in enumerate(lines):
        cells = [c.strip() for c in ln.strip().strip("|").split("|")] if ln.startswith("|") else []
        if "Engine" not in cells:
            continue
        col = cells.index("Engine")
        for row in lines[i + 1:]:
            if not row.startswith("|"):
                break
            vals = [c.strip() for c in row.strip().strip("|").split("|")]
            if col < len(vals) and not set(vals[col]) <= set("-: "):
                found |= {int(m.group(1)) for m in ENGINE_RE.finditer(vals[col])}
    if found:
        return found
    try:
        d = json.loads(p.with_suffix(".json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return found
    v = d.get("engine") if isinstance(d, dict) else None
    return {int(m.group(1)) for m in ENGINE_RE.finditer(v if isinstance(v, str) else " ".join(map(str, v or [])))}


def engine_of(rel):
    """The engines a row's table ran on, read from the table itself (its run table's Engine column, or the engine its JSON
    names), oldest first: "omni-v6", or "omni-v1 and omni-v3" for a table built from several; "not named" where the table
    does not say. The index names every engine its counted tables ran on."""
    if rel.endswith("OMNI_INDEX.md"):
        found = {int(m.group(1)) for c in wv.real_stacks(wv.load_index()) if c["counted"]
                 for m in ENGINE_RE.finditer(engine_of(c["source"]))}
    else:
        p, texts = ROOT / rel, []
        for q in (p.with_suffix(".json"), p):
            try:
                texts.append(q.read_text(encoding="utf-8"))
            except OSError:
                pass
        found = stated_engines(p) or {int(m.group(1)) for t in texts for m in ENGINE_RE.finditer(t)}
        if not found:                                              # a table named for its engine (V3_...), or one that says "Omni v3"
            m = re.match(r"V(\d+)_", p.name)
            found = {int(m.group(1))} if m else {int(x) for t in texts for x in re.findall(r"\bOmni v(\d+)\b", t)}
        if not found:                                              # the engine of the commit the table names, by the version tool
            m = next((re.search(r"commit `([0-9a-f]{7,40})`", t) for t in texts if re.search(r"commit `([0-9a-f]{7,40})`", t)), None)
            if m and not has_commit(m.group(1)):                   # a checkout without that history (GitHub's is one commit
                return recorded_engine(rel)                        # deep): the engine the sheet recorded where it was there
            if m:
                try:
                    out = subprocess.run([sys.executable, str(ROOT / "tools" / "omni_version.py"), "--commit", m.group(1)], cwd=ROOT,
                                         capture_output=True, text=True, timeout=300).stdout
                    found = {int(x) for x in ENGINE_RE.findall(out)}
                except (OSError, subprocess.SubprocessError):
                    pass
    return " and ".join(f"omni-v{v}" for v in sorted(found)) if found else "not named"


# the three-run tables on the engine that stands; each takes the place of the same benchmark's table on an older engine,
# which stays in results/live under its own name
NEWEST = [
    ("V7_KEDA_REQUESTS.json", "Real Kubernetes, With its add-ons: KEDA's HTTP add-on on the live requests in flight, Omni-Compass on top, ten pairs, three runs",
     "every judged gauge of the three-run table: p95, alert minutes, replicas, machines, energy"),
    ("V7_KEDA_CPU_REQUESTS.json", "Real Kubernetes, With its add-ons: KEDA on the CPU target and the live requests in flight, Omni-Compass on top, ten pairs, three runs",
     "every judged gauge of the three-run table: p95, alert minutes, replicas, machines, energy"),
    ("V7_GOLDILOCKS.json", "Real Kubernetes, a service rightsized by Goldilocks and the VPA's recommender, Omni-Compass on top, ten pairs, three runs",
     "every judged gauge of the three-run table: p95, time over the line, machines, energy"),
    ("V7_CRUISEKUBE.json", "Real Kubernetes, a service rightsized by CruiseKube applying its own recommendations, Omni-Compass on top, ten pairs, three runs",
     "every judged gauge of the three-run table: p95, time over the line, machines, energy"),
]


def gmean(xs):
    xs = [x for x in xs if x and x > 0]
    return math.exp(sum(math.log(x) for x in xs) / len(xs)) if xs else 1.0


def pct(r):
    return 100.0 * (r - 1.0)


def fmt_pct(x):
    if x is None:
        return "no number"
    if abs(x) < 0.05:
        return "0%"
    return f"{x:+.0f}%" if abs(x) >= 10 else f"{x:+.1f}%"


def fmt_pct_words(x, loss=0):
    """The one number with its word, its size alone beside the word, as tools/readings.py by_word prints it (the referee's work
    order of 25 October: a number beside a word carries no sign, so it is never read as a raw direction): '31% GAIN'; a fall
    is a LOSS where a gauge read LOSS ('25% LOSS'), otherwise power given, the resources put in outweighing what they bought by
    this scoring ('25% power given'); '0%: STEADY'."""
    if x is None:
        return "no number"
    if abs(x) < 0.05:
        return f"0%: {STEADY}"
    w = GAIN if x > 0 else LOSS if loss else GIVEN
    return f"{fmt_pct(abs(x))[1:]} {w}"


def verb(fell, aim):
    """A change in its plain verb: a fall is a cut where less is the aim (time waited, a resource spent) and down where more is
    the aim (work done); a rise is up."""
    if fell:
        return "down" if aim in ("higher", "never less") else "cut"
    return "up"


def fell_of(w, aim):
    """Which way a gauge read GAIN, LOSS or power given went, from its word and its aim (tools/readings.py word, read backward):
    True where it fell, False where it rose, None where the word does not settle it."""
    a = str(aim or "")
    if a not in ("higher", "lower", "spent", "never more", "never less", "work per resource"):
        return None                               # no declared aim: the table's own cells carry the gauge's direction
    if w == GAIN:
        return a not in ("higher", "never less", "work per resource")
    if w == LOSS:
        return a in ("higher", "never less")
    if w == GIVEN:
        return a == "work per resource"
    return None


def in_words(items):
    """Every change judged across our three runs of a benchmark in words, grouped by gauge: (name, word, range, aim) ->
    'p95 cut 65% to 71% (GAIN)', 'memory ceiling held up 215% (power given)', 'work down 5% (LOSS)'."""
    groups = {}
    for name, w, rg, aim in items:
        nums = re.findall(r"[-+\u2212]?\d+(?:\.\d+)?%", rg or "")
        if not nums:
            continue
        # which way the gauge went is read from its word and its aim, never from the first printed number's sign (the mathematics
        # seat of 24 October: a range "-0% to +430%" on a 95th percentile read LOSS had printed "cut")
        fell = fell_of(w, aim)
        if fell is None:
            fell = nums[0].startswith(("-", "\u2212"))
        groups.setdefault((name, w, fell, aim), []).extend(abs(float(n.rstrip("%").replace("\u2212", "-"))) for n in nums)
    out = []
    for (name, w, fell, aim), mags in groups.items():
        mags = sorted(mags)
        f = (lambda x: f"{x:.0f}%") if mags[-1] >= 10 else (lambda x: f"{x:.1f}%")
        m = f(mags[0]) if f(mags[0]) == f(mags[-1]) else f"{f(mags[0])} to {f(mags[-1])}"
        out.append(f"{name} {verb(fell, aim)} {m} ({w})")
    return "; ".join(out) if out else f"{STEADY}: nothing moved 0.5% or more across our three runs"


def benefit_word(gain, loss, given=0):
    """The row's word from its counts of gauges that read GAIN, LOSS and power given across our three runs."""
    if gain and loss:
        return GAIN_AND_LOSS
    if gain and given:
        return GAIN_GIVEN
    if gain:
        return GAIN
    if loss:
        return LOSS
    if given:
        return GIVEN
    return STEADY


WORD_OF = {"gain": GAIN, "loss": LOSS, "given": GIVEN}


def items_of(j):
    """A case's judged gauges as (name, word, range, aim)."""
    return [(it[1], WORD_OF[c], it[2], it[4]) for c in ("gain", "loss", "given") for it in j[c]]


def shallow():
    """A shallow checkout (GitHub's default) carries no history: the dates must then come from the committed sheet."""
    r = subprocess.run(["git", "-c", "safe.directory=*", "rev-parse", "--is-shallow-repository"], cwd=ROOT, capture_output=True, text=True)
    return r.stdout.strip() == "true"


def boundary():
    """The commits a shallow checkout's history stops at: each stands in for every older change, so a date read from one is
    not the day the file changed."""
    r = subprocess.run(["git", "-c", "safe.directory=*", "rev-parse", "--git-path", "shallow"], cwd=ROOT, capture_output=True, text=True)
    f = ROOT / r.stdout.strip() if r.stdout.strip() else None
    return set(f.read_text().split()) if f and f.exists() else set()


def updated(path):
    """The date the file was last changed in the repository (the day the result landed); None where the history is not here
    (in a shallow checkout, a file last touched by the commit the history stops at, or not yet committed)."""
    st = subprocess.run(["git", "-c", "safe.directory=*", "status", "--porcelain", "--", str(path)], cwd=ROOT, capture_output=True, text=True)
    if st.stdout.strip():                                          # new or changed in this working tree: it lands with the next commit, today
        return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    r = subprocess.run(["git", "-c", "safe.directory=*", "log", "-1", "--format=%H %cs", "--", str(path)], cwd=ROOT, capture_output=True, text=True)
    found = r.stdout.split()
    if not found:
        return None if shallow() else "uncommitted"
    return None if found[0] in boundary() else found[1]


# ------------------------------------------------------------------------------- the tests inside the index
def from_index():
    """One row per Kubernetes test and one per stack. The number is the index's own (the resource reading of the test, or the
    stack's category); the benefit word counts every judged gauge of the test's table, as the wiring page does."""
    cases = wv.real_stacks(wv.load_index())
    rows = []
    names = {"V7_PGBENCH.md": "PostgreSQL, the pooler's pool size", "V7_KAFKA.md": "Kafka, the consumer group's size",
             "V7_REDIS.md": "Redis, the cache's memory ceiling", "V7_YCSB.md": "MongoDB, the storage engine's cache size",
             "V7_SYSBENCH.md": "MySQL, the buffer pool's size"}
    stacks = {}
    for c in cases:
        if not c["counted"]:
            continue
        g, l_, gv = (len(c["judged"][k]) for k in ("gain", "loss", "given"))
        items = items_of(c["judged"])
        f = c["source"].rsplit("/", 1)[-1]
        if "Kubernetes" in c["domain"]:
            rows.append({"date": updated(LIVE / f), "benchmark": "Real Kubernetes, " + c["case"], "benefit": benefit_word(g, l_, gv), "pct": c["resource_pct"],
                         "gain": g, "loss": l_, "given": gv, "words": in_words(items), "what": "the index's reading of this test: p95, machines, energy, and work where measured", "file": c["source"]})
        else:
            s_ = stacks.setdefault(f, {"ratios": [], "gain": 0, "loss": 0, "given": 0, "parts": [], "items": []})
            s_["ratios"].append(1 + (c["resource_pct"] or 0.0) / 100.0); s_["gain"] += g; s_["loss"] += l_; s_["given"] += gv; s_["items"] += items
            s_["parts"].append({"case": c["workload"], "pct": c["resource_pct"] or 0.0, "benefit": benefit_word(g, l_, gv), "loss": l_, "words": in_words(items)})
    for f, s_ in stacks.items():
        rows.append({"date": updated(LIVE / f), "benchmark": names.get(re.sub(r"^V\d+_", "V7_", f), f), "benefit": benefit_word(s_["gain"], s_["loss"], s_["given"]), "pct": pct(gmean(s_["ratios"])),
                     "gain": s_["gain"], "loss": s_["loss"], "given": s_["given"], "words": in_words(s_["items"]),
                     "what": "the index's category: its untouched workloads together (work, p95, the resource held, host CPU)",
                     "file": f"results/live/{f}", "parts": s_["parts"]})
    return rows


def headline_row():
    """The one number over every real test, from the index's own file."""
    p = ROOT / "results" / "OMNI_INDEX.json"
    if not p.exists():
        return None
    d = json.loads(p.read_text())
    hl = d.get("headline_pct", d.get("resource_headline_pct"))
    if hl is None:
        return None
    cases = [c for c in wv.real_stacks(wv.load_index()) if c["counted"]]
    g, l_, gv = (sum(len(c["judged"][k]) for c in cases) for k in ("gain", "loss", "given"))
    return {"date": updated(ROOT / "results" / "OMNI_INDEX.md"), "benchmark": "Every real test together: the Omni index", "benefit": benefit_word(g, l_, gv), "pct": hl,
            "gain": g, "loss": l_, "given": gv, "words": "the six real categories together; each stack's own words are in its row",
            "what": "the headline: six real categories weighed the same (the index's resource reading)", "file": "results/OMNI_INDEX.md"}


# -------------------------------------------------------------------------- three-run tables outside the index
def from_abc_table(fname, name, what):
    """A Kubernetes-style three-run table (rows keyed by gauge), scored with the index's measures where present and every
    judged gauge otherwise."""
    p = LIVE / fname
    if not p.exists():
        return None
    d = json.loads(p.read_text())
    ratios, n_ = [], {"gain": 0, "loss": 0, "given": 0}
    items = []
    for key, row in d["rows"].items():
        aim = wv.row_aim(key, row)                                  # every judged gauge of these tables is time waited or a resource spent but the capacity
        try:
            c = wv.classify(row["reading"], aim)
        except ValueError:                                         # a row of its own kind (a hand-back receipt): shown, not a gauge
            continue
        if c == "unjudged":
            continue
        if c in n_:
            rs = []
            for r in row["runs"]:
                n, o = r.get("native"), r.get("omni")
                if n is None or o is None or n <= 0 or o <= 0:
                    continue
                rs.append(o / n if aim == "higher" else n / o)
            if rs:
                ratios.append(gmean(rs)); n_[c] += 1
                items.append((wv.K8S_GAUGE.get(key, key), WORD_OF[c], wv.pct_range(row["runs"]), aim))
            else:
                ratios.append(1.0)
        else:
            ratios.append(1.0)
    return {"date": updated(LIVE / fname.replace(".json", ".md")), "benchmark": name, "benefit": benefit_word(n_["gain"], n_["loss"], n_["given"]),
            "pct": pct(gmean(ratios)), **n_, "words": in_words(items), "what": what, "file": f"results/live/{fname.replace('.json', '.md')}"}


# ------------------------------------------------------------------------------------- the simulators (markdown)
def sim_case_ratio(rows, aims=None):
    """One case's oriented ratio from a simulator table's rows: gauges judged across our three runs only, each oriented
    by its aim (wv.sim_aims(): a gauge that aims higher counts omni / native, any other native / omni). Returns the ratio and
    the counts of GAIN, LOSS and power given."""
    head = rows[0]; ridx = len(head) - 1
    abc = [i for i, h in enumerate(head) if h in ("A", "B", "C")]
    ratios, n_ = [], {"gain": 0, "loss": 0, "given": 0}
    for r in rows[1:]:
        if len(r) != len(head):
            continue
        aim = (aims or {}).get(r[0])
        c = wv.classify(r[ridx], aim)
        if c == "unjudged":
            continue
        if c not in n_:
            ratios.append(1.0); continue
        vals = []
        for i in abc:
            s = r[i].replace("−", "-")
            if s.endswith("%"):
                try:
                    vals.append(float(s[:-1]) / 100.0)
                except ValueError:
                    pass
        if not vals:
            ratios.append(1.0); continue
        change = sum(vals) / len(vals)
        aims_lower = (c == "gain" and change < 0) or (c in ("loss", "given") and change > 0)
        r_ = (1.0 / (1.0 + change)) if aims_lower else (1.0 + change)
        if r_ <= 0:
            r_ = 1e-6
        ratios.append(r_); n_[c] += 1
    return gmean(ratios), n_["gain"], n_["loss"], n_["given"]


def from_sim(fname, name, moved_titles, what, left_native_title=None):
    p = LIVE / fname
    if not p.exists():
        return None
    cases = []
    for sec in wv.parse_sim(p):
        if left_native_title and sec["title"].startswith(left_native_title):
            for r in sec["table"][1:]:                             # nothing moved: nothing gained, nothing lost
                if r and r[0]:
                    cases.append({"case": r[0] + " (left native by the engine's own trial)", "pct": 0.0, "benefit": STEADY, "gain": 0, "loss": 0, "given": 0,
                                  "words": f"{STEADY}: nothing moved", "items": []})
            continue
        tag = next((t for t in moved_titles if sec["title"].startswith(t)), None)
        if tag is None:
            continue
        for sub in sec["subs"]:
            cname = sub["title"].split(":", 1)[0].strip()
            if fname in ("V3_SWARM.md", "V7_SWARM.md") and cname == "tuning":
                continue
            if not sub["rows"]:
                continue
            aims = wv.sim_aims(fname)
            r, g, l_, gv = sim_case_ratio(sub["rows"], aims)
            j = wv.sim_rows_judged(sub["rows"], aims)
            items = items_of(j)
            cases.append({"case": cname + (f" ({moved_titles[tag]})" if moved_titles[tag] else ""), "pct": pct(r), "benefit": benefit_word(g, l_, gv),
                          "gain": g, "loss": l_, "given": gv, "words": in_words(items), "items": items})
    if not cases:
        return None
    g, l_, gv = (sum(c[k] for c in cases) for k in ("gain", "loss", "given"))
    all_items = [it for c in cases for it in c.get("items", [])]
    for c in cases:
        c.pop("items", None)
    return {"date": updated(p), "benchmark": name, "benefit": benefit_word(g, l_, gv), "pct": pct(gmean([1 + c["pct"] / 100.0 for c in cases])),
            "gain": g, "loss": l_, "given": gv, "words": in_words(all_items), "what": what, "file": f"results/live/{fname}", "parts": cases}


# ---------------------------------------------------------------------------------------------- the organisms
def from_organisms(fname, name, what):
    p = LIVE / fname
    if not p.exists():
        return None
    d = json.loads(p.read_text())
    cells, all_items = [], []
    for cell, c in d["organisms"].items():
        ratios, n_, items = [], {"gain": 0, "loss": 0, "given": 0}, []
        for k, v in c["rows"].items():
            if k.startswith("organism") or v.get("neutral") or v.get("same"):
                continue                                           # the cluster's own gauges decide; the modelled organism is judged in the realms table
            sure = v["n"] > 1 and (v["lo"] > 0 or v["hi"] < 0)
            if not sure or v["native"] <= 0 or v["omni"] <= 0:
                ratios.append(1.0); continue
            t = row_gain(v)
            lower = t == (v["omni"] < v["native"])                 # the report's own aim: a GAIN that fell means the gauge aims lower or is spent
            aim = gel_aim("lower", k) if lower else "higher"
            ratios.append(v["native"] / v["omni"] if lower else v["omni"] / v["native"])
            c_ = "gain" if t else ("given" if aim == "spent" else "loss")
            n_[c_] += 1
            items.append((wv.K8S_GAUGE.get(k, k), WORD_OF[c_], f"{v['pct']:+.1f}%", aim))
        all_items += items
        cells.append({"case": cell.replace("@", " at ") + " copies", "pct": pct(gmean(ratios)), "benefit": benefit_word(n_["gain"], n_["loss"], n_["given"]),
                      **n_, "words": in_words(items)})
    g, l_, gv = (sum(x[k] for x in cells) for k in ("gain", "loss", "given"))
    return {"date": updated(LIVE / fname.replace(".json", ".md")), "benchmark": name, "benefit": benefit_word(g, l_, gv),
            "pct": pct(gmean([1 + x["pct"] / 100.0 for x in cells])), "gain": g, "loss": l_, "given": gv, "words": in_words(all_items), "what": what,
            "file": f"results/live/{fname.replace('.json', '.md')}", "parts": cells}


def from_realms():
    p = ROOT / "results" / "realms" / "REALMS.json"
    if not p.exists():
        return None
    d = json.loads(p.read_text())
    tower = d["organisms"].get("tower")
    if not tower:
        return None
    prim = tower["summary"]["primary"]
    clear = prim[1] > 0 or prim[2] < 0
    g = int(clear and prim[0] > 0); l_ = 0; given = int(clear and prim[0] < 0)   # work per energy that fell is power given
    return {"date": updated(ROOT / "results" / "realms" / "REALMS.md"), "benchmark": "The 945 modelled muscles as one tower, every muscle written at once",
            "benefit": benefit_word(g, l_), "pct": 100 * prim[0] if clear else 0.0, "gain": g, "loss": l_, "given": given,
            "words": (f"work per energy up {100 * prim[0]:.1f}% ({GAIN})" if clear and prim[0] > 0
                      else f"work per energy down {abs(100 * prim[0]):.1f}% ({GIVEN})" if clear else f"{STEADY}: nothing moved 0.5% or more across our three runs"),
            "what": "the tower's work per energy over ten paired seeds; a model, evidence class S", "file": "results/realms/REALMS.md"}


def newest_table(fname):
    """The same benchmark's table on the newest engine that has one (V<n>_<BENCHMARK>.json with the highest n), so a later
    engine's three runs take the row the moment their table lands with a reading (tools/readings.py, landed); tables of two
    engines are never pooled."""
    base = re.sub(r"^V\d+_", "", fname)
    found = sorted((int(m.group(1)), f.name) for f in LIVE.glob("V*_" + base) if (m := re.fullmatch(r"V(\d+)_" + re.escape(base), f.name)))
    return next((n for _, n in reversed(found) if landed(LIVE / n)), found[-1][1]) if found else fname


def card_line() -> str:
    """The card's paragraph, from the newest engine's three-run card tables on disk (tools/gpu_abc.py), never written by hand.
    The card is not on the sheet: at the factory dial (the max) native already runs both knobs at their top and the governor
    writes nothing; the tune-down and the cap are other tunes, their results their own."""
    def version(f):
        m = re.match(r"V(\d+)_", f.name)
        return int(m.group(1)) if m else -1
    found = sorted((ROOT / "results" / "gpu").glob("V*_ABC.json"), key=lambda f: (version(f), f.name))
    newest = [f for f in found if version(f) == version(found[-1])] if found else []
    if not newest:
        return ("- **The card (NVIDIA)**: no three-run card table on disk; every rental, its cost and what came back is in "
                "`docs/RUN_LEDGER.md`.")
    parts = []
    for f in newest:
        rec = json.loads(f.read_text())
        rows = rec.get("rows", {})
        if isinstance(rows, list):                     # the stacked box (tools/hil_abc.py): the card's work per energy, size by size
            by_size = {}
            for r in rows:
                if r.get("part") == "card" and r.get("measure") == "primary":
                    by_size.setdefault(r["copies"], []).append(reading_kind(r["reading"]))
            sizes = []
            for copies, kinds in sorted(by_size.items()):
                counts = {}
                for k in kinds:
                    counts[k] = counts.get(k, 0) + 1
                sizes.append(f"at {copies} {'copy' if copies == 1 else 'copies'} " + ", ".join(f"{n} {k}" for k, n in sorted(counts.items(), key=lambda kv: -kv[1])) + f" of {len(kinds)} organisms")
            parts.append(f"{rec.get('title', f.stem)}: the card's work per energy " + "; ".join(sizes) + f" (`{f.with_suffix('.md').relative_to(ROOT)}`)")
            continue
        row = rows.get("work per energy (served requests per kJ)", {})
        parts.append(f"{rec.get('title', f.stem)}: work per energy {row.get('reading', 'no value')} "
                     f"(`{f.with_suffix('.md').relative_to(ROOT)}`)")
    return ("- **The card (NVIDIA)**: at the factory dial (the max) native already runs both knobs at their top and the "
            "governor writes nothing, so the card is not on the sheet; the other tunes, each its own result: "
            + "; ".join(parts) + ". Every rental, its cost and what came back is in `docs/RUN_LEDGER.md`.")


def manual_block(rows) -> str:
    """The Owner's Manual's evidence table: every row of the sheet, each naming the engine its table ran on."""
    L = [M_BEGIN, "", "| What (engine, three runs each) | Benefit? | How much | Every change judged across our three runs, in words | Table |",
         "|---|---|---:|---|---|"]
    for r in rows:
        L.append(f"| {r['benchmark']} ({r['engine']}) | **{r['benefit']}** | {fmt_pct_words(r['pct'], r.get('loss', 0))} | "
                 f"{r.get('words', '')} | `{r['file']}` |")
    return "\n".join(L + ["", M_END])


def main(check=False):
    rows = from_index()
    for fname, name, what in [
        ("V3_ROBUST_KILL.json", "Robustness: the governor killed outright mid-run", "the whole window, a kill and a restart inside it; p95, machines, energy"),
        ("V7_ROBUST_LONG.json", "Robustness: the two-hour run", "the two-hour window; p95, machines, energy"),
    ]:
        r = from_abc_table(newest_table(fname), name, what)
        if r:
            rows.append(r)
    for fname, name, titles, what, *left in [
        ("V7_MUJOCO.md", "Robot arms (MuJoCo), the three untouched robots", {"Robots where Omni moved the override": ""}, "every judged gauge of each robot's table (energy, copper heating, torque, tracking); a robot the engine left native reads 0", "Robots where the paired trial left the override native"),
        ("V7_PANDAPOWER.md", "Power grids (SimBench), both load models", {"ZIP loads": "ZIP loads", "constant-power loads": "constant-power loads"}, "every judged gauge of every grid, then the grids together"),
        ("V7_CITYLEARN.md", "Buildings and batteries (CityLearn), the districts with batteries", {"Districts with electric batteries": ""}, "every CityLearn score of every district, then the districts together"),
        ("V7_SWARM.md", "Drone swarms, the three untouched cells", {"Cells where Omni moved the cruise": ""}, "every judged gauge of every cell"),
    ]:
        r = from_sim(newest_table(fname), name, titles, what, left[0] if left else None)
        if r:
            rows.append(r)
    for fname, name, what in [
        ("V3_SIX_KUBE.json", "The six organisms with the real cluster inside, 10 and 100 copies", "the cluster's own gauges in every cell; the modelled organism is judged in the realms table"),
        ("V3_BIG_ORGANISM.json", "The big organisms with the real cluster inside, 1,000 copies on Azure", "the cluster's own gauges in both cells"),
    ]:
        r = from_organisms(fname, name, what)
        if r:
            rows.append(r)
    r = from_realms()
    if r:
        rows.append(r)
    for fname, name, what in NEWEST:
        fname = newest_table(fname)
        r = from_abc_table(fname, name, what)
        if not r:
            continue
        same = re.sub(r"^V\d+_", "", fname).replace(".json", ".md")
        rows = [x for x in rows if not re.search(r"/V\d+_" + re.escape(same) + "$", x["file"])]
        rows.append(r)
    hl = headline_row()
    if hl:
        rows.append(hl)
    for r in rows:
        r["engine"] = engine_of(r["file"])
        # nine places: the last digits of a geometric mean differ between Python versions, and the sheet is checked as text
        r["pct"] = None if r.get("pct") is None else round(r["pct"], 9)
        for p_ in r.get("parts") or []:
            p_["pct"] = None if p_.get("pct") is None else round(p_["pct"], 9)
    if any(r["date"] is None for r in rows):                       # no history here: the dates the sheet already carries, by benchmark
        known = {}
        if OUT_JSON.exists():
            known = {(x["benchmark"], x["file"]): x["date"] for x in json.loads(OUT_JSON.read_text())["rows"]}
        for r in rows:
            if r["date"] is None:
                r["date"] = known.get((r["benchmark"], r["file"]), "unknown")
    rows.sort(key=lambda x: (x["date"], x["benchmark"]), reverse=True)
    if hl:
        rows.remove(hl); rows.insert(0, hl)

    L = ["# The benefit sheet: one number per benchmark, its word, and every change said in words", "", *receipt_key(), "",
         "The founder's orders of 9 and 13 October 2026: next to every benchmark, say whether Omni-Compass on top was a benefit to the "
         "system and by how much, in one number whose sign always means the same thing, and say it in **GAIN**, **STEADY** and **LOSS**, "
         "judged by what each gauge is for and never by the sign of its number (the key: `docs/HOW_TO_READ_THE_RESULTS.md`). **On this sheet "
         "the sign is the system's own declared aims, gauge by gauge: a plus is a GAIN; a minus is a LOSS on work, speed, misses or "
         "failures, and power given on a resource spent (energy, machines, memory).** The number carries its word. Beside it every change "
         "judged across our three runs is written out with which way it went and its word: \"p95 cut 65% (GAIN)\", \"memory ceiling "
         "held up 215% (power given)\". An operator whose aims differ reads the same numbers the other way.", "",
         "The result tables (the files in the last column) keep every change with its raw sign: a response time that fell reads \"-65%\" "
         "there, and the Reading column beside it says GAIN.", "",
         "The number is the Omni index's rule (`results/OMNI_INDEX.md`): each judged gauge becomes a ratio oriented so that above one is "
         "a GAIN; it counts only where judged across our three runs, anything else counts as exactly one; the number "
         "is the geometric mean of the ratios, minus one, in percent. For the tests inside the index the number is the index's own "
         "resource reading of that test; for a stack with several workloads it is the stack's index category; for the simulators and the "
         "organisms the same arithmetic runs over every judged gauge of their tables. Built from the tables by `tools/benefit_sheet.py`, "
         "checked by `verify.py`.", "",
         "**Benefit?** reads **GAIN** (gauges GAIN across our three runs, none LOSS or power given), **GAIN, power given** (a GAIN bought "
         "with a resource put in, named beside it), **GAIN AND LOSS** (both; the number says which way the trade nets by this scoring, and "
         "the wiring page `docs/WIRING_VERDICTS.md` says what pays for what), **LOSS** (a LOSS and no GAIN), **power given** (a resource put "
         "in and nothing gained) or **STEADY** (nothing moved 0.5% or more across our three runs). LOSS should never appear: where it "
         "does, the row stands and its cause is found and fixed.", "",
         "Every row names the engine its table ran on (read from the table). Results are never read across engines: a row on an "
         "older engine stands as that engine's result until the same benchmark's three runs on the engine that stands replace "
         "it here, and every benchmark is rerun on the engine that stands.", "",
         "| Date | Benchmark | Engine | Benefit? | How much | Every change judged across our three runs, in words | Table |",
         "|---|---|---|---|---:|---|---|"]
    for r in rows:
        L.append(f"| {r['date']} | {r['benchmark']} | {r['engine']} | **{r['benefit']}** | **{fmt_pct_words(r['pct'], r.get('loss', 0))}** | {r.get('words', '')} | `{r['file']}` |")
    L += ["", "## The parts behind a row", "",
          "Where a row sums several workloads, grids, districts, cells or robots, each part with its own number, the same way round:", ""]
    for r in rows:
        if r.get("parts"):
            L.append(f"- **{r['benchmark']}**: " + "; ".join(f"{p_['case']} {fmt_pct_words(p_['pct'], p_.get('loss', 0))} ({p_['benefit']}" + (f": {p_['words']}" if p_.get('words') else "") + ")" for p_ in r["parts"]) + ".")
    L += ["", "## Not on the sheet, and why", "",
          "- **Azure's managed Kubernetes, the bill** (`results/live/V1_AKS_STEADY.md`, `V1_AKS_BURST.md`): Omni v1, a 4-worker fleet, every gauge STEADY, inside the noise: 0%, and too small a fleet to show one machine.",
          "- **The governor's own share of the machine** (`results/live/V3_OWN_COST.md`): 0.6% to 1.3% of one core at every size; shown, not a benchmark against native.",
          card_line(),
          "- **The index's second reading** (service alone, `results/OMNI_INDEX.md`): a second true number for the same tests, not repeated here; this sheet carries the preregistered one.", ""]
    md = "\n".join(legal_stamp(with_own_runs(L))) + "\n"
    js = json.dumps({"rows": rows}, indent=1) + "\n"
    book = MANUAL.read_text(encoding="utf-8") if MANUAL.exists() else ""
    if M_BEGIN in book and M_END in book:
        a, z = book.index(M_BEGIN), book.index(M_END) + len(M_END)
        book = book[:a] + manual_block(rows) + book[z:]
    if check:
        bad = [str(p.relative_to(ROOT)) for p, text in ((OUT_MD, md), (OUT_JSON, js), (MANUAL, book)) if not p.exists() or p.read_text() != text]
        if M_BEGIN not in book:
            bad.append(f"{MANUAL.relative_to(ROOT)} (its evidence block is missing)")
        if bad:
            print("benefit sheet out of date (python3 tools/benefit_sheet.py): " + ", ".join(bad))
            return 1
        print("benefit sheet: in line with the tables")
        return 0
    OUT_MD.write_text(md); OUT_JSON.write_text(js)
    if M_BEGIN in book:
        MANUAL.write_text(book, encoding="utf-8")
    print(f"{OUT_MD.relative_to(ROOT)}: {len(rows)} rows; {OUT_JSON.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(check="--check" in sys.argv[1:]))

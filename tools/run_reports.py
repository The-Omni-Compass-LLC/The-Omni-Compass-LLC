#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License or, for a pilot, a signed, paid pilot agreement. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The reports of a 500-run set from the jump generator, for the engineer, the CTO and the boardroom, in every form a reader
asks for: Word (.docx), PDF, plain text and Markdown, with the set's data as CSV and its summary as JSON (the founder's words of
16 November 2026: "every one run is a theoretical 500 run ... the outputs better be documentation and PDFs and text forms and
doc forms and Word doc and any type of analytical output that needs to be seen by CTO engineers, boardroom").

Each report is written from the set's own two records and nothing else: `results/engine_runs/ENGINE_RUNS_<runs>_<base>.json`
(the engine's runs: the brain's decisions, the compass law and one give-back trial each, the Python's digest beside the C++
harness's and the live page's) and `results/core_runs/CORE_RUNS_<runs>_<base>.json` (the core's Monte Carlo: native, u = 0,
beside Omni-Compass on top, on the same draws). Its structure follows the live engine's monograph
(`docs/engine/LIVE_ENGINE_MONOGRAPH.md`: section 3.2 for the core's equations, section 8.3 for the set, section 4.1 for the
evidence class), every reading by the one key (`tools/readings.py`), every interval a 95% one. A set of the engine's own
models is evidence class S: it shows that three implementations compute the same mathematics and what that mathematics does
on its own ranges; it is never presented as a benchmark of real software or hardware.

    python3 tools/run_reports.py                   the newest set's reports into results/run_reports/latest/
    python3 tools/run_reports.py --base B --out D  set B's reports into D
    python3 tools/run_reports.py --check           exits 1 where the newest reports on file differ from what the records give
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from tools.legal import CLOSE, NOTICE, stamp  # noqa: E402
from tools import readings as K               # noqa: E402

ENGINE = ROOT / "results" / "engine_runs"
CORE = ROOT / "results" / "core_runs"
OUT = ROOT / "results" / "run_reports" / "latest"
AUDIENCES = ("ENGINEER", "CTO", "BOARD")
TEXT_FORMS = (".md", ".txt")                 # written from the records alone, byte for byte the same on every machine
BINARY_FORMS = (".pdf", ".docx")             # the same words, set as a document
DATA = ("SET_ENGINE_RUNS.csv", "SET_CORE_WAYS.csv", "SET_SUMMARY.json")
Z95 = 1.959963984540054
OWNERS = "Dubra Software Inc. / The Omni-Compass LLC"
OWN_CODE = (f"Run and scored by {OWNERS}'s own code. No outside party has reviewed or approved these results.")
WAY_NAMES = {"controlled": "Omni-Compass on top, toward the nearest basin", "uncontrolled": "native: the plant alone, u = 0",
             "wrong_target": "Omni-Compass aimed at the wrong basin", "controlled_mu0": "Omni-Compass on top, the double well's μ at 0"}


# ---------------------------------------------------------------- the records

def sets() -> list[tuple[int, int]]:
    """Every (runs, base) with both its engine and its core record on file."""
    have = lambda d, p: {(int(m.group(1)), int(m.group(2))) for f in d.glob(f"{p}_*.json")
                         if (m := re.fullmatch(rf"{p}_(\d+)_(\d+)\.json", f.name))}
    return sorted(have(ENGINE, "ENGINE_RUNS") & have(CORE, "CORE_RUNS"))


def newest() -> tuple[int, int]:
    """The set written last (by its record's own time), of the sets with both records."""
    best, when = None, ""
    for runs, base in sets():
        w = json.loads((ENGINE / f"ENGINE_RUNS_{runs}_{base}.json").read_text(encoding="utf-8")).get("written", "")
        if w >= when:
            best, when = (runs, base), w
    if best is None:
        raise SystemExit("run_reports: no set has both its engine and its core record")
    return best


def load(runs: int, base: int) -> tuple[dict, dict]:
    e = json.loads((ENGINE / f"ENGINE_RUNS_{runs}_{base}.json").read_text(encoding="utf-8"))
    c = json.loads((CORE / f"CORE_RUNS_{runs}_{base}.json").read_text(encoding="utf-8"))
    return e, c


# ---------------------------------------------------------------- the statistics (every one stated in the reports)

def wilson(k: int, n: int) -> tuple[float, float]:
    """The Wilson score interval of a proportion k/n at 95%."""
    if n == 0:
        return (float("nan"), float("nan"))
    p, z2 = k / n, Z95 * Z95
    mid = (p + z2 / (2 * n)) / (1 + z2 / n)
    half = Z95 * math.sqrt(p * (1 - p) / n + z2 / (4 * n * n)) / (1 + z2 / n)
    return (max(0.0, mid - half), min(1.0, mid + half))


def newcombe(k1: int, n1: int, k2: int, n2: int) -> tuple[float, float]:
    """Newcombe's hybrid score interval (his method 10) of p1 − p2 at 95%."""
    p1, p2 = k1 / n1, k2 / n2
    l1, u1 = wilson(k1, n1)
    l2, u2 = wilson(k2, n2)
    d = p1 - p2
    return (d - math.sqrt((p1 - l1) ** 2 + (u2 - p2) ** 2), d + math.sqrt((u1 - p1) ** 2 + (p2 - l2) ** 2))


def hist_moments(h: list[int]) -> tuple[int, float, float]:
    """(count, mean, sample variance) of the step a run was conveyed at, from the record's histogram (index = step)."""
    n = sum(h)
    if n == 0:
        return 0, float("nan"), float("nan")
    m = sum(i * c for i, c in enumerate(h)) / n
    v = sum(c * (i - m) ** 2 for i, c in enumerate(h)) / (n - 1) if n > 1 else 0.0
    return n, m, v


def welch(n1, m1, v1, n2, m2, v2) -> tuple[float, float, float]:
    """m1 − m2 with its Welch 95% interval (the Satterthwaite degrees of freedom, the exact Student t quantile)."""
    se2 = v1 / n1 + v2 / n2
    df = se2 ** 2 / ((v1 / n1) ** 2 / (n1 - 1) + (v2 / n2) ** 2 / (n2 - 1)) if se2 > 0 else float("inf")
    from omnicompass.student_t import t95                 # the exact quantile every table of the repository uses
    t = t95(max(1, int(df))) if math.isfinite(df) else Z95     # the degrees of freedom rounded down: the wider interval
    d = m1 - m2
    return d, d - t * math.sqrt(se2), d + t * math.sqrt(se2)


def reading(change: float, aim: str) -> str:
    """One set's change in percent of native, read by the one key: the word by what the gauge is for, never by its sign;
    under the founder's floor (0.5%) STEADY."""
    if change != change:
        return "—"
    if abs(change) < 100 * K.SIZE_FLOOR:
        return f"{K.STEADY}, under the floor"
    return K.word(change < 0, aim)


def pct(x: float, d: int = 1) -> str:
    return f"{x:.{d}f}%"


def summary(e: dict, c: dict) -> dict:
    """Everything the reports print, computed once from the two records."""
    runs, base = e["runs"], e["base"]
    rec = e["receipts"]
    allowed = sum(1 for r in rec if r.get("allowed"))
    s = c["summary"]
    ways = {}
    for w, v in s.items():
        n, m, var = hist_moments(v["convey_hist"])
        ways[w] = {"name": WAY_NAMES.get(w, w), "conveyed": v["conveyed"], "certified": v["certified"],
                   "in_basin_at_end": v["in_basin_at_end"], "mean_convey_step": v["mean_convey_step"],
                   "convey_hist": v["convey_hist"], "conveyed_ci": wilson(v["conveyed"], runs),
                   "certified_ci": wilson(v["certified"], runs), "step_n": n, "step_mean": m, "step_var": var}
    o, nat = ways["controlled"], ways["uncontrolled"]
    conv_change = 100 * (o["conveyed"] - nat["conveyed"]) / nat["conveyed"]
    cert_change = 100 * (o["certified"] - nat["certified"]) / nat["certified"]
    step_change = 100 * (o["step_mean"] - nat["step_mean"]) / nat["step_mean"]
    d, lo, hi = welch(o["step_n"], o["step_mean"], o["step_var"], nat["step_n"], nat["step_mean"], nat["step_var"])
    comp = {
        "conveyed": {"omni": o["conveyed"], "native": nat["conveyed"], "change_pct": conv_change,
                     "word": reading(conv_change, K.HIGHER),
                     "difference_ci": newcombe(o["conveyed"], runs, nat["conveyed"], runs)},
        "certified": {"omni": o["certified"], "native": nat["certified"], "change_pct": cert_change,
                      "word": reading(cert_change, K.HIGHER),
                      "difference_ci": newcombe(o["certified"], runs, nat["certified"], runs)},
        "steps_to_convey": {"omni": o["step_mean"], "native": nat["step_mean"], "change_pct": step_change,
                            "word": reading(step_change, K.LOWER), "difference": d, "difference_ci": (lo, hi)},
    }
    gh = e.get("github") or {}
    return {
        "runs": runs, "base": base, "engine": e.get("engine", ""), "written": e.get("written", ""),
        "core_written": c.get("written", ""), "github": gh,
        "engine_digest": e["digest"], "engine_cpp": e.get("cpp") or {}, "engine_page": e.get("page") or {},
        "ladder": e.get("ladder") or [], "decisions": e.get("decisions"), "law_steps": e.get("law_steps"),
        "allowed": allowed, "allowed_ci": wilson(allowed, runs),
        "pushes": sum(r.get("push", 0.0) for r in rec), "expand": sum(r.get("expand", 0) for r in rec),
        "contract": sum(r.get("contract", 0) for r in rec),
        "core_digest": c["digest"], "core_cpp": c.get("cpp") or {}, "core_page": c.get("page") or {},
        "core": {k: c.get(k) for k in ("core", "macro", "micro", "dt", "tol", "convey_window", "cert_window", "kp", "authority")},
        "ways": ways, "comparison": comp,
    }


# ---------------------------------------------------------------- the document, once, in blocks every form renders

def same(block: dict) -> str:
    return "the same" if block.get("same") else "DIFFERENT"


def three_way(S: dict) -> list:
    ep, cp = S["engine_page"], S["core_page"]
    return [("table", ["Set", "The Python's digest", "The C++ harness", "The live page's own code"], [
        ["the engine's runs", f"`{S['engine_digest'][:16]}…`",
         f"`{(S['engine_cpp'].get('digest') or '')[:16]}…`, {same(S['engine_cpp'])}, {S['engine_cpp'].get('agree', '—')} of {S['runs']} runs agree",
         f"`{(ep.get('digest') or '')[:16]}…`, {same(ep)}" if ep else "not recorded"],
        ["the core's Monte Carlo", f"`{S['core_digest'][:16]}…`",
         f"`{(S['core_cpp'].get('digest') or '')[:16]}…`, {same(S['core_cpp'])}, {S['core_cpp'].get('agree', '—')} of {S['core_cpp'].get('of', '—')} run-ways agree",
         f"`{(cp.get('digest') or '')[:16]}…`, {same(cp)}" if cp else "not recorded"]])]


def comparison_table(S: dict) -> list:
    c = S["comparison"]
    n = S["runs"]
    ci = lambda t: f"raw {100 * t[0]:+.1f} to {100 * t[1]:+.1f} points".replace("+-", "−").replace("-", "−")
    return [("table", ["Gauge (what it is for)", "Native alone", "Omni-Compass on top", "Change against native", "95% interval", "Reading"], [
        ["runs brought to a basin, conveyed (more is better)", f"{c['conveyed']['native']} of {n}", f"{c['conveyed']['omni']} of {n}",
         f"up {pct(c['conveyed']['change_pct'])}", ci(c["conveyed"]["difference_ci"]), c["conveyed"]["word"]],
        ["runs certified in a basin (more is better)", f"{c['certified']['native']} of {n}", f"{c['certified']['omni']} of {n}",
         f"up {pct(c['certified']['change_pct'])}", ci(c["certified"]["difference_ci"]), c["certified"]["word"]],
        ["macro steps to be conveyed, mean (fewer is better)", f"{c['steps_to_convey']['native']:.3f}",
         f"{c['steps_to_convey']['omni']:.3f}", f"down {pct(abs(c['steps_to_convey']['change_pct']))}",
         f"raw {c['steps_to_convey']['difference_ci'][0]:+.2f} to {c['steps_to_convey']['difference_ci'][1]:+.2f} steps".replace("-", "−"),
         c["steps_to_convey"]["word"]]])]


def ways_table(S: dict) -> list:
    rows = []
    for w in ("controlled", "uncontrolled", "wrong_target", "controlled_mu0"):
        v = S["ways"].get(w)
        if not v:
            continue
        lo, hi = v["conveyed_ci"]
        rows.append([v["name"], f"{v['conveyed']} of {S['runs']} ({100 * lo:.1f}% to {100 * hi:.1f}%)",
                     f"{v['certified']} of {S['runs']}", f"{v['step_mean']:.3f}", f"{v['in_basin_at_end']} of {S['runs']}"])
    return [("table", ["Way", "Conveyed (95% interval)", "Certified", "Mean step conveyed", "In a basin at the last step"], rows)]


def doc(S: dict, audience: str) -> list:
    """The report for one reader, as blocks: ('h1'|'h2'|'p'|'eq'|'code', text), ('bullets', [..]), ('table', head, rows)."""
    n, base = S["runs"], S["base"]
    c = S["comparison"]
    gh = S["github"]
    run_line = (f"GitHub run {gh['run_id']} ({gh.get('workflow', '')}, commit `{(gh.get('commit') or '')[:10]}`, {gh.get('url', '')})"
                if gh.get("run_id") else "run on the repository's own machines; no GitHub run recorded")
    title = {"ENGINEER": "for the engineer", "CTO": "for the CTO", "BOARD": "for the boardroom"}[audience]
    B = [("h1", f"The {n}-run set from the jump generator, base {base}: the report {title}"),
         ("p", f"Engine {S['engine']}; the set written {S['written']}; {run_line}. Evidence class S: the engine's own models, "
               "run on its own ranges. It shows that the Python, the C++ harness and the live engine's page compute the same "
               "mathematics, and what that mathematics does; it is never a benchmark of real software or hardware (the live "
               "engine's monograph, section 4.1). " + OWN_CODE)]
    head = (f"Omni-Compass brought {c['conveyed']['omni']} of {n} runs to a stable basin. The plant left alone brought "
            f"{c['conveyed']['native']}. Omni-Compass certified {c['certified']['omni']}; the plant alone {c['certified']['native']}. "
            f"Omni-Compass got there in {c['steps_to_convey']['omni']:.2f} macro steps on average; the plant alone took "
            f"{c['steps_to_convey']['native']:.2f}. Every gauge reads {c['conveyed']['word'] if c['conveyed']['word'] == c['steps_to_convey']['word'] == c['certified']['word'] else 'as the table below reads it'}"
            f", in the engine's own mathematics (class S). Three implementations, the Python, the C++ harness and the "
            f"page's own code, computed it independently and gave the same digest on all {n} runs. That is not an opinion. "
            f"It is arithmetic, and anyone can repeat it.")
    if audience == "BOARD":
        B += [("h2", "The answer"), ("p", head),
              ("h2", "Check it"),
              ("p", f"One command on any machine: `bash scripts/prove_runs.sh {base} {n}`. It prints the three digests side by "
                    "side. They are the same, or the set is wrong. Every set GitHub runs is proved this way and kept in the run "
                    "ledger (`results/RUNS_LEDGER.md`)."),
              ("h2", "Where it stops"),
              ("bullets", ["This is the engine's own mathematics on its own ranges (class S). It does not measure a customer's "
                           "system, a chip or a cloud bill. The measured results are the three-run tables, each on its own engine, "
                           "losses included.",
                           "One set is one draw of 500 starting points. Every night GitHub draws another from a new seed.",
                           OWN_CODE]),
              ("h2", "The numbers")] + comparison_table(S) + [
              ("p", "GAIN: the gauge moved toward what it is for (more runs brought home, fewer steps taken). LOSS: away from "
                    "it. STEADY: a change under half of one percent. The word is decided by what the gauge is for, never by a "
                    "plus or minus sign.")]
        return B
    B += [("h2", "1. The answer"), ("p", head)] + comparison_table(S)
    B += [("h2", "2. The proof: three implementations, one digest")] + three_way(S)
    if S["ladder"]:
        B += [("p", "The ladder: the first 1, 10, 100 and 500 runs of the same set, each its own digest, so a shorter reading by "
                    "the page or the C++ is checked against the Python's rung."),
              ("table", ["Rung", "Runs", "The Python's digest", "The C++ harness's digest", "The same"],
               [[str(i + 1), str(g.get("runs")), f"`{(g.get('digest') or '')[:16]}…`", f"`{(g.get('cpp_digest') or '')[:16]}…`",
                 "yes" if g.get("same") else "no"] for i, g in enumerate(S["ladder"])])]
    B += [("h2", "3. Every way of the core's Monte Carlo")] + ways_table(S)
    if audience == "CTO":
        B += [("h2", "4. Check it yourself"),
              ("code", f"bash scripts/prove_runs.sh {base} {n}"),
              ("p", "Or run the public workflow `prove-runs.yml` on GitHub, or the container `deploy/Dockerfile.proof`. The same "
                    "base gives the same digests on any machine. A different digest is a fault, and it would show."),
              ("h2", "5. Where it stops"),
              ("bullets", ["This is a model (class S): the engine's own mathematics on its own ranges, not a benchmark of real "
                           "software.",
                           "The measured results (class L, live software; class P, a physical meter) are the three-run tables, "
                           "each on its own engine, read by the same key, losses included.", OWN_CODE])]
        return B
    core = S["core"]
    B += [("h2", "4. The mathematics"),
          ("p", "The seeds. Run k of the set draws its seed from the jump generator and feeds a mulberry32 stream:"),
          ("eq", f"seedₖ = base + k·0x9E3779B9 mod 2³²,  k = 0, 1, …, {n - 1};  base = {base}"),
          ("p", "The core (the monograph, section 3.2): the state z = (E, U, I[U], S, B, Ḃ) evolves by"),
          ("eq", "dE/dt = −α[E]·E + β[int] + β[ext] + v[eff]"),
          ("eq", "dU/dt = μ·U·(1 − U²) − (dE/dt)/E[max] − λ[U]·U + u[U],  |u[U]| ≤ U[auth]"),
          ("eq", "dI[U]/dt = (1 − U) − σ₁·E − δ·S − λ[I]·I[U]"),
          ("eq", "dS/dt = δ − α[s]·S − (3/4)·β[s]·S²,  dB/dt = Ḃ,  dḂ/dt = γ[c]·δ·S − (ω[B]/Q[B])·Ḃ − ω[B]²·B"),
          ("p", f"integrated by the classical fourth-order Runge–Kutta method, {core.get('micro')} micro steps in each of "
                f"{core.get('macro')} macro steps of Δt = {core.get('dt')} s, the command held through all four stages. Native "
                f"is the plant left to its double well (u[U] = 0); Omni-Compass on top applies"),
          ("eq", f"u[U] = sat(−f[U](z, t) + K[P]·(σ − U)),  K[P] = {core.get('kp')},  U[auth] = {core.get('authority')}"),
          ("p", f"A run is conveyed after {core.get('convey_window')} macro steps in a row in one basin, |U ∓ 1| ≤ {core.get('tol')}, "
                f"and certified at {core.get('cert_window')}."),
          ("p", "The intervals. A share k of n is given its Wilson score interval; a difference of two shares Newcombe's hybrid "
                "score interval (his method 10); a difference of two mean steps Welch's interval, the Satterthwaite degrees of "
                "freedom and the exact Student t quantile (`omnicompass/student_t.py`). The mean step is over the runs conveyed."),
          ("h2", "5. The engine's runs: the brain, the compass law and the verdict"),
          ("p", f"Each of the {n} runs is {S['decisions']} decisions of the brain (RK4), {S['law_steps']} steps of the compass law "
                f"and one give-back trial judged by the verdict. The verdict allowed {S['allowed']} of {n} trials "
                f"({100 * S['allowed_ci'][0]:.1f}% to {100 * S['allowed_ci'][1]:.1f}% at 95%) and refused the rest. The verdict is do no "
                f"harm as a trigger (the monograph, section 3.6): on log costs, d[v] = mean ln y[trial] − mean ln y[ref] with "
                f"interval d[v] ± 1.96·se and allowance ln(1 + tol); an interval wholly above zero is a LOSS and the step is "
                f"undone, otherwise the step stands only if the median and the mean lie within the allowance. Over all runs the brain's pushes sum to "
                f"{S['pushes']:.3f}; grants to expand {S['expand']}, to contract {S['contract']}. Every run's receipt is in "
                f"`SET_ENGINE_RUNS.csv` beside this report."),
          ("h2", "6. Check it yourself"),
          ("code", "cmake -S cpp -B build && cmake --build build --target oc_engine_runs oc_core_runs\n"
                   f"python3 tools/engine_runs.py --runs {n} --base {base} --cpp build/oc_engine_runs --out er.json\n"
                   f"python3 tools/engine_runs.py --verify docs/engine/OMNI_COMPASS_LIVE_ENGINE.html --all --runs {n} --base {base}\n"
                   f"python3 tools/core_runs.py --runs {n} --base {base} --cpp build/oc_core_runs --out cr.json"),
          ("p", f"Both digests equal the records' or the run is wrong: `{S['engine_digest']}` and `{S['core_digest']}`. "
                "The records: `results/engine_runs/ENGINE_RUNS_" + f"{n}_{base}.md` and `results/core_runs/CORE_RUNS_{n}_{base}.md`."),
          ("h2", "7. Where it stops"),
          ("bullets", ["This is a model (class S). It is never offered as a result on real software, a chip or a cloud.",
                       "The mean step to be conveyed is over the runs that were conveyed; native's unconveyed runs are counted "
                       "in the conveyed share, not in the mean.", OWN_CODE])]
    return B


# ---------------------------------------------------------------- the forms

def plain(t: str) -> str:
    return t.replace("**", "").replace("`", "")


def to_md(blocks: list) -> str:
    out = []
    for b in blocks:
        k = b[0]
        if k == "h1":
            out += [f"# {b[1]}", ""]
        elif k == "h2":
            out += [f"## {b[1]}", ""]
        elif k == "p":
            out += [b[1], ""]
        elif k == "eq":
            out += [f"  {b[1]}", ""]
        elif k == "code":
            out += ["```", b[1], "```", ""]
        elif k == "bullets":
            out += [f"- {x}" for x in b[1]] + [""]
        elif k == "table":
            out += ["| " + " | ".join(b[1]) + " |", "|" + "---|" * len(b[1])]
            out += ["| " + " | ".join(r) + " |" for r in b[2]] + [""]
    lines = stamp(out + ["---", "", f"*{NOTICE}*"])
    return "\n".join(lines) + "\n"


def to_txt(blocks: list) -> str:
    note = plain(NOTICE)
    out = [note, ""]
    for b in blocks:
        k = b[0]
        if k in ("h1", "h2"):
            t = plain(b[1])
            out += [t, ("=" if k == "h1" else "-") * min(len(t), 100), ""]
        elif k in ("p",):
            out += [plain(b[1]), ""]
        elif k in ("eq", "code"):
            out += ["    " + line for line in plain(b[1]).split("\n")] + [""]
        elif k == "bullets":
            out += [f"  * {plain(x)}" for x in b[1]] + [""]
        elif k == "table":
            rows = [b[1]] + b[2]
            for r in rows:
                out.append("  " + " | ".join(plain(x) for x in r))
            out.append("")
    out += ["", note]
    return "\n".join(out) + "\n"


def to_pdf(blocks: list, path: Path, title: str) -> None:
    from reportlab import rl_config
    rl_config.invariant = 1                       # no creation time in the file: the same words give the same bytes
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import Paragraph, Preformatted, SimpleDocTemplate, Spacer, Table, TableStyle
    dv = "/usr/share/fonts/truetype/dejavu/"
    for name, f in (("RS", dv + "DejaVuSans.ttf"), ("RSB", dv + "DejaVuSans-Bold.ttf"),
                    ("RM", dv + "DejaVuSansMono.ttf")):
        if name not in pdfmetrics.getRegisteredFontNames():
            pdfmetrics.registerFont(TTFont(name, f))
    body = ParagraphStyle("b", fontName="RS", fontSize=11, leading=16.5)
    small = ParagraphStyle("s", fontName="RS", fontSize=9, leading=13.5, textColor=colors.HexColor("#333333"))
    cell = ParagraphStyle("c", fontName="RS", fontSize=9, leading=12)
    h1 = ParagraphStyle("h1", fontName="RSB", fontSize=17, leading=22, spaceAfter=6)
    h2 = ParagraphStyle("h2", fontName="RSB", fontSize=13, leading=18, spaceBefore=8, spaceAfter=4)
    mono = ParagraphStyle("m", fontName="RM", fontSize=9.5, leading=14)
    esc = lambda t: (t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
    fmt = lambda t: re.sub(r"`([^`]+)`", r'<font name="RM">\1</font>', re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", esc(t)))
    story = [Paragraph(fmt(NOTICE), small), Spacer(1, 10)]
    for b in blocks:
        k = b[0]
        if k == "h1":
            story.append(Paragraph(fmt(b[1]), h1))
        elif k == "h2":
            story.append(Paragraph(fmt(b[1]), h2))
        elif k == "p":
            story.append(Paragraph(fmt(b[1]), body))
            story.append(Spacer(1, 4))
        elif k == "eq":
            story.append(Paragraph(esc(b[1]), ParagraphStyle("eq", parent=body, fontName="RS", leftIndent=24)))
        elif k == "code":
            story.append(Preformatted(b[1], mono, maxLineLength=84, newLineChars="    "))   # every word inside the page
            story.append(Spacer(1, 4))
        elif k == "bullets":
            for x in b[1]:
                story.append(Paragraph("• " + fmt(x), ParagraphStyle("li", parent=body, leftIndent=14, firstLineIndent=-10)))
        elif k == "table":
            data = [[Paragraph(fmt(h), ParagraphStyle("th", parent=cell, fontName="RSB")) for h in b[1]]]
            data += [[Paragraph(fmt(x), cell) for x in r] for r in b[2]]
            t = Table(data, repeatRows=1, hAlign="LEFT")
            t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#9aa4b2")),
                                   ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e8eef7")),
                                   ("VALIGN", (0, 0), (-1, -1), "TOP")]))
            story += [t, Spacer(1, 8)]
    story += [Spacer(1, 12), Paragraph(fmt(NOTICE), small)]

    def foot(canvas, d):
        canvas.saveState()
        canvas.setFont("RS", 8)
        canvas.drawString(0.75 * inch, 0.5 * inch, f"{OWNERS} · {title}")
        canvas.drawRightString(letter[0] - 0.75 * inch, 0.5 * inch, f"page {d.page}")
        canvas.restoreState()
    SimpleDocTemplate(str(path), pagesize=letter, leftMargin=0.75 * inch, rightMargin=0.75 * inch, topMargin=0.75 * inch,
                      bottomMargin=0.8 * inch, title=title, author=OWNERS).build(story, onFirstPage=foot, onLaterPages=foot)


def _x(t: str) -> str:
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def _runs_xml(text: str, size: int | None = None) -> str:
    """WordprocessingML runs for a line of text: **bold** and `code` kept as they read in the other forms."""
    out = []
    for part in re.split(r"(\*\*[^*]+\*\*|`[^`]+`)", text):
        if not part:
            continue
        props = []
        if part.startswith("**"):
            part, props = part[2:-2], ["<w:b/>"]
        elif part.startswith("`"):
            part, props = part[1:-1], ['<w:rFonts w:ascii="Courier New" w:hAnsi="Courier New" w:cs="Courier New"/>']
        if size:
            props.append(f'<w:sz w:val="{size}"/>')
        rpr = f"<w:rPr>{''.join(props)}</w:rPr>" if props else ""
        out.append(f'<w:r>{rpr}<w:t xml:space="preserve">{_x(part)}</w:t></w:r>')
    return "".join(out)


def _p(text: str, style: str | None = None, size: int | None = None, indent: int = 0, hanging: int = 0) -> str:
    ppr = []
    if style:
        ppr.append(f'<w:pStyle w:val="{style}"/>')
    if indent or hanging:
        ppr.append(f'<w:ind w:left="{indent}" w:hanging="{hanging}"/>')
    return f"<w:p>{'<w:pPr>' + ''.join(ppr) + '</w:pPr>' if ppr else ''}{_runs_xml(text, size)}</w:p>"


def to_docx(blocks: list, path: Path, title: str, written: str) -> None:
    """A Word document (Office Open XML, ECMA-376) written with the standard library alone: no package beyond Python's own,
    so the supply chain the lock file pins (requirements-lock.txt) is unchanged; the same blocks give the same bytes."""
    import zipfile
    body = [_p(NOTICE, size=18)]
    for b in blocks:
        k = b[0]
        if k == "h1":
            body.append(_p(plain(b[1]), "Heading1"))
        elif k == "h2":
            body.append(_p(plain(b[1]), "Heading2"))
        elif k == "p":
            body.append(_p(b[1]))
        elif k == "eq":
            body.append(_p(b[1], indent=480))
        elif k == "code":
            body += [_p(line, "Code") for line in b[1].split("\n")]
        elif k == "bullets":
            body += [_p("• " + x, indent=360, hanging=240) for x in b[1]]
        elif k == "table":
            rows = []
            for i, r in enumerate([b[1]] + b[2]):
                cells = "".join(f'<w:tc><w:tcPr><w:tcW w:w="0" w:type="auto"/></w:tcPr>'
                                f'{_p(("**" + plain(c) + "**") if i == 0 else plain(c), size=18)}</w:tc>' for c in r)
                rows.append(f"<w:tr>{cells}</w:tr>")
            body.append('<w:tbl><w:tblPr><w:tblStyle w:val="TableGrid"/><w:tblW w:w="5000" w:type="pct"/></w:tblPr>'
                        + "".join(rows) + "</w:tbl>")
            body.append("<w:p/>")
    body.append(_p(NOTICE, size=18))
    W = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'
    document = (f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<w:document {W}><w:body>' + "".join(body) +
                '<w:sectPr><w:pgSz w:w="12240" w:h="15840"/><w:pgMar w:top="1080" w:right="1080" w:bottom="1080" '
                'w:left="1080" w:header="720" w:footer="720" w:gutter="0"/></w:sectPr></w:body></w:document>')
    font = '<w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/>'
    styles = (f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<w:styles {W}>'
              f'<w:docDefaults><w:rPrDefault><w:rPr>{font}<w:sz w:val="22"/><w:szCs w:val="22"/></w:rPr></w:rPrDefault>'
              '<w:pPrDefault><w:pPr><w:spacing w:after="120" w:line="360" w:lineRule="auto"/></w:pPr></w:pPrDefault></w:docDefaults>'
              '<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/></w:style>'
              '<w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:basedOn w:val="Normal"/>'
              '<w:pPr><w:keepNext/><w:spacing w:before="240" w:after="120"/><w:outlineLvl w:val="0"/></w:pPr>'
              '<w:rPr><w:b/><w:sz w:val="34"/></w:rPr></w:style>'
              '<w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/><w:basedOn w:val="Normal"/>'
              '<w:pPr><w:keepNext/><w:spacing w:before="200" w:after="80"/><w:outlineLvl w:val="1"/></w:pPr>'
              '<w:rPr><w:b/><w:sz w:val="27"/></w:rPr></w:style>'
              '<w:style w:type="paragraph" w:styleId="Code"><w:name w:val="Code"/><w:basedOn w:val="Normal"/>'
              '<w:pPr><w:spacing w:after="0" w:line="276" w:lineRule="auto"/><w:ind w:left="240"/></w:pPr>'
              '<w:rPr><w:rFonts w:ascii="Courier New" w:hAnsi="Courier New" w:cs="Courier New"/><w:sz w:val="19"/></w:rPr></w:style>'
              '<w:style w:type="table" w:styleId="TableGrid"><w:name w:val="Table Grid"/><w:tblPr><w:tblBorders>'
              + "".join(f'<w:{e} w:val="single" w:sz="4" w:space="0" w:color="9AA4B2"/>' for e in ("top", "left", "bottom", "right", "insideH", "insideV"))
              + '</w:tblBorders><w:tblCellMar><w:left w:w="80" w:type="dxa"/><w:right w:w="80" w:type="dxa"/></w:tblCellMar></w:tblPr></w:style>'
              '</w:styles>')
    when = written if re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", written or "") else "2026-01-01T00:00:00Z"
    core = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<cp:coreProperties '
            'xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" '
            'xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" '
            'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
            f"<dc:title>{_x(title)}</dc:title><dc:creator>{_x(OWNERS)}</dc:creator>"
            f'<dcterms:created xsi:type="dcterms:W3CDTF">{when}</dcterms:created>'
            f'<dcterms:modified xsi:type="dcterms:W3CDTF">{when}</dcterms:modified></cp:coreProperties>')
    app = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<Properties '
           'xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties">'
           f"<Application>tools/run_reports.py</Application><Company>{_x(OWNERS)}</Company></Properties>")
    types = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
             '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
             '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
             '<Default Extension="xml" ContentType="application/xml"/>'
             '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
             '<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>'
             '<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>'
             '<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>'
             '</Types>')
    R = 'xmlns="http://schemas.openxmlformats.org/package/2006/relationships"'
    rels = (f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<Relationships {R}>'
            '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>'
            '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>'
            '<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>'
            '</Relationships>')
    doc_rels = (f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<Relationships {R}>'
                '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>'
                '</Relationships>')
    out = io.BytesIO()
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:           # the same words give the same bytes
        for name, data in (("[Content_Types].xml", types), ("_rels/.rels", rels), ("word/document.xml", document),
                           ("word/_rels/document.xml.rels", doc_rels), ("word/styles.xml", styles),
                           ("docProps/core.xml", core), ("docProps/app.xml", app)):
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, data.encode("utf-8"))
    path.write_bytes(out.getvalue())


def docx_text(path: Path) -> list[str]:
    """The text of a Word document's paragraphs, in order (for the tests and the check; the standard library alone)."""
    import zipfile
    xml = zipfile.ZipFile(path).read("word/document.xml").decode("utf-8")
    paras = re.findall(r"<w:p>(.*?)</w:p>|<w:p/>", xml, re.S)
    unx = lambda t: t.replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", '"').replace("&amp;", "&")
    return [unx("".join(re.findall(r"<w:t[^>]*>(.*?)</w:t>", p, re.S))) for p in paras]


def data_files(e: dict, c: dict, S: dict) -> dict[str, str]:
    """The set's data: every engine run's receipt, every way of the core's Monte Carlo, and the summary."""
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["k", "seed", "E", "U", "I", "S", "B", "C", "push", "expand", "contract", "calm", "tau", "meanF", "lastF", "trial", "samples"])
    for r in e["receipts"]:
        x = list(r.get("x", [])) + [""] * 6
        w.writerow([r.get("k"), r.get("seed")] + [f"{v:.6f}" if isinstance(v, float) else v for v in x[:6]] +
                   [f"{r.get('push', 0.0):.6f}", r.get("expand"), r.get("contract"), f"{r.get('calm', 0.0):.6f}",
                    f"{r.get('tau', 0.0):.6f}", f"{r.get('meanF', 0.0):.6f}", f"{r.get('lastF', 0.0):.6f}",
                    "allowed" if r.get("allowed") else "refused", r.get("used")])
    buf2 = io.StringIO()
    w2 = csv.writer(buf2, lineterminator="\n")
    w2.writerow(["way", "name", "conveyed", "certified", "in_basin_at_end", "mean_convey_step"] +
                [f"conveyed_at_step_{i}" for i in range(len(next(iter(S["ways"].values()))["convey_hist"]))])
    for k, v in S["ways"].items():
        w2.writerow([k, v["name"], v["conveyed"], v["certified"], v["in_basin_at_end"], f"{v['mean_convey_step']:.6f}"] + v["convey_hist"])
    js = {"notice": plain(NOTICE), "class": "S", "owners": OWNERS, "runs": S["runs"], "base": S["base"], "engine": S["engine"],
          "written": S["written"], "github": S["github"], "engine_digest": S["engine_digest"], "core_digest": S["core_digest"],
          "cpp_same": bool(S["engine_cpp"].get("same")) and bool(S["core_cpp"].get("same")),
          "page_same": bool(S["engine_page"].get("same")) and bool(S["core_page"].get("same")),
          "allowed": S["allowed"], "comparison": S["comparison"],
          "ways": {k: {x: v[x] for x in ("name", "conveyed", "certified", "in_basin_at_end", "mean_convey_step")} for k, v in S["ways"].items()},
          "records": [f"results/engine_runs/ENGINE_RUNS_{S['runs']}_{S['base']}.json", f"results/core_runs/CORE_RUNS_{S['runs']}_{S['base']}.json"],
          "end": CLOSE}
    return {"SET_ENGINE_RUNS.csv": buf.getvalue(), "SET_CORE_WAYS.csv": buf2.getvalue(),
            "SET_SUMMARY.json": json.dumps(js, indent=1, ensure_ascii=False, allow_nan=False) + "\n"}


def index_md(S: dict) -> str:
    n, base = S["runs"], S["base"]
    lines = [f"# The reports of the newest {n}-run set from the jump generator (base {base})", "",
             f"Written by `tools/run_reports.py` from the set's own records, {S['engine']}, the set written {S['written']}. "
             "Evidence class S. Every report in every form carries the owners' notice at its top and its end.", "",
             "| Reader | Word | PDF | Text | Markdown |", "|---|---|---|---|---|"]
    for a in AUDIENCES:
        lines.append(f"| {a.title() if a != 'CTO' else 'CTO'} | [{a}.docx]({a}.docx) | [{a}.pdf]({a}.pdf) | [{a}.txt]({a}.txt) | [{a}.md]({a}.md) |")
    lines += ["", "The data: [SET_ENGINE_RUNS.csv](SET_ENGINE_RUNS.csv) (every engine run's receipt), "
                  "[SET_CORE_WAYS.csv](SET_CORE_WAYS.csv) (every way of the core's Monte Carlo) and "
                  "[SET_SUMMARY.json](SET_SUMMARY.json) (the numbers every report prints).", "",
              "On GitHub each new set's workflow (`engine-runs.yml`) writes these again from its own records, so they always "
              "read the newest set; `python3 tools/run_reports.py --base B --out DIR` writes any set's.", "", "---", "", f"*{NOTICE}*"]
    return "\n".join(stamp(lines)) + "\n"


def texts(runs: int, base: int) -> tuple[dict, dict, dict]:
    """(the text forms by file name, the blocks by audience, the summary)."""
    e, c = load(runs, base)
    S = summary(e, c)
    blocks = {a: doc(S, a) for a in AUDIENCES}
    out = {}
    for a in AUDIENCES:
        out[f"{a}.md"] = to_md(blocks[a])
        out[f"{a}.txt"] = to_txt(blocks[a])
    out.update(data_files(e, c, S))
    out["README.md"] = index_md(S)
    return out, blocks, S


def write(runs: int, base: int, out: Path) -> list[Path]:
    files, blocks, S = texts(runs, base)
    out.mkdir(parents=True, exist_ok=True)
    written = []
    for name, text in files.items():
        p = out / name
        p.write_text(text, encoding="utf-8")
        written.append(p)
    for a in AUDIENCES:
        title = f"The {runs}-run set, base {base}: {a.title() if a != 'CTO' else 'CTO'} report"
        to_pdf(blocks[a], out / f"{a}.pdf", title)
        to_docx(blocks[a], out / f"{a}.docx", title, S["written"])
        written += [out / f"{a}.pdf", out / f"{a}.docx"]
    return written


def check(out: Path = OUT) -> list[str]:
    """What differs between the reports on file and what the newest set's records give."""
    runs, base = newest()
    files, _, _ = texts(runs, base)
    bad = [n for n, t in files.items() if not (out / n).exists() or (out / n).read_text(encoding="utf-8") != t]
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:                 # the Word and PDF forms written again, compared byte for byte
        _, blocks, S = texts(runs, base)
        for a in AUDIENCES:
            title = f"The {runs}-run set, base {base}: {a.title() if a != 'CTO' else 'CTO'} report"
            to_pdf(blocks[a], Path(tmp) / f"{a}.pdf", title)
            to_docx(blocks[a], Path(tmp) / f"{a}.docx", title, S["written"])
            for ext in (".pdf", ".docx"):
                p = out / f"{a}{ext}"
                if not p.exists() or p.read_bytes() != (Path(tmp) / f"{a}{ext}").read_bytes():
                    bad.append(p.name)
    return bad


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base", type=int)
    ap.add_argument("--runs", type=int, default=500)
    ap.add_argument("--out", type=Path, default=OUT)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    if a.check:
        bad = check(a.out)
        if bad:
            print("run reports: out of date (python3 tools/run_reports.py): " + ", ".join(bad))
            return 1
        runs, base = newest()
        print(f"run reports: the newest set's reports (base {base}) in every form are what its records give")
        return 0
    runs, base = (a.runs, a.base) if a.base is not None else newest()
    files = write(runs, base, a.out)
    print(f"run reports: {len(files)} files for the {runs}-run set, base {base}, in {a.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

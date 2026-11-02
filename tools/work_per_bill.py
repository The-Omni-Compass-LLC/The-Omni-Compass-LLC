# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Work for the bill: the one number the receipts must prove (the founder's words of 2 November 2026: "how much work is being
done in the bill and native, and how much is being done with OmniCompass on it ... that is only the only thing we need to in
the end prove, is that we get more work for the bill ... formalize this equation to add up to explain its whole total benefit
and how it is and where it does and lives").

The equation, one line per place and one for the two together, every term read from a receipt the repository holds
(results/TWO_BILLS.json, written by tools/two_bills.py from each place's own table); nothing here is a new measurement:

    Y(p, a)   = W(p, a) / B(p, a)                       the work done for each dollar of the bill, place p, arm a
    G(p)      = Y(p, omni) / Y(p, native) − 1           the benefit in place p: more work for the bill when G(p) > 0
              = (1 + w(p)) / (1 + b(p)) − 1             w = the change in the work done, b = the change in the bill
              ≈ w(p) − b(p)                             for small changes (exactly: ln(1 + G) = ln(1 + w) − ln(1 + b))
    G(total)  = Σₚ Bₙ(p)(1 + w(p)) / Σₚ Bₙ(p)(1 + b(p)) − 1
                                                        for an owner who runs work in both places: each place's work valued
                                                        at what native's own receipt charged for it, so the places add in
                                                        dollars (a system that runs in one place reads that place's G alone)

    W  the work done inside the line, as the place's own receipt counts it (requests served)
    B  the bill: on bare metal the rental of the card for the arm's window (hours × the hourly price); through the cloud the
       cloud's own bill at list price (machine-hours × the price); B = Σₖ cₖ over the bill's components, b = Σₖ sₖ·bₖ with
       sₖ each component's share of native's bill

Each run is read on its own (G of run 1, 2 and 3, each with its own word) and the three together by the one key
(tools/readings.py: the mean of the runs' changes from 0.5% up reads GAIN or LOSS; runs that move 0.5% or more in opposite
directions read "the runs disagree"). A place whose receipt counts no work, or that is not yet run, has no G and says so;
G(total) is read only when every place has its G. Omni-Compass acts at the software end alone (where the benefit is made);
the bill is read where it is paid (the chip's rental and meter, the cloud's own bill).

    python3 tools/work_per_bill.py           write results/WORK_PER_BILL.json and docs/WORK_PER_BILL.md
    python3 tools/work_per_bill.py --check   exit 1 when they are not what the receipts give
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.legal import stamp  # noqa: E402
from tools.readings import HIGHER, OWN_RUNS, three_run_reading  # noqa: E402

SRC = ROOT / "results" / "TWO_BILLS.json"
OUT_JSON = ROOT / "results" / "WORK_PER_BILL.json"
OUT_MD = ROOT / "docs" / "WORK_PER_BILL.md"


def _pct(x: float) -> str:
    t = f"{x * 100:+.2f}%"
    return "±0.00%" if t in ("+0.00%", "-0.00%") else t.replace("-", "−")


def run_g(native: dict, omni: dict) -> dict:
    """One run: w, b, G by the identity, and G read straight off the receipt's work per dollar, which must agree."""
    w = omni["work"] / native["work"] - 1
    b = omni["bill"] / native["bill"] - 1
    g = (1 + w) / (1 + b) - 1
    g_receipt = (omni["work"] / omni["bill"]) / (native["work"] / native["bill"]) - 1
    if abs(g - g_receipt) > 1e-12:
        raise SystemExit(f"the identity G = (1 + w)/(1 + b) − 1 fails on a receipt: {g} against {g_receipt}")
    return {"w": w, "b": b, "G": g, "approx_w_minus_b": w - b, "log_check": math.log1p(g) - (math.log1p(w) - math.log1p(b)),
            "Y_native": native["work"] / native["bill"], "Y_omni": omni["work"] / omni["bill"],
            "W": [native["work"], omni["work"]], "B": [native["bill"], omni["bill"]]}


def places() -> dict:
    tb = json.loads(SRC.read_text(encoding="utf-8"))
    out = {}
    chip = tb.get("chip") or {}
    runs = []
    for i, pr in enumerate(chip.get("per_run") or [], 1):
        g = run_g(pr["native"], pr["omni"])
        runs.append({"run": i, "id": (chip.get("runs") or [None] * 9)[i - 1], **g})
    if runs:
        rd = three_run_reading([{"native": r["Y_native"], "omni": r["Y_omni"], "diff": r["Y_omni"] - r["Y_native"], "significant": True}
                                for r in runs], HIGHER)
        out["bare_metal"] = {"label": "Bare metal: the chip's own bill (the card's rental) and the work it served", "engine": chip.get("engine"),
                             "title": chip.get("title"), "source": "results/TWO_BILLS.json chip (results/gpu/V23_A10_CAP_FULL_ABC.json)",
                             "runs": runs, "mean_G": sum(r["G"] for r in runs) / len(runs), "reading": (rd if isinstance(rd, str) else rd[0] if isinstance(rd, (list, tuple)) else str(rd)).replace("**", ""),
                             "status": "read"}
    cl = tb.get("cloud") or {}
    if cl:
        bn, bo = (cl.get("bill") or {}).get("native"), (cl.get("bill") or {}).get("omni")
        has_work = bool(cl.get("work_key")) and bool(cl.get("work"))
        out["cloud"] = {"label": "Through the cloud: the cloud's own bill and the work answered inside the line", "engine": cl.get("engine"),
                        "source": f"results/TWO_BILLS.json cloud ({cl.get('page')})",
                        "b": (bo / bn - 1) if bn and bo else None, "bill": [bn, bo], "repetitions": cl.get("repetitions"),
                        "w": None, "G": None,
                        "status": "read" if has_work else "work not counted",
                        "note": ("the set counted the bill and the machine-hours but not the work done (its load sent a fixed rate of "
                                 "requests, so its work could not grow); the work per dollar waits for the sets at the max with the work "
                                 "meter (scripts/azure_queue.txt), on the engine that stands")}
    for o in tb.get("organisms") or []:
        key = "organisms_" + ("chip" if o.get("where") == "chip" else "cloud") + "_" + (o.get("table") or o.get("label") or "x").split("/")[-1].split(".")[0]
        out[key] = {"label": o.get("label"), "status": o.get("status"), "runs": o.get("runs"), "table": o.get("table"), "G": None}
    return out


def total(pl: dict) -> dict:
    """G(total), the two places in dollars: read only when both places have their G."""
    bm, cl = pl.get("bare_metal"), pl.get("cloud")
    if not bm or not cl or cl.get("G") is None:
        return {"G": None, "status": "not yet read: the cloud's receipt has no work counted yet, so its G(cloud) is not read"}
    rows = []
    for r in bm["runs"]:
        num = r["B"][0] * (1 + r["w"]) + cl["bill"][0] * (1 + cl["w"])
        den = r["B"][0] * (1 + r["b"]) + cl["bill"][0] * (1 + cl["b"])
        rows.append(num / den - 1)
    return {"G": sum(rows) / len(rows), "runs": rows, "status": "read"}


def build() -> dict:
    pl = places()
    return {"equation": {"Y": "Y(p, a) = W(p, a) / B(p, a)", "G": "G(p) = Y(p, omni) / Y(p, native) − 1 = (1 + w(p)) / (1 + b(p)) − 1 ≈ w(p) − b(p)",
                         "total": "G(total) = Σₚ Bₙ(p)(1 + w(p)) / Σₚ Bₙ(p)(1 + b(p)) − 1",
                         "bill": "B = Σₖ cₖ, b = Σₖ sₖ·bₖ, sₖ = cₖ(native) / B(native)"},
            "places": pl, "total": total(pl), "source": "results/TWO_BILLS.json (tools/two_bills.py)"}


def markdown(d: dict) -> str:
    pl, eq = d["places"], d["equation"]
    L = ["# Work for the Bill: the One Number the Receipts Prove", "",
         "What the receipts of the chip and of the clouds must show is how much work is done for the bill, native against "
         "Omni-Compass on native (the founder's words of 2 November). This page writes it as one equation, reads every term from a "
         "receipt the repository holds, and says where the benefit lives and where it is counted. Nothing here is a new measurement.", "",
         "## The equation", "",
         "    Y(p, a)  = W(p, a) / B(p, a)                       work done for each dollar of the bill, in place p, arm a",
         "    G(p)     = Y(p, omni) / Y(p, native) − 1           the benefit in place p: more work for the bill when G(p) > 0",
         "             = (1 + w(p)) / (1 + b(p)) − 1             w: the change in the work done; b: the change in the bill",
         "             ≈ w(p) − b(p)                             for small changes; exactly ln(1 + G) = ln(1 + w) − ln(1 + b)",
         "    G(total) = Σₚ Bₙ(p)·(1 + w(p)) / Σₚ Bₙ(p)·(1 + b(p)) − 1",
         "                                                       for an owner who runs work in both places, each place's work",
         "                                                       valued at what native's own receipt charged for it, so the places",
         "                                                       add in dollars; a system in one place reads that place's G alone",
         "    B        = Σₖ cₖ,   b = Σₖ sₖ·bₖ,   sₖ = cₖ(native) / B(native)   the bill as the sum of its components", "",
         "W is the work done inside the line, as the place's own receipt counts it (requests served). B is the bill: on bare metal "
         "the card's rental for the arm's window (hours × the hourly price, so the same window bills the same: b ≈ 0 and G ≈ w); "
         "through the cloud the cloud's own bill at list price (machine-hours × the price: a bill that rises is power given, and "
         "G > 0 exactly when the work rises more than the bill, w > b).", "",
         "## Where the benefit lives and where it is counted", "",
         "| | Bare metal (arms A and B) | Through the cloud (arms C and D) |", "|---|---|---|",
         "| Where Omni-Compass acts | the software end: the service on the card (its power cap, its queue) | the software end: the "
         "cluster's pods, their room and the cloud's own autoscaler under it |",
         "| Where the benefit is made | the work the card serves inside the line, faster | the work answered inside the line, on the "
         "machines the cloud bills |",
         "| The bill B | the card's rental for the window (the same hours in both arms) | the cloud's own bill at list price |",
         "| The work W | requests served (the card's own receipt) | requests answered inside the line (the work meter) |",
         "| The second receipt | the card's own meter: energy for each request served | the machine-hours beside the bill |", "",
         "## What the receipts say today", ""]
    bm = pl.get("bare_metal")
    if bm:
        L += [f"**Bare metal** ({bm['title']}; {bm['engine']}; `{bm['source']}`):", "",
              "| Run | Work, native → Omni-Compass | w | Bill, native → Omni-Compass | b | Work per dollar, native → Omni-Compass | G (its own word) |",
              "|---|---|---:|---|---:|---|---|"]
        for r in bm["runs"]:
            word = "GAIN" if r["G"] >= 0.005 else "LOSS" if r["G"] <= -0.005 else "STEADY, under the floor"
            L.append(f"| run {r['run']} | {r['W'][0]:,.1f} → {r['W'][1]:,.1f} requests | {_pct(r['w'])} | ${r['B'][0]:.4f} → ${r['B'][1]:.4f} | "
                     f"{_pct(r['b'])} | {r['Y_native']:,.0f} → {r['Y_omni']:,.0f} | {_pct(r['G'])} {word} |")
        L += ["", f"The three runs together, by the one key: **{bm['reading']}** (the mean of the three G {_pct(bm['mean_G'])}). Each run's G "
              "is read two ways that agree to the last digit: from the receipt's own work per dollar, and from (1 + w)/(1 + b) − 1.", ""]
    cl = pl.get("cloud")
    if cl:
        L += [f"**Through the cloud** ({cl['engine']}, {cl['repetitions']} paired repetitions; `{cl['source']}`): the bill "
              f"${cl['bill'][0]:.4f} → ${cl['bill'][1]:.4f} a window, b {_pct(cl['b'])}, inside the noise; the work done "
              f"was not counted, so G(cloud) is not read: {cl['note']}.", ""]
    rest = [v for k, v in pl.items() if k.startswith("organisms_")]
    if rest:
        L += ["**Not yet read** (their receipts will carry W and B, and G is read the same way):", ""]
        for v in rest:
            L.append(f"- {v['label']}: {v['status']}" + (f" ({v['runs']})" if v.get("runs") else ""))
        L.append("")
    t = d["total"]
    L += ["**Both places, for an owner who runs work in both**, G(total): " + (f"{_pct(t['G'])}" if t["G"] is not None else t["status"]) + ".", "",
          "## Is it proven", "",
          "Not yet, said plainly. On bare metal two runs of three gave more work for the bill and the third gave less, so the "
          "three runs disagree; the card's energy for each request served fell in all three (GAIN in all three of our runs). Through "
          "the cloud the work was not counted in the one set read so far. The sets that will decide it are running or queued on the "
          "engine that stands, and each lands here by itself when its table does (`python3 tools/two_bills.py`, then this page).", "",
          OWN_RUNS]
    return "\n".join(stamp(L)) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    d = build()
    js = json.dumps(d, indent=1, ensure_ascii=False) + "\n"
    md = markdown(d)
    if a.check:
        bad = [p.relative_to(ROOT).as_posix() for p, s in ((OUT_JSON, js), (OUT_MD, md)) if not p.exists() or p.read_text(encoding="utf-8") != s]
        print("work for the bill: " + ("in line with the receipts" if not bad else ", ".join(bad) + " differ (python3 tools/work_per_bill.py)"))
        return 1 if bad else 0
    OUT_JSON.write_text(js, encoding="utf-8")
    OUT_MD.write_text(md, encoding="utf-8")
    print(f"{OUT_MD.relative_to(ROOT)}, {OUT_JSON.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

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

    E(p, a)   = W(p, a) / B(p, a)                       the work done for each dollar of the bill, place p, arm a
    G(p)      = E(p, omni) / E(p, native) − 1           the benefit in place p: more work for the bill when G(p) > 0
              = (1 + w(p)) / (1 + b(p)) − 1             w = the change in the work done, b = the change in the bill
              ≈ w(p) − b(p)                             for small changes (exactly: ln(1 + G) = ln(1 + w) − ln(1 + b))
    G(total)  = Σₚ S(p)(1 + w(p)) / Σₚ S(p)(1 + b(p)) − 1
                                                        for an owner who runs work in both places, S(p) the owner's own native
                                                        spend in place p over one period (never the benchmark windows, whose
                                                        lengths are arbitrary); a system that runs in one place reads that
                                                        place's G alone

    W  the work done, as each place's own receipt counts it: on the chip the requests served within the arm's fixed window (the
       card's receipt counts no response line); through the cloud the requests answered inside the response line (the work meter)
    B  the bill: on bare metal the card's metered window at the launch price (seconds × $1.29 an hour, tools/two_bills.py, not a
       billing statement); through the cloud the cloud's own bill at list price (machine-hours × the price); B = Σₖ cₖ over the
       bill's components, b = Σₖ sₖ·bₖ with sₖ each component's share of native's bill

Each run is read on its own (G of run 1, 2 and 3, each with its own word) and the three together by the one key
(tools/readings.py: the mean of the runs' changes from 0.5% up reads GAIN or LOSS; runs that move 0.5% or more in opposite
directions read "the runs disagree"). A place whose receipt counts no work, or that is not yet run, has no G and says so;
G(total) is read only for an owner's stated spend and only when every place's G is read on the engine that stands. The bill is
read where it is paid (the chip's rental and meter, the cloud's own bill); what Omni-Compass wrote in each receipt's run is named
beside it (on the A10 the card's own power limit and clock ceiling under the operator's cap; in the cloud set read so far the
machines alone, at the tune-down).

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
    """One run: w, b and G = (1 + w)/(1 + b) − 1 (the ratio of the two arms' work per dollar, the same arithmetic, checked)."""
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
        # no interval is carried for a run's work per dollar, so no run is counted beyond the noise (the key then reads by the mean)
        rd = three_run_reading([{"native": r["Y_native"], "omni": r["Y_omni"], "diff": r["Y_omni"] - r["Y_native"]} for r in runs], HIGHER)
        out["bare_metal"] = {"label": "Bare metal: the chip's own bill (the card's rental) and the work it served", "engine": chip.get("engine"),
                             "title": chip.get("title"), "source": "results/TWO_BILLS.json chip (results/gpu/V23_A10_CAP_FULL_ABC.json)",
                             "runs": runs, "mean_G": sum(r["G"] for r in runs) / len(runs), "reading": (rd if isinstance(rd, str) else rd[0] if isinstance(rd, (list, tuple)) else str(rd)).replace("**", ""),
                             "status": "read"}
    cl = tb.get("cloud") or {}
    if cl:
        bn, bo = (cl.get("bill") or {}).get("native"), (cl.get("bill") or {}).get("omni")
        has_work = bool(cl.get("work_key")) and bool(cl.get("work"))
        out["cloud"] = {"label": "Through the cloud: the cloud's own bill and the work answered inside the line", "engine": cl.get("engine"),
                        "conditions": cl.get("conditions") or ("Omni-Compass on top of native at the tune-down (dial save) on the machines alone "
                                                               "(OMNI_MACHINES_ONLY=1), the rule of 14 October struck on 31 October"),
                        "source": f"results/TWO_BILLS.json cloud ({cl.get('page')})",
                        "b": (bo / bn - 1) if bn and bo else None, "bill": [bn, bo], "repetitions": cl.get("repetitions"),
                        "w": None, "G": None,
                        "status": "read" if has_work else "work not counted",
                        "note": ("the set counted the bill and the machine-hours but not the work done (its load sent a fixed rate of "
                                 "requests, so its work could not grow); the work per dollar waits for the sets at the max with the work "
                                 "meter (scripts/azure_queue.txt), on the engine that stands")}
    for o in tb.get("organisms") or []:
        key = "organisms_" + ("chip" if o.get("where") == "chip" else "cloud") + "_" + (o.get("table") or o.get("label") or "x").split("/")[-1].split(".")[0]
        out[key] = {"label": o.get("label"), "status": o.get("status"), "runs": o.get("runs"), "table": o.get("table"), "G": None,
                    "reader": "tools/two_bills.py reads its card rows (requests served, energy) as the A10's" if o.get("where") == "chip"
                              else "no reader yet writes its W and B: tools/two_bills.py reads card rows only"}
    return out


LADDER = ROOT / "results" / "model_gate" / "V23_LADDER_CORRECTED.json"
LADDER_PAGE = "results/model_gate/V23_LADDER_CORRECTED.md"


def ladder_cloud() -> dict | None:
    """The machine-hours our own model reads against native at every beat in the cloud's setting at the max (class S, the work
    fixed by the model's own load), from the corrected ladder's record; None when the record is absent."""
    try:
        d = json.loads(LADDER.read_text())
        rel = {int(b): r["machine_hours"]["vs_native"]["relative"] for b, r in d["models"]["pace_cloud"]["rows"].items()}
    except (OSError, KeyError, ValueError, TypeError):
        return None
    main = int(d.get("main_s") or 60)
    return {"lo": min(rel.values()), "hi": max(rel.values()), "main": rel.get(main), "main_s": main}


def ladder_words() -> str:
    lc = ladder_cloud()
    if not lc:
        return "our own model of the cloud at the max is not read here (its record is absent)"
    at = f", {100 * lc['main']:.0f}% at the main engine's {lc['main_s']} s" if lc.get("main") is not None else ""
    return (f"our own model at the max reads the machine-hours up {100 * lc['lo']:.0f}% to {100 * lc['hi']:.0f}% across the beats"
            f"{at}, with the work fixed by the model's own load (`{LADDER_PAGE}`, class S)")


def aim(db: float = 0.01, dw: float = 0.12, spend: float = 100.0) -> dict:
    """The founder's aim of 31 October put through the equation on an example spend ($ M a year): the bill up db, the work up dw.
    Every dollar figure is at native's price per unit of work, p0 = native's bill / native's work."""
    g = (1 + dw) / (1 + db) - 1
    return {"G": g, "work_x": 1 + dw, "bill": spend * (1 + db), "work_value": spend * (1 + dw), "more_work": spend * dw, "more_bill": spend * db,
            "per_spend": spend * g, "native_work_cost": spend / (1 + g)}


def owner_bill(items: dict, moved: dict) -> dict:
    """An owner's own bill read through the equation: items {line: dollars a period, native}, moved {line: change in that line's
    quantity with Omni-Compass on native, as a fraction}. Returns B native, B with Omni-Compass, b and each line's share."""
    bn = sum(items.values())
    bo = sum(c * (1 + moved.get(k, 0.0)) for k, c in items.items())
    return {"B_native": bn, "B_omni": bo, "b": bo / bn - 1, "shares": {k: c / bn for k, c in items.items()}}


def total_for(spend: dict, wb: dict) -> float:
    """G(total) for an owner's own native spend S(p) in each place over one period: Σ S(p)(1 + w(p)) / Σ S(p)(1 + b(p)) − 1.
    It equals the change in total work per dollar with each place's work valued at native's own price per unit of work there,
    and it always lies between the places' own G (it is their mean weighted by Omni-Compass's spend)."""
    num = sum(spend[p] * (1 + wb[p][0]) for p in spend)
    den = sum(spend[p] * (1 + wb[p][1]) for p in spend)
    return num / den - 1


def total(pl: dict) -> dict:
    """G(total) is never read from the benchmark receipts (their windows' lengths are arbitrary): it is read for an owner's own
    spend in each place (total_for), once every place's G is read on the engine that stands."""
    cl = pl.get("cloud") or {}
    why = ("read only for an owner's stated native spend in each place, never from the benchmark windows; and only once every "
           "place's G is read on the engine that stands (the cloud's work is not yet counted)")
    return {"G": None, "status": why if cl.get("G") is None else "read only for an owner's stated native spend in each place"}


def build() -> dict:
    pl = places()
    return {"equation": {"E": "E(p, a) = W(p, a) / B(p, a)", "G": "G(p) = E(p, omni) / E(p, native) − 1 = (1 + w(p)) / (1 + b(p)) − 1 ≈ w(p) − b(p)",
                         "total": "G(total) = Σₚ S(p)(1 + w(p)) / Σₚ S(p)(1 + b(p)) − 1, S(p) the owner's native spend in place p",
                         "bill": "B = Σₖ cₖ, b = Σₖ sₖ·bₖ, sₖ = cₖ(native) / B(native)"},
            "places": pl, "total": total(pl), "source": "results/TWO_BILLS.json (tools/two_bills.py)"}


def markdown(d: dict) -> str:
    pl, eq = d["places"], d["equation"]
    bm0, cl0 = pl.get("bare_metal") or {}, pl.get("cloud") or {}
    chip_w = ", ".join(_pct(r["w"]) for r in bm0.get("runs", [])) or "not yet read"
    chip_usd = ", ".join(("$" if r["w"] >= 0 else "−$") + f"{abs(500 * r['w']):.2f}" for r in bm0.get("runs", [])) or "not yet read"
    cloud_b = _pct(cl0["b"]) if cl0.get("b") is not None else "not read"
    chip_100m = ", ".join(("+$" if r["w"] >= 0 else "−$") + f"{abs(100 * r['w']):.2f} M" for r in bm0.get("runs", [])) or "not yet read"
    on_items = {"compute": 720 * 4.50, "egress": 500 * 0.08, "storage": 30.0}
    we_items = {"compute": 40 * 4.50, "egress": 50 * 0.08, "storage": 30.0}
    on, we = owner_bill(on_items, {}), owner_bill(we_items, {})
    a = aim()
    L = ["# Work for the Bill: the One Number the Receipts Prove", "",
         "What the receipts of the chip and of the clouds must show is how much work is done for the bill, native against "
         "Omni-Compass on native (the founder's words of 2 November). This page writes it as one equation, reads every term from a "
         "receipt the repository holds, and says where the benefit lives and where it is counted. Nothing here is a new measurement.", "",
         "## The equation", "",
         "    E(p, a)  = W(p, a) / B(p, a)                       work done for each dollar of the bill, in place p, arm a",
         "    G(p)     = E(p, omni) / E(p, native) − 1           the benefit in place p: more work for the bill when G(p) > 0",
         "             = (1 + w(p)) / (1 + b(p)) − 1             w = ΔW(p): the change in the work done; b = ΔB(p): in the bill",
         "             ≈ w(p) − b(p)                             for small changes; exactly ln(1 + G) = ln(1 + w) − ln(1 + b)",
         "    G(total) = Σₚ S(p)·(1 + w(p)) / Σₚ S(p)·(1 + b(p)) − 1",
         "                                                       for an owner who runs work in both places: S(p) the owner's own",
         "                                                       native spend in place p over one period, never the benchmark",
         "                                                       windows; a system in one place reads that place's G alone",
         "    B        = Σₖ cₖ,   b = Σₖ sₖ·bₖ,   sₖ = cₖ(native) / B(native)   the bill as the sum of its components", "",
         "The letters are those of `results/TWO_BILLS.md` (\"The one equation\"), with w and b short for ΔW and ΔB. " + "W is the work done as each place's own receipt counts it: on the chip the requests served within the arm's fixed window "
         "(the card's receipt counts no response line); through the cloud the requests answered inside the response line (the work "
         "meter). B is the bill: on bare metal the card's metered window at Lambda's launch price, $1.29 an hour (seconds × the price, "
         "computed by `tools/two_bills.py`, not a billing statement; the same window bills nearly the same, so b ≈ 0 and G ≈ w); through "
         "the cloud the cloud's own bill at list price (machine-hours × the price). A bill that rises is power given; there is more "
         "work for the bill when the work rises more than the bill (w > b, G > 0). G(total) is the places' own G weighted by the "
         "owner's spend, so it always lies between them.", "",
         "**Why the places' prices do not move G.** A cloud usually bills far more than bare metal for the same work on the same "
         "silicon (its margin, the software it wraps around the machine, egress and storage fees, paying only for the hours used). "
         "Inside one place both arms pay the same prices, so the price level cancels in G(p): with the bill B = Σₖ πₖ·qₖ (prices πₖ, "
         "quantities qₖ), b = Σₖ sₖ·(qₖ(omni)/qₖ(native) − 1) depends on the quantities alone. A component Omni-Compass does not move "
         "(egress, storage, a managed service's fee) has bₖ = 0 and only dilutes b toward 0; the cloud receipt read so far prices the "
         "machine-hours alone, at list price, so its b is the compute bill's. The places' price levels enter only G(total), through "
         "the owner's spend S(p), and the owner's choice of place, which Omni-Compass does not make.", "",
         "## Where the benefit lives and where it is counted", "",
         "| | Bare metal (arms A and B) | Through the cloud (arms C and D) |", "|---|---|---|",
         "| What Omni-Compass writes in the receipts read so far | the card's own power limit and clock ceiling, under the operator's "
         "cap, through the card's published interface (the service's queue is its signal, not a knob it writes) | the machines alone, at "
         "the tune-down (the omni-v18 set); the sets at the max add the cluster's pods and their room, with the cloud's own autoscaler "
         "under them |",
         "| Where the benefit shows | the requests the card completes in the same metered window | the requests answered inside the "
         "line, on the machines the cloud bills |",
         "| The bill B | the card's rental for the window (the same hours in both arms) | the cloud's own bill at list price |",
         "| The work W | requests served in the window (the card's own receipt; no response line) | requests answered inside the line (the work meter) |",
         "| The second receipt | the card's own meter: energy for each request served | the machine-hours beside the bill |", "",
         "**What a place sets and what Omni-Compass moves.** Write the work as W = C·(1 − Vₒ)·U·t: C the chip's raw capacity, Vₒ the "
         "share a place's own software layer takes (0 on bare metal; a hypervisor's and an orchestrator's share in a cloud), U how much "
         "of what is left becomes served work, t the time. Write the cloud's bill as B = R·H + E·Rₑ + S·Rₛ + I (the hourly rate × the "
         "hours on, egress × its rate, storage × its rate, the metered extras) and bare metal's as B = M + L (the lease and the "
         "owner's own staff). Inside one place C, Vₒ, t and every rate are the same in both arms, so they cancel: w = U(omni)/U(native) − 1, "
         "and b moves only through the quantities Omni-Compass changes, the hours H in a cloud (E only as the work grows) and nothing of "
         "M + L on bare metal (so b = 0 there and G = w). The place sets C, Vₒ and the prices; Omni-Compass moves U and, in a cloud, H. "
         "Which place costs less for the same work (a cloud for a few hours a month, bare metal for a box busy all day) is the owner's "
         "choice of place, not a benefit of Omni-Compass.", "",
         "**How Omni-Compass can lower a cloud's bill, and what it does not do.** A cloud bills every hour a machine is on, busy or "
         "idle. Omni-Compass's levers there are the ones the Kubernetes API already accepts (the Operator's Manual, 14.5): it closes to "
         "new work and parks machines the cloud's own autoscaler made but the work does not need, so the autoscaler can remove them "
         "and the idle hours stop being billed (b falls); it moves the autoscalers' targets so pods are ready ahead of the load, and it "
         "gives a pod the processor its machine can spare, so less work waits and more is answered inside the line (w rises). It holds "
         "no cloud credential and asks the cloud for no machine. It does not reorder data in memory, fill a chip's cache, change a "
         "network or make silicon faster; and no cut of a cloud's hours has been measured yet (the one set read so far moved its "
         "machine-hours up 1.21%, inside the noise).", "",
         "## The bill, line by line", "",
         "The bill is the sum of its line items, B = Σₖ cₖ, and each item's change counts by its share of native's bill, b = Σₖ sₖ·bₖ. "
         "Which items Omni-Compass can move, and which the receipts read so far have priced:", "",
         "| Line item | Through the cloud: how it is billed | Moved by Omni-Compass? | Bare metal: how it is billed | Moved by Omni-Compass? |",
         "|---|---|---|---|---|",
         "| The server (compute) | by the second: machine-hours × the hourly price | yes: the machines it parks and wakes, the pods it "
         "places (priced in the cloud receipt read so far, at list price) | a flat lease or a rental by the hour for the same box | no: the "
         "same box in both arms, so this item holds and G ≈ w (priced in the chip receipt: the metered window at $1.29 an hour) |",
         "| Electricity | inside the price | no line of its own | paid by the owner where the box sits on its own meter | yes: the card's "
         "own meter reads the energy for each request served (GAIN in all three A10 runs); not priced in the receipt, a line an owner adds "
         "at its own rate |",
         "| Data out (egress) | per gigabyte that leaves the cloud | only through the work: more requests served can send more data out, "
         "a rise proportional to the work (not priced in the receipt read so far) | an allowance or a flat port | no, inside the allowance |",
         "| Storage and its speed | per gigabyte stored, plus the speed tier bought | no (not priced) | inside the box | no |",
         "| The hidden labour | inside the cloud's premium | no | the owner's staff | no |", "",
         "So the receipts read so far price the item Omni-Compass moves most in each place (the cloud's machine-hours; the chip's window), "
         "and leave out items it does not move. An item it does not move has bₖ = 0 and only pulls b toward 0, so an owner's full bill "
         "shows a smaller b than the compute line alone; an item that grows with the work (egress) takes back a share of w in the cloud, "
         "and an owner's own electricity rate gives bare metal a second line where the card's energy cut is paid back.", "",
         "## Reading your own bill: a worked example", "",
         "The prices below are an owner's example (a three-node cluster, the founder's illustration of 2 November), not a result; "
         "the changes put through them are only what the receipts measured. Each place is read on its own.", "",
         "| Example | Its bill, line by line (native) | What Omni-Compass can move | Read through the equation |",
         "|---|---|---|---|",
         "| Bare metal, always on | the lease $500 a month (egress and storage inside the box) | none of the bill: the same boxes in "
         "both arms, b = 0 | G = w, the work the same boxes serve: on the A10's receipts w was " + chip_w + "; at native's price per "
         "unit of work that is " + chip_usd + " of work a month out of the same $500, and the three runs disagree |",
         f"| Through the cloud, always on | compute 720 h × $4.50 = ${on_items['compute']:,.0f}, egress 500 GB × $0.08 = "
         f"${on_items['egress']:,.0f}, storage ${on_items['storage']:,.0f}: ${on['B_native']:,.0f} | the hours (the machines it parks "
         f"and wakes), {100 * on['shares']['compute']:.1f}% of this bill; egress only as the work grows; storage not at all | b ≈ "
         f"{on['shares']['compute']:.3f} × the change in machine-hours; the one cloud set read so far moved its machine-hours " + cloud_b +
         " (inside the noise, at the tune-down on the machines alone) and did not count its work, so G is not read |",
         f"| Through the cloud, weekends only (40 h) | compute 40 h × $4.50 = ${we_items['compute']:,.0f}, egress 50 GB × $0.08 = "
         f"${we_items['egress']:,.0f}, storage ${we_items['storage']:,.0f}: ${we['B_native']:,.0f} | the hours, "
         f"{100 * we['shares']['compute']:.1f}% of this bill | the same reading: b ≈ {we['shares']['compute']:.3f} × the change in "
         "machine-hours |", "",
         "Which place is cheaper for the same work (the weekend cluster in a cloud, the always-on one on bare metal) is the owner's "
         "choice of place, and a cloud's hypervisor share is the same in both arms: neither is a benefit of Omni-Compass. What "
         "Omni-Compass changes is the work the same machines serve and, in a cloud, the hours billed (`owner_bill` in "
         "`tools/work_per_bill.py` reads any owner's line items the same way).", "",
         "## A $100 million budget, read by the equation", "",
         "The $100 M is an example, the founder's of 2 November: a company whose IT infrastructure costs 2.9% of its revenue (the "
         "example's own figure, of the order public surveys of IT spending report for large firms, about 3% of revenue), so the "
         "budget stands for a revenue of about $3.45 B ($100 M / 0.029). The 2.9% is the size of the budget against the revenue; it "
         "is not a cost Omni-Compass removes.", "",
         "An owner's budget is read the same way, place by place, from the receipts and nothing else. Split the owner's native spend "
         "into the places it runs in, S(cloud) + S(bare metal) = $100 M, and read each place's G from its own receipt; G(total) is "
         "their spend-weighted mean and lies between them. The scale is plain arithmetic: each point of G on a $100 M spend is $1 M "
         "of work at native's price per unit of work, about 0.029% of the example's revenue. What can be written today:", "",
         "| Place | Its bill with Omni-Compass | The work with Omni-Compass | What the receipts let an owner write today |",
         "|---|---|---|---|",
         "| Bare metal (a lease of $100 M) | the same $100 M: the same boxes in both arms, b = 0 | w, the work the same boxes serve | "
         "the A10 receipt's own ratios applied to the spend (arithmetic, not a measurement of a fleet): " + chip_100m + " of work at "
         "native's price per unit of work, out of the same $100 M; the three runs disagree, so no figure is claimed |",
         "| Through the cloud ($100 M a year) | b, read from the cloud's own bill: only the hours Omni-Compass parks or adds move it | w, "
         "the work answered inside the line (the work meter) | the one set read so far moved the compute bill " + cloud_b + " (inside "
         "the noise) and did not count its work; " + ladder_words() + ": the cloud's bill may rise where the work rises more, so a "
         "smaller cloud bill is not what the record points to |", "",
         "**The arithmetic at the founder's aim, an example and not a result.** The founder's words of 31 October state the aim the "
         "cloud is judged by: \"We're pushing 1% more bill, but we're getting ~12% more work.\" Put through the equation on the example's "
         f"$100 M a year in a cloud: ΔB = +1%, ΔW = +12%, G = 1.12 / 1.01 − 1 = +{100 * a['G']:.1f}%, the work for each dollar up "
         f"{100 * a['G']:.1f}%. In dollars, each at native's price per unit of work (native's $100 M bill for native's year of work): "
         f"the bill is ${a['bill']:.0f} M and the work {a['work_x']:.2f} times native's, worth ${a['work_value']:.0f} M, so "
         f"${a['more_work']:.0f} M more work for ${a['more_bill']:.0f} M more bill; at that work for each dollar, $100 M of bill buys "
         f"${a['per_spend']:.1f} M more work than native's $100 M did; read the other way, native's year of work costs $100 M / "
         f"{1 + a['G']:.3f} = ${a['native_work_cost']:.1f} M. On bare metal the bill holds (ΔB = 0), so G = ΔW: each 1% more work "
         "from the same boxes is "
         "$1 M of work a year on the example's $100 M. These are the equation's arithmetic on an aim; the receipts above are what has "
         "been measured, and a page that shows the example says so beside it.", "",
         "**What no budget may show.** Three limits come from the engine and from physics, not from the receipts:", "",
         "- No line item called a \"stack tax\" falls to zero. The share a place's own software layer takes (Vₒ above: a "
         "hypervisor's, an orchestrator's) is the same in both arms, because Omni-Compass sits on top of that layer and removes "
         "nothing; it cancels in G and is never a saving.",
         "- No machine runs at 100% of its silicon. Every muscle is driven to its own limit and never past it, and the compass law "
         "keeps a 5% cushion at each line; and in any queue the waiting grows without bound as the busy share nears one (for one "
         "server, the mean time in the system is 1/(μ − λ), which diverges as the arrival rate λ nears the service rate μ). A "
         "budget that turns 75% of a fleet's capacity into 100% of it contradicts the engine's own rule.",
         "- Idle hours are not \"eliminated\". Omni-Compass parks machines the cloud's own autoscaler made and the work does not need, "
         "so that autoscaler can remove them; it keeps the cushion the response line needs, and it wakes a machine before the line "
         "is crossed. How many hours that removes is what the cloud sets are measuring.", "",
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
        L += ["", f"The three runs together, by the one key: **{bm['reading']}** (the mean of the three G {_pct(bm['mean_G'])}). No interval "
              "is carried for a run's work per dollar, so no run is counted beyond the noise; each run's word is its own size against the "
              "0.5% floor.", ""]
    cl = pl.get("cloud")
    if cl:
        L += [f"**Through the cloud** ({cl['engine']}, {cl['repetitions']} paired repetitions, {cl['conditions']}; `{cl['source']}`): the bill "
              f"${cl['bill'][0]:.4f} → ${cl['bill'][1]:.4f} a window, b {_pct(cl['b'])}, inside the noise; the work done "
              f"was not counted, so G(cloud) is not read: {cl['note']}.", ""]
    rest = [v for k, v in pl.items() if k.startswith("organisms_")]
    if rest:
        L += ["**Not yet read:**", ""]
        for v in rest:
            L.append(f"- {v['label']}: {v['status']}" + (f" ({v['runs']})" if v.get("runs") else "") + f"; {v['reader']}")
        L.append("")
    t = d["total"]
    L += ["**Both places, for an owner who runs work in both**, G(total): " + t["status"] + ".", "",
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

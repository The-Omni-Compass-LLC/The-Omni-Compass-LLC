#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The two bills: four arms, read by the bill and the work done inside it (the founder's design of 1 November 2026: "we gauge
those two bills with the amount of work done native in both. Then ... OmniCompass on native in both. We will see that the bill
should be the same, but that we hopefully will be getting more work done within the bill ... It's four arms, A, B, C, D").

  A  the chip, native                      a rented graphics card run directly; its bill is the rental (hours x the hourly price)
  B  the chip, Omni-Compass on native      the same card and the same hours
  C  the cloud, native                     Kubernetes on Azure's machines; its bill is Azure's own, at list price
  D  the cloud, Omni-Compass on native     the same set, paired

Each arm runs three times where its table has three runs (labelled run 1, 2 and 3 here, so the run letters never meet the arm
letters). Every number is read from a table the repository already holds, each place on its own engine and named; nothing here
is a new measurement. The work done is what the place's own receipt counts (requests served); a place whose receipt counts no
work says so, and its work per dollar is not read.

  python3 tools/two_bills.py           write results/TWO_BILLS.md and results/TWO_BILLS.json
  python3 tools/two_bills.py --check   exit 1 when the page is not what the tables give
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.legal import stamp  # noqa: E402
from tools.readings import (HIGHER, SPENT, OWN_RUNS, by_word, run_word,  # noqa: E402
                            three_run_reading)

PAGE = ROOT / "results" / "TWO_BILLS.md"
DATA = ROOT / "results" / "TWO_BILLS.json"
CHIP = ROOT / "results" / "gpu" / "V23_A10_CAP_FULL_ABC.json"   # the full load: more offered than served, so the work can rise
CHIP_FIXED = ROOT / "results" / "gpu" / "V23_A10_CAP_ABC.json"  # the fixed job, beside it
CHIP_PRICE = 1.29        # dollars an hour, the price each Lambda launch printed for gpu_1x_a10 (docs/RUN_LEDGER.md)
CLOUD = ROOT / "results" / "live" / "AKS_STEADY_100_OMNI_V18.json"
CLOUD_ENGINE = "omni-v18"
CLOUD_PAGE = "results/live/AKS_STEADY_100_OMNI_V18.md"

# The founder's order of 1 November: the seven organisms, each run native and with Omni-Compass on native, in each place,
# so fourteen runs on the chip (A against B) and fourteen through the cloud (C against D). Each place reads its own three-run
# table (tools/hil_abc.py on the card-inside runs: the card's work, its bill and its work per dollar); a place whose table is
# not yet written says which runs feed it, and a place never run says so.
ORGANISMS = (("spine", "The spine"), ("compute_ai_cloud", "Compute / AI / Cloud"),
             ("physics_robotics_autonomous", "Physics / Robotics / Autonomous"),
             ("energy_facility_industrial", "Energy / Facility / Industrial"), ("distribution_specialized", "Distribution / Specialized"),
             ("stack", "The four stacked"), ("tower", "The whole tower"))
ORG_PLACES = (
    ("chip", "the chip: eight A100 cards on Lambda, each organism on its own card",
     ROOT / "results" / "gpu" / "V23_A100_8CARD_STACKS_ABC.json", "lambda-gpu 8card pooled, runs 41271477833, 41279081905 and 41271481737"),
    ("chip", "the chip: one A10 on Lambda, the card fully loaded inside the organism (docs/GPU_PREREGISTRATION.md, amendment 16)",
     ROOT / "results" / "gpu" / "V23_A10_STACKS_FULL_ABC.json", "lambda-gpu 1card stacks-full, runs 41271470803, 41271473309 and 41271475877"),
    ("cloud", "through the cloud: Azure, one rented machine with the real cluster inside each organism",
     ROOT / "results" / "live" / "V23_AZURE_ORGANISMS_ABC.json", "big-organism-detached, run 41269562586 (100 copies, three repetitions)"),
    ("cloud", "through the cloud: Google Cloud", None, "its key is not in the repository's secrets (docs/GOOGLE_SETUP.md)"),
    ("cloud", "through the cloud: Amazon Web Services", None,
     "its key is not in the repository's secrets and the account is on the Free plan (docs/AMAZON_SETUP.md)"),
)
ORG_MEASURES = (("work", "work done (requests served)"), ("bill", "bill (the rental for the window)"),
                ("per_dollar", "work per dollar"))


def organisms() -> list:
    """Each place's organisms: the three-run readings of the card's work, bill and work per dollar at each size, from the
    place's own table, or the runs that will write it."""
    out = []
    for where, label, path, runs in ORG_PLACES:
        place = {"where": where, "label": label, "table": str(path.relative_to(ROOT)) if path else None, "runs": runs}
        if path is None or not path.exists():
            place["status"] = "not yet run" if path is None else "not yet read"
            out.append(place)
            continue
        rec = json.loads(path.read_text(encoding="utf-8"))
        place.update(status="read", engine=rec.get("engine", ""), run_ids=rec.get("runs", []), rows=[])
        for name, title in ORGANISMS:
            for size in sorted({r["copies"] for r in rec["rows"] if r["organism"] == name}):
                cell = {"organism": name, "title": title, "copies": size}
                for m, _ in ORG_MEASURES:
                    row = next((r for r in rec["rows"] if r["organism"] == name and r["copies"] == size and r["part"] == "card"
                                and r["measure"] == m), None)
                    cell[m] = row["reading"] if row else "not read"
                place["rows"].append(cell)
        out.append(place)
    return out


def chip() -> dict:
    """The chip's three runs: each arm's bill (the rental for its own window, the window its own energy over its mean power),
    the requests it served, and the requests per dollar; each paired by run and read by the one key."""
    t = json.loads(CHIP.read_text(encoding="utf-8"))
    rows = t["rows"]
    energy, power, served = rows["energy, GPU (J)"]["runs"], rows["power, GPU mean (W)"]["runs"], rows["requests served"]["runs"]
    runs = []
    for e, p, s in zip(energy, power, served):
        arm = {}
        for side in ("native", "omni"):
            seconds = e[side] / p[side]
            bill = CHIP_PRICE * seconds / 3600.0
            arm[side] = {"seconds": seconds, "bill": bill, "work": s[side], "per_dollar": s[side] / bill}
        runs.append(arm)

    def paired(key):
        out = []
        for r in runs:
            n, o = r["native"][key], r["omni"][key]
            out.append({"native": n, "omni": o, "diff": o - n})   # no interval is carried for these, so none is claimed beyond the noise
        return out
    rows_out = {
        "bill ($, the rental for the arm's window)": (paired("bill"), SPENT),
        "work done (requests served)": (paired("work"), HIGHER),
        "work per dollar (requests served per $)": (paired("per_dollar"), HIGHER),
    }
    for g in ("energy, GPU (J)", "energy per served request (J)", "response time, 95th percentile (ms)"):
        rows_out[g] = (rows[g]["runs"], SPENT if g.startswith("energy") else "lower")
    fixed = json.loads(CHIP_FIXED.read_text(encoding="utf-8"))["rows"]
    engine = t["engine"][0] if isinstance(t["engine"], list) else t["engine"]
    return {"engine": engine, "title": t["title"], "runs": t["runs"], "per_run": runs,
            "rows": {g: {"reading": three_run_reading(rs, a), "runs": rs, "aim": a} for g, (rs, a) in rows_out.items()},
            "fixed_job": {g: fixed[g]["reading"] for g in ("requests served", "energy, GPU (J)") if g in fixed}}


def cloud() -> dict:
    """The cloud's newest set with a bill: its means and its paired bill, one set of paired repetitions (no three-run reading)."""
    t = json.loads(CLOUD.read_text(encoding="utf-8"))
    p = t["paired"]["compass"]
    bill = p["compute bill at list price ($)"]
    mh = p["machines billed, machine-hours"]
    work_keys = [k for k in t["means"]["native"] if "requests served" in k or "work done" in k]
    return {"engine": CLOUD_ENGINE, "page": CLOUD_PAGE, "repetitions": len(set(t["repetitions"]["native"]) & set(t["repetitions"]["compass"])),   # the pairs: present in both arms
            "bill": bill, "machine_hours": mh, "work_key": work_keys[0] if work_keys else None,
            "work": {k: (t["means"]["native"][k], t["means"]["compass"][k]) for k in work_keys}}


def pct(x):
    return f"{100 * x:.2f}%"


def equation(c: dict, k: dict) -> list:
    """The one equation (the founder's words of 2 November: "the only thing we need to prove is that we get more work for
    the bill"): the work for each dollar in each place, its benefit split into the work it added and the bill it moved, and the
    four arms' cells as the tables read them today."""
    L = ["## The one equation: work for the bill", "",
         "The founder's words of 2 November: what the receipts of the chips and the clouds show in the end is how much work is done "
         "inside the bill natively and how much with Omni-Compass on native, and the one thing to prove is more work for the bill. "
         "For a place p (the chip, run directly; or the cloud) and an arm a (native, or Omni-Compass on native), on the same offered "
         "load over the same window:", "",
         "- W(p, a): the work done (the requests served, the jobs finished);",
         "- B(p, a) = Σₖ c(p, a, k): the bill, every cost component k inside the place's own boundary (on the chip, the rental for "
         "the arm's window; in the cloud, every machine it bills at the cloud's own price);",
         "- E(p, a) = W(p, a) / B(p, a): the work for each dollar.", "",
         "The benefit in a place is", "",
         "    G(p) = E(p, Omni-Compass) / E(p, native) − 1 = (1 + ΔW(p)) / (1 + ΔB(p)) − 1,", "",
         "where ΔW(p) = W(p, Omni-Compass) / W(p, native) − 1 is the work Omni-Compass added and ΔB(p) = B(p, Omni-Compass) / "
         "B(p, native) − 1 is the bill it moved. In logarithms the two sides add:", "",
         "    ln(1 + G) = ln(1 + ΔW) − ln(1 + ΔB),", "",
         "so every benefit lives on one side or both: more work inside the bill (ΔW above zero), or the same work for a smaller bill "
         "(ΔB below zero). A bill that rises is power given, and the place gains only where the work rises more (G above zero).", "",
         "**The four arms.** A is the chip native, B the chip with Omni-Compass on native, C the cloud native, D the cloud with "
         "Omni-Compass on native, so G(chip) = E(B) / E(A) − 1 and G(cloud) = E(D) / E(C) − 1.", "",
         "**Where each place's benefit can live.**", "",
         "- **On the chip** (a card rented directly): the price of an hour is fixed and both arms rent the same window, so ΔB is "
         "near zero and G(chip) is near ΔW: the benefit is the work the card does in the time already paid for.",
         "- **Through the cloud**: B is the sum over the machines it bills of machine-hours times the cloud's price for each, with the "
         "cloud's own services inside that price; Omni-Compass moves the machines kept in service (a machine parked while idle leaves "
         "the bill) and the work each machine does, so both sides can move.",
         "- **The places are never added or set against each other.** The same work carries a different bill in each place (a "
         "cloud's price holds its own services and margin over the silicon), so each G is a ratio inside its own place, read the "
         "same way in both, and one place's price never enters another's reading.", "",
         "**Layers inside one place.** Where Omni-Compass governs two layers of one stack (the software end on top of the chip it "
         "runs on), the work for the bill composes, 1 + G(stack) = (1 + G(software end)) × (1 + G(chip)), when the two layers' "
         "effects do not overlap. That product is a composition of two measurements and is written as one; the stack's own run is "
         "the measurement.", "",
         "**The bill's line items** (the founder's checklist of 2 November: build each place's receipt line by line, so the two bills "
         "compare like for like). B is the sum of the place's own line items for the window; what each place charges for each, and "
         "what these runs meter:", "",
         "| Line item k | On the chip, run directly (a rented card) | Through the cloud | Metered in these runs |",
         "|---|---|---|---|",
         "| the machine (compute) | a flat rate for the hours rented, the same whether the card runs full or idle | an hourly rate for "
         "every hour each machine is on, billed by the second | yes: the rental for each arm's window; the machine-hours at the cloud's "
         "list price |",
         "| data out (egress) | a large allowance or a flat port in the rental | a fee for every gigabyte that leaves the cloud | not "
         "metered: both arms serve the same offered load, so the same data leaves in both |",
         "| storage and its speed (IOPS) | the drives inside the rented machine, in its rate | a fee a gigabyte stored, and one for the "
         "speed provisioned | not metered: both arms hold the same data on the same disks |",
         "| the labor to run it | the operator's own staff | much of it inside the cloud's price | not counted; Omni-Compass's own "
         "processor is counted, as power given, beside each run |", "",
         "**What Omni-Compass can move, term by term.** The work done in a window is W = C × (1 − V) × U: C the work one chip "
         "can do in the window fed all through it, V the share the place's own software layer takes before the work reaches the "
         "chip (a cloud's virtual machines and orchestration; none on a card run directly), U the chip-time kept fed in the window, "
         "counted in chip-windows (one chip fed all through the window is 1; a machine parked is fed none of the time it is "
         "parked). Inside one place both arms run the same chips under the same layer, so C and V are the same in both and cancel: "
         "ΔW = U(Omni-Compass) / U(native) − 1, the utilization Omni-Compass wins (the chip fed, the queue drained, the machines in "
         "service doing work). The bill, line by line: on a card rented directly B = the rate × the hours rented, the same in both "
         "arms, so ΔB = 0 and G(chip) = U(B) / U(A) − 1; through a cloud B = R × H + (data out × its rate) + (storage × its rate) + "
         "the cloud's other metered services, and of these Omni-Compass moves H, the machine-hours kept on (a machine parked while "
         "idle leaves the bill and takes no fed time with it), the others the same in both arms for the same workload, so G(cloud) "
         "= (U(D) / U(C)) × (B(C) / B(D)) − 1: the same work for fewer machine-hours is a GAIN, and so is more work for the same "
         "hours. Omni-Compass moves no C (the chip's own speed) and no V (the place's own layer, and the path the data takes "
         "through it). C and V differ between places and are why the same work carries a different bill in each: the places are "
         "never set against each other, and a figure for any place's V or price that this repository did not measure is never "
         "written as one of its own.", "",
         "A line item the same in both arms adds the same dollars to both bills: it leaves ΔW as it is and draws ΔB toward zero, so "
         "a receipt drawn inside a wider boundary reads a smaller bill change for the same work change. Each table names its "
         "boundary; a line item not metered stays written as not metered, never filled with a guessed price.", "",
         "**How a G is judged.** Each run's G is read by the one key across the three runs (`tools/readings.py`): from 0.5% up, GAIN "
         "where the work for the bill rose and LOSS where it fell, in all three runs or by their mean; STEADY under the floor; the "
         "runs disagree where clear runs point opposite ways.", "",
         "**The equation's cells today**, each read from its place's own table on its own engine:", "",
         "| Place and arms | Run | W, native → Omni-Compass | ΔW | B ($), native → Omni-Compass | ΔB | E (work per $), native → Omni-Compass | G |",
         "|---|---|---|---|---|---|---|---|"]
    sign = lambda x: "±0.00%" if abs(100 * x) < 0.005 else f"{'+' if x > 0 else '−'}{abs(100 * x):.2f}%"
    for i, r in enumerate(c.get("per_run") or [], 1):
        n, o = r["native"], r["omni"]
        dw, db = o["work"] / n["work"] - 1, o["bill"] / n["bill"] - 1
        g = (1 + dw) / (1 + db) - 1
        L.append(f"| the chip, A against B ({c['engine'].split(' (')[0]}) | {i} | {n['work']:,.0f} → {o['work']:,.0f} | {sign(dw)} | "
                 f"{n['bill']:.4f} → {o['bill']:.4f} | {sign(db)} | {n['per_dollar']:,.0f} → {o['per_dollar']:,.0f} | {sign(g)} |")
    b = k.get("bill") or {}
    if b:
        db = b["diff"] / b["native"]
        if k.get("work_key"):
            wn, wo = k["work"][k["work_key"]]
            dw = wo / wn - 1
            g = (1 + dw) / (1 + db) - 1
            L.append(f"| the cloud, C against D ({k['engine']}) | one set | {wn:,.1f} → {wo:,.1f} | {sign(dw)} | {b['native']:.5f} → "
                     f"{b['omni']:.5f} | {sign(db)} | | {sign(g)} |")
        else:
            L.append(f"| the cloud, C against D ({k['engine']}, Azure) | one set of {k.get('repetitions')} | not counted in that set | | "
                     f"{b['native']:.5f} → {b['omni']:.5f} | {sign(db)}, inside the noise | not read | not read |")
    L += ["| the cloud, C against D (Google, Amazon) | | not yet run | | | | | |", ""]
    w = (c.get("rows") or {}).get("work per dollar (requests served per $)", {}).get("reading", "")
    L += [f"**What it reads today.** On the chip the three runs' G read **{w.replace('**', '')}**: the work for the bill has not "
          "yet been shown to rise. In the cloud the work was not counted in the set that stands, so G is not read. The runs that "
          "read it next are started or queued: the card fully loaded with the seven organisms, the eight-card machine, and the "
          "cloud at the max with its work meter, each read by this equation as it lands.", ""]
    return L


def page(c: dict, k: dict, organisms_: list) -> str:
    L = ["# The two bills: four arms, the bill and the work done inside it", "",
         "The founder's design of 1 November 2026: the same work measured against what it cost, on the two bills a customer "
         "pays. **A**, the chip native, and **B**, the chip with Omni-Compass on native: a rented graphics card run directly, its "
         "bill the rental. **C**, the cloud native, and **D**, the cloud with Omni-Compass on native: Kubernetes on Azure's "
         "machines, its bill Azure's own at list price. The question for each bill: is it the same, and is more work done inside "
         "it. Each arm's runs are labelled run 1, 2 and 3 so the run letters never meet the arm letters. Every number is read from "
         "a table the repository already holds, each place on its own engine; nothing here is a new measurement.", "",
         *equation(c, k),
         f"## The chip: A against B (an NVIDIA A10 on Lambda, {c['engine'].split(' (')[0]}, three runs)", "",
         f"From `results/gpu/V23_A10_CAP_FULL_ABC.md` (runs {', '.join(c['runs'])}): the full load, more requests offered than the "
         "card serves in its window, so the work done can rise inside the same rented time. The bill is the rental for each arm's "
         f"own window (its energy over its mean power) at ${CHIP_PRICE:.2f} an hour, the price each launch printed "
         "(`docs/RUN_LEDGER.md`); Lambda's billing page is the exact figure. Beside it, the same runs' fixed job "
         "(`results/gpu/V23_A10_CAP_ABC.md`, a set number of requests in each window, so the work cannot rise): requests served "
         f"{c['fixed_job'].get('requests served', 'not read')}; energy {c['fixed_job'].get('energy, GPU (J)', 'not read')}.", "",
         "| Gauge | Three runs | Run 1 | Run 2 | Run 3 |", "|---|---|---|---|---|"]
    for g, r in c["rows"].items():
        cells = []
        for x in r["runs"]:
            w = run_word(x, r["aim"]) or "STEADY"
            rel = (x["diff"] / x["native"]) if x.get("native") else 0.0
            cells.append(f"{w}, {by_word(100 * rel, w, digits=2) if w != 'STEADY' else pct(abs(rel))}")
        reading = r["reading"] if r["reading"].startswith("**") else f"**{r['reading']}**"
        L.append(f"| {g} | {reading} | " + " | ".join(cells) + " |")
    L += ["", "| Run | Arm | Window (s) | Bill ($) | Requests served | Requests per $ |", "|---|---|---:|---:|---:|---:|"]
    for i, r in enumerate(c["per_run"], 1):
        for side, name in (("native", "A, native"), ("omni", "B, Omni-Compass on native")):
            a = r[side]
            L.append(f"| {i} | {name} | {a['seconds']:.1f} | {a['bill']:.4f} | {a['work']:,.0f} | {a['per_dollar']:,.1f} |")
    b = k["bill"]; m = k["machine_hours"]
    bill_rel = b["diff"] / b["native"]
    L += ["", f"## The cloud: C against D (Kubernetes on Azure's AKS, {k['engine']}, one set of {k['repetitions']} paired repetitions)", "",
          f"From `{k['page']}`, the newest cloud set with a metered bill. The engine that stands has not yet run in the cloud: its "
          "set starts when Azure's current long set ends, and this row is then read again on it.", "",
          "| Gauge | C, native | D, Omni-Compass on native | The change | 95% interval | Beyond the noise |", "|---|---:|---:|---|---|---|",
          f"| bill at list price ($ a window) | {b['native']:.5f} | {b['omni']:.5f} | {pct(abs(bill_rel))} ({run_word(b, SPENT)}"
          f"{'' if b['significant'] else ', inside the noise'}) | "
          f"{b['ci95'][0]:+.5f} to {b['ci95'][1]:+.5f} | {'yes' if b['significant'] else 'no'} |",
          f"| machines billed (machine-hours a window) | {m['native']:.4f} | {m['omni']:.4f} | {pct(abs(m['diff'] / m['native']))} "
          f"({run_word(m, SPENT)}{'' if m['significant'] else ', inside the noise'}) | {m['ci95'][0]:+.4f} to {m['ci95'][1]:+.4f} | "
          f"{'yes' if m['significant'] else 'no'} |"]
    if k["work_key"]:
        n, o = k["work"][k["work_key"]]
        L.append(f"| {k['work_key']} | {n:,.1f} | {o:,.1f} | {pct((o - n) / n)} | | |")
    else:
        L += ["", "This set counted no work done: the cloud's work meter came with the cloud sets after 31 October, so its work "
              "per dollar is not read here; the set on the engine that stands reads it."]
    names = {"bill": "bill ($, the rental for the arm's window)", "work": "work done (requests served)",
             "per_dollar": "work per dollar (requests served per $)", "energy_per": "energy per served request (J)"}

    def chip_word(key):
        return c["rows"][names[key]]["reading"].strip("*")
    L += ["", "## The seven organisms in the four arms", "",
          "Each organism runs native and with Omni-Compass on native in each place: on the chip, A against B, and through the "
          "cloud, C against D. Every cell is a three-run reading by the one key of the card's own receipts with the organism "
          "running around it: the requests the card served (the work), the rental for the arm's window (the bill) and the two "
          "together (work per dollar); the organism's modelled plants are in each place's own table, never in these cells.", ""]
    for place in organisms_:
        L += [f"### {place['label'][0].upper()}{place['label'][1:]}", ""]
        if place["status"] != "read":
            L += [f"{'Not yet run' if place['status'] == 'not yet run' else 'Not yet read'}: {place['runs']}.", ""]
            continue
        L += [f"From `{place['table']}` ({place['engine'].split(' (')[0]}; runs {', '.join(place['run_ids'])}).", "",
              "| Organism | Copies | " + " | ".join(n for _, n in ORG_MEASURES) + " |", "|---|---:|" + "---|" * len(ORG_MEASURES)]
        for r in place["rows"]:
            L.append(f"| {r['title']} | {r['copies']} | " + " | ".join(r[m] for m, _ in ORG_MEASURES) + " |")
        L.append("")
    L += ["## What the two bills say today", "",
          f"- **The chip:** the bill {chip_word('bill')} (the same rented window in both arms); the work done inside it "
          f"{chip_word('work')}; the work per dollar {chip_word('per_dollar')}; the energy for each request served "
          f"{chip_word('energy_per')}.",
          f"- **The cloud:** the bill {pct(abs(bill_rel))} {'higher' if bill_rel > 0 else 'lower'} with Omni-Compass on native, "
          "inside the noise; the work done was not counted in that set, so the work per dollar waits for the set on the engine "
          "that stands.", "", OWN_RUNS, ""]
    return "\n".join(L)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    c, k, o = chip(), cloud(), organisms()
    text = "\n".join(stamp(page(c, k, o).split("\n"))) + "\n"
    data = json.dumps({"chip": c, "cloud": k, "organisms": o}, indent=1, default=str) + "\n"
    if a.check:
        ok = PAGE.exists() and PAGE.read_text(encoding="utf-8") == text and DATA.exists() and DATA.read_text(encoding="utf-8") == data
        print("the two bills: " + ("in line with the tables" if ok else "out of date (python3 tools/two_bills.py)"))
        return 0 if ok else 1
    PAGE.write_text(text, encoding="utf-8")
    DATA.write_text(data, encoding="utf-8")
    print(f"{PAGE.relative_to(ROOT)} and its record: the chip on {c['engine'].split(' (')[0]}, the cloud on {k['engine']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

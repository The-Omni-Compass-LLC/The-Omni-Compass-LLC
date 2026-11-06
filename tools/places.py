#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Where Omni-Compass sits and what each benchmark shows: the words for the places, written once (the founder's words of
31 October 2026, night: "Did we determine how we're defining the cloud, the chip, the Kubernetes through, and what the
benchmark shows? ... We don't have to show benefit. We know that. We just need to show we hold, and then we know where the
benefit lives, and we can explain. But either way, you need the terminology ... wherever it's supposed to be, however it's
supposed to be").

The block is written here and nowhere else; every page in PAGES carries it word for word between its two markers, under a
heading of the page's own, as the key of tools/readings.py is carried. It holds no number: what each place's runs read stands
on the pages its table names.

  python3 tools/places.py --print    the block
  python3 tools/places.py --fix      write it on every page that carries the markers
  python3 tools/places.py --check    exit 1 when a page lacks it or differs (run by verify.py)
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

BEGIN = "<!-- the places: where Omni-Compass sits and what each benchmark shows (tools/places.py) -->"
END = "<!-- end of the places -->"
PAGES = ("README.md", "DISCLOSURES.md", "docs/HOW_TO_READ_THE_RESULTS.md", "docs/OMNI_COMPASS_MANUAL.md",
         "docs/OMNI_COMPASS_OWNERS_MANUAL.md", "docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md")

TERMS = (
    ("The software end",
     "The programs that carry the work: Kubernetes with its pod and cluster autoscalers, its schedulers and the orchestrators on "
     "it, the data stores (PostgreSQL, MySQL, Redis, MongoDB, Kafka) and the services they serve. Omni-Compass sits on top of "
     "their native controllers. This is where its benefit lives and where it is measured: real software on real computers "
     "(class L), on GitHub's own machines in kind clusters. Those machines are rented runners, never called bare metal and never "
     "called the chip."),
    ("Bare metal",
     "The first of the two places a system runs (the founder's order of 1 November 2026): the owner's own machines, or a chip run "
     "directly, with the chip's own controllers under the software. Its bill is the machine's own: the hours it runs, and the "
     "energy the chip's own meter reads. The software end goes with Omni-Compass to it, and there Omni-Compass can reach the "
     "chip's own knobs too."),
    ("Through the cloud",
     "The same software end on a cloud provider's rented machines: Kubernetes through the cloud (Azure's AKS today; Google's GKE "
     "and Amazon's EKS wired the same way, not yet run), the machines billed by the hour at list price and added or removed by "
     "the cloud's own autoscaler. Its bill is the cloud's own; the cloud's chips and back end are inside its price and out of "
     "Omni-Compass's reach: it governs what the cloud gives, through the cloud's own Kubernetes. The cloud is the wire between the "
     "software end and the provider's bare metal. The wire makes no benefit of its own, and no tenant can meter the provider's "
     "chips."),
    ("The chip",
     "Bare metal's own part: the processor or graphics card under the software, with its own controllers (the power limit, the clocks, the heat), "
     "measured with the card's own power meter (class P) where Omni-Compass sets the card's knobs through the card's published "
     "interface. Omni-Compass built into the silicon, or into a battery's own controller, is not something any run here can "
     "test, and it is not claimed."),
    ("The four arms",
     "Two places, two arms in each: A, native on bare metal; B, Omni-Compass on top of native on bare metal; C, native through "
     "the cloud; D, Omni-Compass on top of native through the cloud. Each is read by its bill and the work done inside it, "
     "each place on its own, since a system runs in one or the other; an owner who runs work in both may weigh them only by its "
     "own spend, through G(total) (`results/TWO_BILLS.md`, `docs/WORK_PER_BILL.md`). The software end's "
     "tests are one set read three ways (the Omni index on work, speed and machines; the same on work and speed alone; the "
     "layers composed): they never add together, and none of them is either place's bill."),
    ("Hold",
     "Omni-Compass on top of native harms nothing in that place: every judged gauge (the work done, the response time, the "
     "minutes over the line, the pods waiting, the failures) reads STEADY or GAIN against native by the one key, and a resource "
     "that rose (the bill, the machine-hours, the energy) is read beside it as power given. A place holds when its runs read no "
     "LOSS."),
    ("Where the benefit lives",
     "At the software end, where it is made and measured, with no bill in it. It shows through on the two bills, native against "
     "Omni-Compass on native: on bare metal the work done inside the machine's own bill (each dollar, and each joule of the chip's "
     "own meter), and through the cloud the work done inside the cloud's own bill (each dollar). The chip and "
     "the wire themselves add no gain of their own: they are where Omni-Compass must hold. A benchmark that holds is the proof "
     "of no harm in its place; the benefit is shown where it lives and explained for the rest."),
    ("Work for the bill",
     "The one number every receipt is read for: the work done for each dollar of the bill, E = W / B (written once in "
     "`results/TWO_BILLS.md`), in each place native against Omni-Compass on native, G = E(Omni-Compass on native) / E(native) "
     "− 1 = (1 + ΔW) / (1 + ΔB) − 1 ≈ ΔW − ΔB, ΔW the change in the work done and ΔB the change in the bill. A bill that rises "
     "is power given; there is more work for the bill when the work rises more than the bill (ΔW > ΔB, G > 0). Both arms pay the same prices, so a place's price level "
     "cancels in its G. A system that runs in one place reads that place's G alone; an owner who runs work in both weighs them by "
     "its own native spend S(p), G(total) = Σₚ S(p)(1 + ΔW(p)) / Σₚ S(p)(1 + ΔB(p)) − 1 (`docs/WORK_PER_BILL.md`)."),
    ("One mechanism, in one place, felt along the whole path",
     "Omni-Compass acts in one place, the software end, on top of the controllers a stack already runs; it changes nothing in the "
     "chip and nothing in the network or the cloud. Its effect travels the whole path the work travels: a request starts in the "
     "software, crosses the wire (the owner's own racks or a cloud's machines), is computed on the chip and comes back. So the "
     "effect is checked at every place: the software end shows the gain (more work, faster, the machines it took read beside it, a rise "
     "power given), and the wire and the chip are read for whether it holds and carry the gain to their bills. Two places are tested because a system runs in only those "
     "two; one mechanism makes the gain, the way a city's traffic signals make more trips an hour on the same roads and the same "
     "cars."),
)

ROWS = (
    ("The software end", "Kubernetes and the data stores on GitHub's machines (kind), class L",
     "the benefit, by the one key, and that it holds", "`docs/BENEFIT_SHEET.md`, `results/OMNI_INDEX.md`"),
    ("Bare metal, the chip", "a graphics card on Lambda run directly, its rental the bill and its own power meter beside it, class P",
     "that it holds, and the work done inside its bill, A against B: the work per dollar and per joule",
     "`results/TWO_BILLS.md`, `results/gpu/`"),
    ("Through the cloud", "Kubernetes through Azure's AKS, the machines it bills, class L",
     "that it holds, and the work done inside its bill, C against D: the work per dollar",
     "`results/TWO_BILLS.md` and each set's `results/live/AKS_*.md`"),
    ("The whole organism", "the places composed by the product law, class S of P and L",
     "how the places add up, an explanation and never a measurement", "`results/WHOLE_SYSTEM.md`"),
)


def block_lines() -> list[str]:
    L = [BEGIN, "",
         "Omni-Compass is software. It always sits on top of a native controller. A system runs it in one of two places, on bare "
         "metal or through the cloud, and in each place there are two arms, native and Omni-Compass on top of native: four arms, "
         "each read by its bill and the work done inside it. These are the words for them, used the same way on every page.", ""]
    # the table first, its words after it: a printed chapter that ended on the table left its last rows alone on a page
    # (1 November: 12% of a page in the Live Benchmark Engine Manual, 22% in the Operator's)
    L += ["| Place | Its benchmark | What it must show | Its readings |", "|---|---|---|---|"]
    L += [f"| {a} | {b} | {c} | {d} |" for a, b, c, d in ROWS]
    L += [""] + [f"- **{t}.** {d}" for t, d in TERMS]
    L += ["", END]
    return L


def block() -> str:
    return "\n".join(block_lines())


def with_block(text: str) -> str:
    if BEGIN in text and END in text:
        a = text.index(BEGIN)
        b = text.index(END) + len(END)
        return text[:a] + block() + text[b:]
    return text


def check(root: Path = ROOT) -> list[str]:
    bad = []
    for p in PAGES:
        f = root / p
        if not f.exists():
            bad.append(f"{p}: missing")
            continue
        t = f.read_text(encoding="utf-8")
        if BEGIN not in t or END not in t:
            bad.append(f"{p}: the places (between {BEGIN} and {END}) are missing")
        elif with_block(t) != t:
            bad.append(f"{p}: the places are not word for word tools/places.py's")
    return bad


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--print", action="store_true")
    g.add_argument("--fix", action="store_true")
    g.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    if a.print:
        print(block())
        return 0
    if a.fix:
        for p in PAGES:
            f = ROOT / p
            if f.exists():
                t = f.read_text(encoding="utf-8")
                n = with_block(t)
                if n != t:
                    f.write_text(n, encoding="utf-8")
                    print(f"the places rewritten in {p}")
        return 0
    bad = check()
    for b in bad:
        print(b)
    print("the places: every page carries them word for word" if not bad else f"the places: {len(bad)} pages differ")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())

# © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

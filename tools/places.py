#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
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
    ("On site",
     "The software end on the owner's own machines, the bare metal, made and paid for before any run: the pool is fixed and its "
     "hours are no bill. The software end's benefit is the same there. In our own models (class S) the on-site plant keeps every "
     "machine it starts with."),
    ("Through the cloud",
     "The same software end on a cloud provider's rented machines: Kubernetes through the cloud (Azure's AKS today; Google's GKE "
     "and Amazon's EKS wired the same way, not yet run), the machines billed by the hour at list price and added or removed by "
     "the cloud's own autoscaler. The cloud is the wire between the software end and the provider's bare metal. The wire makes no "
     "benefit of its own, and no tenant can meter the provider's chips."),
    ("The chip",
     "The processor or graphics card under the software, with its own controllers (the power limit, the clocks, the heat), "
     "measured with the card's own power meter (class P) where Omni-Compass sets the card's knobs through the card's published "
     "interface. Omni-Compass built into the silicon, or into a battery's own controller, is not something any run here can "
     "test, and it is not claimed."),
    ("Hold",
     "Omni-Compass on top of native harms nothing in that place: every judged gauge (the work done, the response time, the "
     "minutes over the line, the pods waiting, the failures) reads STEADY or GAIN against native by the one key, and a resource "
     "that rose (the bill, the machine-hours, the energy) is read beside it as power given. A place holds when its runs read no "
     "LOSS."),
    ("Where the benefit lives",
     "At the software end, where it is measured. The cloud's wire and the chip are where Omni-Compass must hold: the wire carries "
     "the software end's benefit to the bill and adds none of its own (what a cloud's bill shows, machines parked or more work "
     "for each dollar, is made at the software end), and a resource the chip's runs cut, its energy at the tune-down, is read "
     "beside the work and never claimed as the benefit. A benchmark that holds is the proof of no harm in its place; the benefit "
     "is shown where it lives and explained for the rest."),
)

ROWS = (
    ("The software end", "Kubernetes and the data stores on GitHub's machines (kind), class L",
     "the benefit, by the one key, and that it holds", "`docs/BENEFIT_SHEET.md`, `results/OMNI_INDEX.md`"),
    ("Through the cloud", "Kubernetes through Azure's AKS, the machines it bills, class L",
     "that it holds; the work per dollar read beside the bill", "`results/live/AKS_BILL.md` and each set's `results/live/AKS_*.md`"),
    ("The chip", "a graphics card on Lambda, its own power meter, class P",
     "that it holds; its energy read beside the work", "`results/gpu/`"),
    ("On site", "the software end on the owner's own machines; in our own models the on-site plant, class S",
     "the software end's benefit, the machines' hours no bill", "`results/model_gate/`"),
    ("The whole organism", "the places composed by the product law, class S of P and L",
     "how the places add up, an explanation and never a measurement", "`results/WHOLE_SYSTEM.md`"),
)


def block_lines() -> list[str]:
    L = [BEGIN, "",
         "Omni-Compass is software. It always sits on top of a native controller, and it can sit in three places: the software "
         "end, the cloud's wire and the chip. The software end runs on site or through the cloud. These are the words for "
         "them, used the same way on every page.", ""]
    L += [f"- **{t}.** {d}" for t, d in TERMS]
    L += ["", "| Place | Its benchmark | What it must show | Its readings |", "|---|---|---|---|"]
    L += [f"| {a} | {b} | {c} | {d} |" for a, b, c, d in ROWS]
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

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

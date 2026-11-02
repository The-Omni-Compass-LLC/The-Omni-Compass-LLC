# The Website's Claims: What the Record Supports, Word for Word

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Every claim the company's website may make about Omni-Compass's benefit, worded as the repository's own records support it, each
with the file it is read from; and every number that has appeared on the site, or in an outside AI's reading of it, that no record
supports and that must come off. A page that needs a number takes it from here, and from nowhere else. When a record changes, this
page changes with it.

## The three benefits, as the record supports them

**1. More work (the software end).** "The Omni index, 5.0% GAIN: more work, faster, on fewer machines; 12.9% GAIN on work and speed
alone. Measured on real software on GitHub's own machines, Omni-Compass on top of native against native on the same machines
(class L). It is not a bare-metal result, not a cloud result, not a comparison of the two, and not a bill."
Source: `results/OMNI_INDEX.md` (the newest three-run table of each product, omni-v21 among them).

**2. The bill (bare metal and the cloud).** "Work for the bill, the work done for each dollar of the bill, native against
Omni-Compass on native in the same place, is being measured. On one A10 card (omni-v23, fully loaded) the three runs moved it
+1.46%, +0.73% and −0.69%: the runs disagree. In the cloud (Azure, omni-v18, 97 paired repetitions, at the tune-down on the
machines alone) the bill moved +1.2%, inside the noise, and the work was not counted. No bill saving is claimed yet."
Source: `docs/WORK_PER_BILL.md` (`tools/work_per_bill.py`, from `results/TWO_BILLS.json`).

**3. Less oversight (fewer pages to answer).** "Fewer alert minutes, the minutes an on-call page would be open, in the Kubernetes
tests on GitHub's machines (omni-v21), in all three runs of each: a public day of demand (Google 2011) −61% to −72%; the KEDA event
autoscaler −94% to −100%; faults (a machine down, a spike) −14% to −22%; the governor killed mid-run −18% to −25%; all four
together −16% to −24%. One batch-queue test is mixed (the runs disagree). Every change the governor makes is its own, logged with its
reason and read back, and after a crash every setting walks back to native by itself."
Sources: `results/live/V21_TRACE_GOOGLE2011.md`, `results/live/V21_KEDA_REQUESTS.md`, `results/live/V21_FAULTS.md`,
`results/live/V21_ROBUST_KILL.md`, `results/live/V21_ALL_FOUR.md`, `results/live/V21_BATCH.md`.

Not to be said, because it was never measured: "your operations team shrinks", "it replaces the human in the loop", "you need fewer
people".

## Numbers that must come off (no record supports them)

| Seen on the site or in an outside AI's reading | What the record says |
|---|---|
| "+47.2%" as a headline, or labelled bare metal | the machine-hours of one capacity test on GitHub's machines, 4 October, an engine long replaced (`results/live/CAPACITY_2.md`) |
| "+49.9%" as a headline, or labelled cloud | the 99th percentile of one test set on GitHub's machines, 3 October, an engine long replaced (`results/live/LIVE_REPS_30.md`) |
| "+12.9% to +13.1% whole-system gain" | 12.9% is the software end's service reading; 13.1% is one row of a composed table; the composed whole is 22.5%, class S (`results/WHOLE_SYSTEM.md`) |
| "112 vs 100 units" in the cloud; "113 units an hour vs 100" on bare metal | no such measurement |
| "Azure, 97 repetitions: output +12%"; "the bill +1.2% while the output +12%" | that Azure set counted no work; its +1.2% is its bill, inside the noise |
| "unit cost $5.00 → $4.42" | no such measurement |
| "13% faster on bare metal"; "13% fewer cloud hours"; "$423 a month saved" | no such measurement; the A10's runs disagree and no cut of a cloud's hours has been measured |
| "shut the meter off early"; data "pipelined into the chip's cache"; "1 hour instead of 4" | Omni-Compass works in the control plane: it reads native controllers' meters and writes the settings they accept; no byte of the workload passes through it |
| "deterministic SLAs"; "deterministic behaviour across the system" | never claimed |
| "data centers waste 30% to 40% of their compute" | not a measurement in the record; the front matter names the problem (capacity held idle, late reaction, loops at cross purposes) without a number |
| "+13.1% on bare metal"; "+5.3% through the full cloud path" | no such readings: the only bare-metal receipt's three runs disagree, the cloud's work is not yet counted; 5.3% appears only in unrelated rows (one run of a three-run table; an omni-v3 organisms row) |
| "standard schedulers have no closed-circle state guarantee"; "every cluster is ungoverned" | not the record's words; Omni-Compass sits on top of those schedulers and needs them |
| other companies' products (cloud cost tools, chip makers, Kubernetes, Kafka) called "band-aids"; Omni-Compass "the lone exception", "the only unified law" | never claimed; Omni-Compass is never a competitor to the native controllers and products it sits on top of, and no outside party has reviewed the results |
| "eliminates" or "bypasses" Kubernetes or the orchestration layer | the opposite: Omni-Compass always sits on top of a system's native controllers and orchestrator (Kubernetes, its scheduler and kubelet stay in every arm) and never replaces them |
| "zero oversight", "zero manual maintenance", "no engineers needed" | never measured; what is measured is fewer alert minutes, and the governor's own audit (every change logged with its reason, read back, handed back to native after a crash) is there for people to read |
| "native = code with no controller" | native is the system's own controllers (the Kubernetes autoscaler among them), which stay in every arm |

## The manuals on the website

The website should carry the repository's own manuals as they are built (`docs/OMNI_COMPASS_MANUAL.pdf`,
`docs/OMNI_COMPASS_OWNERS_MANUAL.pdf`, `docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.pdf`), never a rewritten page under their names: numbers
attributed to "the Owner's Manual" by outside readers (30% to 40% waste, +13.1% on bare metal, +5.3% through the cloud) are in none
of them.

## On every page

"Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results." And the legal notice
at the top and the end, as `tools/legal.py` writes it.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

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

## An example budget, as it may be shown

A page may show the founder's $100 M example (an IT budget of 2.9% of a revenue of about $3.45 B) as the equation's arithmetic,
labelled beside it "an example at the founder's aim, not a result": through a cloud, at the aim of 31 October (the bill +1%, the
work +12%), the work for each dollar up 10.9%, $10.9 M more work a year at native's price per unit of work for a bill of $101 M;
on bare metal the bill holds and each 1% more work from the same boxes is $1 M a year. It is written once, in
`docs/WORK_PER_BILL.md` ("A $100 million budget, read by the equation"), with what the receipts have measured beside it. An
example never describes the mechanism differently from the record: Omni-Compass moves the settings native controllers accept
and touches no data, cache or network.

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
| "the 2.9% IP operational stack tax", "suppressed to 0%" | 2.9% may stand in an example as the size of an IT budget against revenue (the founder's example: $100 M is 2.9% of a revenue of about $3.45 B, labelled as an example), never as a cost Omni-Compass removes: no such tax is measured, and a place's own software share (a hypervisor's, an orchestrator's) is the same in both arms and is never a saving (`docs/WORK_PER_BILL.md`, "A $100 million budget") |
| a "$100 M blueprint": $2.9 M tax and $22.1 M idle cost to $0, core compute $75 M → $84 M, "+12% work", "$16 M cash saved", a bill of $84 M | no such measurement; every figure is invented. What an owner can write about a $100 M budget today is in `docs/WORK_PER_BILL.md`, "A $100 million budget, read by the equation" |
| "cloud $100 M → $84 M", "$15 M wire access and egress", "core work $60 M → $69 M, +15%" | no such measurement; the one cloud set read moved its compute bill +1.21%, inside the noise, and counted no work; our model at the max reads the machine-hours up 9% to 35% (class S) |
| "bare metal: core work $75 M → $100 M", "+33% free work", "100% of the silicon", "flawless, unthrottled" | no such measurement, and impossible by the engine's own rule: every muscle to its own limit and never past it, a 5% cushion at each line; queueing delay diverges as a machine's busy share nears one. The only bare-metal receipt's three runs disagree (w +1.51%, +0.73%, −0.70%) |
| "removed human oversight", "complete autopilot, no DevOps engineers or monitoring platforms" | never measured; what is measured is fewer alert minutes, and the governor's audit is there for people to read |
| a "Deterministic Optimization Identity", V = W·(1 − IP_tax) / (M·T·(1 + Vₒ)), with IP_tax 0.029 natively and 0 under Omni-Compass; "10 h → 8.7 h"; "1,000,000 → 1,131,000 tasks"; "sub-millisecond hardware alignment" | the equation writes its own answer in: a native-only factor (1 − 0.029) puts a 3.0% gain into every reading before anything is measured, and it counts a loss twice, since a measured W already carries every loss. Vₒ is the same in both arms and cancels, as it does in the repository's equation. 8.7 h and 1,131,000 are inputs typed in, not readings, and the equation's own arithmetic contradicts its text (1.131 / 0.971 = +16.5%, not +13.1%; 10 / 8.7 ÷ 0.971 = +18.4%). Without the IP term it is the repository's equation, G = (1 + ΔW) / (1 + ΔB) − 1 (`results/TWO_BILLS.md`, `docs/WORK_PER_BILL.md`). The governor decides every 10 s on site and every 60 s through a cloud (omni-v24), and nothing in it is sub-millisecond |
| a "20% structural drain": a "13% IP stack tax" plus a "7% engineering and observation tax", both "dropping to 0%"; engineering hours that "collapse"; Datadog and New Relic "no longer needed" | no such measurement: every figure is invented, and none of them is a share of anything the record measured. The cost identity it writes, total = machine-hours × rate + engineering hours × rate, is sound as a bill's line items (the repository's B = Σₖ cₖ, the owner's staff one line of it, `docs/WORK_PER_BILL.md`), but its engineering hours must come from the owner's own timesheets, native against Omni-Compass on native, and none have been measured. What is measured is fewer alert minutes, the minutes an on-call page would be open, and the commands the governor wrote on its own, each logged with its reason for people to read |
| an "audit template" or a "referee_benchmark.sh" whose Omni-Compass column is filled in before any run ("0.00 hrs", "0.00 %", `OMNI_ENG_OVERSIGHT_HOURS=0`, `MACHINE_FRICTION_TAX=13`, a "locked 20%", "$84,000,000", a GPU idle of "10.5" printed where no GPU is present) and that prints "Confirmed" whatever the machines did; citations such as "[2.1]" | a script that types its results in is not a measurement, and its output must never be shown as one. Its real commands (`vmstat`'s I/O wait, `nvidia-smi`'s utilization) read how busy a processor is, a resource shown beside the result, never the work done; its task counter (`tail -f … \| grep -c`) never ends. The measurement is the repository's paired harness, both arms measured on the same machines, every row reported (`results/WORK_TODAY.md`, `docs/WORK_PER_BILL.md`) |
| other products' figures called "true verified benefits" (Cilium or eBPF "10% to 15% CPU reclaimed", Run:ai "2× to 3×" or "30% more work", Granulate "15% to 20% smaller bill", CAST AI "up to 50% invoice cut"), or other products called "cleaners" of "human waste" | those are each vendor's own published claims, never tested by us; the record verifies no other product's number and characterizes none. Several of them are what Omni-Compass sits on top of, never beside: the KAI scheduler (Run:ai's scheduler, open-sourced) and KubeRay (Ray) are among the governors it governs on real Kubernetes (`results/live/GOVERNORS.md`; on omni-v12 the KAI table read 5 GAIN, 5 LOSS, 6 STEADY and 6 where the runs disagree, `results/live/V12_KAI.md`). Each layer's products, from their own public material: `docs/LANDSCAPE.md` |
| "silo optimization against whole-system GAIN": "+13.1% whole-system on bare metal", "+5.3% through the full cloud path", "13% more throughput out of silicon already at full capacity", "the data streams governed before they hit the infrastructure" | no such readings (see the rows above), and the mechanism is wrong: Omni-Compass moves the settings native controllers accept, every muscle to its own limit and never past it; it touches no data stream, packet, queue or chip. The software end's reading is the Omni index, 5.0% GAIN (12.9% on work and speed alone), on GitHub's machines, not bare metal and not the cloud |
| a PDF titled "Omni-Compass Architecture & Control Law Specification", "OC-SPEC-V21-CORE", "Security classification: Referee Benchmark Authenticated" (an outside AI's, 2 November): an identity Λ = ∏ Φ·τ/(1 + γ) · (1 − α·IP_tax) with α "a binary gate" set to 0 by Omni-Compass, C code of a packet ring buffer, and the $100 M table | none of it is Omni-Compass's, and it must never be shown as the company's specification: nothing was authenticated or reviewed by anyone; its equation writes its own answer in (α set to 0 by definition) and its markup is broken (backslash sequences eaten, "rac", "lpha", "ext"); the C code copies 16-byte packets into a ring buffer, a data path Omni-Compass never touches, and is not in the repository; "V21" names an engine that no longer stands (omni-v24 stands); it carries no legal notice. Omni-Compass's specification is the repository's own: the compass law (`omnicompass/compass_law.py`), the governor (`omni_controller/`), the factory profile (`docs/FACTORY_PROFILE.md`), the one equation (`results/TWO_BILLS.md`), the mathematics in the Owner's Manual |
| "perfect pipelining", "guarantees a deterministic state", "regulates data admissibility at the gateway" | Omni-Compass works in the control plane: no request or byte passes through it, and no determinism is claimed |
| "a definitive, referee-level underwriting opinion"; "Approved as a high-viability architectural asset"; "the architectural review is formally closed" (an outside AI's text, 2 November) | no underwriter, auditor or outside referee has reviewed or approved anything, and every results page says so: "Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results." Its figures are the rows above (+13.1%, +5.3%, $100 M → $84 M, $16 M, 33% more work, a 20% "tax" whose parts, 2.9% + 10% + 7%, make 19.9%). Its "alerts drop to zero" is not the record: on omni-v21 thirteen three-run tables read the alert minutes, eleven GAIN (seven in all three runs, four by the mean of the three), one STEADY (CruiseKube) and one where the runs disagree (the batch queue), none at zero (`results/live/V21_*.md`). Other companies' products (CAST AI, Turbonomic) said to be "cleaning up human negligence" is a claim the company never makes |

## The industry landscape page

The website's `/docs/industry-landscape` page is `docs/INDUSTRY_LANDSCAPE.md`, word for word: the chip, the cloud and the
software, what each layer's tools act on, where Omni-Compass sits on top of them (a supervisory outer loop over the native inner
loops, in the control plane only), and each benefit at the strength the record shows. It names no product as falling short and does
not claim the only approach, a smaller bill, fewer people or no trade-off; the products of each layer are graded from their own
public material in `docs/LANDSCAPE.md`.

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

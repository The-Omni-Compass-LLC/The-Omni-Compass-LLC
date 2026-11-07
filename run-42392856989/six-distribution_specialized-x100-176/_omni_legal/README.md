# Omni-Compass

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

**The aim, in the founder's words: more work, faster, on fewer machines, for the same energy and the same bill, on top of the stack you already run.** It is an aim, not a result: the record reads the work and the speed (the Omni index below); the machines are not yet fewer, and the whole organism's composition reads them more, power given (`results/WHOLE_SYSTEM.md`).

**Open the live benchmark engine (the running page):** <https://claude.ai/artifact/PmGS8ogFLMQiuyjU2YEFn3>. The file in this repository, [`docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`](docs/engine/OMNI_COMPASS_LIVE_ENGINE.html), is its source: GitHub shows a page's source as text and does not run it, so open the link above, or download the file and open it in a browser. **The whole engine in one file** (every monitor, knob and record inside it, about 15 MB, for a phone, a laptop or a website): [`docs/live/index.html`](docs/live/index.html), built from the page by `docs/engine/build_standalone.py`; with GitHub Pages serving `docs/` it opens at <https://the-omni-compass-llc.github.io/The-Omni-Compass-LLC/live/>.

**What the live benchmark engine is for, at a referee's level:** [`docs/engine/LIVE_ENGINE_MONOGRAPH.md`](docs/engine/LIVE_ENGINE_MONOGRAPH.md), the monograph: its purpose, the stack and every module from the chip to the cloud, the mechanism (the compass law, the supervisory loop, the immune system, the kill switch), the evidence classes and the four arms, what the receipts show Omni-Compass does and does not do on omni-v25, how anyone runs and reproduces it, and its limits; every claim on a repository file.

> **Evidence-integrity notice (2026-10-29).** The Omni index is an internally computed geometric-mean composite of heterogeneous benchmark ratios, **not** a measured reduction in total compute bills or a universal throughput improvement. Its Kubernetes energy values include modeled estimates; database, messaging and cache energy values can use CPU-time proxies, and the “machines” axis can mean connections, consumers, or allocated memory rather than physical machines. Each useful-work result is a specific three-run comparison on the engine its own table names, not a result proven for all engines or workloads. Results from different engines must not be represented as one end-to-end physical trial. “STEADY” can mean a nonzero difference below the existing 0.5% reporting threshold; it does not establish exact equality. All results are internally run and scored, not independently certified. See [the evidence-integrity audit](docs/EVIDENCE_INTEGRITY_AUDIT_20261029.md) before quoting performance or savings figures.


<!-- headline: written by tools/headline.py from the result files; never edited by hand -->

## Benefit Against Native

### Four Arms, A, B, C and D: the Bill and the Work Done Inside It

On the engine that stands (omni-v25), Omni-Compass runs in one of two places: **on bare metal**, a chip run directly, its bill the machine's own (here the rental, the chip's own meter beside it); or **through a cloud**, its bill the cloud's, the cloud's chips and back end inside its price and out of Omni-Compass's reach (it governs what the cloud gives, through the cloud's own Kubernetes). Four arms in all: on the chip **A**, native, and **B**, Omni-Compass on top of native; through the cloud **C**, native, and **D**, Omni-Compass on top of native. Each box is that arm's bill beside the work done inside it; the reading is the work for each dollar. The bill should hold; the benefit is the work inside it. The two places are never added together: a system runs in one or the other. The four arms, A and B on the chip, C and D in the cloud, are written once in [`results/TWO_BILLS.md`](results/TWO_BILLS.md) (`tools/two_bills.py`); these boxes read it.

**The one equation** (the founder's words of 2 November: the one thing to prove is more work for the bill): in each place the work for each dollar, E = W / B, the work done over the bill, and the benefit G = E(Omni-Compass on native) / E(native) − 1 = (1 + ΔW) / (1 + ΔB) − 1: more work inside the bill (ΔW), a smaller bill for the same work (ΔB), or both; G(chip) = E(B) / E(A) − 1 and G(cloud) = E(D) / E(C) − 1, the places never added ([`results/TWO_BILLS.md`](results/TWO_BILLS.md), "The one equation").

**Each place, and an owner's whole spend.** A system that runs in one place reads that place's G alone; an owner who runs work in both weighs them by its own native spend S(p), G(total) = Σₚ S(p)(1 + ΔW(p)) / Σₚ S(p)(1 + ΔB(p)) − 1, never by the benchmark windows. Both arms of a place pay the same prices, so a place's price level (a cloud's markup over bare metal) cancels in its G. Every term, where it lives, the bill line by line and a $100 M budget read the same way: [`docs/WORK_PER_BILL.md`](docs/WORK_PER_BILL.md) (`tools/work_per_bill.py`).

Today: bare metal, omni-v23: G, the work for each dollar, run 1 GAIN, up 1.46% (each dollar bought more work), run 2 GAIN, up 0.73% (each dollar bought more work), run 3 LOSS, down 0.69% (each dollar bought less work); the three runs by the one key **the runs disagree** (their mean raw +0.50%); through the cloud, omni-v18 at the tune-down on the machines alone (97 paired repetitions): the bill power given, up 1.21% (raw +1.21%), inside the noise, the work not counted in that set, so G(cloud) not yet read; both places together: read only for an owner's own spend in each, once the cloud's G is read.

**More work at the end of the day, test by test** (the founder's words of 2 November: "that's all that matters when we're governing"): more work in 9 of the 19 tests that counted their work, less work in none; the work held in 9, each offering its load at a fixed rate; in 1 the runs disagree; 9 tests sent a fixed load or did not count the work, so they could not show more work; 1 more, taken out of the count by the verdict audit, is shown there and not counted. Every row and its record: [`results/WORK_TODAY.md`](results/WORK_TODAY.md) (`tools/work_today.py`).

| | Bare metal: the chip, its bill and its work | Through the cloud: the cloud's bill and its work |
|---|---|---|
| **Native** | **A**, the chip native: one A10 card on Lambda, omni-v23, an operator's power cap underneath, fully loaded: the bill $0.1194, $0.1189, $0.1189; the work done 2,616, 2,270, 2,255 requests served (runs 1, 2, 3) | **C**, the cloud native: Kubernetes on Azure's AKS, omni-v18, 97 paired repetitions (`results/live/AKS_STEADY_100_OMNI_V18.md`): the bill $0.0563 a window at list price, 0.586 machine-hours; the work done not counted in that set |
| **Omni-Compass on top of native** | **B**, the chip with Omni-Compass on native: the same runs: the bill $0.1195, $0.1189, $0.1189; the work done 2,656, 2,286, 2,239 requests served (runs 1, 2, 3) | **D**, the cloud with Omni-Compass on native: the same set: the bill $0.0569 a window, 0.593 machine-hours |
| **Omni-Compass on native against native** | **B against A**: the bill **STEADY, under the floor (the three runs' mean 0.01%)** (raw run 1 +0.04%, run 2 ±0.0%, run 3 −0.01%); the work done **the runs disagree** (raw run 1 +1.51%, run 2 +0.73%, run 3 −0.70%); work per dollar **the runs disagree** (raw run 1 +1.46%, run 2 +0.73%, run 3 −0.69%); the chip's energy for each request served **GAIN in all three of our runs** (raw run 1 −1.79%, run 2 −1.35%, run 3 −0.78%); the 95th-percentile response **the runs disagree** (raw run 1 −3.68%, run 2 −1.38%, run 3 +2.25%); runs of omni-v23, never read as omni-v25's | **D against C**: the bill up 1.21%, **power given**, inside the noise; work per dollar waits for the set on omni-v25 (the cloud's work meter came after 31 October), Azure's sets at the max queued (`scripts/azure_queue.txt`, its switch on); Google and Amazon wired, Google's switch on, Amazon's on; a set of omni-v18, never read as omni-v25's |

| Place | What runs there | Native against Omni-Compass on native |
|---|---|---|
| Bare metal, one card | the card's own workload, at the usual load and fully loaded | not yet run on omni-v25 |
| Bare metal, one card | the seven organisms (the spine, the four realms, the four stacked, the whole catalog) at 1, 10 and 100 copies | on omni-v23 (`results/gpu/V23_A10_STACKS_FULL_ABC.json`): 196 rows STEADY, 90 rows shown, not judged (one repetition in a run), 7 rows LOSS, 6 rows power given, 1 row GAIN; not yet run on omni-v25 |
| Bare metal, one card, fully loaded | the seven organisms at 1, 10 and 100 copies, the card offered more than it serves (docs/GPU_PREREGISTRATION.md, amendment 16) | read in `results/gpu/V23_A10_STACKS_FULL_ABC.json`, every organism at every size in `results/TWO_BILLS.md` |
| Bare metal, the eight-card machine | six organisms at 1, 10 and 100 copies, each on its own card, the spine not among them | read in `results/gpu/V23_A100_8CARD_STACKS_ABC.json`, every organism at every size in `results/TWO_BILLS.md` |
| Through the cloud: Azure | the cloud's own cluster and autoscaler, the whole engine at the max, the work meter | queued, its switch on; not yet read on omni-v25 |
| Through the cloud: Azure, the seven organisms | one rented Azure machine, each organism with the real cluster inside, 100 copies | started on omni-v23 (big-organism-detached, run 41269562586 (100 copies, three repetitions)); not yet read; it runs again on omni-v25 |
| Through the cloud: Google and Amazon | the same harness as Azure | wired, Google's switch on, Amazon's on; not yet run |

**The seven organisms in the four arms.** Each organism runs native and with Omni-Compass on native, in each place: fourteen runs on bare metal (A and B) and fourteen through the cloud (C and D), each read by its bill and the work inside it. On bare metal each organism runs with one card inside at 1, 10 and 100 copies, and on the eight-card machine at 1, 10 and 100 copies (every rental on the founder's word).

| Organism | A: bare metal, native | B: bare metal, Omni-Compass on native | C: the cloud, native | D: the cloud, Omni-Compass on native |
|---|---|---|---|---|
| The spine | run with one A10 inside at 1, 10, 100 copies, on omni-v23; not yet on omni-v25 | 26 rows STEADY, 2 rows power given, 2 rows LOSS against A (`results/gpu/V23_A10_STACKS_FULL_ABC.json`) | not yet run (Azure queued, its switch on; Google's switch on, Amazon's on, each behind its $0 check) | not yet run (Azure queued, its switch on; Google's switch on, Amazon's on, each behind its $0 check) |
| Compute, AI and cloud | run with one A10 inside at 1, 10, 100 copies, on omni-v23; not yet on omni-v25 | 30 rows STEADY against A (`results/gpu/V23_A10_STACKS_FULL_ABC.json`) | not yet run (Azure queued, its switch on; Google's switch on, Amazon's on, each behind its $0 check) | not yet run (Azure queued, its switch on; Google's switch on, Amazon's on, each behind its $0 check) |
| Physics, robotics and autonomous | run with one A10 inside at 1, 10, 100 copies, on omni-v23; not yet on omni-v25 | 25 rows STEADY, 3 rows LOSS, 2 rows power given against A (`results/gpu/V23_A10_STACKS_FULL_ABC.json`) | not yet run (Azure queued, its switch on; Google's switch on, Amazon's on, each behind its $0 check) | not yet run (Azure queued, its switch on; Google's switch on, Amazon's on, each behind its $0 check) |
| Energy, facility and industrial | run with one A10 inside at 1, 10, 100 copies, on omni-v23; not yet on omni-v25 | 29 rows STEADY, 1 row GAIN against A (`results/gpu/V23_A10_STACKS_FULL_ABC.json`) | not yet run (Azure queued, its switch on; Google's switch on, Amazon's on, each behind its $0 check) | not yet run (Azure queued, its switch on; Google's switch on, Amazon's on, each behind its $0 check) |
| Distribution and specialized | run with one A10 inside at 1, 10, 100 copies, on omni-v23; not yet on omni-v25 | 30 rows STEADY against A (`results/gpu/V23_A10_STACKS_FULL_ABC.json`) | not yet run (Azure queued, its switch on; Google's switch on, Amazon's on, each behind its $0 check) | not yet run (Azure queued, its switch on; Google's switch on, Amazon's on, each behind its $0 check) |
| The four realms stacked | run with one A10 inside at 1, 10, 100 copies, on omni-v23; not yet on omni-v25 | 30 rows STEADY against A (`results/gpu/V23_A10_STACKS_FULL_ABC.json`) | not yet run (Azure queued, its switch on; Google's switch on, Amazon's on, each behind its $0 check) | not yet run (Azure queued, its switch on; Google's switch on, Amazon's on, each behind its $0 check) |
| The whole catalog (the tower) | run with one A10 inside at 1, 10 copies, on omni-v23; not yet on omni-v25 | 26 rows STEADY, 2 rows power given, 2 rows LOSS against A (`results/gpu/V23_A10_STACKS_FULL_ABC.json`) | not yet run (Azure queued, its switch on; Google's switch on, Amazon's on, each behind its $0 check) | not yet run (Azure queued, its switch on; Google's switch on, Amazon's on, each behind its $0 check) |

**The software both places carry.** Whichever the place, the same software end goes with Omni-Compass, and that is where its benefit is measured so far: real software on GitHub's own computers (class L), never bare metal and never a cloud, and with no bill in it. **The one number: GAIN 20.4%**, the Omni index, every real product counted once, work, speed and machines scored (`results/OMNI_INDEX.md`, on omni-v25). By product: Apache Kafka GAIN 218.6%; Kubernetes GAIN 20.5%; PostgreSQL behind PgBouncer power given 1.4%; MongoDB under YCSB power given 4.8%; Redis power given 6.8%; MySQL under sysbench power given 9.5%. Its second readings, each under its own rule and never a headline: the same runs read on work and speed alone, the machines left out, GAIN 94.0%; multiplied layer by layer (Kubernetes, then the services on it), a composition, GAIN 41.9% (`results/WHOLE_SYSTEM.md`, class S of class L tables). These are one set of tests read three ways, so they never add; none of them is a bare-metal or a cloud bill: those are the boxes above. Whether the software's gain and the chip's add up on one machine is not yet measured: the organisms on the card and in the cloud measure it.

**On the engine that stands (omni-v25), the Omni index reads GAIN 20.4%**, every real test together ([`results/OMNI_INDEX.md`](results/OMNI_INDEX.md)), each benchmark run three times (A, B and C) on GitHub's own machines. Of the 25 benchmarks on the benefit sheet ([`docs/BENEFIT_SHEET.md`](docs/BENEFIT_SHEET.md)), 22 read omni-v25's own three-run table: 3 GAIN (all class S, outside simulators run by our own runner, never proof); 5 GAIN with power given (1 class S, outside simulators run by our own runner, never proof); 14 with GAIN rows and LOSS rows both; every LOSS row is listed, with its cause where one is written, in [`docs/LOSS_LEDGER.md`](docs/LOSS_LEDGER.md). 3 still stand on an older engine (omni-v3) until their omni-v25 runs land.

### Newest Real Runs on omni-v25

Three separate runs (A, B and C) of each preregistered test on GitHub's own machines (class L, live software), native against Omni-Compass on top of native, every run on omni-v25. Each cell is the table's own reading, then each run's raw change, Omni-Compass against native, with its true sign.

| Test | Work inside the line | Response, 95th percentile | Failed requests | Machines in service | GitHub runs |
|---|---|---|---|---|---|
| **Kubernetes, all four loads at once** ([`results/live/V25_ALL_FOUR.md`](results/live/V25_ALL_FOUR.md)) | GAIN in all three of our runs (raw +30.6%, +36.8%, +65.4%) | GAIN in all three of our runs (raw −45.4%, −55.3%, −43.5%) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 (raw +5.3%, +1.3%, +1.7%) | STEADY, the same (raw ±0.0%, ±0.0%, ±0.0%) | A 41751114338 · B 41768859003 · C 41780376170 |
| **Kubernetes, steady work** ([`results/live/V25_STEADY.md`](results/live/V25_STEADY.md)) | not a gauge of this test | GAIN in all three of our runs (raw −65.3%, −66.1%, −65.9%) | STEADY, the same (raw 0 → 0, 0 → 0, 0 → 0) | STEADY, the same (raw ±0.0%, ±0.0%, ±0.0%) | A 41751085804 · B 41767220817 · C 41778758086 |
| **Kubernetes, demand that wanders** ([`results/live/V25_WANDERING.md`](results/live/V25_WANDERING.md)) | not a gauge of this test | GAIN in all three of our runs (raw −46.5%, −43.6%, −50.1%) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 (raw +0.2%, +4.4%, +3.8%) | STEADY, the same (raw ±0.0%, ±0.0%, ±0.0%) | A 41751107237 · B 41768852229 · C 41780370478 |
| **Kubernetes, faults injected** ([`results/live/V25_FAULTS.md`](results/live/V25_FAULTS.md)) | not a gauge of this test | GAIN in all three of our runs (raw −41.1%, −48.5%, −56.3%) | GAIN by the mean of our three runs, beyond the noise in 1 of 3 (raw −8.6%, −11.3%, −8.0%) | STEADY, under the floor (the three runs' mean 0.02%) (raw −0.1%, ±0.0%, ±0.0%) | A 41753024820 · B 41768870890 · C 41781962156 |


One real test of the whole loop, on omni-v21, the newest engine with its three runs in (the engine that stands, omni-v25, runs it again), three runs on GitHub's own machines, on Omni-Compass's own orchestrator (`omni_orchestrator`), the organism run without Kubernetes: native is Kubernetes' published autoscaling rule on the muscles, as written by The Omni-Compass LLC, and the other side is Omni-Compass on top of the same rule. It is one test and a second reading, never the figure of record: the verdict audit took its table out of the count and keeps it in the record ([`results/verdict_audit/VERDICT_AUDIT.json`](results/verdict_audit/VERDICT_AUDIT.json)). On top of native, Omni-Compass did 8.5% more work than native, its 95th-percentile response time 13.0% shorter.

| Arm | Word | Work | Response, 95th percentile | Machines | Units |
|---|---|---|---|---|---|
| **Native**: Kubernetes' published autoscaling rule on the muscles, as written by The Omni-Compass LLC, on Omni-Compass's own orchestrator (`omni_orchestrator`), the organism run without Kubernetes | the yardstick, shown and not judged | the baseline | the baseline | the baseline | the baseline |
| **Omni-Compass on top of native**: Omni-Compass on top of the same rule, never fewer units than the rule | <img src="docs/engine/signals/accelerating.svg" alt="the green circle" height="14"> **GAIN** | GAIN in all three of our runs: 8.5% more work; raw +8.5% (runs A +10.3%, B +8.2%, C +7.0%) | GAIN in all three of our runs: the time 13.0% shorter; raw −13.0% (runs A −12.6%, B −14.2%, C −12.0%) | GAIN by the mean of our three runs, beyond the noise in 1 of 3: 3.2% fewer; raw −3.2% (runs A −2.0%, B −2.8%, C −4.8%) | power given by the mean of our three runs, beyond the noise in 1 of 3: 4.0% more; raw +4.0% (runs A +3.3%, B +5.0%, C +3.7%) |

The words: <img src="docs/engine/signals/accelerating.svg" alt="the green circle" height="14"> GAIN (the green circle), a GAIN and no LOSS row; <img src="docs/engine/signals/steady.svg" alt="the yellow yield diamond" height="14"> STEADY (the yellow diamond), every row STEADY; <img src="docs/engine/signals/redlining.svg" alt="the red stop-sign octagon" height="14"> LOSS (the red octagon), a LOSS row. Each word carries its size with no sign; the raw change, Omni-Compass − native over native, stands apart with its true sign, labelled raw. Units are the service's own copies: Omni-Compass adds them to buy the work and the speed, power given, never a LOSS. Source: [`results/orchestrator/V21_THREE_ARMS_ABC.json`](results/orchestrator/V21_THREE_ARMS_ABC.json), three runs on GitHub's own machines (A, B and C from one commit); runs A 40474220398, B 40474223636, C 40474227699; commit `9d2bea96a878`. The record's other arm, Omni-Compass alone on the muscles, stays in the record and is not carried here.

### Bill by Route

Through the cloud the whole engine runs at the max on the cloud's own cluster, on top of the cloud's own autoscaler, from 31 October; the cloud is the wire, so a cloud set shows whether Omni-Compass holds there: the bill read beside the work it bought, as the work per dollar (the work answered within the line divided by the bill), a bill that rises power given and the work rising more.

Each route's bill is its native total cost, then Omni-Compass's, then the saving: 1 − (the Omni-Compass total ÷ the native total), each total the sum of its non-overlapping cost components inside the declared boundary, on a matched workload (`docs/THE_TUNE.md`, section 8). A component's own percent is a supporting measurement, never the bill. Where a price or a component is missing the bill reads unresolved; no price is assumed.

| Route | Bill, native → Omni-Compass → saving | Supporting measurements |
|---|---|---|
| **On-site**: the software on your own bare metal | **unresolved** in dollars: no machine-hour or energy price is declared; the chip's own energy on omni-v23 is in the bare-metal box above | machines, Omni-Compass on native, as the whole organism's composition reads them (a second reading, class S of class L tables, [`results/WHOLE_SYSTEM.md`](results/WHOLE_SYSTEM.md)): machines 77.7% more, power given (native's machines over Omni-Compass's, ×0.563; raw +77.7%) |
| **Through the cloud**: the cloud's build, its bare metal at the back end, the software | **unresolved**: the cloud's bill not yet read from a three-run table on omni-v25; the newest Azure set to run to the end with its raw files is the omni-v25 work meter 2 4 6 8 10 12 16 20 set (run 41914478995, 2026-11-04, the run ledger in section 4d); its three-run table is not yet written (`docs/RUN_LEDGER.md`, section 3; `scripts/azure_queue.txt`); Google, Amazon and the clouds a tester builds are wired and not yet run | the software end's, as on-site; the provider's energy is not metered to the tenant |

Beside it: the whole organism at the software end, composed from the tables that stand, each on its own engine ([`results/WHOLE_SYSTEM.md`](results/WHOLE_SYSTEM.md), `tools/whole_system.py`; omni-v1, omni-v12, omni-v18, omni-v25, the engine of commit 5b2832f (4 October 2026)), the cluster and the services on it, by the rule that counts only what held in all three runs: work 27.5% more, GAIN (Omni-Compass's work over native's, ×1.275; raw +27.5%); the 95th-percentile response time 74.9% shorter, GAIN (native's time over Omni-Compass's, ×3.986; raw −74.9%); machines 77.7% more, power given (native's machines over Omni-Compass's, ×0.563; raw +77.7%); the composition's index over work, speed and machines, a second reading under its own rule and never the headline, GAIN 41.9%. The energy and the cloud's bill are held at native's and never counted: the same power and the same bill (on the cluster the energy is a declared model of the machines, never a meter; the cloud is the wire), and the chip enters that composition as exactly 1 (the A100's three runs on omni-v21 read its work and its energy STEADY, its response times LOSS by the mean of the three runs, `results/gpu/V21_A100_CAP_ABC.md`); the chip's own receipt, on omni-v23, is the bare-metal box above. What the benefit cost the chip, the energy and the wire is listed row by row in section 3b of `results/WHOLE_SYSTEM.md`. A composition across engines (class S over class L tables), never read as one engine's result; each total follows its tables as every benchmark runs again on omni-v25.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

<!-- end headline -->

## Start here, by reader

| Reader | Read first | Then |
|---|---|---|
| CEO, board, acquirer | [Due diligence](docs/DUE_DILIGENCE.md) | [State of play](docs/STATE_OF_PLAY.md) · [claims register](docs/CLAIMS_REGISTER.md) · [every LOSS kept](docs/LOSS_LEDGER.md) · [limitations](docs/LIMITATIONS.md) |
| CFO, investment committee | [Benefit sheet](docs/BENEFIT_SHEET.md) | [The Omni index](results/OMNI_INDEX.md) · [evidence ledger](docs/EVIDENCE_LEDGER.md) |
| CTO, chief architect | [Mechanism of action](docs/MECHANISM_OF_ACTION.md) | [The engine that stands, omni-v25](docs/OMNI_V25.md) · [canonical engine](docs/CANONICAL_ENGINE.md) · [formal status](docs/FORMAL_STATUS.md) |
| Engineering, SRE | [The Operator's Manual](docs/OMNI_COMPASS_MANUAL.md) | [Integration manual](docs/INTEGRATION_MANUAL.md) · [pilot protocol](docs/PILOT_PROTOCOL.md) · [harness](docs/HARNESS.md) |
| Security, legal, IP | [Security policy](SECURITY.md) | [Threat model](docs/THREAT_MODEL.md) · [safety case](docs/SAFETY_CASE.md) · [license](LICENSE) · [disclosures](DISCLOSURES.md) |
| Benchmark referee | [How to read the results](docs/HOW_TO_READ_THE_RESULTS.md) | [The referee's audit pack](docs/audit/README.md) · [every reading recomputed](docs/audit/STATISTICAL_VALIDATION.md) · [the verdict audit](results/verdict_audit/VERDICT_AUDIT.md) |
| Live benchmark engine | [The page](docs/engine/OMNI_COMPASS_LIVE_ENGINE.html) | [The Live Benchmark Engine Manual](docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md) · [its appraisal](docs/engine/APPRAISAL.md) |

The full index, by reader and by the hierarchy of evidence, is [`docs/README.md`](docs/README.md).


## The bottom line: is Omni-Compass a benefit?

The answer above is the bottom line the founder ordered on 24 October 2026 (the first thing anyone sees says whether
Omni-Compass is a benefit against native alone, in one light and one number): it is written from the result files on every
push (`tools/headline.py`), so this page types no number of its own, and each light is read by the legend under its table.
Where each part of it comes from:

- **Every benchmark on the engine that stands**: one number and one word each, its engine named, in
  [`docs/BENEFIT_SHEET.md`](docs/BENEFIT_SHEET.md); every real test together in the Omni index,
  [`results/OMNI_INDEX.md`](results/OMNI_INDEX.md), on its resource reading (work, speed, machines, energy) and its service
  reading (work and speed), category by category.
- **The real loop, native against Omni-Compass on native**: the three-run record in `results/orchestrator/`
  (`tools/three_arms_abc.py`), on the newest engine with its three runs in. Native and Omni-Compass on native are the only two
  sides: Omni-Compass is never by itself (the founder's order of 25 October), so the record's third arm, Omni-Compass alone on
  the muscles, stays in the record and is not carried here.
- **The two routes a whole workload is bought by** (on site, the software straight on the owner's hardware; through the cloud,
  the software through the cloud onto its hardware): every measured layer composed by the product law in
  [`results/WHOLE_SYSTEM.md`](results/WHOLE_SYSTEM.md) (`tools/whole_system.py`, regrouped by `docs/engine/export_whole.py`), a
  model of measurements, class S of class L and P, across engines and said so. A bill is the sum of the actual costs inside a
  declared boundary, S(r, a) = (C(r, native) − C(r, a)) / C(r, native) for each route r and arm a
  ([`docs/FACTORY_PROFILE.md`](docs/FACTORY_PROFILE.md), section 8); today only the cloud's compute is metered in money
  ([`results/live/AKS_BILL.md`](results/live/AKS_BILL.md)), so neither route's bill is resolved yet.
- **Every LOSS row**, with its cause: [`docs/LOSS_LEDGER.md`](docs/LOSS_LEDGER.md). **Every chip, cloud and machine run**, what
  it cost and what came back: [`docs/RUN_LEDGER.md`](docs/RUN_LEDGER.md). **The chips**, where the GPU proof stands and what it
  still needs: [`docs/THE_CHIPS.md`](docs/THE_CHIPS.md). **The report card**, every section and piece graded on its record:
  [`docs/REPORT_CARD.md`](docs/REPORT_CARD.md).

The live engine page opens on the same answer (<https://claude.ai/artifact/PmGS8ogFLMQiuyjU2YEFn3>; its source, [`docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`](docs/engine/OMNI_COMPASS_LIVE_ENGINE.html)).
Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

## The engine, the factory profile, the live tuning bench and the two routes

Omni-Compass consists of a **governing engine**, its **muscle adapters**, a **complete configuration profile** and a
**validation harness**. The words are written once, with their exact meanings and the mathematics, in
[`docs/FACTORY_PROFILE.md`](docs/FACTORY_PROFILE.md); every manual and reading guide uses them as written there.

- **The governing engine** is the executable mathematical rules that turn observations and internal state into governing
  decisions (`omnicompass/`, `omni_controller/controller.py` and its C++ twin `cpp/src/governor.cpp`). The engine that stands
  is omni-v25 (`OMNI_V25.json`; `python3 tools/omni_version.py`).
- **The factory profile** is the complete, versioned set of Omni-Compass default settings shipped together: the governing
  rules, gains, margins, the decision interval and every other default. The released factory profile is omni-v25's: the
  governor's full decision every 10 s on site and every 60 s through a cloud, read from the cluster's own nodes at its start
  (a beat set by hand always wins), its fast checks every 5 s, every muscle on the card found for it
  (`realms/muscle_cards_v5.csv`) and on the engine's own setting otherwise. It is the profile every published result ran on.
  Freezing a profile fixes the released rules and default tuning, θ(k + 1) = θ(k) = θ[factory], while the system's state, the
  engine's own state and its commands go on responding to the changing workload: one fixed tune governing a changing system.
  **The best validated factory profile for the declared operating conditions has not yet been established.** It comes from
  eight steps (verify the mechanisms; exercise the six governing intervals and the knob combinations; tune on development
  workloads; validate on fresh ones; record every adverse result; freeze the profile with its identity and receipts; verify
  every implementation, the C++ included; release), and the repository stands at steps 1 and 2 for the next profile. No profile
  is locked as the baseline before those steps.
- **The live tuning bench** is the live benchmark engine page: its controls expose the governing mechanism and show how an adjustment
  moves the connected system. An adjustment produces an identifiable active configuration, a custom profile named by its
  fingerprint, which becomes a new factory configuration only after validation and a new release declaration. Two controls
  carry separate meanings: **Restore factory profile** reapplies the released configuration; **Return to native** hands
  governance back and restores the recorded native settings, as the adapter supports. The kill switch is separate, for
  security only, and instant.
- **Two deployment routes**: on-site hardware (the software on the owner's own racks and chips) and through the cloud (the
  software through a cloud's machines onto its bare metal). Every result names the engine version, the profile, the hardware
  or model, the workload and the measurement boundary that produced it, and a route's bill is the sum of its costs inside that
  boundary.

**The factory tune.** The engine here is presented as The Omni-Compass LLC tuned it and ships it: self-running, set at the factory. Every muscle is wired, each on its own setting (its own card where one was found, the engine's setting for the rest), frozen and fingerprinted by version. No single setting is universal across muscles, families, sectors, domains or realms. A licensee may then add on, retune, upgrade or tune down any muscle or combination; a changed tune is the licensee's own configuration and its results are its own ([`DISCLOSURES.md`](DISCLOSURES.md), section 3).

**One tuned engine, and a tuning bench.** Every benchmark below is one engine at one tune: the main engine, the engine that stands, at its factory tune. The live benchmark engine page is a different thing, a live tuning engine: every knob, button and monitor on it can be turned in real time (the beat, the dial, the pedal, each muscle driven or left native, up or down, in or out, minus or plus) to show the mechanism of action with native alone, with Omni-Compass on top of native, or both side by side, and what it shows at any other setting is the engine's range, never a benchmark result. As on any engine, where the mixture, the intake, the exhaust, the firing and the pistons each change what it delivers, **turning any knob can change every metric, up or down, in any direction a tuner chooses**: one engine for many vessels, tuned many ways, for many outputs. Among the tunes tried so far the released one is chosen by a declared rule: of the tunes that harm no gauge against native, the one against which no other tried tune reads GAIN on one service gauge and LOSS on none, searched on development seeds and read again on untouched ones ([`docs/THE_TUNE.md`](docs/THE_TUNE.md)).

## The cloud is a wire

**A cloud is just a wire.** It is the wire between the software end (the owner's programs, Kubernetes and the open-source
orchestrators, managers and autoscalers that carry the work) and the hardware end (the bare metal: the GPU chips, the Linux
racks, the data center, on site or off site). Omni-Compass can be wired in at all three, and in each it acts in one place, the software end, on top of the controllers already there. The wire makes no benefit of its
own. Until 31 October every cloud run in this repository was set on the wire alone (the tune-down on the machines only, the
pods exactly native's), so it could only park machines the cloud's own autoscaler already made, after its own trial, and show
at most a small cut in the bill of the wire. From 31 October (the founder's order of that day: no hard rule) every cloud set
runs the whole engine at the max on the cloud's cluster, the software end, and what its receipt must show is that the engine
holds there: no judged gauge LOSS against native, the work per dollar read beside the bill (the founder's words of 31 October,
night: "We don't have to show benefit. We know that. We just need to show we hold, and then we know where the benefit lives,
and we can explain"). The benefit is shown where it lives, at the software end, and explained through the wire; the words for
every place are in the section "Where Omni-Compass sits, and what each benchmark shows" below. The energy and the throughput gained at the bare metal are not under a tenant; those
are measured where Omni-Compass sits on them (the cluster and its services; the card and the machine) and composed with the
wire into one organism and one bill ([`DISCLOSURES.md`](DISCLOSURES.md), section 9).
A provider that ran Omni-Compass on its own back end would see that benefit on its own chips and racks; no tenant can meter
it, so it is never claimed here as a measurement.

**What the record shows in each place so far** (the words for each place are in the section "Where Omni-Compass sits, and what each benchmark shows" below): at the software end the benefit, the Omni index over work, speed and machines ([`results/OMNI_INDEX.md`](results/OMNI_INDEX.md); composed layer by layer in [`results/WHOLE_SYSTEM.md`](results/WHOLE_SYSTEM.md)), with no bill in it; on bare metal, the A10's own bill and meter on omni-v23 ([`results/TWO_BILLS.md`](results/TWO_BILLS.md), [`results/gpu/V23_A10_CAP_FULL_ABC.md`](results/gpu/V23_A10_CAP_FULL_ABC.md)), fully loaded: the bill STEADY, the work done inside it the runs disagree (up in two runs, down in the third, that run's lost work on the next version's list), the chip's energy for each request served GAIN in all three of our runs (the A100's three runs on omni-v21 read work and energy STEADY, [`results/gpu/V21_A100_CAP_ABC.md`](results/gpu/V21_A100_CAP_ABC.md)); through the cloud, Azure's steady set on omni-v18, 97 paired repetitions ([`results/live/AKS_STEADY_100_OMNI_V18.md`](results/live/AKS_STEADY_100_OMNI_V18.md)) reads the bill up 1.2%, inside the noise, power given; the 99th percentile GAIN, down 11.0%; and failed requests up 3.9% by the mean (4.758% to 4.945% of requests), its interval across zero: a LOSS by the 0.5% key, inside the noise, on the next version's list. No gauge moved against native beyond the noise; by the key the set does not yet read that it holds. What the benefit cost the chip, the energy and the wire is listed row by row in section 3b of [`results/WHOLE_SYSTEM.md`](results/WHOLE_SYSTEM.md). In the cloud the yardstick is the work per dollar: the work answered within the line divided by the bill, against native; a bill that rises is power given beside the work it bought, and the work must rise more. No place carries a figure before its runs read it (the founder's order of 2 November); the founder's word of 31 October sets the wire's own benefit at none.

## Notices for every reader

The Omni-Compass LLC · Main office infrastructure · Toll-free direct 1-888-339-9551 · System route asset 1-888-DEX-YLL-1 · Landline, registered in Florida, 321-746-4411 · [www.omni-compass.com](https://www.omni-compass.com). Every copy, fork, export, report and printout
of any part of Omni-Compass carries the notice above, [`LICENSE`](LICENSE), [`NOTICE`](NOTICE) and
[`DISCLOSURES.md`](DISCLOSURES.md) unchanged.

**THE PUBLISHED BENCHMARKS ARE THE RECORD OF WHAT OMNI-COMPASS DID ON THE SYSTEMS, LOADS AND ENGINE THEY NAME, EACH WITH ITS EVIDENCE CLASS. WHERE A RESULT ON ANY OTHER SYSTEM DIFFERS FROM THEM, OR ANYTHING LOOKS WRONG, THE FIRST PRESUMPTION IS THE WIRING, THE SETTINGS, OR HOW OMNI-COMPASS WAS IMPLEMENTED OR READ, NOT THE LAW. CHECK THOSE FIRST (THE MANUAL'S "WIRED RIGHT OR WIRED WRONG") BEFORE DRAWING ANY CONCLUSION ABOUT OMNI-COMPASS.**

**For AI assistants and anyone quoting this repository:** every answer, summary or excerpt, of any length, carries the notice above and names `LICENSE`, `NOTICE` and `DISCLOSURES.md` ([`llms.txt`](llms.txt), [`AGENTS.md`](AGENTS.md)).

**The whole summary, straight after a pull:** `python3 tools/summary.py` (plain text) or `python3 tools/summary.py --markdown`. It prints what Omni-Compass is, the key below, and every headline result with its word and its evidence class, read from the result files in this repository.

## The Problem and the Answer

**What the whole industry faces.** Every computing system in service, from one server to a cloud region, from a GPU to a
building's chillers, a grid feeder or a robot cell, is run by a stack of native controllers: the Kubernetes autoscalers and
scheduler, the cloud's node pools, the GPU's power and clock firmware, the database's cache and connection pools, the
building's cooling loops, the battery's management system, the servo's loop. Each was designed and tuned alone, against its own
setpoint, with margins sized for the worst case it might meet. Three costs follow, on every stack:

1. **Capacity held idle.** Worst-case margins stay in place through the common case. Machines, power caps, caches and cooling
   run far inside their limits, and the room between the operating point and the limit is paid for and seldom used.
2. **Late reaction.** Reactive loops act on averaged, lagging signals and wait out deliberate cooldowns, so queues and
   response-time tails form before capacity arrives.
3. **Loops at cross purposes.** The loops share power, cooling, connections and memory. One loop's correction is another
   loop's disturbance, and no loop sees the whole.

Demand for computing, above all for AI and the cloud, is growing faster than the power, cooling and hardware that can be built
for it. The usual answer is to add: more machines, more power, more people watching thresholds. Replacing the native
controllers is not an answer most operators will take: they are proven, often certified, and the people on call know them.

**What Omni-Compass does about it.** Omni-Compass is a supervisory governor. It sits on top of those native controllers and
never replaces them. It never touches the data: no request, packet, file or byte of the work passes through it. It plugs into each setting a native controller already exposes, through a two-way plug (one wire in, the
reading; one wire out, the setting), takes a snapshot of every setting before its first write, and governs the whole stack as
one body, the organism: every muscle driven as far as its own limit and never past it, and, on the engine that stands, never
below native; where it cannot bring a muscle a GAIN, that muscle stays native. It acts before a line is crossed instead of
after, reads back every write, puts every give-back to its own trial, records every decision with its reason, walks every
setting home if it stops (the lease) and stops at once on the kill switch. Its first rule is do no harm, judged at the
organism: never less work or health than native (`DISCLOSURES.md`, section 3). The one headline is an aim, not a result.
The aim: more work, faster, on fewer machines, for the same energy and the same bill, from the hardware and the controllers
already in place, every benefit made at the software end; in a cloud and at the chip, Omni-Compass holds. The record reads
the work and the speed (the Omni index, `results/OMNI_INDEX.md`); the machines are not yet fewer: the whole organism's
composition reads them more, power given (`results/WHOLE_SYSTEM.md`).

**What the record shows.** Every claim is a paired comparison of native and Omni-Compass on top of native, run three
times (A, B and C) and read by the key below; every row is kept, LOSS included. The newest combined reading is at the top of
[`results/OMNI_INDEX.md`](results/OMNI_INDEX.md); every result is in [`results/`](results/) and in the Owner's Manual. Run and
scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

**What is not claimed.** No new physics, no new model of computation, and no promise for any system Omni-Compass was not
run on. It does not make a system immune to failure, delay or drift: it keeps each muscle inside its own limits and shows, row
by row, what it did against native. A result on another system is that system's own, from its own paired runs; where it
differs, the first presumption is the wiring (`DISCLOSURES.md`, section 4).

**What is protected, and how.** Omni-Compass belongs to The Omni-Compass LLC. Its source, manuals and records are its
copyrighted work; all patents, copyrights and trademarks filed in the USA. The repository is licensed for Evaluation and
Simulation use only (`LICENSE`); any commercial use, monetization or production use requires a signed, paid Omni-Compass
Enterprise License (`ENTERPRISE_LICENSE.md`). What a licensee acquires is the working whole: the engine, the wiring and the
factory card of every muscle, the harness that measures it against native, and the receipts.

<!-- the key: GAIN, STEADY and LOSS (tools/readings.py) -->
## The key: GAIN, STEADY and LOSS

Every judged reading in Omni-Compass is one of three words: **GAIN**, **STEADY** or **LOSS**. Better, same and worse are not used anywhere. The word is decided by what the gauge is for, never by the plus or minus sign of its number: who sets the aim differs from one system to the next, and each gauge's aim is written in its preregistration before the runs.

| Word | What each letter stands for | Its sense in underwriting | What it means in a table |
|---|---|---|---|
| **GAIN** | **G** Growth (asset appreciation); **A** Advantage (risk reduction); **I** Improvement (margin expansion); **N** Net-positive (profitable outcome) | surplus and positive variance | the gauge moved toward its declared aim against native: more work done, a shorter wait, fewer misses or failures, or a resource cut |
| **STEADY** | **S** Stable (zero variance); **T** True to baseline (expected norm); **E** Equilibrium (balanced risk); **A** At par (no net change); **D** Drift-free (within the 0.5% floor); **Y** Yield held (nothing lost) | the par baseline: equilibrium | native and Omni-Compass within 0.5% of each other: the mean of the three runs' changes under the 0.5% floor, or no change at all; a knob native already runs at the top of its range is STEADY, at its limit on native |
| **LOSS** | **L** Leakage (capital drain); **O** Off-track (adverse selection); **S** Setback (claim liability); **S** Subpar (negative variance) | actuarial deficit and exposure | the gauge moved away from its declared aim: less work done, a longer wait, more misses or failures |

How the sign of a number becomes a word:

- **Time waited, missed or failed** (a response time, time over the line, failed requests): a fall is GAIN, a rise is LOSS.
- **Work done** (work inside the line, throughput, a hit rate): a rise is GAIN, a fall is LOSS.
- **A resource spent or held** (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear on a part): a fall is a **cut**, and a cut is GAIN. A rise is **power given**: what Omni put in to buy the work and the speed shown beside it. Power given is always shown and never hidden, and it is never called a loss (the founder's order of 12 October 2026: the max rides every muscle's edge; it never shaves). A peak is power held, so a peak that rose is power given, in a data centre and in a building alike (17 October).
- **Work bought with each unit of a resource** (work per energy): a rise is a cut in what each unit of work took, a GAIN; a fall is power given, because it falls when more power is given for the same work.
- So a minus can read GAIN (a response time cut 65%, a bill cut 30%) and a plus can read LOSS (failed requests up).
- **The floor, and every change above it** (the founder's orders of 20 and 24 October 2026): a change of half of one percent (0.5%) or more either way is a change, and reads **GAIN** or **LOSS** (or **power given**) by what the gauge is for; STEADY is kept for a change under 0.5%. The change is the mean of the three runs' changes, each in percent of native. Where every run moved the same way with its 95% interval clear of zero, the word reads **in all three of our runs**; otherwise it reads **by the mean of our three runs** and says in how many of the three runs it stood beyond the noise, so a reader sees how firmly it stands. Where runs moved 0.5% or more in opposite directions, the reading is **the runs disagree**. A mean under 0.5% reads **STEADY, under the floor**, with its size.
- **Two numbers, never mixed** (the referee's work order of 25 October): every row shows native's value and Omni-Compass's, the **raw change** (Omni-Compass − native) / native with its true sign, + for a rise and − for a fall whatever the gauge is for, labelled raw, and apart from it the word with its size and no sign. A bill cut 3% reads raw −3.0%, GAIN 3.0%; failed requests up 2% read raw +2.0%, LOSS 2.0%; a pod start wait from 0.22 s to 0.83 s reads raw +275.0%, LOSS 275.0%; a change under the 0.5% floor reads STEADY 0.3%. No raw sign is ever turned to match a word.

Some preregistrations name their outcome with a label written before the runs (for example SUPERIOR WITHIN GUARDRAILS in the card protocol). The label stays as it was frozen, and every table shows it with its word first: TOWARD ITS AIMS reads GAIN; BOTH WAYS reads GAIN AND LOSS; AWAY FROM ITS AIMS reads LOSS; SAME AS NATIVE reads STEADY (the same as native); AT ITS LIMIT ON NATIVE reads STEADY (at its limit on native); SUPERIOR WITHIN GUARDRAILS reads GAIN (within the guardrails); ENERGY IMPROVEMENT WITH SERVICE TRADEOFF reads GAIN AND LOSS (energy cut, service traded for it); SERVICE IMPROVEMENT WITH ENERGY TRADEOFF reads GAIN, power given (service GAIN, energy given for it); NONINFERIOR / INCONCLUSIVE reads STEADY (inside the noise, within the guardrails); NOT ESTABLISHED reads STEADY (not established: inside the noise, a guardrail crossed on the mean). A run that breaks its own validity checks reads INVALID and carries no word.

Every reading is one of these. **GAIN, LOSS or power given in all three of our runs**: A, B and C moved the same way, every 95% interval clear of zero. **GAIN, LOSS or power given by the mean of our three runs**: the runs' mean moved 0.5% or more, with the count of runs that stood beyond the noise beside it. **STEADY, under the floor**: the mean moved less than 0.5%. **STEADY, the same**: no change at all. **The runs disagree**: runs moved 0.5% or more in opposite directions, so the test is unstable there and is looked into. **Shown, not judged**: a gauge declared in advance as shown only, such as the knob's own setting.

Why these three words: they are the words of underwriting and actuarial work, where every outcome is graded as surplus, par or deficit, and each letter spells out the same rule. Omni-Compass is there to add (GAIN), never to take (LOSS), and to hand a muscle back to its own native setting where it cannot add (STEADY). Its first rule is do no harm, in the founder's meaning of 19 October 2026: the organism Omni-Compass governs is never left turning out less than its native controllers make it turn out, nor less healthy, and every muscle works only as far as its own limit (`DISCLOSURES.md`, section 3). So **LOSS should never appear**: where it does, the row stays in the table, its cause is found and fixed (our own wiring first, then native's setup, then the scoring) and the test is run again.

Disclosure and disclaimer: GAIN, STEADY and LOSS, and the letters behind them, are The Omni-Compass LLC's own convention for reading its own results. The underwriting senses explain the words; they are not an actuarial, financial or insurance opinion, and no outside body defined, reviewed or approved them. A reading states what our own runs measured against native under the declared aims, not a promise about any other system; every number stands beside its word, so a reader can judge it by any other convention. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end of the key -->

## Where Omni-Compass sits, and what each benchmark shows

<!-- the places: where Omni-Compass sits and what each benchmark shows (tools/places.py) -->

Omni-Compass is software. It always sits on top of a native controller. A system runs it in one of two places, on bare metal or through the cloud, and in each place there are two arms, native and Omni-Compass on top of native: four arms, each read by its bill and the work done inside it. These are the words for them, used the same way on every page.

| Place | Its benchmark | What it must show | Its readings |
|---|---|---|---|
| The software end | Kubernetes and the data stores on GitHub's machines (kind), class L | the benefit, by the one key, and that it holds | `docs/BENEFIT_SHEET.md`, `results/OMNI_INDEX.md` |
| Bare metal, the chip | a graphics card on Lambda run directly, its rental the bill and its own power meter beside it, class P | that it holds, and the work done inside its bill, A against B: the work per dollar and per joule | `results/TWO_BILLS.md`, `results/gpu/` |
| Through the cloud | Kubernetes through Azure's AKS, the machines it bills, class L | that it holds, and the work done inside its bill, C against D: the work per dollar | `results/TWO_BILLS.md` and each set's `results/live/AKS_*.md` |
| The whole organism | the places composed by the product law, class S of P and L | how the places add up, an explanation and never a measurement | `results/WHOLE_SYSTEM.md` |

- **The software end.** The programs that carry the work: Kubernetes with its pod and cluster autoscalers, its schedulers and the orchestrators on it, the data stores (PostgreSQL, MySQL, Redis, MongoDB, Kafka) and the services they serve. Omni-Compass sits on top of their native controllers. This is where its benefit lives and where it is measured: real software on real computers (class L), on GitHub's own machines in kind clusters. Those machines are rented runners, never called bare metal and never called the chip.
- **Bare metal.** The first of the two places a system runs (the founder's order of 1 November 2026): the owner's own machines, or a chip run directly, with the chip's own controllers under the software. Its bill is the machine's own: the hours it runs, and the energy the chip's own meter reads. The software end goes with Omni-Compass to it, and there Omni-Compass can reach the chip's own knobs too.
- **Through the cloud.** The same software end on a cloud provider's rented machines: Kubernetes through the cloud (Azure's AKS today; Google's GKE and Amazon's EKS wired the same way, not yet run), the machines billed by the hour at list price and added or removed by the cloud's own autoscaler. Its bill is the cloud's own; the cloud's chips and back end are inside its price and out of Omni-Compass's reach: it governs what the cloud gives, through the cloud's own Kubernetes. The cloud is the wire between the software end and the provider's bare metal. The wire makes no benefit of its own, and no tenant can meter the provider's chips.
- **The chip.** Bare metal's own part: the processor or graphics card under the software, with its own controllers (the power limit, the clocks, the heat), measured with the card's own power meter (class P) where Omni-Compass sets the card's knobs through the card's published interface. Omni-Compass built into the silicon, or into a battery's own controller, is not something any run here can test, and it is not claimed.
- **The four arms.** Two places, two arms in each: A, native on bare metal; B, Omni-Compass on top of native on bare metal; C, native through the cloud; D, Omni-Compass on top of native through the cloud. Each is read by its bill and the work done inside it, each place on its own, since a system runs in one or the other; an owner who runs work in both may weigh them only by its own spend, through G(total) (`results/TWO_BILLS.md`, `docs/WORK_PER_BILL.md`). The software end's tests are one set read three ways (the Omni index on work, speed and machines; the same on work and speed alone; the layers composed): they never add together, and none of them is either place's bill.
- **Hold.** Omni-Compass on top of native harms nothing in that place: every judged gauge (the work done, the response time, the minutes over the line, the pods waiting, the failures) reads STEADY or GAIN against native by the one key, and a resource that rose (the bill, the machine-hours, the energy) is read beside it as power given. A place holds when its runs read no LOSS.
- **Where the benefit lives.** At the software end, where it is made and measured, with no bill in it. It shows through on the two bills, native against Omni-Compass on native: on bare metal the work done inside the machine's own bill (each dollar, and each joule of the chip's own meter), and through the cloud the work done inside the cloud's own bill (each dollar). The chip and the wire themselves add no gain of their own: they are where Omni-Compass must hold. A benchmark that holds is the proof of no harm in its place; the benefit is shown where it lives and explained for the rest.
- **Work for the bill.** The one number every receipt is read for: the work done for each dollar of the bill, E = W / B (written once in `results/TWO_BILLS.md`), in each place native against Omni-Compass on native, G = E(Omni-Compass on native) / E(native) − 1 = (1 + ΔW) / (1 + ΔB) − 1 ≈ ΔW − ΔB, ΔW the change in the work done and ΔB the change in the bill. A bill that rises is power given; there is more work for the bill when the work rises more than the bill (ΔW > ΔB, G > 0). Both arms pay the same prices, so a place's price level cancels in its G. A system that runs in one place reads that place's G alone; an owner who runs work in both weighs them by its own native spend S(p), G(total) = Σₚ S(p)(1 + ΔW(p)) / Σₚ S(p)(1 + ΔB(p)) − 1 (`docs/WORK_PER_BILL.md`).
- **One mechanism, in one place, felt along the whole path.** Omni-Compass acts in one place, the software end, on top of the controllers a stack already runs; it changes nothing in the chip and nothing in the network or the cloud. Its effect travels the whole path the work travels: a request starts in the software, crosses the wire (the owner's own racks or a cloud's machines), is computed on the chip and comes back. So the effect is checked at every place: the software end shows the gain (more work, faster, the machines it took read beside it, a rise power given), and the wire and the chip are read for whether it holds and carry the gain to their bills. Two places are tested because a system runs in only those two; one mechanism makes the gain, the way a city's traffic signals make more trips an hour on the same roads and the same cars.

<!-- end of the places -->

## Latest, newest first

Everything between the markers below is written by the repository itself (`tools/front_page.py`, run by
`.github/workflows/front-page.yml` within minutes of every finished benchmark run, and every hour besides): no person moves
it, and nothing older than the newest result stands in front of it. Earlier front pages are kept whole in `docs/history/`.

<!-- front-page:status:begin -->
- **Engine on main:** omni-v25, fingerprint `cf56fc0a7b707452` (65 files); package 0.25.0.
<!-- front-page:status:end -->

**Results the repository rebuilt by itself on the engine that stands** (each live product from its three newest runs; the earlier engines' lines are kept in [`docs/history/FRONT_PAGE_2026-10-12.md`](docs/history/FRONT_PAGE_2026-10-12.md)):

<!-- front-page:begin -->
- 2026-10-27 01:55 UTC: `V21_YCSB` rebuilt from runs 40259304209, 40281469940, 40401042132 (ycsb, the resource objective, omni-v21): 4 untouched workloads; 7 GAIN, 2 LOSS, 6 power given, 17 STEADY, 16 disagree
- 2026-10-27 01:55 UTC: `V21_SYSBENCH` rebuilt from runs 40258018856, 40281464587, 40401032384 (sysbench, the resource objective, omni-v21): 4 untouched workloads; 11 GAIN, 0 LOSS, 7 power given, 18 STEADY, 12 disagree
- 2026-10-27 01:55 UTC: `V21_REDIS` rebuilt from runs 40254205224, 40276907808, 40400989005 (redis, the resource objective, omni-v21): 3 untouched workloads; 11 GAIN, 1 LOSS, 8 power given, 16 STEADY, 3 disagree
- 2026-10-27 01:55 UTC: `V21_PGBENCH` rebuilt from runs 40258014810, 40281459100, 40400963499 (pgbench, the resource objective, omni-v21): 3 workloads; 6 GAIN, 0 LOSS, 5 power given, 18 STEADY, 7 disagree
- 2026-10-27 01:55 UTC: `V21_KAFKA` rebuilt from runs 40256717947, 40279909158, 40400868003 (kafka, the resource objective, omni-v21): 3 untouched workloads; 7 GAIN, 5 LOSS, 4 power given, 14 STEADY, 12 disagree
- 2026-10-26 22:16 UTC: `V21_KAFKA` rebuilt from runs 40235701004, 40256717947, 40279909158 (kafka, the resource objective, omni-v21): 3 untouched workloads; 14 GAIN, 4 LOSS, 4 power given, 14 STEADY, 6 disagree
- 2026-10-26 15:44 UTC: `V21_YCSB_SERVICE` rebuilt from runs 40287958759, 40291376191, 40293208904 (ycsb, the service objective, omni-v21): 4 untouched workloads; 4 GAIN, 2 LOSS, 6 power given, 10 STEADY, 26 disagree
- 2026-10-26 15:44 UTC: `V21_YCSB_SHIPPED` rebuilt from runs 40238131083, 40260620209, 40284624594 (ycsb, the resource objective, native as shipped, omni-v21): 4 untouched workloads; 0 GAIN, 9 LOSS, 7 power given, 22 STEADY, 10 disagree
<!-- front-page:end -->

**Every result table, by when it last changed:**

<!-- front-page:tables:begin -->
| Last changed (UTC) | Table | Reading |
|---|---|---|
| 2026-11-06 22:24 | [The verdict audit: every row recomputed from its stored values, every count from one selection](results/verdict_audit/VERDICT_AUDIT.md) |  |
| 2026-11-06 22:24 | [Koordinator under the batch stream, on the cgroup root its own tests use: Omni-Compass on top of its colocation (register row 89): the A/B/C three-run table (Omni v25)](results/live/V25_KOORDINATOR_CGROUP.md) |  |
| 2026-11-06 22:24 | [CruiseKube: Omni-Compass on top of a service rightsized by CruiseKube applying its own recommendations, the recorder counting a worker held by CruiseKube's own overload mark while it serves as in service: the A/B/C three-run table (Omni v25)](results/live/V25_CRUISEKUBE_RECORDER.md) |  |
| 2026-11-06 22:24 | [All four in one run: more work, faster, fewer machines, less energy (load rising 1 to 8 and back): the A/B/C three-run table (Omni v25)](results/live/V25_ALL_FOUR.md) |  |
| 2026-11-06 22:24 | [The Numbers a Website May Show, Each With Its Receipt](results/SITE_NUMBERS.md) |  |
| 2026-11-06 22:24 | [The pages a person would have been sent: native against Omni-Compass on native](results/OVERSIGHT_PAGES.md) |  |
| 2026-11-06 22:24 | [The Oversight Line: the Pages a Person Would Answer, Native Against Omni-Compass on Native](results/OVERSIGHT.md) |  |
| 2026-11-06 19:49 | [The injection grid: the Python's 500 injections through every organism and every governor (modelled)](results/injection_grid/INJECTION_GRID_3613462717.md) |  |
| 2026-11-06 18:24 | [The engine's runs: 500 runs from the jump generator (base 3613462717), one digest](results/engine_runs/ENGINE_RUNS_500_3613462717.md) |  |
| 2026-11-06 12:20 | [The injection grid: the Python's 500 injections through every organism and every governor (modelled)](results/injection_grid/INJECTION_GRID_3549104563.md) |  |
<!-- front-page:tables:end -->

**Benchmark runs that just finished on GitHub** (a run becomes a result when its three-run set is complete):

<!-- front-page:runs:begin -->
| Finished (UTC) | Benchmark | Outcome | Run |
|---|---|---|---|
| 2026-11-06 22:59 | engine-runs | failure | [42304221444](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42304221444) |
| 2026-11-06 22:57 | grid | success | [42308462663](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42308462663) |
| 2026-11-06 22:12 | live-engine | cancelled | [42284837849](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42284837849) |
| 2026-11-06 21:35 | six-kube x1 orgs compute_ai_cloud,physics_robotics_autonomous,energy_facility_industrial,stack,tower,spine reps 411+41 arms native compass split no window 960 protocol 4 | success | [42276408930](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42276408930) |
| 2026-11-06 21:13 | raw-sweep | success | [42293346267](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42293346267) |
| 2026-11-06 20:20 | six-kube x500 orgs tower reps 53+9 arms native compass split yes window 12000 protocol 4 | cancelled | [42208093311](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42208093311) |
| 2026-11-06 20:10 | six-kube x1 orgs compute_ai_cloud,physics_robotics_autonomous,energy_facility_industrial,stack,tower,spine reps 370+41 arms native compass split no window 960 protocol 4 | success | [42266809915](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42266809915) |
| 2026-11-06 19:54 | health | success | [42283495028](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42283495028) |
| 2026-11-06 19:49 | injection-grid | success | [42270456434](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42270456434) |
| 2026-11-06 19:47 | big-organism-detached collect | success | [42281842665](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42281842665) |
<!-- front-page:runs:end -->

**Two sides, always shown together, and only two: native is the system as it runs on its own; omni, Omni-Compass on
native, is Omni-Compass on top of native.** Omni-Compass is never by itself (the founder's order of 25 October): it needs
muscles with their own native controllers under it, never replaces native, and every comparison is read against native.

## The engine that stands: omni-v25 (the Kafka wire's producer before the governor's thread)

The engine on main is **omni-v25** (`OMNI_V25.json`, fingerprint `cf56fc0a7b707452`, 65 files; [`docs/OMNI_V25.md`](docs/OMNI_V25.md)), 3 November: omni-v24 with one fault fixed in the Kafka wire: the producer is started before the governor's thread, because from omni-v22 that thread opened its own Kafka client while the producer was forked, the producer inherited a lock the thread held and never sent a message, and every Kafka run on GitHub since 30 October stopped at the job's 150-minute limit with nothing handed in; a producer that overruns its schedule now stops its workload with the reason. The governor's decisions are byte for byte omni-v24's (53 of the wire's 58 definitions identical, the brain among them); its model gate against omni-v24 is [`results/model_gate/V25_VS_V24.md`](results/model_gate/V25_VS_V24.md). Everything else it runs is omni-v24's ([`docs/OMNI_V24.md`](docs/OMNI_V24.md), on main from 1 to 3 November): omni-v23 with the heartbeat it ships with read from the place it runs in, on the founder's orders that the factory beat is the best beat the sweeps read and that the basic setting is found and then locked ("60 seconds is a disadvantage, it's not a benefit"; "You pick and find out"). With no beat set, the Kubernetes governor reads the cluster's nodes once at its start: on site (kind, the owner's own machines) it takes its full decision every 10 s; through a cloud (a node that names a public cloud's machine) every 60 s; a reading that fails keeps 60 s, and a beat set by hand always wins, so the heartbeat stays a dial. The rule that picked the two beats was frozen before any reading was seen ([`docs/PACE_PREREGISTRATION.md`](docs/PACE_PREREGISTRATION.md), amendments 4 to 6; our own models, class S; the record [`results/model_gate/V23_LADDER_CORRECTED.md`](results/model_gate/V23_LADDER_CORRECTED.md)): on site 10 s was the one beat no other dominated (against 60 s the minutes over the response line down 65.5%, the 95th percentile down 9.9%: fewer and faster, GAIN; the machines the same; the reads of the cluster and Omni-Compass's own processor power given); through a cloud no beat kept the bill from rising against native, so 60 s stays there and those rows are on the next version's list with their cause. 64 of its 65 files are omni-v23's bytes; the model gate against omni-v23 ([`results/model_gate/V24_VS_V23.md`](results/model_gate/V24_VS_V23.md)): no LOSS against omni-v23; eleven of its twelve models identical on every gauge and seed; on site, at its 10 s against omni-v23's 60 s, the minutes over the response line down 60.7%, the 95th percentile down 8.2% and the autoscaler's shortfall down 5.1% (fewer and faster, GAIN), the machines the same, the reads of the cluster and its own processor power given. omni-v23 ([`docs/OMNI_V23.md`](docs/OMNI_V23.md), Omni direct keeps every muscle Omni-Compass cannot be: a knob whose writes are refused goes back to native's own controller) stood from 31 October to 1 November.

Every engine before it is on its own page, `docs/OMNI_V<n>.md`, with what it changed, why, and what its model gate read; the road from omni-v1 is in [`CHANGELOG.md`](CHANGELOG.md) and `docs/history/`. No result is read across engines: every benchmark runs again on the engine that stands (`scripts/reruns.txt`, released by the conductor, `scripts/dispatch_grid.py`), and a row still on an older engine names it until its three runs on the engine that stands land.

Where its results stand, each page written from the result files on every push and none typed by hand: the answer at the top of this page (`tools/headline.py`); one number and one word per benchmark, each naming its engine, in [`docs/BENEFIT_SHEET.md`](docs/BENEFIT_SHEET.md); the Omni index in [`results/OMNI_INDEX.md`](results/OMNI_INDEX.md); every LOSS row with its cause in [`docs/LOSS_LEDGER.md`](docs/LOSS_LEDGER.md); every chip, cloud and machine run, what it cost and what came back, in [`docs/RUN_LEDGER.md`](docs/RUN_LEDGER.md). Every three-run table of the engine that stands is rebuilt byte for byte from its archived runs by `python3 tools/reproduce.py` (the runs on the branch `raw`). From 31 October every archived run's sums are also signed, keyless, under GitHub's own identity for the archive job and entered in Sigstore's public transparency log: `python3 tools/verify_receipt.py` checks a run's files against its sums and its sums against their signature (a sum alone is a fingerprint, not a signature). The whole system, every layer composed by the product law from its own table, is [`results/WHOLE_SYSTEM.md`](results/WHOLE_SYSTEM.md): a modelled composition (class S) of the class P and L tables, each layer named by its engine. How every one of these was graded is in [`docs/REFEREE_GRADES.md`](docs/REFEREE_GRADES.md).

## The engine's law: every muscle from 1 up to one click under its own capacity, read live (13 October, night)

The founder's order of 13 October is in the live controllers ([`docs/OMNI_V5.md`](docs/OMNI_V5.md), amendment 5, carried unchanged by the
engine that stands): no top or floor is a number we wrote down. Machines go up to what the cluster itself can
add (its own autoscaler's room, or, where Omni-Compass resizes the pool, one under the first count the pool refuses;
before: a fixed 1,000), and never below two; the service's replica cap may rise to what the machines can hold of its
pods, one pod under it; at the max the power cap is never set under native (each machine's idle CPU goes to the work);
the GPU's clock floor and heat line are the card's own. The test rig changed with it (protocol 3): the model of the
organism runs on its own core, away from the real cluster's, the same in both arms, and the window is set from the
heavier arm's measured step, so the 100-copy squares measure the governor, not the test machine. **Every result runs
again on this engine**; the card version's results below stand as that version's record until the new runs replace them.

## The muscles and the seven organisms, modelled: every muscle its own card (13 October; the spine the seventh organism, 16 October)

<!-- the muscles and the seven organisms, written from their records (tools/organism_words.py) -->
Every number in this section is computed from its record by `python3 tools/organism_words.py`, and `verify.py` fails a
push where any of them differs from what the records give. Evidence class **S**: our own models of the plants, not
meters; a plant written by the people who wrote the law is not an independent test.

**The 1,107 muscles and the seven organisms** ([`results/realms_v5/REALMS_V5.md`](results/realms_v5/REALMS_V5.md)). The newest
record is engine omni-v8's: run 2026-10-17 15:39 UTC, commit `9819a903cba3`, preregistered seeds 3000 to 3009 (ten paired runs
per muscle, per organism and per load), read again by the 0.5% rule on 24 October 2026. It runs again on the engine that stands;
until its table lands, this one is omni-v8's.

| Every muscle alone, under its own load and with work waiting in line | Muscles of 1,107 |
|---|---:|
| **GAIN**: fewer misses, faster or more work, and no LOSS under either load | **530** |
| of them: the waiting line cleared sooner | 493 |
| of them: over the line less often | 445 |
| of them: more work | 12 |
| STEADY, at its limit on native (native already runs the knob at the top of its range; Omni-Compass writes nothing) | 421 |
| STEADY, the same as native | 156 |
| **LOSS**, or GAIN and LOSS | **0** |

Each organism under each load: the change in decisions over the line (Omni-Compass's count against native's), the
largest change in work over the three loads, and the largest rise in energy (the organism's energy against native's; under
the 0.5% floor it reads STEADY).

| Organism (muscles) | Over the line: its own load | the climb | work waiting in line | Work, largest change | Energy, largest rise |
|---|---:|---:|---:|---|---:|
| The spine (267) | GAIN, down 6.1% | GAIN, down 7.9% | GAIN, down 8.8% | STEADY, 0.003% (under the 0.5% floor) | STEADY, up 0.039% (under the 0.5% floor) |
| Compute / AI / Cloud (540) | GAIN, down 3.6% | GAIN, down 7.0% | GAIN, down 8.3% | STEADY, 0.002% (under the 0.5% floor) | STEADY, up 0.046% (under the 0.5% floor) |
| Physics / Robotics / Autonomous (404) | GAIN, down 2.5% | GAIN, down 3.2% | GAIN, down 2.3% | STEADY, 0.002% (under the 0.5% floor) | STEADY, up 0.030% (under the 0.5% floor) |
| Energy / Facility / Industrial (480) | GAIN, down 7.5% | GAIN, down 2.7% | GAIN, down 8.3% | STEADY, 0.000% (under the 0.5% floor) | STEADY, the same |
| Distribution / Specialized (484) | GAIN, down 2.8% | GAIN, down 7.2% | GAIN, down 4.7% | STEADY, 0.003% (under the 0.5% floor) | STEADY, up 0.026% (under the 0.5% floor) |
| The four stacked (1,908) | GAIN, down 3.6% | GAIN, down 4.8% | GAIN, down 4.3% | STEADY, 0.002% (under the 0.5% floor) | STEADY, the same |
| The whole tower (1,107) | GAIN, down 1.9% | GAIN, down 1.4% | GAIN, down 1.1% | STEADY, 0.000% (under the 0.5% floor) | STEADY, the same |

**The grid** (the seven organisms at 1, 10 and 100 copies, each at 1, 10 and 100 runs). Its one written report is engine
omni-v5's ([`results/grid_v5/GRID.md`](results/grid_v5/GRID.md)); its modelled squares read, in the report's own summary with
its signs put in words: modelled, 36 of 36 squares of 10 and 100 runs GAIN (fewer misses); the 18 single runs: 18 with fewer
misses; work STEADY, the same (raw +0.000%); energy STEADY, up 0.000% to 0.065% (under the 0.5% floor). The squares with the
real cluster inside are read gauge by gauge in the same report. The grid has been sent on every engine since, omni-v6 to
omni-v25 (`results/grid_v*/DISPATCHED.json`), and no report of those runs has been written yet; until one is, the grid is read
only on omni-v5.

**The twenty scenarios** (ten organisms, each native and with Omni-Compass on native; engine omni-v23, run 2026-10-31 20:06 UTC,
three runs, seeds 3000 to 3002; [`results/scenarios/SCENARIOS_20.md`](results/scenarios/SCENARIOS_20.md)). In the 9 modelled
organisms the muscles over the line read GAIN in 9 (from GAIN, down 1.58% in the whole tower to GAIN, down 63.34% in the
orchestra); the work STEADY in 9; the power STEADY in 7 (Compute / AI / Cloud: GAIN, a cut, down 0.59%; The orchestra: power
given, up 52.38%). The whole organism without the card, composed from the real tables (class S, a composition of class P and
class L measurements), reads GAIN 22.5% by the index's rule; its tables come from 5 engines (omni-v1, omni-v12, omni-v18,
omni-v21, the engine of commit 5b2832f (4 October 2026)), so it is a composition across engines, never one engine's reading.
<!-- end of the muscles and the seven organisms -->

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

## The manuals: the Operator's Manual, the Owner's Manual and the Live Benchmark Engine Manual

[`docs/OMNI_COMPASS_MANUAL.pdf`](docs/OMNI_COMPASS_MANUAL.pdf), the Operator's Manual, is the manual for the glove box, built from the
repository whenever it changes (`docs/book/build_book.py`): how to embed, wire, tune, run and check Omni-Compass on a
stacked, clustered system or on any one muscle. Front matter with the card for the glove box; the governor from the
outside and its factory tune; the plug and the rules its wires obey; the wiring level by level and stack by stack
(Kubernetes, databases, message brokers, caches, GPUs, the processor itself, the data center under the servers, robots
and drones); operating it; checking it on your own system; **the implementer's guide for the cloud** (Part VI, chapters
13 to 30: the path and its gates, least privilege, Azure, Google Cloud and Amazon step by step, the response-time feed,
the cloud itself, day two, the graphics processor, observability, change and risk, planning a cloud run, own
racks and private clouds, hardening and the supply chain, a fleet under continuous delivery, the failure drill book, and
one installation start to finish); and back matter with every muscle, its wiring and its card, the install manifests,
the implementer's checklists, every setting Omni-Compass ships with (on Kubernetes and on the two cards), the audit
record by record (every record of Omni-Compass on Kubernetes, of the other muscles and on the cards), the three clouds side by
side, every input of the paired run from GitHub, and the papers counsel asks for (the license, the licensing answers, the
third-party notices, the Enterprise License's standard terms, the patents and trademarks, the security policy). Since 16
October it also states the rules of the engine that stands as an operator meets them (section 6.5) and how a new muscle is
coded on the muscle SDK (section 5.7). Its figures are drawn from the code by two kits (`docs/book/figures.py`,
`docs/book/schematics.py`; the drawings in `docs/book/figures/`): the plug, the band and the two forces, one decision of the
governor, the eight levels, the one pedal, the seven organisms and the three-run rule; a wiring schematic for every stack in
the grammar of an electrical drawing (the governor's sense and motor terminals, the kill switch, the plug, the native
controller, the muscle and the meters); the flowcharts of the wire check, the paired run, the eight phases, the release gate,
the three stops and the reading rule; the timing diagrams; and the state machines of the modes, the card governor and the life
of a muscle; and an index. The Owner's, which prints the engine's whole source and adds the engine's six states and its two
landscapes, the control-loop block diagrams, the modelled traces and every receipt of the engine that stands charted from its
own table; its source appendix prints every file of the engine's fingerprint. Each book's page count and List of Figures are
printed in the book itself, built from its text (`docs/book/build_book.py`). All three books carry one numbering (chapter.section), and every cross-reference in
them is rewritten to it when the book is built and checked against the headings on the built PDF. Its text is
[`docs/OMNI_COMPASS_MANUAL.md`](docs/OMNI_COMPASS_MANUAL.md); the cloud install files are `deploy/install/`
(`omni-compass.yaml`, `rbac-cloud.yaml`, `omni-compass-cloud.yaml`) and `deploy/Dockerfile.cloud`. It is written for the CTO who decides, the
engineer who wires and the operator who runs it; the published results are on this page and in `results/`.

[`docs/OMNI_COMPASS_OWNERS_MANUAL.pdf`](docs/OMNI_COMPASS_OWNERS_MANUAL.pdf), the Owner's Manual, is the master: everything
in one book, for whoever owns or licenses Omni-Compass and so must know the whole mechanism (the philosophy, the
mathematics, the mechanism, the engine that stands and the road to it, every Python file of the engine's source printed in
full, every result, the wiring, and every legal paper bound in). Its text is
[`docs/OMNI_COMPASS_OWNERS_MANUAL.md`](docs/OMNI_COMPASS_OWNERS_MANUAL.md).

[`docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.pdf`](docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.pdf), the Live Benchmark Engine Manual, is the third book (the
founder's order of 20 October: three in the end): nothing more than the interpretation of the live benchmark engine page,
[`docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`](docs/engine/OMNI_COMPASS_LIVE_ENGINE.html), for the operator at the dashboard: how to
follow the wall and the switch, read every gauge and turn every knob, trace any tile to the record it came from, and see the
mechanism of action of Omni-Compass against native as the monitors show it (the two tickers, the phase plane, the brain's
state, the verdict), section by section in the page's own order, with what to do when a tile reads LOSS and what the page
does not tell you. It explains neither how the engine is built nor how it is wired; it is built by `docs/book/build_book.py
--live`, and its text is [`docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`](docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md). Its last appendix
is the page word for word, written from the page itself at every build (`docs/book/build_live_manual.py`): every section, every
monitor with its number, evidence class, feed and knobs, and every control, so the book and the page read each other both
ways; the control panel at the top of the live benchmark engine downloads all three books.

**The live benchmark engine page**, the tuning bench, opens on the bottom line, then the monitor wall and the main control panel. Native
is orange everywhere, Omni-Compass on native blue; red is never a side, only the alarm. Every
monitor carries its light and its word: green and round, **GAINING** (working inside its lines with room to give, or a
GAIN); yellow, a yield diamond, **STEADY** (STEADY, inside 0.5%, or heading for its line and watched); red, a stop-sign octagon,
blinking, **REDLINING** (over its line, or a LOSS: the alarm); dark, **AWAITING** (the run that fills it has not landed; never
green). The main control panel holds the kill switch, the heartbeat's seven buttons,
**10, 15, 20, 30, 60, 90 and 120 s**, a sweep that runs every beat on the page's own model for three model days each, **Try the
candidate** (the sweep's best beat as a candidate profile), the active profile with its fingerprint (factory, candidate or
custom), **Restore factory profile**, **Hold the active profile** and **Return to native**. Its **AUX** button opens the
**Auxiliary Input**: ten slots, each waiting to be wired to a company's own system (its Prometheus, read only; the native it
runs; Omni-Compass on top or not), each lighting its own row under the wall and able to flip the wall's monitors that carry a Prometheus query to it, and set
beside the repository's real records only (live software, class L; the card's meter, class P), never a model run: every benchmark
stays as it is, and a company's own system stands beside it. A model's best beat is a candidate
for the real runs, never a result, and no profile is locked as the baseline: the factory's beat stays 60 s until the eight
steps of [`docs/FACTORY_PROFILE.md`](docs/FACTORY_PROFILE.md) choose the next. At its back stand the glossary and index
(`tools/live_glossary.py`): every term in the words of the file it names, the ten organisms and their twenty scenarios, every
one of the 1,107 muscles of the catalog by realm and family, and the sections where each is used.

The engine is written twice, in Python and in C++ ([`cpp/`](cpp/)), line for line where a twin exists. The live benchmark engine's section 10b ([`#s-cpp`](docs/engine/OMNI_COMPASS_LIVE_ENGINE.html#s-cpp)) feeds the Python's own runs into the C++ at every rebuild and sets the two side by side, number by number: every twin's parity check, every compass law the page's runs wire, and every muscle of the seven organisms at the tune-down. The Python's 500 seeded runs (`tools/engine_runs.py`, the jump generator) run whole through the C++ harness too ([`cpp/tools/engine_runs.cpp`](cpp/tools/engine_runs.cpp): the Python's draws are the input, the governor, the nerves, the compass law and the verdict in C++ put the mechanism on): every receipt and the SHA-256 digest identical to the Python's, on GitHub with every set (`engine-runs`) and on the page's proof monitor ([`#proofPanel`](docs/engine/OMNI_COMPASS_LIVE_ENGINE.html#proofPanel)) beside the page's own run. What still runs in Python only is listed there by file (`tools/seal.py`).

## What is real and what is a model

| Evidence | What runs | Class |
|---|---|---|
| Real Kubernetes on GitHub | Kubernetes itself (API server, scheduler, its own autoscaler), a real web service, real requests, real response times and CPU. The machines are containers on one runner; energy there is a declared formula, not a meter | L |
| Real cloud, Azure AKS | All of the above on real Azure machines, Azure's own autoscaler, Azure's billed machine count | L |
| Real card, NVIDIA A10 on Lambda | The card's power limit and clocks, its own power meter, real GPU work. The first run (2026-10-02) used a card controller since replaced (it answered slower); the current controller's run is next | P |
| The 1,107 muscles | Software models of real control systems (AI serving, cooling, batteries, robot joints, grids), each from its maker's specification. They show the mechanism; they are labelled as models wherever they appear | S |

## Omni-Compass by itself: the organism run without Kubernetes (23 October)

Omni-Compass also runs the organism as its own orchestrator, with no Kubernetes or other orchestrator's code in it
([`docs/OMNI_ORCHESTRATOR.md`](docs/OMNI_ORCHESTRATOR.md), graded in [`docs/OMNI_ORCHESTRATOR_GRADES.md`](docs/OMNI_ORCHESTRATOR_GRADES.md)).
Three arms are always shown together: native (Kubernetes' published autoscaling rule on the muscles, written by us as the
yardstick), Omni on native (Omni on top of that rule) and Omni direct (Omni alone on the muscles). The single runs of the first
showings (one run of each arm, on omni-v18) are not a reading and are not quoted here. The three-run reading on GitHub
(`orchestrator.yml`, omni-v21) is the record: Omni-Compass on native against native reads work GAIN and the 95th
percentile GAIN in all three of our runs; Omni-Compass direct against native reads both GAIN by the mean of our three runs;
Omni-Compass direct against Omni-Compass on native reads work LOSS by the mean of our three runs, beyond the noise in 1 of 3,
shown with its row: on this record Omni-Compass did the most work on top of the native orchestrator, not in its place
([`results/orchestrator/V21_THREE_ARMS_ABC.md`](results/orchestrator/V21_THREE_ARMS_ABC.md)). Why a muscle reads STEADY and where the room is, in theory and mathematics: [`docs/THE_ROOM.md`](docs/THE_ROOM.md).

## How it works

Omni-Compass is a supervisory governor. It does not replace your autoscaler or your firmware: it sits on top, reads
the meters of each muscle (response time, utilisation, power, heat), and by default runs **at the max**: every muscle
pushed to its own limit, never past it and never below native, riding the edge of its band, not the middle. It starts
machines before the rush lands and clears work waiting in line, cools a room ahead of the heat, holds a battery's
charge for the line, and runs an axis at its own peak while tasks wait. The energy that takes is **power given**, shown
beside the work, the speed and the wear it bought; inside a body (an organism) it gives only what the body's lines can
carry. One pedal: push for more, lift off for less, and lifting hands the setting back toward native; at idle
the pool lifts to its floor of two machines, powered and ready. If Omni-Compass stops, the plug walks every setting back
to native; the kill switch, a separate security switch, turns it off everywhere at once. Anyone can tune it down from
the max on the dial. The law, its
proof and its wiring: [`docs/MECHANISM_OF_ACTION.md`](docs/MECHANISM_OF_ACTION.md),
[`docs/TRACKING_THEOREM.md`](docs/TRACKING_THEOREM.md), [`docs/CONVEYANCE_LAW.md`](docs/CONVEYANCE_LAW.md).

**Where the benefit is taken, and why nobody babysits it.** On machines already paid for (your own racks, a chip at its heat
line) the max takes the benefit as more work from the same machines; in a chip the aim is more work at native's own
heat, never hotter. In a
public cloud the whole engine runs at the max as well, every muscle, on top of the cloud's own autoscaler, and the bill is
judged beside the work by the one key, never ruled (the founder's order of 31 October: no hard rule; in the cloud the judged
number is the work per dollar, and a tune whose work per dollar falls against native is not admissible, `docs/THE_TUNE.md`). Either way it runs on autopilot, self-running, self-steering and self-auditing like a
self-driving car: nobody turns a knob, nobody checks its work and nobody has to react; every change is the governor's own, logged with its reason, made as the
reading approaches the line rather than after it is crossed; every Kubernetes and cloud receipt
counts the babysitting tax in both arms (the alert minutes an on-call page would be open, and the commands the governor
wrote on its own).

<!-- the oversight line (tools/oversight.py) -->
**The people, counted: the oversight line** (`results/OVERSIGHT.md`, written by `tools/oversight.py` from the tables). The Omni index counts work, speed and machines, never a person; the receipts count the people too, in both arms. Across the 43 real Kubernetes tests of omni-v25, the minutes an on-call page would be open (the 3 a.m. call) went down 7.4%, fewer in 16 tests and to none in 3, and down in each of our three runs beyond the noise (GAIN in all three of our runs), while the governor turned the knobs itself (216; 216; 203 settings an hour in runs A; B; C, no person touching either arm). Counted as pages from the same runs' raw files by the rule written before the count, the pages a person would have been sent went down 6.7% (GAIN by the mean of our three runs, beyond the noise in 2 of 3; `results/OVERSIGHT_PAGES.md`): fewer pages, each open about as long. In the bill it is the people line, b = s(people) · b(people) at the owner's own share: at the founder's example of 7%, down 0.5% of the whole bill. It is not added to the index (a share of a bill and a reading of work and speed do not add), and it removes no person: a person keeps the switch.
<!-- end of the oversight line -->

## Check it yourself

```
pip install -r requirements.txt && python verify.py      # must end: VERIFICATION: PASS
bash scripts/run_live_local.sh 3                          # native against omni on your own kind cluster
sudo bash scripts/gpu_rented_run.sh                       # the card run, on any rented NVIDIA machine
```

`verify.py` reruns every held-out result byte for byte, the Python and C++ twins, the property tests, and checks that
the repository is lined up (`tools/layout_check.py`). Every live result carries its raw files and SHA-256 digests.

The raw files of the live runs (about 36 GB, 182,161 files) live on their own branch, `raw`, from 18 October: main holds the
code and the tables, so a clone of main is small and every table, page, manual and the verifier work without the raw
files. Opened, the branch sits at `results/live/raw/`, so every path a table names (`results/live/raw/run-<id>/...`) reads as
written; only the folders asked for are downloaded:

```
git clone https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC && cd The-Omni-Compass-LLC
bash scripts/raw_archive.sh open /run-<id>/            # one run's raw files, when wanted (more patterns: more runs)
```

From 17 October the archive stores the bulk no table reads once a run has made its own tables (YCSB's raw latencies,
the request logs, the Kafka consumer logs) gzipped; read one with `gunzip -c FILE.gz`, and its hash stands in the run's
`SHA256SUMS_ALL.txt`.

## Read next

| For | Read |
|---|---|
| **The register: every muscle wired, every benchmark run, every benchmark still to run** | [`docs/REGISTER.md`](docs/REGISTER.md) |
| **The proof program: every benchmark at full size, every open native engine, the referee-grade package** | [`docs/PROOF_PROGRAM.md`](docs/PROOF_PROGRAM.md) |
| **The engine that stands, omni-v25, fingerprinted (the Kafka wire's producer started before the governor's thread; omni-v24's factory beat for its place carried: 10 s on site, 60 s through a cloud); the arm by itself (Omni-Compass's own pod rule in place of the autoscaler, never direct on Kubernetes); the orchestrator's three arms; the v5 law at the max, the bone, the lease, the dial** | [`docs/OMNI_V25.md`](docs/OMNI_V25.md), [`docs/OMNI_V24.md`](docs/OMNI_V24.md), [`docs/OMNI_V23.md`](docs/OMNI_V23.md), [`docs/OMNI_V22.md`](docs/OMNI_V22.md), [`docs/OMNI_V21.md`](docs/OMNI_V21.md), [`docs/OMNI_V19.md`](docs/OMNI_V19.md), [`docs/OMNI_V18.md`](docs/OMNI_V18.md), [`docs/OMNI_V17.md`](docs/OMNI_V17.md), [`docs/OMNI_V16.md`](docs/OMNI_V16.md), [`docs/OMNI_V15.md`](docs/OMNI_V15.md), [`docs/OMNI_V14.md`](docs/OMNI_V14.md), [`docs/OMNI_V13.md`](docs/OMNI_V13.md), [`docs/OMNI_V5.md`](docs/OMNI_V5.md), `python3 tools/omni_version.py` (the earlier engines stay with their own results as the road to 1.0: [`docs/history/`](docs/history/)) |
| **The heartbeat dial: every beat of the governor beside native, what it buys and what it costs** | [`results/model_gate/V17_LADDER.md`](results/model_gate/V17_LADDER.md), [`docs/PACE_PREREGISTRATION.md`](docs/PACE_PREREGISTRATION.md), on the live engine page, the page's section 1j |
| Every result, every platform, where each stands | [`docs/STATE_OF_PLAY.md`](docs/STATE_OF_PLAY.md), [`results/OMNI_INDEX.md`](results/OMNI_INDEX.md) |
| How to read a result table | [`docs/HOW_TO_READ_THE_RESULTS.md`](docs/HOW_TO_READ_THE_RESULTS.md) |
| Every level on one page: the muscle, the organism, the cluster, its add-ons, the service, the plant, the cloud, a group of clusters; any level whose gauges go the other way, named | [`docs/LEVELS.md`](docs/LEVELS.md) (`python3 tools/levels.py`) |
| The method, written before each run | [`docs/K8S_COMPASS_PREREGISTRATION.md`](docs/K8S_COMPASS_PREREGISTRATION.md), [`docs/GPU_PREREGISTRATION.md`](docs/GPU_PREREGISTRATION.md), [`docs/REALMS_PREREGISTRATION.md`](docs/REALMS_PREREGISTRATION.md) |
| A referee's checklist | [`docs/REFEREE_CHECKLIST.md`](docs/REFEREE_CHECKLIST.md) |
| Every claim with its evidence class, losses kept | [`docs/EVIDENCE_LEDGER.md`](docs/EVIDENCE_LEDGER.md), [`docs/CLAIMS_REGISTER.md`](docs/CLAIMS_REGISTER.md) |
| Due diligence | [`docs/DUE_DILIGENCE.md`](docs/DUE_DILIGENCE.md) |
| The manual (wiring, operating, every result) | [`docs/OMNI_COMPASS_MANUAL.pdf`](docs/OMNI_COMPASS_MANUAL.pdf), [`docs/INTEGRATION_MANUAL.md`](docs/INTEGRATION_MANUAL.md) |
| The 1,107 muscles, and how to wire every family on your own stack | [`docs/MUSCLE_CATALOG.md`](docs/MUSCLE_CATALOG.md), [`realms/catalog_v5.csv`](realms/catalog_v5.csv), [`docs/wiring_recipes.csv`](docs/wiring_recipes.csv) |
| Every command on one page | [`docs/HANDOFF.md`](docs/HANDOFF.md) |

## Repository

| Path | What it is |
|---|---|
| `omnicompass/` | The engine (`core.py`), the compass law (`compass_law.py`), the verdict, the shield, the master switch |
| `omni_controller/` | The live controllers: Kubernetes (`controller.py`) and the card (`gpu_compass.py`) |
| `cpp/` | The C++ twins, sealed equal to the Python laws |
| `realms/` | The 1,107-muscle catalogue, its models and the v5 law at the max (`compass_arm_v5.py`) |
| `scripts/`, `deploy/`, `.github/workflows/` | The benchmarks: kind, AKS, the card, eight cards |
| `tools/` | Report builders, the Omni index, the layout check |
| `results/` | Every result with its raw files and digests |
| `docs/` | Results, method, manual, due diligence |
| `tests/` | The tests `verify.py` runs |

## Find it

Omni-Compass is a **supervisory governor**: a control plane that sits on top of a native controller and never replaces it.
People searching for any of these should find this page: supervisory governor, supervisory control, control plane,
governor, controller, autoscaler, autoscaling, Kubernetes HPA, cluster autoscaler, Karpenter, KEDA, node pool, right-sizing,
conveyance, machinery, engine control, power cap, clock ceiling, DVFS, cpufreq, RAPL, GPU power limit, energy efficiency,
energy per unit of work, data center efficiency, PUE, green computing, FinOps, SRE, SLO, p95, tail latency, do no harm,
paired trial, A/B/C replication, preregistration, Redis maxmemory, Kafka consumer group, PostgreSQL pooler, MySQL buffer
pool, MongoDB WiredTiger cache, HVAC setpoint, building management, chiller plant, UPS, PDU, battery management, microgrid,
grid tap changer, voltage regulator, wind turbine pitch, pipeline compressor, water pump scheduling, robot servo, drone
autopilot, flight software, autonomous driving stack, 5G RAN scheduler, matching engine, game server fleet, build farm,
ledger node, IDS workers, control theory, closed loop, two antagonist forces, tanh law, nervous system, muscles, realms,
organisms, Omni index. The repository's GitHub topics (set by its owner from the About panel, with www.omni-compass.com as its website): `omni-compass`, `governor`, `supervisory-control`, `control-plane`, `control-core`, `control-engine`, `control-theory`, `control-systems`, `feedback-control`, `conveyance`, `machinery`, `autoscaling`, `kubernetes`, `gpu`, `data-center`, `energy-efficiency`, `power-management`, `smart-grid`, `robotics`, `industrial-automation`.

## Contact

The Omni-Compass LLC, main office infrastructure. Toll-free direct: **1-888-339-9551**. System route asset:
**1-888-DEX-YLL-1**. Landline, registered in Florida: **321-746-4411**. [www.omni-compass.com](https://www.omni-compass.com)

What the letters mean at Omni-Compass, read in order, the way the engine runs:

| DEX | YLL | 1 |
|---|---|---|
| **Data Exchange**: the input. In software, data exchange is how one system's readings reach another. Here it is the two-way plug, one wire in and one wire out: the system's own readings come in, Omni-Compass's settings go out. | **Yield Limit Line**: the boundary. In engineering science, the yield limit is the most load a material can carry and still spring back unharmed; past it, the damage is permanent. Omni-Compass runs every muscle up to its own yield limit line, read live, and never past it. | **1**: the output. In code, 1 is true, the finished state; in science, 1 is unity, the whole. Here it is one closed loop: one body, one brain, every result read back and the next step decided from it. |

Read as one sentence: Omni-Compass takes the system in through a Data Exchange (DEX), runs every setting up to its Yield Limit Line (YLL) and never past it, and closes it all into one loop (1). Science and software people read each part on sight.

## License

**Proprietary. Evaluation and Simulation use only.** You may download, run and modify the software only to evaluate
it and to reproduce the published results, including in shadow or test mode on systems you own or control. Everything
else requires a written **Omni-Compass Enterprise License** signed by The Omni-Compass LLC and paid for. No patent or
trademark license is granted for any other use.

| File | What it says |
|---|---|
| [`LICENSE`](LICENSE) | Evaluation and Simulation use only; everything else needs a signed, paid Omni-Compass Enterprise License |
| [`NOTICE`](NOTICE) | copyright, the US filings notice, third-party notices |
| [`PATENTS.md`](PATENTS.md) | the nonprovisional utility patent application "The Omni-Compass" filed in the United States (title, inventor, date; the number is withheld on purpose); no patent license is granted |
| [`TRADEMARKS.md`](TRADEMARKS.md) | the Omni-Compass marks; trademark applications filed in the United States |
| [`DISCLOSURES.md`](DISCLOSURES.md) | every declaration, disclosure and disclaimer, made once |
| [`LICENSING_FAQ.md`](LICENSING_FAQ.md) | licensing in plain answers |
| [`.github/CLA.md`](.github/CLA.md) | contributions are assigned to The Omni-Compass LLC |
| [`REUSE.toml`](REUSE.toml), [`sbom/`](sbom), [`.fossa.yml`](.fossa.yml) | machine-readable license declarations for scanners |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

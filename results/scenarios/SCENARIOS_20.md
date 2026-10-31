# The twenty scenarios: ten organisms, each native and with Omni-Compass on native (modelled)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

The founder's words of 24 October set the organisms: "We have 4 realms ... the 4 realms stacked ... the spine of the 4 realms ... Then we have the whole thing native. And with OmniCompass on native ... 9 to 10 different organisms." His order of 25 October took the third way out: "we don't need an omnicompass by itself ... Never is going to omnicompass be by itself. It needs muscles somewhere, somehow." Omni-Compass always sits on top of a native controller. Ten organisms, each two ways: twenty scenarios, every one tabulated below, every row reported, LOSS included.

Evidence class **S** (our own models): a model's energy is not a meter's, and a plant written by the people who wrote the law is not an independent test. Engine **omni-v19** (`tools/omni_version.py`, digest 36ee67284c035235), commit `ba37d31186ca`, run 2026-10-25 01:57 UTC, 36 s on 8 processes. Runs A, B and C are seeds 3000, 3001, 3002 (the live engine's harness record's runs, the first three of the realms' preregistered seeds 3000-3009), the same seed in every arm. The load is the climb (the load stepping by one, 1 2 3 2 3 4 5 6 ..., level 4 the organism's own load, 8 twice it), for 240 decisions of 15 s (an hour, every organism at full length); at 80% of every run the brain goes silent and the lease walks every setting back to native over 24 decisions. Written by `python3 tools/scenarios_20.py`; every run's every gauge is in `results/scenarios/SCENARIOS_20.json`.

## The two arms

| Arm | What runs |
|---|---|
| Native (Omni-Compass off) | every plant under its own native controller alone (`realms/harness.py` `run_bodies`, arm native) |
| Omni-Compass on native | the max (`realms/compass_arm_v5.py`, `V5CFG`), the factory tune, on top of every native controller: every muscle to its own limit, never past it and never below native, the bone granting only the power the body's lines and rooms have room for (arm v5, as `tools/run_realms_v5.py` runs it) |

## How each scenario is read

Omni-Compass on native is read against native gauge by gauge as the live engine's harness record reads it (`docs/engine/export_harness_trace.py` `gauges` and `interval`): in each run the paired change per decision, averaged over blocks of ten decisions, with its 95% interval by Student t over the 24 blocks. The word is the key's (`tools/readings.py` `stack_reading`, with the founder's half-percent floor through `in_all_three`): **GAIN**, **LOSS** or **power given in all three of our runs** when all three runs point the same way with every interval clear of zero, judged by what the gauge is for and never by its sign; **STEADY** when an interval includes zero (no difference beyond the noise), when nothing moved (the same), or when every run's change is under half of one percent (under the floor); **the runs disagree** when clear runs point different ways. The number beside a word carries the word's sign. The gauges:

| Gauge | What it is for | What it measures |
|---|---|---|
| work | work done: a rise is GAIN | the work index: each decision, the mean over the muscles of the work each did against the reference arm's own mean rate (1.0 is the reference's own work) |
| muscles over the line | time over the line: a fall is GAIN | the muscles over their own line, counted each decision (a muscle-decision over the line is time over the line) |
| power | a resource spent: a fall is a cut (GAIN), a rise is power given | the organism's electrical draw each decision, kW, as its lines carry it (realms/harness.py Body.all_w, the reading the bone grants from); the runner's energy beside it is each plant's own metered energy with a battery's charge left below its start bought back at its round trip, so the two can move apart |
| spread | shown, not judged | the spread of the muscles' service positions each decision (shown, never judged) |

Beside them stand the realms runner's own contrasts (`tools/run_realms_v5.py` `paired_organism`, `plant_harms`: the work, the energy with a battery's charge left below its start bought back at its round trip, the decisions over the line, the work per energy, the wear, and every plant that did less work or missed its line more often) and the runner's label over the three seeds (`label_max`: 95% intervals over the seeds, Student t with two degrees of freedom), in the words of the key.

## The twenty scenarios

Native's own gauges (the mean of runs A, B and C), then Omni-Compass on native read against native (the word, and the mean of the three runs' changes). The per-run numbers and intervals follow.

| # | Organism | Muscles | Native (Omni-Compass off) | Omni-Compass on native, against native |
|---:|---|---:|---|---|
| 1 | The spine | 267 | work index 1.000; 21.38 muscles over the line a decision (8.01% of muscle-decisions); 3,418.4 kW (13,262.9 MJ) | work **STEADY** =0.00% · muscles over the line **GAIN** +8.36% · power **STEADY** =0.49% |
| 2 | Compute / AI / Cloud | 540 | work index 1.000; 29.80 muscles over the line a decision (5.52% of muscle-decisions); 3,890.7 kW (14,962.9 MJ) | work **STEADY** =0.00% · muscles over the line **GAIN** +7.41% · power **GAIN** +0.59% |
| 3 | Physics / Robotics / Autonomous | 404 | work index 1.000; 38.22 muscles over the line a decision (9.46% of muscle-decisions); 4,811.8 kW (19,023.4 MJ) | work **STEADY** =0.00% · muscles over the line **GAIN** +3.89% · power **STEADY** =0.26% |
| 4 | Energy / Facility / Industrial | 480 | work index 1.000; 39.22 muscles over the line a decision (8.17% of muscle-decisions); 2,953,821.5 kW (10,659,898.0 MJ) | work **STEADY** =0.00% · muscles over the line **GAIN** +3.02% · power **STEADY** =0.00% |
| 5 | Distribution / Specialized | 484 | work index 1.000; 29.72 muscles over the line a decision (6.14% of muscle-decisions); 15,072.9 kW (55,218.8 MJ) | work **STEADY** =0.00% · muscles over the line **GAIN** +7.22% · power **STEADY** =0.17% |
| 6 | The four stacked | 1,908 | work index 1.000; 136.97 muscles over the line a decision (7.18% of muscle-decisions); 2,977,596.8 kW (10,749,103.1 MJ) | work **STEADY** =0.00% · muscles over the line **GAIN** +5.13% · power **STEADY** =0.00% |
| 7 | The whole tower | 1,107 | work index 1.000; 75.27 muscles over the line a decision (6.80% of muscle-decisions); 2,967,368.7 kW (10,709,412.1 MJ) | work **STEADY** =0.00% · muscles over the line **GAIN** +1.58% · power **STEADY** =0.00% |
| 8 | The orchestra | 55 | work index 1.000; 1.72 muscles over the line a decision (3.13% of muscle-decisions); 91.5 kW (329.4 MJ) | work **STEADY** =0.19% · muscles over the line **GAIN** +63.34% · power **power given** +52.38% |
| 9 | The live engine's organism | 60 | work index 1.000; 3.73 muscles over the line a decision (6.21% of muscle-decisions); 408,580.7 kW (1,471,946.9 MJ) | work **STEADY** =0.00% · muscles over the line **GAIN** +5.61% · power **STEADY** =0.00% |
| 10 | The whole organism, three sectors | layers | the reference of every factor | work **GAIN** +24.6% · speed **GAIN** +45.3% · machines **GAIN** +5.7% · energy **GAIN** +3.1% · bill **STEADY** =0.0%; the index **GAIN** +14.5% (+13.3% to +15.8%, the gauges perfectly correlated) (the composition, by the index's rule, without the card) |

Muscles over the line: the mean change in muscles over their line each decision, as a share of the reference's own (a change counted in muscles where the reference had none). Power: the organism's electrical power against the reference's; a rise is power given, what Omni-Compass put in for the work and the time over the line beside it.

## Omni-Compass on native against native: every gauge, every run

| # | Organism | Gauge | Run A (seed 3000) | Run B (seed 3001) | Run C (seed 3002) | Reading |
|---:|---|---|---|---|---|---|
| 1 | The spine | work | =0.01% (−0.01% to +0.02%) | =0.00% (−0.01% to +0.02%) | =0.00% (−0.00% to +0.00%) | **STEADY, under the floor (the three runs' mean 0.00%)** |
| 1 | The spine | muscles over the line | +9.03% (+3.82% to +14.25%) | +8.62% (+3.39% to +13.85%) | +7.41% (+2.55% to +12.27%) | **GAIN in all three of our runs** |
| 1 | The spine | power | =0.60% (−0.91% to −0.28%) | =0.46% (−0.68% to −0.23%) | =0.42% (−0.67% to −0.17%) | **STEADY, under the floor (the three runs' mean 0.49%)** |
| 1 | The spine | spread | +0.40% (−0.21% to +1.01%) | +0.32% (−0.40% to +1.05%) | +0.27% (−0.31% to +0.86%) | **shown, not judged** |
| 2 | Compute / AI / Cloud | work | =0.00% (−0.01% to +0.01%) | =0.00% (−0.00% to +0.01%) | =0.00% (−0.00% to +0.00%) | **STEADY, under the floor (the three runs' mean 0.00%)** |
| 2 | Compute / AI / Cloud | muscles over the line | +7.28% (+2.77% to +11.79%) | +8.18% (+2.96% to +13.41%) | +6.77% (+1.98% to +11.56%) | **GAIN in all three of our runs** |
| 2 | Compute / AI / Cloud | power | +0.66% (+0.27% to +1.06%) | +0.59% (+0.26% to +0.92%) | +0.51% (+0.18% to +0.85%) | **GAIN in all three of our runs** |
| 2 | Compute / AI / Cloud | spread | +0.42% (−0.00% to +0.85%) | +0.38% (−0.09% to +0.85%) | +0.33% (−0.09% to +0.74%) | **shown, not judged** |
| 3 | Physics / Robotics / Autonomous | work | =0.00% (−0.01% to +0.02%) | =0.00% (−0.01% to +0.01%) | =0.00% (−0.00% to +0.00%) | **STEADY, under the floor (the three runs' mean 0.00%)** |
| 3 | Physics / Robotics / Autonomous | muscles over the line | +4.48% (+1.68% to +7.27%) | +3.76% (+1.09% to +6.42%) | +3.43% (+0.74% to +6.12%) | **GAIN in all three of our runs** |
| 3 | Physics / Robotics / Autonomous | power | =0.33% (−0.50% to −0.16%) | =0.26% (−0.38% to −0.13%) | =0.20% (−0.31% to −0.09%) | **STEADY, under the floor (the three runs' mean 0.26%)** |
| 3 | Physics / Robotics / Autonomous | spread | +0.02% (−0.33% to +0.37%) | +0.00% (−0.40% to +0.40%) | −0.03% (−0.40% to +0.34%) | **shown, not judged** |
| 4 | Energy / Facility / Industrial | work | =0.00% (±0.00% to ±0.00%) | =0.00% (±0.00% to ±0.00%) | =0.00% (±0.00% to ±0.00%) | **STEADY, the same** |
| 4 | Energy / Facility / Industrial | muscles over the line | +3.82% (+1.89% to +5.74%) | +2.66% (+1.38% to +3.93%) | +2.57% (+1.22% to +3.92%) | **GAIN in all three of our runs** |
| 4 | Energy / Facility / Industrial | power | =0.00% (−0.00% to −0.00%) | =0.00% (−0.00% to +0.00%) | =0.00% (−0.00% to +0.00%) | **STEADY, under the floor (the three runs' mean 0.00%)** |
| 4 | Energy / Facility / Industrial | spread | +0.13% (+0.06% to +0.21%) | +0.08% (+0.04% to +0.12%) | +0.07% (+0.03% to +0.11%) | **shown, not judged** |
| 5 | Distribution / Specialized | work | =0.00% (−0.01% to +0.02%) | =0.00% (−0.01% to +0.02%) | =0.00% (−0.01% to +0.01%) | **STEADY, under the floor (the three runs' mean 0.00%)** |
| 5 | Distribution / Specialized | muscles over the line | +7.02% (+1.26% to +12.77%) | +7.69% (+1.73% to +13.64%) | +6.95% (+1.65% to +12.25%) | **GAIN in all three of our runs** |
| 5 | Distribution / Specialized | power | =0.18% (−0.32% to −0.03%) | =0.14% (−0.23% to −0.05%) | =0.18% (−0.33% to −0.04%) | **STEADY, under the floor (the three runs' mean 0.17%)** |
| 5 | Distribution / Specialized | spread | +0.48% (−0.23% to +1.20%) | +0.37% (−0.38% to +1.12%) | +0.53% (−0.21% to +1.28%) | **shown, not judged** |
| 6 | The four stacked | work | =0.00% (−0.00% to +0.01%) | =0.00% (−0.00% to +0.01%) | =0.00% (−0.00% to +0.00%) | **STEADY, under the floor (the three runs' mean 0.00%)** |
| 6 | The four stacked | muscles over the line | +5.42% (+2.26% to +8.59%) | +5.25% (+1.99% to +8.52%) | +4.72% (+1.65% to +7.79%) | **GAIN in all three of our runs** |
| 6 | The four stacked | power | =0.00% (−0.00% to −0.00%) | =0.00% (−0.00% to −0.00%) | =0.00% (−0.00% to −0.00%) | **STEADY, under the floor (the three runs' mean 0.00%)** |
| 6 | The four stacked | spread | +0.16% (−0.09% to +0.40%) | +0.11% (−0.17% to +0.38%) | +0.12% (−0.13% to +0.37%) | **shown, not judged** |
| 7 | The whole tower | work | =0.00% (±0.00% to ±0.00%) | =0.00% (±0.00% to ±0.00%) | =0.00% (±0.00% to ±0.00%) | **STEADY, the same** |
| 7 | The whole tower | muscles over the line | +2.01% (+0.99% to +3.02%) | +1.35% (+0.70% to +2.00%) | +1.38% (+0.65% to +2.10%) | **GAIN in all three of our runs** |
| 7 | The whole tower | power | =0.00% (−0.00% to −0.00%) | =0.00% (−0.00% to +0.00%) | =0.00% (−0.00% to +0.00%) | **STEADY, under the floor (the three runs' mean 0.00%)** |
| 7 | The whole tower | spread | +0.06% (+0.02% to +0.09%) | +0.03% (+0.02% to +0.05%) | +0.03% (+0.01% to +0.05%) | **shown, not judged** |
| 8 | The orchestra | work | =0.16% (−0.19% to +0.50%) | =0.13% (−0.23% to +0.49%) | =0.29% (−0.07% to +0.66%) | **STEADY, under the floor (the three runs' mean 0.19%)** |
| 8 | The orchestra | muscles over the line | +66.42% (+25.40% to +107.44%) | +68.35% (+30.04% to +106.67%) | +55.26% (+29.15% to +81.37%) | **GAIN in all three of our runs** |
| 8 | The orchestra | power | +60.29% (+50.07% to +70.51%) | +47.18% (+38.85% to +55.51%) | +49.66% (+41.01% to +58.31%) | **power given in all three of our runs** |
| 8 | The orchestra | spread | −11.30% (−19.95% to −2.65%) | −8.98% (−18.43% to +0.48%) | −6.23% (−15.06% to +2.60%) | **shown, not judged** |
| 9 | The live engine's organism | work | =0.00% (−0.00% to +0.00%) | =0.00% (±0.00% to ±0.00%) | =0.00% (±0.00% to ±0.00%) | **STEADY, the same** |
| 9 | The live engine's organism | muscles over the line | +5.67% (+1.80% to +9.53%) | +5.16% (+1.32% to +8.99%) | +6.00% (+1.58% to +10.42%) | **GAIN in all three of our runs** |
| 9 | The live engine's organism | power | =0.00% (−0.00% to −0.00%) | =0.00% (−0.00% to −0.00%) | =0.00% (−0.00% to −0.00%) | **STEADY, under the floor (the three runs' mean 0.00%)** |
| 9 | The live engine's organism | spread | +0.13% (+0.03% to +0.24%) | +0.13% (+0.01% to +0.24%) | +0.10% (+0.02% to +0.18%) | **shown, not judged** |
| 10 | The whole organism, three sectors | work | composed: A, B and C pooled in each test | | | **GAIN** +24.56% (+21.47% to +27.72%) (the composition, by the index's rule, without the card) |
| 10 | The whole organism, three sectors | speed | composed: A, B and C pooled in each test | | | **GAIN** +45.30% (+42.16% to +48.51%) (the composition, by the index's rule, without the card) |
| 10 | The whole organism, three sectors | machines | composed: A, B and C pooled in each test | | | **GAIN** +5.67% (+5.05% to +6.30%) (the composition, by the index's rule, without the card) |
| 10 | The whole organism, three sectors | energy | composed: A, B and C pooled in each test | | | **GAIN** +3.05% (+2.71% to +3.40%) (the composition, by the index's rule, without the card) |
| 10 | The whole organism, three sectors | bill | composed: A, B and C pooled in each test | | | **STEADY** =0.00% (±0.00% to ±0.00%) (the composition, by the index's rule, without the card) |

## Each arm's own gauges, run by run (A / B / C)

The work index is each arm's work against native's own (native's is 1.0 less the share of plants that did no work in the hour); muscles over the line is the mean count each decision; power is the organism's mean electrical power; energy is the runner's total (a battery's charge left below its start bought back at its round trip); writes are the settings Omni-Compass changed before the brain went silent; the lease is every setting back at the operator's before the run ended; the pools' machines are the machines in service and starting over every pool whose own count is its knob, at the first decision, their mean over the hour and their peak (shown, never judged).

| # | Organism | Arm | Work index | Muscles over the line a decision | Power (kW) | Energy (MJ) | Muscle-decisions over the line | Writes | Lease handed back | The pools' machines: first, mean, peak |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | The spine | Native (Omni-Compass off) | 1.0000 / 1.0000 / 1.0000 | 22.09 / 21.40 / 20.64 | 3,432.9 / 3,405.7 / 3,416.7 | 13,314.90 / 13,217.11 / 13,256.59 | 5,302 / 5,137 / 4,953 | 0 / 0 / 0 | yes / yes / yes | 487, 1,499, 2,402 / 491, 1,538, 2,537 / 494, 1,505, 2,426 |
| 1 | The spine | Omni-Compass on native | 1.0001 / 1.0000 / 1.0000 | 20.10 / 19.56 / 19.11 | 3,412.5 / 3,390.1 / 3,402.4 | 13,321.83 / 13,222.44 / 13,261.56 | 4,823 / 4,694 / 4,586 | 4,596 / 4,171 / 4,099 | yes / yes / yes | 487, 1,501, 2,402 / 491, 1,539, 2,537 / 494, 1,506, 2,426 |
| 2 | Compute / AI / Cloud | Native (Omni-Compass off) | 1.0000 / 1.0000 / 1.0000 | 30.95 / 29.84 / 28.62 | 3,900.8 / 3,884.5 / 3,886.7 | 14,999.49 / 14,940.79 / 14,948.51 | 7,429 / 7,161 / 6,868 | 0 / 0 / 0 | yes / yes / yes | 884, 2,915, 4,784 / 898, 2,958, 4,884 / 896, 2,955, 4,944 |
| 2 | Compute / AI / Cloud | Omni-Compass on native | 1.0000 / 1.0000 / 1.0000 | 28.70 / 27.40 / 26.68 | 3,874.9 / 3,861.7 / 3,866.8 | 15,008.13 / 14,948.41 / 14,955.11 | 6,888 / 6,575 / 6,403 | 7,719 / 7,435 / 7,342 | yes / yes / yes | 884, 2,917, 4,784 / 898, 2,960, 4,884 / 896, 2,957, 4,944 |
| 3 | Physics / Robotics / Autonomous | Native (Omni-Compass off) | 1.0000 / 1.0000 / 1.0000 | 39.29 / 40.25 / 35.12 | 4,849.5 / 4,822.7 / 4,763.4 | 19,158.79 / 19,062.32 / 18,848.96 | 9,429 / 9,661 / 8,430 | 0 / 0 / 0 | yes / yes / yes | 588, 2,049, 3,191 / 599, 2,068, 3,281 / 600, 2,022, 3,156 |
| 3 | Physics / Robotics / Autonomous | Omni-Compass on native | 1.0000 / 1.0000 / 1.0000 | 37.53 / 38.74 / 33.92 | 4,833.5 / 4,810.3 / 4,753.8 | 19,164.38 / 19,066.63 / 18,852.28 | 9,007 / 9,298 / 8,141 | 4,930 / 4,461 / 4,465 | yes / yes / yes | 588, 2,051, 3,191 / 599, 2,069, 3,281 / 600, 2,024, 3,156 |
| 4 | Energy / Facility / Industrial | Native (Omni-Compass off) | 1.0000 / 1.0000 / 1.0000 | 40.72 / 38.87 / 38.08 | 3,047,577.7 / 2,895,877.3 / 2,918,009.5 | 10,997,420.33 / 10,451,298.89 / 10,530,974.81 | 9,773 / 9,328 / 9,140 | 0 / 0 / 0 | yes / yes / yes | 487, 1,499, 2,402 / 491, 1,538, 2,537 / 494, 1,505, 2,426 |
| 4 | Energy / Facility / Industrial | Omni-Compass on native | 1.0000 / 1.0000 / 1.0000 | 39.17 / 37.83 / 37.10 | 3,047,555.3 / 2,895,864.5 / 2,917,997.1 | 10,997,427.32 / 10,451,302.88 / 10,530,978.67 | 9,400 / 9,080 / 8,905 | 5,169 / 5,209 / 5,201 | yes / yes / yes | 487, 1,499, 2,402 / 491, 1,538, 2,537 / 494, 1,505, 2,426 |
| 5 | Distribution / Specialized | Native (Omni-Compass off) | 1.0000 / 1.0000 / 1.0000 | 28.21 / 30.25 / 30.70 | 14,251.0 / 15,013.7 / 15,953.9 | 52,259.94 / 55,005.86 / 58,390.57 | 6,770 / 7,259 / 7,367 | 0 / 0 / 0 | yes / yes / yes | 780, 2,667, 4,366 / 793, 2,726, 4,580 / 801, 2,723, 4,533 |
| 5 | Distribution / Specialized | Omni-Compass on native | 1.0000 / 1.0000 / 1.0000 | 26.23 / 27.92 / 28.56 | 14,225.8 / 14,992.4 / 15,924.6 | 52,268.89 / 55,014.31 / 58,403.68 | 6,295 / 6,701 / 6,855 | 7,215 / 7,148 / 6,972 | yes / yes / yes | 780, 2,669, 4,366 / 793, 2,728, 4,580 / 801, 2,725, 4,533 |
| 6 | The four stacked | Native (Omni-Compass off) | 1.0000 / 1.0000 / 1.0000 | 139.17 / 139.20 / 132.52 | 3,070,578.9 / 2,919,598.2 / 2,942,613.4 | 11,083,838.54 / 10,540,307.86 / 10,623,162.85 | 33,401 / 33,409 / 31,805 | 0 / 0 / 0 | yes / yes / yes | 2,739, 9,131, 14,743 / 2,781, 9,289, 15,282 / 2,791, 9,205, 15,055 |
| 6 | The four stacked | Omni-Compass on native | 1.0000 / 1.0000 / 1.0000 | 131.62 / 131.89 / 126.27 | 3,070,489.6 / 2,919,528.9 / 2,942,542.4 | 11,083,868.71 / 10,540,332.24 / 10,623,189.74 | 31,590 / 31,654 / 30,304 | 25,033 / 24,253 / 23,980 | yes / yes / yes | 2,739, 9,137, 14,743 / 2,781, 9,295, 15,282 / 2,791, 9,210, 15,055 |
| 7 | The whole tower | Native (Omni-Compass off) | 1.0000 / 1.0000 / 1.0000 | 77.39 / 76.60 / 71.81 | 3,060,316.9 / 2,909,404.0 / 2,932,385.1 | 11,044,025.61 / 10,500,739.43 / 10,583,471.31 | 18,574 / 18,383 / 17,234 | 0 / 0 / 0 | yes / yes / yes | 1,278, 4,633, 7,537 / 1,308, 4,676, 7,675 / 1,309, 4,691, 7,783 |
| 7 | The whole tower | Omni-Compass on native | 1.0000 / 1.0000 / 1.0000 | 75.84 / 75.56 / 70.82 | 3,060,294.5 / 2,909,391.2 / 2,932,372.7 | 11,044,032.60 / 10,500,743.44 / 10,583,475.20 | 18,201 / 18,135 / 16,997 | 11,619 / 11,468 / 11,511 | yes / yes / yes | 1,278, 4,633, 7,537 / 1,308, 4,676, 7,675 / 1,309, 4,691, 7,783 |
| 8 | The orchestra | Native (Omni-Compass off) | 1.0000 / 1.0000 / 1.0000 | 1.66 / 1.65 / 1.86 | 86.7 / 91.0 / 96.8 | 312.14 / 327.50 / 348.53 | 399 / 395 / 447 | 0 / 0 / 0 | yes / yes / yes | 110, 335, 493 / 109, 329, 531 / 112, 359, 607 |
| 8 | The orchestra | Omni-Compass on native | 1.0016 / 1.0013 / 1.0029 | 0.56 / 0.52 / 0.83 | 139.0 / 133.9 / 144.9 | 500.33 / 482.03 / 521.61 | 134 / 125 / 200 | 1,159 / 1,178 / 1,146 | yes / yes / yes | 110, 920, 1,380 / 109, 817, 1,355 / 112, 889, 1,494 |
| 9 | The live engine's organism | Native (Omni-Compass off) | 1.0000 / 1.0000 / 1.0000 | 3.75 / 3.96 / 3.47 | 420,892.2 / 416,491.7 / 388,358.2 | 1,516,268.30 / 1,500,426.51 / 1,399,145.98 | 900 / 950 / 833 | 0 / 0 / 0 | yes / yes / yes | 66, 256, 403 / 70, 236, 342 / 73, 263, 438 |
| 9 | The live engine's organism | Omni-Compass on native | 1.0000 / 1.0000 / 1.0000 | 3.54 / 3.75 / 3.26 | 420,890.2 / 416,488.9 / 388,356.4 | 1,516,269.29 / 1,500,427.38 / 1,399,146.63 | 849 / 901 / 783 | 830 / 763 / 739 | yes / yes / yes | 66, 258, 403 / 70, 236, 342 / 73, 263, 438 |

## The realms runner's own contrasts and label

`tools/run_realms_v5.py`'s measure of each pair, run by run (A / B / C): work (the mean over the plants of each plant's work against the reference's), the decisions over the line (the change in their share, points), the energy (power given when it rose), work per energy, the wear (shown, never judged), and the plants that did less work or missed their line more often than the reference. The label is the runner's own over the three seeds (95% intervals over the seeds). These numbers stand beside no word of their own: each carries its own direction (+ up, − down), and the label is the word.

| # | Organism | Pair | The runner's label | Work | Misses (points) | Energy | Work per energy | Wear | Plants with less work, more misses |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | The spine | Omni-Compass on native against native | **GAIN (fewer misses)** | +0.01% / +0.00% / ±0.00% | −0.75 / −0.69 / −0.57 | +0.05% / +0.04% / +0.04% | −0.05% / −0.04% / −0.04% | +0.59% / +0.46% / +0.42% | 0, 0 / 0, 0 / 0, 0 |
| 2 | Compute / AI / Cloud | Omni-Compass on native against native | **GAIN (fewer misses)** | +0.00% / +0.00% / ±0.00% | −0.42 / −0.45 / −0.36 | +0.06% / +0.05% / +0.04% | −0.05% / −0.05% / −0.04% | +0.37% / +0.33% / +0.29% | 0, 0 / 0, 0 / 0, 0 |
| 3 | Physics / Robotics / Autonomous | Omni-Compass on native against native | **GAIN (fewer misses)** | +0.00% / +0.00% / ±0.00% | −0.44 / −0.37 / −0.30 | +0.03% / +0.02% / +0.02% | −0.02% / −0.02% / −0.02% | +0.32% / +0.25% / +0.19% | 0, 0 / 0, 0 / 0, 0 |
| 4 | Energy / Facility / Industrial | Omni-Compass on native against native | **GAIN (fewer misses)** | ±0.00% / ±0.00% / ±0.00% | −0.32 / −0.22 / −0.20 | +0.00% / +0.00% / +0.00% | −0.00% / −0.00% / −0.00% | +0.33% / +0.19% / +0.18% | 0, 0 / 0, 0 / 0, 0 |
| 5 | Distribution / Specialized | Omni-Compass on native against native | **GAIN (fewer misses)** | +0.00% / +0.00% / +0.00% | −0.41 / −0.48 / −0.44 | +0.02% / +0.02% / +0.02% | −0.01% / −0.01% / −0.02% | +0.41% / +0.36% / +0.47% | 0, 0 / 0, 0 / 0, 0 |
| 6 | The four stacked | Omni-Compass on native against native | **GAIN (fewer misses)** | +0.00% / +0.00% / +0.00% | −0.40 / −0.38 / −0.33 | +0.00% / +0.00% / +0.00% | +0.00% / +0.00% / +0.00% | +0.36% / +0.29% / +0.29% | 0, 0 / 0, 0 / 0, 0 |
| 7 | The whole tower | Omni-Compass on native against native | **GAIN (fewer misses)** | ±0.00% / ±0.00% / ±0.00% | −0.14 / −0.09 / −0.09 | +0.00% / +0.00% / +0.00% | −0.00% / −0.00% / −0.00% | +0.14% / +0.08% / +0.08% | 0, 0 / 0, 0 / 0, 0 |
| 8 | The orchestra | Omni-Compass on native against native | **GAIN (fewer misses)** | +0.16% / +0.13% / +0.29% | −2.01 / −2.05 / −1.87 | +60.29% / +47.18% / +49.66% | −37.52% / −31.97% / −32.99% | +109.64% / +95.26% / +97.00% | 0, 0 / 0, 0 / 0, 0 |
| 9 | The live engine's organism | Omni-Compass on native against native | **GAIN (fewer misses)** | ±0.00% / ±0.00% / ±0.00% | −0.35 / −0.34 / −0.35 | +0.00% / +0.00% / +0.00% | −0.00% / −0.00% / −0.00% | +0.43% / +0.36% / +0.28% | 0, 0 / 0, 0 / 0, 0 |

## Organism 10, the whole organism, three sectors

The software (the cluster and the services on it), the cloud as the wire (the machines it bills) and the bare metal / the data center (the card, the machine), composed by the product law from the real tables (`tools/whole_system.py`, `results/WHOLE_SYSTEM.json`, regrouped by `docs/engine/export_whole.py`). Every factor is a ratio against native, each layer measured with its own native as its own test ran it; native carries no number of its own.

The composition's rule: R(g) = ∏ℓ Rℓ(g), log R = Σℓ log Rℓ, the variances added; a scenario sums the layers it stacks; the index is the mean of the gauge logarithms, its 95% interval under two bounds (the gauges independent; perfectly correlated); by the index's rule only what held the same way in all three of our runs enters, with every interval carried everything measured enters with its interval. The tests' engines: omni-v1; omni-v10; omni-v11; omni-v12; omni-v16; the card controller of commit c908054 (2 October), replaced since; the engine of commit 5b2832f (4 October 2026). Separability (a layer's ratio unchanged when the layer under it carries Omni-Compass), tested on the governors' four ways: 18 of 30 pairs agree.

| Scope | Reading | Sector | Layers | work | speed | machines | energy | bill |
|---|---|---|---|---|---|---|---|---|
| with the card's one run | by the index rule | the software | 3, 4 | **GAIN** +24.56% (+21.47% to +27.72%) | **GAIN** +45.30% (+42.16% to +48.51%) | **GAIN** +5.67% (+5.05% to +6.30%) | **GAIN** +3.05% (+2.71% to +3.40%) | — |
| with the card's one run | by the index rule | the cloud as the wire | 5 | — | **STEADY** =0.00% (±0.00% to ±0.00%) | **STEADY** =0.00% (±0.00% to ±0.00%) | — | **STEADY** =0.00% (±0.00% to ±0.00%) |
| with the card's one run | by the index rule | the bare metal / the data center | 1 | **STEADY** =0.00% (±0.00% to ±0.00%) | **STEADY** =0.00% (±0.00% to ±0.00%) | — | **STEADY** =0.00% (±0.00% to ±0.00%) | — |
| with the card's one run | by the index rule | the whole | all | **GAIN** +24.56% (+21.47% to +27.72%) | **GAIN** +45.30% (+42.16% to +48.51%) | **GAIN** +5.67% (+5.05% to +6.30%) | **GAIN** +3.05% (+2.71% to +3.40%) | **STEADY** =0.00% (±0.00% to ±0.00%) |
| with the card's one run | every interval carried | the software | 3, 4 | **GAIN** +24.95% (+21.72% to +28.27%) | **GAIN** +41.33% (+36.32% to +46.51%) | **GAIN** +8.53% (+7.65% to +9.42%) | **GAIN** +2.76% (+1.54% to +3.99%) | — |
| with the card's one run | every interval carried | the cloud as the wire | 5 | — | **STEADY** =4.40% (−21.50% to +38.84%) | **STEADY** =2.39% (−9.96% to +5.81%) | — | **STEADY** =0.82% (−18.83% to +21.18%) |
| with the card's one run | every interval carried | the bare metal / the data center | 1 | **STEADY** =0.00% (±0.00% to ±0.00%) | **LOSS** −36.91% (−32.96% to −40.63%) | — | **GAIN** +3.59% (+2.76% to +4.43%) | — |
| with the card's one run | every interval carried | the whole | all | **GAIN** +24.95% (+21.72% to +28.27%) | **STEADY** =6.92% (−30.61% to +24.86%) | **STEADY** =5.94% (−2.32% to +14.88%) | **GAIN** +6.45% (+4.93% to +7.99%) | **STEADY** =0.82% (−18.83% to +21.18%) |
| without the card (the cluster, the services and the cloud) | by the index rule | the software | 3, 4 | **GAIN** +24.56% (+21.47% to +27.72%) | **GAIN** +45.30% (+42.16% to +48.51%) | **GAIN** +5.67% (+5.05% to +6.30%) | **GAIN** +3.05% (+2.71% to +3.40%) | — |
| without the card (the cluster, the services and the cloud) | by the index rule | the cloud as the wire | 5 | — | **STEADY** =0.00% (±0.00% to ±0.00%) | **STEADY** =0.00% (±0.00% to ±0.00%) | — | **STEADY** =0.00% (±0.00% to ±0.00%) |
| without the card (the cluster, the services and the cloud) | by the index rule | the bare metal / the data center | none measured | — | — | — | — | — |
| without the card (the cluster, the services and the cloud) | by the index rule | the whole | all | **GAIN** +24.56% (+21.47% to +27.72%) | **GAIN** +45.30% (+42.16% to +48.51%) | **GAIN** +5.67% (+5.05% to +6.30%) | **GAIN** +3.05% (+2.71% to +3.40%) | **STEADY** =0.00% (±0.00% to ±0.00%) |
| without the card (the cluster, the services and the cloud) | every interval carried | the software | 3, 4 | **GAIN** +24.95% (+21.72% to +28.27%) | **GAIN** +41.33% (+36.32% to +46.51%) | **GAIN** +8.53% (+7.65% to +9.42%) | **GAIN** +2.76% (+1.54% to +3.99%) | — |
| without the card (the cluster, the services and the cloud) | every interval carried | the cloud as the wire | 5 | — | **STEADY** =4.40% (−21.50% to +38.84%) | **STEADY** =2.39% (−9.96% to +5.81%) | — | **STEADY** =0.82% (−18.83% to +21.18%) |
| without the card (the cluster, the services and the cloud) | every interval carried | the bare metal / the data center | none measured | — | — | — | — | — |
| without the card (the cluster, the services and the cloud) | every interval carried | the whole | all | **GAIN** +24.95% (+21.72% to +28.27%) | **GAIN** +47.54% (+10.70% to +96.66%) | **STEADY** =5.94% (−2.32% to +14.88%) | **GAIN** +2.76% (+1.54% to +3.99%) | **STEADY** =0.82% (−18.83% to +21.18%) |

The layers: 3. the cluster (Kubernetes, its add-ons, its governors), class L (measured, 22 tests); 4. the services on the cluster, class L (measured, 17 tests); 1. the card (the chip), class P (measured, 1 test); the machine (the kernel, bare metal, Kepler): not yet run (register row 79), enters as exactly 1 (not yet run, 0 tests); 5. the cloud (Azure, the bill metered), class L (measured, 3 tests).

## What stands behind the numbers

- Organism 9 is read from the harness export's own functions (`docs/engine/export_harness_trace.py` `run`, `gauges`, `interval`); the same sixty muscles run here on `run_bodies` gave, decision by decision in every arm and run, the same record.
- Every LOSS row stands where it reads; a LOSS on the factory tune is a fault to be root-caused and fixed in the next version, never a number to accept.

## Every LOSS row (0)

- none

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

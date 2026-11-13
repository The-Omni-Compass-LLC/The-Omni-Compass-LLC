# A referee's sweep of the engine that stands: where it grades, and what sign-off still needs

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Written by `tools/referee_sweep.py`; every number below is computed from the repository's records when the tool runs. The grades are a referee's judgement on those numbers. This is our own sweep, run on our own code and our own records: no outside party has reviewed or approved it, and it is not an underwriting opinion.

## The grade at a glance

| What is graded | Grade | Why, in one line |
|---|---|---|
| The mechanism and its mathematics | A | Python and C++ equal to the last bit on every law, sealed, every parity check with a planted-fault control; the release check PASS (159 checks) |
| Reproducibility and provenance | A- | every run's raw files kept and hashed; omni-v26's 80 tables written from its own archived runs (11 November), each with its recipe; four sets did not finish three runs (Volcano's, Koordinator's, Karmada's and Armada's four ways) |
| The page's wiring | A | 62 monitors, 478 named files, 0 missing; 37 with a C++ twin, the rest with the reason written |
| Statistical design | B | paired, three runs, preregistered, Student's t; but no control for many comparisons, and 206 rows earn a word by the mean when no run is beyond the noise |
| The headline's strength | C+ | the Omni index reads GAIN, up 19.97%, but without Kafka the other five read down 1.47% |
| Do no harm against native | C+ | 307 rows GAIN in all three runs, 62 LOSS in all three runs, most in the batch-queue governor tests: omni-v26 cut the target's flips there by 55% to 69%, and the conveyance's cycle rose as they fell (`docs/LOSS_CAUSES_2026-11-11.md`) |
| The chip and the cloud | D | the one A10 card's three runs disagree, no other card result stands; the cloud's bill moved inside the noise and its work was not counted |
| Independence | not yet graded | nobody outside the company has run, read or checked any of it; an underwriter signs on an outside party's replication, not on ours |
| Test coverage of the engine | B | 71% of 11,501 statements run under the tests (omni-v26); the database runners run whole only in their own benchmarks |

**Overall:** as an engineering mechanism, A-. As evidence a buyer or an underwriter could sign on today, C+. The gap is not the code; it is the evidence around it.

## 1. The headline leans on one product

The Omni index (omni-v26's tables, work, speed and machines) reads GAIN, up 19.97%. Recomputed with each product left out in turn:

| Left out | The other five |
|---|---|
| Real Kubernetes (GitHub) | up 19.52% |
| Real database (PostgreSQL behind PgBouncer, GitHub) | up 24.86% |
| Real messaging (Apache Kafka, GitHub) | down 1.47% |
| Real cache (Redis, GitHub) | up 25.68% |
| Real database cache (MongoDB under YCSB, GitHub) | up 26.26% |
| Real database buffer pool (MySQL under sysbench, GitHub) | up 27.77% |

Without Kafka the index falls below zero, because the four data stores are charged for the memory Omni-Compass gave them (their work and speed read GAIN or STEADY). On work and speed alone, the five without Kafka read up 28.76%. A referee will ask for the headline to be stated with this leave-one-out beside it, or for a headline that does not rest on one product.

## 2. Against native: how strong the rows are

Every standing table that sets Omni-Compass on native against native alone: 63 tables (omni-v12 2, omni-v25 6, omni-v26 55). The rows that read GAIN or LOSS, by how many of the three runs moved beyond the noise:

| Reading | Rows |
|---|---|
| GAIN, all three runs | 307 |
| GAIN, by the mean, 0 of 3 runs beyond the noise | 91 |
| GAIN, by the mean, 1 of 3 runs beyond the noise | 41 |
| GAIN, by the mean, 2 of 3 runs beyond the noise | 43 |
| LOSS, all three runs | 62 |
| LOSS, by the mean, 0 of 3 runs beyond the noise | 115 |
| LOSS, by the mean, 1 of 3 runs beyond the noise | 50 |
| LOSS, by the mean, 2 of 3 runs beyond the noise | 54 |

The strong rows (307 GAIN, 62 LOSS in all three runs) are the ones a referee counts. The 394 by the mean carry their word under the 0.5% rule even where no single run cleared the noise; they are shown, and they are weak.

Where the LOSS rows in all three runs sit:

| Gauge | Rows |
|---|---|
| pod start wait | 22 |
| queue: job turnaround, submitted to done | 12 |
| response time  | 10 |
| batch: queue finished | 9 |
| time over the response line | 5 |
| alert minutes | 4 |

| Table | Rows |
|---|---|
| V25_KARMADA_4W_BARE | 9 |
| V26_OCM_4W_BARE | 8 |
| V25_ARMADA_4W_BARE | 6 |
| V25_KARMADA_4W_TOP | 6 |
| V26_OCM_4W_TOP | 6 |
| V26_VANILLA | 4 |
| V25_VOLCANO_4W_BARE | 2 |
| V26_BINPACK | 2 |
| V26_GODEL_4W_TOP | 2 |
| V26_KAI_4W_TOP | 2 |

They are the batch queue sharing a cluster with a web service under the governors (pod start waits, the queue finishing later, job turnaround). omni-v26 was landed to fix the fault read on omni-v25 (`docs/OMNI_V26.md`, the target's flips); its tables, written from its own runs on 11 November, read the flips down by 55% to 69% on every scheduler rig and not to none, the conveyance's cycle up by about half, and the governor's own processor unchanged, each counted from the governor's own audit (`results/GOVERNOR_WRITES.md`, `docs/LOSS_CAUSES_2026-11-11.md`). Do no harm is not yet shown on these workloads.

## 3. What sign-off needs, in order

1. **Fix the conveyance's cycle and read the remaining target writes** (the next version, through the model gate, its model set from these runs' own files; free): then the governor tests' three runs again on that engine.
2. **Close the Kubernetes beat question** (free, running: `docs/PACE_PREREGISTRATION.md`, amendment 7), and land the beat that reads best as the next version through the model gate; then every Kubernetes test again on it.
3. **State the headline with its leave-one-out**, or name a primary endpoint per product before the next campaign, so one product cannot carry the whole.
4. **Control for many comparisons**: declare the primary gauge of each test before its runs, and read the rest as secondary; a word earned with no run beyond the noise is reported as such.
5. **Measure the two places beyond the software end**: the cloud's work for each dollar over three runs on one engine, and the chip's own meter on the engine that stands (both paid: each needs the owner's approval first).
6. **An outside replication**: a party with no stake runs the published recipe on its own machines and writes what it finds. Nothing else turns this record into something an underwriter can sign.
7. **Keep main green**: GitHub's release check failed on every push to main from 9 to 11 November, and the job that refreshes the front page failed with it on a stale release manifest; both were repaired on 11 November. The front page's own rebuild had stopped at one incomplete Kafka run on every refresh from 31 October, its failure hidden by a pipe, so no store table landed by itself on omni-v25 or omni-v26; repaired the same day (`tools/front_page.py`).

## Reproduce

`python3 tools/referee_sweep.py --json` prints every number above from the records it names.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

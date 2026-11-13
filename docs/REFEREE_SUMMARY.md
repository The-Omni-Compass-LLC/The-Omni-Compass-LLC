# The referee's summary: what Omni-Compass claims, what has been measured, and what is undetermined

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Two pages for a CTO, an engineer, a CFO or an attorney who needs the standing of every claim before reading anything else.
Every number names its engine and its evidence class: L is live software, the real thing; S is our own models, never
proof; P is a physical meter (the cards' own power meters). Every reading is the key's (`docs/HOW_TO_READ_THE_RESULTS.md`), decided by what the gauge is for: from a change of 0.5% or
more, GAIN, LOSS or power given, in all three of our runs (A, B and C) or by the mean of the three with the count beyond the
noise; STEADY under that floor; the runs disagree where clear runs point opposite ways. Beside every gain stands what it cost. Where no proof exists yet, the word is
**undetermined**.

## 1. What it is

A supervisory governor. It sits on top of a system's own controller (Kubernetes' autoscaler, a database's pool, a battery's
controller), reads the system, and moves the same settings native moves, inside bounds the system and its operator set. It
hands every setting back to native's value when it stops, dies or is switched off (`docs/SAFETY_CASE.md`).

## 2. Each claim and its standing

<!-- results: referee_claims (tools/results_chapter.py) -->
Every standing below is written from its record by `python3 tools/results_chapter.py`, and `verify.py` fails a push where it
differs.

| Claim | Standing | Evidence |
|---|---|---|
| It sits on top of native and never replaces it | **Shown** | Every live test runs native, and Omni-Compass on top of the same native; the setting is read back at native's value at the end of every arm |
| It does no harm: never a LOSS against native | **Not shown**: 288 rows read LOSS against its own native on the tables that stand | Each named with its cause and on the next version's list (`docs/LOSS_LEDGER.md`) |
| More work, faster, on real Kubernetes | **Shown** (L, omni-v26) | All four at once: work inside the response line up 31% to 50% (`results/live/V26_ALL_FOUR.md`); the 95th percentile cut in 9 of 11 Kubernetes tests (`docs/BENEFIT_SHEET.md`) |
| More work, faster, on databases and caches | **Small** (L, omni-v26) | Redis, the cache's memory ceiling: GAIN, power given, 4.9% LOSS; PostgreSQL, the pooler's pool size: GAIN AND LOSS, 1.8% LOSS; MySQL, the buffer pool's size: GAIN, power given, 12.5% LOSS; MongoDB, the storage engine's cache size: GAIN AND LOSS, 7.1% LOSS; Kafka, the consumer group's size: GAIN, power given, 221.1% GAIN (`docs/BENEFIT_SHEET.md`) |
| Fewer machines | **Shown in 2 tests** (L, omni-v26) | a service rightsized by CruiseKube applying its own recommendations, Omni-Compass on top, ten pairs, three runs: machines cut 0.3% to 5.3%, machine-hours cut 0.5% to 5.1%; a queue of jobs: machines cut 13% to 28%, machine-hours cut 13% to 28%, machines after the queue cut 22% to 45% |
| A smaller cloud bill | **Not shown** | Azure, omni-v18, 97 paired repetitions: the bill up 1.2%, inside the noise, and the work not counted (`results/live/AKS_STEADY_100_OMNI_V18.md`); Google and Amazon wired and not yet run |
| Less energy for the work, on the chip | **GAIN in all three of our runs** on one card (P, omni-v23) | An A10 fully loaded, its own power meter: energy per served request in runs A, B and C GAIN, 1.79%; GAIN, 1.35%; GAIN, 0.78% (`results/gpu/V23_A10_CAP_FULL_ABC.md`); an A100 on omni-v21: STEADY, under the floor (the three runs' mean 0.12%) (`results/gpu/V21_A100_CAP_ABC.md`); energy at the software end is a declared model (S), never scored |
| More work for the bill on a GPU | **the runs disagree** (P, omni-v23) | The A10's work for each dollar, its three runs up 1.46%, up 0.73%, down 0.69% (`results/TWO_BILLS.md`) |
| One governor over every muscle and organism | **Modelled** (S) | 1,107 muscles in our own models: 530 GAIN, 577 STEADY, 0 LOSS (`results/realms_v5/REALMS_V5.md`); a few dozen knobs on real systems |
| Its mathematics | **Machine-checked where stated** | 24 of 24 theorems proved by SMT and interval arithmetic on the engine as it executes: the compass law, the plug's clip, the verdict, the invariance of E, I and S, the tracking bound inside the basin and the steps to reach it, the bath's stability (`docs/ENGINE_PROOFS.md`); open: CERT-10 for every fixture, convergence of the whole six-state system (`docs/FORMAL_STATUS.md`) |
<!-- end of results: referee_claims -->

## 3. Real Kubernetes, each gain beside its cost (L, three runs of ten pairs, kind on one GitHub runner)

<!-- results: referee_tests (tools/results_chapter.py) -->
Each test's newest three-run table (the benefit sheet's record, `results/BENEFIT_SHEET.json`), written by `python3
tools/results_chapter.py`: what it gained and what it cost or lost, in the table's own words, each the span of the three runs'
changes.

| Test (engine) | Gain | What it cost, or read LOSS |
|---|---|---|
| Steady work (omni-v26) | mean response cut 47% to 50%; p95 cut 66% to 67%; p99 cut 71% to 73%; time over the line cut 98% to 100%; alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) cut 100%; pods started cut 4% to 29%; pod start wait, total (s) cut 7% to 35%; pod start wait, mean (s) cut 2% to 10% | replicas up 3.2% to 4.7% (power given) |
| Faults (omni-v26) | mean response cut 36% to 50%; p95 cut 54% to 62%; p99 cut 31% to 62%; time over the line cut 20% to 26%; alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) cut 11% to 13% | pod start wait, total (s) up 67% to 92% (LOSS); replicas up 26% to 30% (power given); pods started up 65% to 94% (power given) |
| Demand that wanders (omni-v26) | mean response cut 36% to 41%; p95 cut 48% to 54%; time over the line cut 29% to 37%; alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) cut 22% to 29% | pod start wait, total (s) up 108% to 133% (LOSS); pod start wait, mean (s) up 9% to 21% (LOSS); replicas up 24% to 31% (power given); pods started up 67% to 131% (power given) |
| All four at once (omni-v26) | work inside the line up 31% to 50%; mean response cut 34% to 43%; p95 cut 42% to 53%; time over the line cut 30% to 35%; alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) cut 19% to 26% | pod start wait, total (s) up 107% to 167% (LOSS); pod start wait, mean (s) up 15% to 35% (LOSS); replicas up 5% to 15% (power given); pods started up 75% to 87% (power given) |
| A service rightsized by Goldilocks and the VPA's recommender, Omni-Compass on top, ten pairs, three runs (omni-v26) | mean response cut 34% to 37%; p95 cut 39% to 45%; p99 cut 36% to 38%; time over the line cut 84% to 86% | parked-worker energy up 1.1% to 1.7% (power given); standby-model energy up 1.1% to 1.7% (power given); replicas up 29% to 35% (power given); pods started up 73% to 100% (power given); pod start wait, total (s) up 96% to 149% (LOSS); pod start wait, mean (s) up 12% to 22% (LOSS) |
| A service rightsized by CruiseKube applying its own recommendations, Omni-Compass on top, ten pairs, three runs (omni-v26) | machines cut 0.3% to 5.3%; machine-hours cut 0.5% to 5.1%; standby-model energy cut 0.0% to 3.6% | mean response up 0.5% to 1.8% (LOSS); p95 up 0.7% to 3.1% (LOSS); p99 up 5.8% to 8.9% (LOSS); pods started up 0% to 20% (power given); pod start wait, total (s) up 0% to 14% (LOSS) |
| A queue of jobs (omni-v26) | machines cut 13% to 28%; machine-hours cut 13% to 28%; standby-model energy cut 9% to 19%; mean response cut 5.4% to 9.9%; p95 cut 0.3% to 2.1%; machines after the queue cut 22% to 45% | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) up 1.0% to 3.6% (LOSS); pod start wait, total (s) up 129% to 1700% (LOSS); pod start wait, mean (s) up 14% to 800% (LOSS); queue finished up 2.4% to 3.1% (LOSS); replicas up 1% to 25% (power given); pods started up 100% (power given) |
| A public day of demand (Google 2011) (omni-v26) | mean response cut 49% to 50%; p95 cut 60% to 64%; p99 cut 47% to 54%; time over the line cut 76% to 77%; failed requests cut 8% to 15%; alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) cut 60% to 68% | pod start wait, total (s) up 163% to 173% (LOSS); replicas up 14% to 26% (power given); pods started up 126% to 166% (power given) |
| A noisy neighbour (omni-v26) | mean response cut 0.4% to 8.0% | p95 up 5% to 11% (LOSS); pod start wait, total (s) up 10% to 23% (LOSS); second app: response time (ms), 95th percentile up 0% to 12% (LOSS); second app: failed requests (%) up 2.0% to 3.3% (LOSS); replicas up 2.0% to 4.0% (power given); pods started up 7% to 18% (power given) |
| With its add-ons: KEDA's HTTP add-on on the live requests in flight, Omni-Compass on top, ten pairs, three runs (omni-v26) | mean response cut 46% to 49%; p95 cut 41% to 49%; p99 cut 21% to 23%; time over the line cut 64% to 70%; alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) cut 59% to 71%; replicas cut 8% to 14% | parked-worker energy up 1.7% to 1.8% (power given); standby-model energy up 1.7% to 1.8% (power given) |
| With its add-ons: KEDA on the CPU target and the live requests in flight, Omni-Compass on top, ten pairs, three runs (omni-v26) | mean response cut 28% to 29%; p95 cut 33% to 40%; p99 cut 27% to 34%; time over the line cut 54% to 82% | parked-worker energy up 1.4% to 1.6% (power given); standby-model energy up 1.4% to 1.6% (power given); replicas up 22% to 31% (power given); pods started up 56% to 74% (power given); pod start wait, total (s) up 36% to 112% (LOSS) |
<!-- end of results: referee_tests -->

The processor given in the add-on tests was idle on machines already running. Where machines are billed by the hour, idle
processor put to work costs nothing more unless it raises the machine count, and in these tests the machine count did not
rise. Where processor is billed by use, it is a cost, and the table shows it.

## 4. What is undetermined, and what decides it

- **The cloud bill**: the Azure sets on the engine that stands (one at a time); Google once its key is stored whole; Amazon once its account is on the
  Paid plan.
- **Energy**: a rented machine with the processor's own energy counters and a wall meter.
- **The GPU at scale**: an A100 and an A10 have three-run tables of their own; the eight-card box and the organisms on the card
  are the next runs, each from one exact commit.
- **Production**: a deployment on a customer's system with their sign-off.
- **Outside review**: no outside party has reviewed, replicated or approved any result here.

## 5. How to check any number yourself

Every table names its runs; `scripts/raw_archive.sh open /run-<id>/` places the run's raw files at the path the table
names, with their SHA-256 sums, and the table's own tool rebuilds the table from them (`tools/confirm_abc.py`,
`tools/redis_abc.py`, and the like). `python3 tools/omni_version.py --commit <sha>` names the engine a run's commit carries.
`python3 verify.py` runs every test and check the repository holds.

Run and scored by Dubra Software Inc. / The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

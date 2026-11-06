# The receipts, in their totality: what every result shows, and what it does not

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

A **receipt** here is a result file in this repository made by a paired run: the system as it runs on its own
(native) and the same system with Omni-Compass on top, the same work in both arms, the rules written down before the
counted runs, the engine identified by its fingerprint (`tools/omni_version.py --commit`), every row reported, losses
included. A receipt is read in the class of evidence it is: **P** a physical meter, **L** real software (a real
Kubernetes cluster, a real database), **S** our own models, **V** a property of the code. S is never presented as
proof of a physical saving. A result belongs to the engine it ran on and is never read across engines. Each test is read
from its own newest three-run table, and every line below names the engine its runs were on; omni-v25, the engine that
stands since 3 November, runs every benchmark again, and its tables replace these as they land (what each version changed:
`docs/CHANGE_CONTROL.md`). Every section below is written from its records by `python3 tools/results_chapter.py`, and
`verify.py` fails a push where any of it differs from them.
How to read a single table: `docs/HOW_TO_READ_THE_RESULTS.md`. The wording of every three-run row: `tools/readings.py`.

## 1. What the receipts say, read together

<!-- results: referee_claims (tools/results_chapter.py) -->
Every standing below is written from its record by `python3 tools/results_chapter.py`, and `verify.py` fails a push where it
differs.

| Claim | Standing | Evidence |
|---|---|---|
| It sits on top of native and never replaces it | **Shown** | Every live test runs native, and Omni-Compass on top of the same native; the setting is read back at native's value at the end of every arm |
| It does no harm: never a LOSS against native | **Not shown**: 287 rows read LOSS against its own native on the tables that stand | Each named with its cause and on the next version's list (`docs/LOSS_LEDGER.md`) |
| More work, faster, on real Kubernetes | **Shown** (L, omni-v25) | All four at once: work inside the response line up 31% to 65% (`results/live/V25_ALL_FOUR.md`); the 95th percentile cut in 8 of 11 Kubernetes tests (`docs/BENEFIT_SHEET.md`) |
| More work, faster, on databases and caches | **Small** (L, omni-v25) | Redis, the cache's memory ceiling: GAIN, power given, 6.8% LOSS; PostgreSQL, the pooler's pool size: GAIN AND LOSS, 1.4% LOSS; MySQL, the buffer pool's size: GAIN, power given, 9.5% LOSS; MongoDB, the storage engine's cache size: GAIN AND LOSS, 4.8% LOSS; Kafka, the consumer group's size: GAIN, power given, 218.6% GAIN (`docs/BENEFIT_SHEET.md`) |
| Fewer machines | **Shown in 1 test** (L, omni-v25) | a queue of jobs: machines cut 12% to 19%, machine-hours cut 12% to 19%, machines after the queue cut 21% to 32% |
| A smaller cloud bill | **Not shown** | Azure, omni-v18, 97 paired repetitions: the bill up 1.2%, inside the noise, and the work not counted (`results/live/AKS_STEADY_100_OMNI_V18.md`); Google and Amazon wired and not yet run |
| Less energy for the work, on the chip | **GAIN in all three of our runs** on one card (P, omni-v23) | An A10 fully loaded, its own power meter: energy per served request in runs A, B and C GAIN, 1.79%; GAIN, 1.35%; GAIN, 0.78% (`results/gpu/V23_A10_CAP_FULL_ABC.md`); an A100 on omni-v21: STEADY, under the floor (the three runs' mean 0.12%) (`results/gpu/V21_A100_CAP_ABC.md`); energy at the software end is a declared model (S), never scored |
| More work for the bill on a GPU | **the runs disagree** (P, omni-v23) | The A10's work for each dollar, its three runs up 1.46%, up 0.73%, down 0.69% (`results/TWO_BILLS.md`) |
| One governor over every muscle and organism | **Modelled** (S) | 1,107 muscles in our own models: 530 GAIN, 577 STEADY, 0 LOSS (`results/realms_v5/REALMS_V5.md`); a few dozen knobs on real systems |
| Its mathematics | **Machine-checked where stated** | 24 of 24 theorems proved by SMT and interval arithmetic on the engine as it executes: the compass law, the plug's clip, the verdict, the invariance of E, I and S, the tracking bound inside the basin and the steps to reach it, the bath's stability (`docs/ENGINE_PROOFS.md`); open: CERT-10 for every fixture, convergence of the whole six-state system (`docs/FORMAL_STATUS.md`) |
<!-- end of results: referee_claims -->

## 2. Receipt by receipt

"In all three" means the same sign in runs A, B and C with every 95% interval clear of zero; STEADY means a change under
the 0.5% floor, or no change at all (the key, `tools/readings.py`). Run and scored by The Omni-Compass LLC's own code. No
outside party has reviewed or approved these results.

### Real software and our own models (L and S)

<!-- results: sheet (tools/results_chapter.py) -->
Every test's newest table in one place, written from the same record (`results/BENEFIT_SHEET.json`) by `python3
tools/results_chapter.py`; the gauges behind each reading, in the table's own words, are in `docs/BENEFIT_SHEET.md`.

| Test | Class | Engine | Reading | By the index's rule | Table |
|---|---|---|---|---:|---|
| Every real test together: the Omni index | L | omni-v25 | **GAIN AND LOSS** | 20.4% GAIN | `results/OMNI_INDEX.md` |
| The six organisms with the real cluster inside, 10 and 100 copies | L | omni-v3 | **GAIN, power given** | 5.3% GAIN | `results/live/V3_SIX_KUBE.md` |
| The big organisms with the real cluster inside, 1,000 copies on Azure | L | omni-v3 | **GAIN** | 155.0% GAIN | `results/live/V3_BIG_ORGANISM.md` |
| The 945 modelled muscles as one tower, every muscle written at once | S | omni-v3 | **GAIN** | 0.3% GAIN | `results/realms/REALMS.md` |
| Robustness: the two-hour run | L | omni-v25 | **GAIN AND LOSS** | 8.9% LOSS | `results/live/V25_ROBUST_LONG.md` |
| Robustness: the governor killed outright mid-run | L | omni-v25 | **GAIN AND LOSS** | 1.5% LOSS | `results/live/V25_ROBUST_KILL.md` |
| Robot arms (MuJoCo), the three untouched robots | S | omni-v25 | **GAIN** | 3.8% GAIN | `results/live/V25_MUJOCO.md` |
| Redis, the cache's memory ceiling | L | omni-v25 | **GAIN, power given** | 6.8% LOSS | `results/live/V25_REDIS.md` |
| Real Kubernetes, steady work | L | omni-v25 | **GAIN, power given** | 30.8% GAIN | `results/live/V25_STEADY.md` |
| Real Kubernetes, faults | L | omni-v25 | **GAIN AND LOSS** | 25.2% GAIN | `results/live/V25_FAULTS.md` |
| Real Kubernetes, demand that wanders | L | omni-v25 | **GAIN AND LOSS** | 23.4% GAIN | `results/live/V25_WANDERING.md` |
| Real Kubernetes, all four at once | L | omni-v25 | **GAIN AND LOSS** | 29.1% GAIN | `results/live/V25_ALL_FOUR.md` |
| Real Kubernetes, a service rightsized by Goldilocks and the VPA's recommender, Omni-Compass on top, ten pairs, three runs | L | omni-v25 | **GAIN AND LOSS** | 22.6% GAIN | `results/live/V25_GOLDILOCKS.md` |
| Real Kubernetes, a service rightsized by CruiseKube applying its own recommendations, Omni-Compass on top, ten pairs, three runs | L | omni-v25 | **GAIN AND LOSS** | 0.9% LOSS | `results/live/V25_CRUISEKUBE.md` |
| Real Kubernetes, a queue of jobs | L | omni-v25 | **GAIN AND LOSS** | 9.0% GAIN | `results/live/V25_BATCH.md` |
| Real Kubernetes, a public day of demand (Google 2011) | L | omni-v25 | **GAIN AND LOSS** | 35.3% GAIN | `results/live/V25_TRACE_GOOGLE2011.md` |
| Real Kubernetes, a noisy neighbour | L | omni-v25 | **GAIN AND LOSS** | 2.3% LOSS | `results/live/V25_FAIRNESS.md` |
| Real Kubernetes, With its add-ons: KEDA's HTTP add-on on the live requests in flight, Omni-Compass on top, ten pairs, three runs | L | omni-v25 | **GAIN AND LOSS** | 28.0% GAIN | `results/live/V25_KEDA_REQUESTS.md` |
| Real Kubernetes, With its add-ons: KEDA on the CPU target and the live requests in flight, Omni-Compass on top, ten pairs, three runs | L | omni-v25 | **GAIN AND LOSS** | 9.0% GAIN | `results/live/V25_KEDA_CPU_REQUESTS.md` |
| Power grids (SimBench), both load models | S | omni-v25 | **GAIN, power given** | 5.8% GAIN | `results/live/V25_PANDAPOWER.md` |
| PostgreSQL, the pooler's pool size | L | omni-v25 | **GAIN AND LOSS** | 1.4% LOSS | `results/live/V25_PGBENCH.md` |
| MySQL, the buffer pool's size | L | omni-v25 | **GAIN, power given** | 9.5% LOSS | `results/live/V25_SYSBENCH.md` |
| MongoDB, the storage engine's cache size | L | omni-v25 | **GAIN AND LOSS** | 4.8% LOSS | `results/live/V25_YCSB.md` |
| Kafka, the consumer group's size | L | omni-v25 | **GAIN, power given** | 218.6% GAIN | `results/live/V25_KAFKA.md` |
| Drone swarms, the three untouched cells | S | omni-v25 | **GAIN** | 2.9% GAIN | `results/live/V25_SWARM.md` |
| Buildings and batteries (CityLearn), the districts with batteries | S | omni-v25 | **GAIN** | 1.4% GAIN | `results/live/V25_CITYLEARN.md` |
<!-- end of results: sheet -->

### Through a cloud (L)

<!-- results: cloud (tools/results_chapter.py) -->
**Azure Kubernetes Service, the steady set of 100 paired repetitions on omni-v18: the bill, the machines, the service**
(`results/live/AKS_STEADY_100_OMNI_V18.md`; run 40069633316, engine omni-v18, 97 paired repetitions read). The record's own
reading, carried from it by `python3 tools/results_chapter.py`, its retired word for no difference beyond the noise written as
the key's STEADY: the compute bill at list price up 1.2% by the mean of the 97 pairs, its 95% interval across zero (−$0.0007 to
+$0.0021 a repetition): power given, not beyond the noise; machines billed up 1.2%, the same; the response time's 99th
percentile GAIN (down 11.0%, its interval clear of zero); every other service gauge STEADY or not beyond the noise; failed
requests up 3.9% by the mean, its interval across zero. The stopping rule read the bill at every look and never decided it, so
the set ran to the paid cap of 100.
<!-- end of results: cloud -->

### A physical meter (P)

<!-- results: chips (tools/results_chapter.py) -->
Every three-run table of a card's own meter (class P) in `results/gpu/`, written from the tables by `python3
tools/results_chapter.py`, newest engine first: the headline gauges in the table's own words, then how all its rows read by the
one key; every row stands in the table. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or
approved these results.

- **The organisms on the eight-card machine: six organisms, each on its own A100, three runs on rented machines**
  (`results/gpu/V23_A100_8CARD_STACKS_ABC.md`, omni-v23): 225 rows, the stacks (our own models, class S): 36 shown, not judged, 24
  other; the card (its own meter, class P): 63 shown, not judged, 42 other; both together: 36 shown, not judged, 24 other.
- **The card on omni-v23, the power cap at 70% of the card's top (cap): three runs on an A10**
  (`results/gpu/V23_A10_CAP_ABC.md`, omni-v23): energy per served request (J) STEADY, under the floor (the three runs' mean
  0.38%); requests served STEADY, the same; response time, 95th percentile (ms) the runs disagree. Its 13 gauges: 3 GAIN, 7
  STEADY, 3 the runs disagree.
- **The card on omni-v23, the power cap at 70% of the card's top, the full load (cap-full): three runs on an A10**
  (`results/gpu/V23_A10_CAP_FULL_ABC.md`, omni-v23): energy per served request (J) GAIN in all three of our runs; requests served
  the runs disagree; response time, 95th percentile (ms) the runs disagree. Its 13 gauges: 7 GAIN, 1 STEADY, 5 the runs disagree.
- **The card's compute run on omni-v23: an A10 at the usual load, the firmware alone against Omni-Compass on top, three runs on
  rented cards** (`results/gpu/V23_A10_FAST_ABC.md`, omni-v23): energy per served request (J) STEADY, under the floor (the three
  runs' mean 0.13%); requests served STEADY, the same; response time, 95th percentile (ms) the runs disagree. Its 13 gauges: 12
  STEADY, 1 the runs disagree.
- **The organisms on the card, fully loaded: the seven organisms with an A10 inside, the card offered 1.3 times its full-power
  capacity, three runs on rented cards** (`results/gpu/V23_A10_STACKS_FULL_ABC.md`, omni-v23): 300 rows, the stacks (our own
  models, class S): 56 STEADY, 24 shown, not judged; the card (its own meter, class P): 1 GAIN, 6 power given, 84 STEADY, 7 LOSS,
  42 shown, not judged; both together: 56 STEADY, 24 shown, not judged.
- **The card on omni-v21, the power cap at 70% of the card's top (cap): three runs on an A100**
  (`results/gpu/V21_A100_CAP_ABC.md`, omni-v21): energy per served request (J) STEADY, under the floor (the three runs' mean
  0.12%); requests served STEADY, the same; response time, 95th percentile (ms) the runs disagree. Its 13 gauges: 2 GAIN, 8
  STEADY, 2 LOSS, 1 the runs disagree.
- **The card on omni-v21, the power cap at 70% of the card's top (cap-full): three runs on an A100**
  (`results/gpu/V21_A100_CAP_FULL_ABC.md`, omni-v21): energy per served request (J) STEADY, under the floor (the three runs' mean
  0.07%); requests served STEADY, under the floor (the three runs' mean 0.15%); response time, 95th percentile (ms) LOSS by the
  mean of our three runs, beyond the noise in 0 of 3. Its 13 gauges: 1 GAIN, 10 STEADY, 2 LOSS.
- **The card on omni-v21, the tune-down (dial save): three runs on an A100** (`results/gpu/V21_A100_SAVE_ABC.md`, omni-v21):
  energy per served request (J) GAIN by the mean of our three runs, beyond the noise in 1 of 3; requests served STEADY, the same;
  response time, 95th percentile (ms) STEADY, under the floor (the three runs' mean 0.04%). Its 13 gauges: 6 GAIN, 6 STEADY, 1 the
  runs disagree.
- **The stacked box on omni-v21: the seven organisms with an A10 inside, three runs on rented cards**
  (`results/gpu/V21_STACKS_A10_ABC.md`, omni-v21): 260 rows, the stacks (our own models, class S): 56 STEADY, 24 shown, not
  judged; the card (its own meter, class P): 1 GAIN, 2 power given, 63 STEADY, 3 LOSS, 1 the runs disagree, 30 shown, not judged;
  both together: 56 STEADY, 24 shown, not judged.
<!-- end of results: chips -->

### The code (V)

The max's guarantees, one by one, with the code path that makes each one true: `docs/FORMAL_V5.md`. The theorems proved by
SMT and interval arithmetic on the engine as it executes: `docs/ENGINE_PROOFS.md`, and what is still open:
`docs/FORMAL_STATUS.md`. The safety shield's four properties (no invariant violated, idempotent, no invented action, minimal
intervention) are checked over 100,000 random and adversarial cases on every push and 1,000,000 in a full check (`verify.py`),
and held over 2,000,000 when the test was run on its own on 3 November 2026 (`python3 tests/test_shield_properties.py`: 0
violations); the C++ twins are checked against the Python on every push (`verify.py`).

### The archive itself

Every archived run carries `SHA256SUMS_ALL.txt`, the SHA-256 of every file in its folder. A sum is a fingerprint: it shows
that a file has not changed since the sum was written, not who wrote it. From 31 October 2026 the archive job signs each
run's sums with Sigstore, keyless, under GitHub's own identity for that job, and the signature is entered in Sigstore's
public transparency log (`SHA256SUMS_ALL.txt.sigstore.json` beside the sums). `python3 tools/verify_receipt.py <run folder>`
checks every file against its sum and the sums against their signature; a run archived before that day reads "sums only".
`python3 tools/reproduce.py` rebuilds every table from the archived runs. Neither check is an outside review: they show that
the files and the tables have not changed, not that an outside party has repeated the runs (`docs/PILOT_PROTOCOL.md` is how
that is done).

## 3. What would change these readings

- On the chip, the card's energy for each request served reads GAIN in all three runs on one A10 at the power cap's full
  load (omni-v23) and STEADY on the other card runs above; a run on other cards that showed no difference at the same work
  would confine that reading to the card and load it ran on.
- An A, B or C run that disagrees with the others turns a row into "the runs disagree"; it is looked into, never
  dropped.
- A loss in all three runs is reported as it stands, its cause looked for in our own wiring, setup and scoring first,
  and the next set run on the fix.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.
Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any
outside body.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

# Run ledger: every chip, cloud and machine run, what it cost, and what came back

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Read from GitHub's own run records on 27 October 2026 (the `lambda-gpu`, `aks-metered`, `cloud-check` and benchmark
workflows), not from memory; sections 1 and 3 read again from them on 11 November 2026. Dollar figures are the hours a machine was rented times the hourly price each launch printed
(`gpu_1x_a10`: $1.29 an hour). Lambda's own billing page is the exact figure; this page is the record of what each rental
was for, whether it finished, and where its receipt is.

## 1. GPU chips on Lambda

| GitHub run | Started (UTC) | What | Card | Hours rented | Cost | Finished? | What came back | Receipt |
|---|---|---|---|---:|---:|---|---|---|
| 40079073999 | 24 Oct 08:42 | one card, fast, omni-v18 | A10 | 0.4 | about $0.52 | No: the run refused to start (the copy shipped to the card had no git record) and the card went back | nothing; the shipping was fixed the same morning | none |
| 40079645681 | 24 Oct 08:51 | one card, omni-v18 | A100 SXM4 40 GB | 6.7 | at Lambda's A100 price (billing page) | **Yes**: one run, 10 paired repetitions | every service gauge STEADY; the governor wrote nothing in 3,050 decisions, both knobs already at their top on native (at its limit on native); wire check 7 of 7, fault drill 5 of 5 | `results/gpu/run-20261024T091235Z/GPU_REPS.md` |
| 40143765437, 40143770324, 40143775773 | 24 Oct 23:41 | the whole stacks with the card inside, A, B and C, omni-v18 | A10 ×3 | 25.1, 25.1, 25.0 | about $97 | **No**: each reached its 25-hour limit inside the stacks (1x copies done, 5 repetitions; 10x in its third) | the wire check and the smoke only: the stacks write each arm on the card and pack them only when they finish, and the watcher fetched only packed files, so every stacks arm stayed on the card when it was given back (fixed 26 October, commit `8e62252e1f`) | `raw` branch, `run-40143765437/` and the other two |
| 40218532131, 40218534998, 40218537259 | 25 Oct 17:52 | the stacks, A, B and C, omni-v21 | none | 0 | $0 | No: started as dry runs by mistake (priced, nothing rented) | the price only | none |
| 40393460334, 40393464531, 40393468676 | 26 Oct 20:11 | the stacks, A, B and C, omni-v21 | A10 ×3 | 0.1, 0.3, 0.3 | about $0.90 | Stopped on the founder's decision: they carried the watcher fault above | nothing | none |
| 40394988327, 40394992822, 40394997159 | 26 Oct 20:22 | the stacks, A, B and C, omni-v21, the watcher fixed | A10 ×3 | 33.1 each (to 28 Oct 05:30) | about $128 | **To its deadline**: sizes 1 and 10 complete in every run (5 and 3 repetitions), 100 copies one repetition a run | the card STEADY in every organism at 1 and 10 copies; two of the card's 95th-percentile rows LOSS by the mean of our three runs at 10 copies, none beyond the noise; 100 copies shown, not judged | `results/gpu/V21_STACKS_A10_ABC.md`; `raw` branch, `run-<id>/` |
| 40461604089 | 27 Oct 06:31 | one card, the factory dial (the max), omni-v21 | A100 SXM4 40 GB | 7.1 | at Lambda's A100 price (billing page) | **Yes**: 10 paired repetitions | every gauge STEADY; the governor wrote nothing: native already runs both knobs at their top (at its limit on native) | its run's own `GPU_REPS.md` on `raw`, `run-40461604089/`; `docs/AUDIT_2026-10-30.md` section 2 |
| 40485597269, 40485602065, 40485605739 | 27 Oct 10:04 | one card, the tune-down (dial save), A, B and C, omni-v21 | A100 SXM4 40 GB | 6.9 each | at Lambda's A100 price (billing page) | **Yes**: 10 paired repetitions each | work per energy GAIN by the mean of our three runs (up 0.84%, 0.71%, 0.69%; beyond the noise in 1 of 3), the energy a cut, GAIN; requests STEADY, the same; every response gauge STEADY; 312, 540 and 485 writes | `results/gpu/V21_A100_SAVE_ABC.md` |
| 40485609401, 40485613546, 40485617318 | 27 Oct 10:04 | one card, the power cap at 70% of the card's top, A, B and C, omni-v21 (two loads: the normal load and the card fully loaded) | A100 SXM4 40 GB | 4.6 each | at Lambda's A100 price (billing page) | **Yes**: 5 paired repetitions each | energy and work per energy STEADY; the mean response time LOSS by the mean of our three runs (A 1.87% slower, B STEADY, C 0.79% slower; beyond the noise in 0 of 3); fully loaded, requests not served LOSS by the mean (A 2.18% more; B and C STEADY; 0 of 3) and the 95th percentile LOSS by the mean (A 1.50% slower; 0 of 3); 7 to 78 writes | `results/gpu/V21_A100_CAP_ABC.md`, `V21_A100_CAP_FULL_ABC.md` |
| 14 runs, 24 Oct 02:57 to 08:41 | | launches that stopped before renting (the key and the shipping being set up) | none | 0 | $0 | No | nothing | none |
| 40400845313 | 26 Oct 21:01 | eight cards, pooled | none | 0 | $0 | dry run (priced only) | the price only | none |
| 41242146122 | 31 Oct 21:08 | one card, the cap, omni-v23 | none | 0 | $0 | dry run (priced only) | the price only | none |
| 41243352339, 41243355485, 41243358705 | 31 Oct 21:23 | one card under the operator's power cap at 70% of its top, A, B, C, omni-v23 (the normal load and the card fully loaded) | A10 ×3 | at most 4.1 each (each run's length on GitHub) | at most about $5.40 each | **Yes**: 5 paired repetitions each | the response time and requests served: the runs disagree (A and B GAIN, C LOSS) | `results/gpu/V23_A10_CAP_ABC.md`, `results/gpu/V23_A10_CAP_FULL_ABC.md` |
| 41243361994, 41243364991, 41243368008 | 31 Oct 21:23 | one card at the factory dial (the max), A, B, C, omni-v23 | A10 ×3 | at most 6.7 each | at most about $8.60 each | **Yes**: 10 paired repetitions each | energy per request served GAIN in all three of our runs (down 1.3%); the 95th percentile: the runs disagree | `results/gpu/V23_A10_FAST_ABC.md` |
| 41271470803, 41271473309, 41271475877 | 1 Nov 04:02 | the seven organisms with the card inside, fully loaded (1.3 times the card's full-power capacity), A, B, C, omni-v23 | A10 ×3 | at most 33.2 each | at most about $43 each | **To its deadline**: 5 paired repetitions at 1 copy in every run | the card STEADY, under the floor, in every organism read | `results/gpu/V23_A10_STACKS_FULL_ABC.md` |
| 41271477833, 41279081905, 41271481737 | 1 Nov 04:02 (B started again at 06:00: its first start, 41271479737, stopped at the launch in 30 s, nothing rented) | eight A100 cards pooled, then six organisms each on its own card, A, B, C, omni-v23 | A100 ×8 ×3 | the run's own budget, 10.5 each (each run's length on GitHub at most 10.8) | at most about $235 each at $22.32 an hour for the eight-card machine (Lambda's list price on 1 November) | **To its deadline**: one repetition a size | shown, not judged (one repetition a run) | `results/gpu/V23_A100_8CARD_STACKS_ABC.md` |
| 41859166943, 41859173103, and 41859862583 to 41859952387 (12 runs; three started again at 17:53) | 4 Nov 15:34 to 15:39 | the omni-v25 card campaign: eight cards pooled, the organisms fully loaded, the factory dial and the cap, A, B and C | none | 0 | $0 | **No**: Lambda refused every launch before anything was rented: "HTTP 403 global/account-inactive: Your account is inactive. Make sure you have verified your email address and have a valid payment method" | nothing | none |
| 42110793585 | 5 Nov 21:14 (three attempts) | a dry check of one card | none | 0 | $0 | **No**: the same refusal (the account inactive) | nothing | none |

**Rented so far:** about 308 A10 hours (about $397 at the $1.29 an hour each launch printed: 176 to 27 October, about 132 on omni-v23), about 48 single-A100 hours (6.7 on omni-v18, 41.6 on omni-v21; Lambda's billing page is the figure) and about 31.5 hours of the eight-A100 machine on omni-v23 (at most about $705 at its list price of 1 November). Lambda's own billing page is the exact figure. **Since 4 November Lambda refuses every launch: the account reads inactive (a verified email address and a valid payment method). No card run can start until the account is active again, and none starts without the founder's approval of its scope and its most it may cost (the record of 9 November, `docs/audits/V25_V26_CHAMPION_SELECTION_2026-11-09.md`).**

**What the record says about the chip** is written on its own page, `docs/THE_CHIPS.md`: at the factory dial the card
reads STEADY with no write, because native already runs both knobs at their top; the tune-down is the one tune that read
GAIN (work per energy by the mean of our three runs); the cap's LOSS rows come from run A alone, none beyond the noise;
and what the chip proof still needs, step by step, with what each step costs.

Older GPU results (2 October, `results/gpu/run-20261002T082232Z/`) are obsolete by the founder's order and stay as history.

## 2. CPU

| Benchmark | State | Why |
|---|---|---|
| The Linux CPU governor and its energy meter (`cpu-power`) | **Not run on real hardware** | GitHub's machines are virtual: no frequency governor and no energy meter. The three omni-v21 runs (A, B, C) are capability checks that read "cannot run here". It needs a bare-metal machine (a self-hosted runner). From 27 October the workflow fails if the harness's own tests or the probe fail, instead of hiding it. |
| Every Kubernetes benchmark | Run on GitHub's processors (class L) | see section 4 |

## 3. Clouds

| Cloud | State | Detail | Receipt |
|---|---|---|---|
| Azure | **On** | The omni-v18 set of 100 paired repetitions (run 40069633316) ran from 24 to 29 October: 97 passed, 3 failed (repetitions 82, 90 and 93); its table, from the run's own receipt, is `results/live/AKS_STEADY_100_OMNI_V18.md` (the bill up 1.2% by the mean of 97 pairs, its interval across zero; the 99th percentile GAIN; failed requests up 3.9% by the mean, its interval across zero, a LOSS by the 0.5% key); it stands as omni-v18's record, read in no later engine's table. The omni-v21 steady set (run 40940616527, 100 paired repetitions under the stopping rule, dial save, the machines alone) started 29 October 19:29 UTC and ended in failure on 3 November 23:40 UTC (GitHub's run record, read 5 November); its finished repetitions' files are the run's artifacts on `raw`, and it is read in no table. 26 of its 27 refused repetitions were refused by one fault of the rig's evidence tool, the pod watch's expired history (30 arms, native and Omni-Compass alike); the tool is repaired (6 November, `docs/REPAIR_20261106.md`) and the repetitions stay refused. On omni-v25, at the max with the work meter, two tuning cases ran to their end: run 41745105583 (the meter's rates 10 to 140 a second, 4 November 00:12 to 01:32 UTC) and run 41914478995 (rates 2 to 20 a second, 4 November 21:16 to 22:48 UTC); a tuning case sets the counted rates before run A and is never counted (`docs/K8S_COMPASS_PREREGISTRATION.md`). Azure runs one set at a time; the omni-v25 sets queue behind them (`scripts/azure_queue.txt`). | `results/live/AKS_BILL.md` (omni-v1: the bill STEADY); `results/live/AKS_STEADY_100_OMNI_V18.md`; the omni-v21 set's and the tuning cases' files on `raw` |
| Azure, the full-control burst set | **On** | The burst 1 4 1 6 1 9 at the tune-down, three paired repetitions a run, three runs on each engine: omni-v25 (41756593448, 41928730439, 42175112195; 4 to 6 November) and omni-v26 (42416651121, 42483841896, 42651049003; 7 to 9 November), tabled from their own receipts on 11 November. On both engines: failed requests GAIN by the mean of our three runs, the response time LOSS by the mean, the machines power given (+27% to +39% node-hours, so the bill rose). Every row shown; the LOSS rows wait for their cause. The work meter's four tuning cases (41745105583 and 41914478995 on omni-v25, 42400923213 and 42408759289 on omni-v26) set the counted rates and are never counted. Of `aks-metered`'s 99 runs, 60 were cancelled while they waited behind a running set (a newer start took the queue's one waiting place); they never ran and cost nothing | `results/live/V25_AKS_FULL_BURST.md`, `results/live/V26_AKS_FULL_BURST.md` |
| Google Cloud | **On, not set up** | Switched on by the founder's word of 1 November; its keys are not in the repository's secrets: `GCP_CREDENTIALS` and `GCP_PROJECT` (the $0 check, `cloud-check`, read them absent again on 11 November, run 42975244864). Nothing has run and nothing is billed; each day's check fails and says so | none |
| Amazon | **On, not set up** | Switched on by the founder's word of 1 November; its keys are not in the repository's secrets: `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` (the $0 check read them absent on 11 November, run 42975251931), and the account's Paid plan comes after them (`docs/AMAZON_SETUP.md`, section 1a). Nothing has run and nothing is billed; each day's check fails and says so | none |
| Oracle, DigitalOcean, Alibaba, Linode, IBM, other | Never run | wired through `byoc-metered`, no cluster connected | none |

## 4. Kubernetes, the data stores and the outside simulators on omni-v21

23 of the 26 benchmarks on the benefit board read omni-v21's own three-run table (`docs/BENEFIT_SHEET.md`, written by
`tools/benefit_sheet.py`); every table names its three GitHub runs, and every run's files are on the `raw` branch.

| Still on an older engine | Its table | What it waits for |
|---|---|---|
| The six organisms with the real cluster inside, 10 and 100 copies | `results/live/V3_SIX_KUBE.md` (omni-v3) | the grid's omni-v21 runs |
| The big organisms with the real cluster inside, 1,000 copies on Azure | `results/live/V3_BIG_ORGANISM.md` (omni-v3) | an Azure set on omni-v21 |
| The 945 modelled muscles as one tower | `results/realms/REALMS.md` (omni-v3) | its table from the omni-v21 realms runs |

Every omni-v21 table was rebuilt on 27 October from its three archived runs by `tools/reproduce.py` (the recipes in
`results/live/RECIPES.json` and the front page's own for the five data stores): all 31 tables (18 Kubernetes and simulator
tables, 13 data-store tables; 58 files), identical to the byte, and every one names omni-v21 alone (the drone swarms' table names
omni-v12 only as the engine before whose runs its preregistration's amendment 2 was written).

## 5. Open, in one list

1. GPU: the A100's three-run tables on omni-v21 are written (`results/gpu/V21_A100_SAVE_ABC.md`, `V21_A100_CAP_ABC.md`,
   `V21_A100_CAP_FULL_ABC.md`; `docs/AUDIT_2026-10-30.md` section 2). The three stacks runs on A10s reached their deadline with
   sizes 1 and 10 finished and 100 in part: read as far as they got, `results/gpu/V21_STACKS_A10_ABC.md` (the card STEADY at 1 and 10).
   What the chip proof still needs, and what each step costs: `docs/THE_CHIPS.md`, section 5. Nothing is rented before the
   founder's word.
2. Azure: the omni-v18 set finished 29 October (97 of 100 passed); the omni-v21 steady set runs (16 of 100 by 30 October,
   16:27 UTC); the omni-v22 sets queue behind it.
3. Google and Amazon: their keys (`docs/GOOGLE_SETUP.md` section 4, `docs/AMAZON_SETUP.md` section 1a).
4. CPU: a bare-metal machine, or it stays not run.
5. The three tables above still on omni-v3.
6. The LOSS rows on omni-v21, each in `docs/LOSS_LEDGER.md`: the pod start wait on the Google day (more pods started; each
   starts as fast) and on Goldilocks (each pod slower too), CruiseKube's response time by the mean, and Kafka's.
7. Omni-Compass by itself on kind (`kubernetes by itself`, three arms): every solo arm since omni-v19 had the governor's pod
   writes refused, 15 of 15 decisions in every repetition (the rig's identity lacked the workload's `deployments/scale`, the
   resource `kubectl scale` patches). omni-v21's three runs (40224674073, 40247823226, 40269972665) were admitted with the
   workload held at the operator's count and are read in no table; omni-v22's two (41115877114, 41153103781) were marked
   invalid by the rig's own end read of the autoscaler the arm removes by design (a read added 29 October). Both causes fixed
   31 October (`docs/SOLO_PREREGISTRATION.md`, amendment 1); A and B queued again behind the campaign (`scripts/reruns.txt`);
   its table, when its three runs land, stays in the record and is not carried on the front page (the order of 25 October).

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

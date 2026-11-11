# The omni-v26 batch rigs' LOSS rows, read from their own files: 11 November 2026

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The omni-v26 campaign's three-run tables landed on 11 November (`results/live/V26_*.md`, written from the archived runs on the
branch `raw` with the same tool and title as omni-v25's; their recipes in `results/live/RECIPES.json`). Every row is in them and
in the LOSS ledger (`docs/LOSS_LEDGER.md`), and no cause written for omni-v25 is carried onto an omni-v26 row unread
(`tools/loss_ledger.py`, `WRITTEN_FOR`). This page reads the batch rigs' LOSS rows from the governor's own audit in every
repetition of both engines' runs, counted by `tools/governor_writes.py` (`results/GOVERNOR_WRITES.md`, 30 repetitions a rig and
engine, Omni-Compass's arms only). Class L. Each number below is that page's mean a repetition.

## 1. What omni-v26 changed, and what it did in the runs

omni-v26 changed one rule (`docs/OMNI_V26.md`): when the web service's target stood below native's and the pods waiting included
those of a workload no autoscaler governs (the batch queue's), the decision now starts the immune hand-back's hold itself, so the
fail-up is not taken again while it runs. Its model gate read the target's flips down 88.6% in the batch queue's replay (class S).

In the real runs the flips fell, by 55% to 69% on every scheduler rig, and did not stop:

| Rig | web target writes, omni-v25 | omni-v26 |
|---|---:|---:|
| the default scheduler | 10.0 | 4.5 |
| the bin-packing profile | 10.2 | 3.4 |
| KAI | 7.3 | 2.8 |
| Kueue | 10.1 | 3.9 |
| Volcano | 7.0 | 2.7 |
| KAI, four ways | 9.3 | 4.0 |
| Kueue, four ways | 9.8 | 4.5 |
| the bin-packing profile, four ways | 10.9 | 4.0 |
| KubeRay, four ways | 6.6 | 2.9 |
| the Gödel scheduler, four ways | 8.9 | 2.8 |
| Open Cluster Management, four ways | 21.8 | 7.9 |

The model's replay is the fault's own regime; the real rigs carry the rest of the organism, and the fall is about two thirds of
the model's. Koordinator's two rigs (1.7 and 1.9 to 1.5 and 1.1) and Crane (1.6 and 1.6) flipped a tenth as often on omni-v25 and
barely moved.

## 2. What rose as the flips fell: the conveyance's cycle

On the same repetitions the conveyance (a web pod's processor limit raised above the operator's on a shared host, and handed back)
wrote about half again as often on omni-v26 on every scheduler rig where it acts:

| Rig | limit raises, omni-v25 | omni-v26 | hand-backs, omni-v25 | omni-v26 |
|---|---:|---:|---:|---:|
| the default scheduler | 41.0 | 62.0 | 38.0 | 57.5 |
| the bin-packing profile | 20.0 | 33.1 | 18.8 | 31.0 |
| KAI | 27.1 | 40.2 | 25.7 | 38.1 |
| Kueue | 37.7 | 50.8 | 29.9 | 45.4 |
| Volcano | 43.1 | 59.2 | 38.8 | 55.6 |
| KAI, four ways | 32.0 | 53.0 | 29.6 | 50.3 |
| Kueue, four ways | 43.3 | 59.1 | 38.8 | 46.6 |
| the bin-packing profile, four ways | 36.3 | 68.0 | 30.4 | 62.4 |
| KubeRay, four ways | 26.3 | 36.6 | 24.6 | 29.9 |

Nearly every raise is followed by a hand-back: the shape of the cycle read on Koordinator's rigs on omni-v25
(`docs/LOSS_CAUSES_2026-11-07.md`, section 2), where one raise took the shared host from under its 70% line to over 75% busy and
the hand-back returned every raised limit to the operator's 500m at once, so the next quiet reading raised again. On omni-v26 the
counts have that shape on every scheduler rig where the conveyance acts; on Koordinator's own rigs they are unchanged (53.2 and
49.2 raises to 50.8 and 50.7). On the Crane and Gödel rigs (Kubernetes 1.25 and 1.24) the conveyance wrote nothing on either
engine.

## 3. What did not change: the governor's own processor

The governor's own processor over each window, from its audit's overhead record, reads 0.069 to 0.083 of a core on the scheduler
rigs on omni-v26 against 0.069 to 0.086 on omni-v25: the 10 s beat on site, unchanged by the fix. On the plain batch stream, where
the governor wrote no target and raised a limit about twice a repetition on either engine, the queue's rise is read by it alone,
as on omni-v25 (`docs/LOSS_CAUSES_2026-11-05.md`): 0.083 of a core (0.059 to 0.105) against 0.086 (0.062 to 0.103).

## 4. What follows

- The LOSS rows of the scheduler rigs stand beside three measured things at once: the conveyance's cycle (up by about half), the
  remaining target flips (down by about two thirds, not to none) and the governor's own processor at the 10 s beat (unchanged).
  Which share of each row each one carries is not separated on these runs; the ledger says so row by row.
- The conveyance's fault is on the next version's list as written on 7 November: a raise sized so the shared host stays under its
  hand-back line, a hand-back that steps a limit down by what the host is over rather than all the way to the operator's, and no
  raise into processor another workload's waiting pods are owed. It goes through the model gate first, with a model whose host and
  conveyance are set from these runs' own files, then the benchmarks' three runs on that engine.
- The remaining flips: the hold now starts on the batch queue's waiting pods, and the target is still written 0 to 14 times a
  repetition. Why each of those writes was taken is read next from the audit's own reason (its `why`), before any change.
- Four sets have no three runs on omni-v26 and keep their omni-v25 tables: Volcano's four ways (run B failed), Koordinator's four
  ways (run A failed every time it ran: in the failed repetitions the arms with Koordinator installed, Koordinator as shipped and
  Omni-Compass on top of it, did not finish their queue or exited with an error, while the arms without it finished), Karmada's
  four ways (runs B and C failed) and Armada's (run B failed). Each goes back in the queue once its failure is read from its
  job's own log (Koordinator's first: its failure repeats, so a rerun alone would only repeat it).

Run and scored by Dubra Software Inc. / The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

# The Numbers a Website May Show, Each With Its Receipt

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Written by `tools/site_numbers.py` from the repository's own records; `results/SITE_NUMBERS.json` is the same in a form a page reads. Every number a page shows comes from 'show', with its word first, its class, its place, its engine and its receipt, in its own sentence. Nothing in 'not_for_the_site' is shown as a result. Our own model (class S) is never shown as proof. Percentages of different bills are never added.

| Number | Word | Why it reads so | Class | Where | Engine | Receipt |
|---|---|---|---|---|---|---|
| The Omni index: GAIN, up 20.4% (work, speed and machines; real software on GitHub's machines, omni-v25). | GAIN | the index scores the work done, the response time and the machines against native's: above native is more work, a faster answer or fewer machines; the change helps the system, so it reads GAIN. | L | the software end: real software on GitHub's own machines, never bare metal and never a cloud, with no bill in it | omni-v25 | `results/OMNI_INDEX.md` |
| On work and speed alone, the same runs: GAIN, up 94.0% (real software on GitHub's machines; not a bill). | GAIN | the same runs scored on the work done and the response time alone: above native is more work or a faster answer; the change helps the system, so it reads GAIN. | L | the software end: real software on GitHub's own machines, never bare metal and never a cloud, with no bill in it | omni-v25 | `results/OMNI_INDEX.md` |
| Real Kubernetes: GAIN, up 20.5% by the index's rule (9 tests on GitHub's machines); one reads LOSS: fairness, down 2.3%. | GAIN | the index's rule on the Kubernetes tests: above native is more work, a faster answer or fewer machines; the change helps the system, so it reads GAIN. | L | the software end: real software on GitHub's own machines, never bare metal and never a cloud, with no bill in it | omni-v25 | `results/OMNI_INDEX.md` |
| The minutes a person would be paged: GAIN in all three of our runs, down 7.4% (omni-v25). | GAIN in all three of our runs | the minutes a person on call would have a page open: fewer minutes mean less waiting on a person; the change helps the system, so it reads GAIN. | L | the software end: real software on GitHub's own machines, never bare metal and never a cloud, with no bill in it | omni-v25 | `results/OVERSIGHT.md` |
| The pages a person would be sent: GAIN by the mean of our three runs, beyond the noise in 2 of 3, down 6.7% (omni-v25). | GAIN by the mean of our three runs, beyond the noise in 2 of 3 | the pages a person would be sent: fewer pages mean less oversight; the change helps the system, so it reads GAIN. | L | the software end: real software on GitHub's own machines, never bare metal and never a cloud, with no bill in it | omni-v25 | `results/OVERSIGHT_PAGES.md` |
| On one A10 card, its own meter: energy per request served GAIN in all three of our runs, down 1.3% (omni-v23). | GAIN in all three of our runs | the energy the card's own meter read for each request served: less energy for each request served is more work from each joule; the change helps the system, so it reads GAIN. | P | the chip: one A10 card rented directly, its own power meter | omni-v23 | `results/gpu/V23_A10_CAP_FULL_ABC.md` |
| On the chip, the work for the bill: the runs disagree (up 1.5%, up 0.7%, down 0.7%); not yet shown to rise. | the runs disagree | the work done for each dollar of the card's rental: more work for the bill helps; the three runs moved in opposite directions, so the test is unstable there and no word is given. | P | the chip: one A10 card rented directly, its bill the rental | omni-v23 | `results/TWO_BILLS.md` |
| Through the cloud (Azure): the bill power given, up 1.2%, inside the noise; the work was not counted, so the work per dollar is not read yet. | power given, inside the noise | the cloud's bill is a resource spent, read beside the work it bought; more of a resource was spent beside the work it bought, so it reads power given, never a loss. | L | through the cloud: Azure, its own bill | omni-v18 | `results/live/AKS_STEADY_100_OMNI_V18.md` |
| Arm B, the chip with Omni-Compass on native, against arm A, the chip native (one A10, three runs, omni-v23): the work for the bill up 1.5%, up 0.7%, down 0.7%: the runs disagree, not yet shown to rise. | the runs disagree | the work done for each dollar on the chip, Omni-Compass on native (B) against native (A); the three runs moved in opposite directions, so the test is unstable there and no word is given. | P | the same card, the same rented window | omni-v23 | `results/TWO_BILLS.md (results/gpu/V23_A10_CAP_FULL_ABC.md)` |
| Arm D, the cloud with Omni-Compass on native, against arm C, the cloud native (Azure, 97 paired repetitions, one run, omni-v18): the 99th percentile GAIN, down 11.0%, beyond the noise; the bill power given, up 1.2%, inside the noise; machine-hours power given, up 1.2%, inside the noise; the mean response time GAIN, down 2.7%, inside the noise; the 95th percentile GAIN, down 4.0%, inside the noise; failed requests LOSS, up 3.9%, inside the noise; the alert minutes GAIN, down 1.2%, inside the noise; the energy power given, up 0.6%, inside the noise; the work not counted, so the work per dollar is not read yet. | one run, read gauge by gauge: LOSS on failed requests; GAIN on the mean response time, the 95th percentile, the 99th percentile, the alert minutes; power given on the bill, machine-hours, the energy; beyond the noise in the 99th percentile | the cloud, Omni-Compass on native (D) against native (C), gauge by gauge; one run so far, so there is no three-run reading yet. | L | Azure (AKS), the same machines, paired with C | omni-v18 | `results/live/AKS_STEADY_100_OMNI_V18.md` |

## The four arms, A, B, C and D, each from its receipt

| Arm | What it is | Where | Class | Engine | Receipt |
|---|---|---|---|---|---|
| A | the chip native | one A10 card rented directly; its bill the rental | P | omni-v23 | `results/TWO_BILLS.md (results/gpu/V23_A10_CAP_FULL_ABC.md)` |
| B | the chip with Omni-Compass on native | the same card, the same rented window | P | omni-v23 | `results/TWO_BILLS.md (results/gpu/V23_A10_CAP_FULL_ABC.md)` |
| C | the cloud native | Azure (AKS), its own bill | L | omni-v18 | `results/live/AKS_STEADY_100_OMNI_V18.md` |
| D | the cloud with Omni-Compass on native | Azure (AKS), the same machines, paired with C | L | omni-v18 | `results/live/AKS_STEADY_100_OMNI_V18.md` |

Arm D is the Omni-Compass side of the Azure set already on file, paired repetition by repetition with arm C: no run is needed to have it, and its counted runs on the engine that stands are queued.


## Not for the site, and why

| Figure | Why it is not a result | Where it comes from |
|---|---|---|
| abc_web_speed (—) | our own model (class S), Omni-Compass alone (its column C, no Kubernetes) against Kubernetes alone (column A): the mean response time only, while the same column used 40.8% more machine-hours and 25.9% more energy. Not a whole-system gain, not bare metal, not the cloud, and a model is never proof. | `docs/history/model_tables/ABC_TABLE_MODEL.json (tools/abc_table.py)` |
| abc_multi_speed (—) | the same model's multi-service column: Omni-Compass alone against Kubernetes alone, the mean response time only, with 41.8% more machine-hours and 26.7% more energy. Class S, never a result. | `docs/history/model_tables/ABC_TABLE_MODEL.json (tools/abc_table.py)` |
| abc_gpu_energy (—) | the same model's GPU scenario (class S): Omni-Compass alone against Kubernetes alone, the energy. Not a GPU measurement: the card's own meter reads energy per request served as the chip number above says. | `docs/history/model_tables/ABC_TABLE_MODEL.json (tools/abc_table.py)` |
| abc_column_b (0.0%) | in that model, Omni-Compass on top of Kubernetes (column B) reads the same as Kubernetes alone on web and multi; the model is a tuning bench, not the record. | `docs/history/model_tables/ABC_TABLE_MODEL.json (tools/abc_table.py)` |
| drain_20_percent (20.0%) | a 20% operational drain (13% machines + 7% people) is not on the record: the Omni index (20.4%, results/OMNI_INDEX.md) is work, speed and machines on GitHub's machines, not a bill, and the people line measured is the pages (results/OVERSIGHT_PAGES.md), worth about 2% of a run cost at a 7% people share; percentages of different bills do not add. | `none` |
| sixteen_million (—) | $16 million is 20% of $100 million; the 20% has no receipt, so neither does the $16 million. | `none` |
| free_work_33 (33.0%) | no table, chip receipt or cloud receipt carries a 33% rise in work for the bill. | `none` |
| arm_d_work_per_dollar (—) | arm D stands, from the Azure set on file (the four arms above, every gauge paired with arm C); what it cannot show yet is the work per dollar, because that set sent a fixed rate of requests and counted no work. Nor is there a column D in docs/history/model_tables/ABC_TABLE_MODEL.json, so no D may be read from our own model. | `results/live/AKS_STEADY_100_OMNI_V18.md` |
| thirteen_point_one (13.1%) | no record carries 13.1% as a headline: it appears only inside single rows of the whole-system page's separability check (Kueue's machines on the organism alone; KubeRay's modelled energy), one-row readings on omni-v12 used to test an assumption, never a result to headline. | `results/WHOLE_SYSTEM.md (section 4)` |

## The letters A, B, C and D

- `docs/history/model_tables/ABC_TABLE_MODEL.json`: class S, our own model: A Kubernetes alone, B Omni-Compass on top of Kubernetes, C Omni-Compass alone.
- `results/TWO_BILLS.json`: the two bills: A the chip native, B the chip with Omni-Compass on native, C the cloud native, D the cloud with Omni-Compass on native.
- `three-run tables`: A, B and C are the three runs of one benchmark.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

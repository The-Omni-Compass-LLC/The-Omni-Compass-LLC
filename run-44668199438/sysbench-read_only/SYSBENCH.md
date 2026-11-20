# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.5, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 293 | +0.5% | -7.49 to 10.5 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 293 | 293 | +0.0% | -5.07 to 5.25 | STEADY, no difference beyond the noise |
| queries a second | 4,693 | 4,694 | +0.0% | -81.1 to 84 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.93 | 2.88 | -1.9% | -0.409 to 0.298 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 122 | 4.49 | -96.3% | -622 to 388 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 4.53 | 2.07 | -54.4% | -13.1 to 8.19 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 537 | +319.9% | 222 to 597 | power given |
| pages holding data, mean (MB) | 120 | 488 | +307.4% | 219 to 518 | power given |
| pages read from disk into the pool (misses) | 1,973,915 | 611,274 | -69.0% | -1,697,671 to -1,027,611 | shown, not judged |
| host CPU busy (share of the run) | 0.173 | 0.173 | -0.1% | -0.00583 to 0.00554 | STEADY, no difference beyond the noise |
| host CPU-seconds | 317 | 316 | -0.1% | -10.9 to 10.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.36 | 2.35 | -0.6% | -0.149 to 0.119 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 |  | -1.84 to 8.5 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

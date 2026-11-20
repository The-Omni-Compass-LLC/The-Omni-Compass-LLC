# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.5, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 292 | +0.1% | -2.55 to 3.16 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 296 | 296 | -0.3% | -5.74 to 4.22 | STEADY, no difference beyond the noise |
| queries a second | 4,742 | 4,730 | -0.3% | -91.8 to 67.5 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.9 | 2.79 | -3.5% | -0.325 to 0.12 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 30.1 | 12.1 | -59.9% | -57.7 to 21.6 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.18 | 2.61 | -18.1% | -1.12 to -0.0318 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,113 | +769.7% | 919 to 1,051 | power given |
| pages holding data, mean (MB) | 120 | 942 | +683.2% | 799 to 844 | power given |
| pages read from disk into the pool (misses) | 2,004,148 | 114,100 | -94.3% | -1,997,197 to -1,782,899 | shown, not judged |
| host CPU busy (share of the run) | 0.171 | 0.161 | -5.7% | -0.0124 to -0.00713 | GAIN |
| host CPU-seconds | 306 | 288 | -5.7% | -22.1 to -12.8 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.3 | 2.16 | -5.8% | -0.179 to -0.0883 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 10.3 |  | 5.16 to 15.5 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

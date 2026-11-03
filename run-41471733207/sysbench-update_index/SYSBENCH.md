# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 3.21 | 5.6 | +74.4% | 0.581 to 4.19 | GAIN |
| throughput (transactions a second) | 982 | 982 | +0.0% | -2.97 to 3.13 | STEADY, no difference beyond the noise |
| queries a second | 982 | 982 | +0.0% | -2.97 to 3.13 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.94 | 1.68 | -13.7% | -0.608 to 0.075 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 38.8 | 5.71 | -85.3% | -176 to 110 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.61 | 1.58 | -39.3% | -4.27 to 2.21 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,283 | +902.3% | 1,082 to 1,227 | power given |
| pages holding data, mean (MB) | 118 | 880 | +644.3% | 754 to 769 | power given |
| pages read from disk into the pool (misses) | 415,434 | 70,963 | -82.9% | -359,527 to -329,415 | shown, not judged |
| host CPU busy (share of the run) | 0.185 | 0.166 | -10.3% | -0.0337 to -0.00457 | GAIN |
| host CPU-seconds | 335 | 300 | -10.4% | -60.7 to -8.91 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 240 | 121 | -49.9% | -253 to 13 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

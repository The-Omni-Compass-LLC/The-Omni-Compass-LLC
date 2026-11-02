# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `7f74bd306bf6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 293 | -0.1% | -2.43 to 2.12 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 293 | 293 | +0.1% | -1.43 to 2.04 | STEADY, no difference beyond the noise |
| queries a second | 4,690 | 4,695 | +0.1% | -22.9 to 32.6 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.85 | 4.82 | -0.6% | -0.15 to 0.0936 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.55 | 6.79 | +3.7% | -0.0738 to 0.56 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.16 | 3.05 | -3.4% | -0.208 to -0.00659 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 908 | +609.6% | 645 to 916 | power given |
| pages holding data, mean (MB) | 121 | 820 | +576.1% | 591 to 806 | power given |
| pages read from disk into the pool (misses) | 604,140 | 118,321 | -80.4% | -587,438 to -384,199 | shown, not judged |
| host CPU busy (share of the run) | 0.244 | 0.237 | -2.8% | -0.0136 to 8.96e-05 | STEADY, no difference beyond the noise |
| host CPU-seconds | 145 | 141 | -2.8% | -8.07 to 0.0392 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.24 | 3.15 | -2.7% | -0.198 to 0.0224 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

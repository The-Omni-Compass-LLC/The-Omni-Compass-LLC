# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 294 | -0.2% | -5.91 to 4.6 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | -0.2% | -5.67 to 4.27 | EVEN, no difference beyond the noise |
| queries a second | 4,725 | 4,714 | -0.2% | -90.7 to 68.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.8 | 4.71 | -1.8% | -0.0905 to -0.0802 | GAIN |
| latency, 99th percentile (ms) | 6.83 | 6.67 | -2.4% | -0.323 to 0.00141 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.13 | 3.11 | -0.6% | -0.0835 to 0.0443 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 712 | +39.0% | 197 to 203 | power given |
| pages holding data, mean (MB) | 451 | 642 | +42.5% | 186 to 198 | power given |
| pages read from disk into the pool (misses) | 247,037 | 181,889 | -26.4% | -71,068 to -59,228 | shown, not judged |
| host CPU busy (share of the run) | 0.242 | 0.24 | -0.6% | -0.00213 to -0.000553 | GAIN |
| host CPU-seconds | 144 | 143 | -0.6% | -1.22 to -0.434 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 3.19 | 3.18 | -0.4% | -0.0614 to 0.038 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `05092772357b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 292 | +0.1% | -4.69 to 5.42 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 293 | 293 | +0.0% | -4.15 to 4.2 | STEADY, no difference beyond the noise |
| queries a second | 4,689 | 4,690 | +0.0% | -66.5 to 67.3 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.03 | 4.94 | -1.9% | -0.539 to 0.353 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.17 | 6.92 | -3.4% | -1.4 to 0.903 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.29 | 3.27 | -0.7% | -0.207 to 0.158 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 813 | +58.9% | 45.3 to 558 | power given |
| pages holding data, mean (MB) | 455 | 736 | +61.8% | 56.5 to 505 | power given |
| pages read from disk into the pool (misses) | 246,079 | 153,053 | -37.8% | -161,342 to -24,710 | shown, not judged |
| host CPU busy (share of the run) | 0.255 | 0.255 | -0.0% | -0.0142 to 0.0141 | STEADY, no difference beyond the noise |
| host CPU-seconds | 151 | 151 | +0.0% | -8.23 to 8.24 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.39 | 3.38 | -0.1% | -0.158 to 0.151 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

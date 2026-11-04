# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 291 | 291 | -0.0% | -4.8 to 4.75 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 292 | 292 | -0.1% | -4.78 to 4.27 | STEADY, no difference beyond the noise |
| queries a second | 4,677 | 4,673 | -0.1% | -76.5 to 68.3 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.01 | 5.07 | +1.1% | -0.185 to 0.297 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.21 | 7.09 | -1.7% | -0.429 to 0.178 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.25 | 3.26 | +0.4% | -0.109 to 0.135 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 880 | +71.9% | 70.8 to 665 | power given |
| pages holding data, mean (MB) | 457 | 794 | +73.9% | 98.5 to 576 | power given |
| pages read from disk into the pool (misses) | 244,265 | 134,193 | -45.1% | -190,751 to -29,392 | shown, not judged |
| host CPU busy (share of the run) | 0.248 | 0.252 | +1.4% | -0.0121 to 0.0193 | STEADY, no difference beyond the noise |
| host CPU-seconds | 148 | 150 | +1.6% | -8.01 to 12.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.32 | 3.36 | +1.5% | -0.172 to 0.269 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

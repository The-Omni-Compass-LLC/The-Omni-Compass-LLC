# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `afbac134f8a1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 90.7 | 77.4 | -14.7% | -36.4 to 9.82 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 987 | 986 | -0.2% | -11.3 to 8.28 | EVEN, no difference beyond the noise |
| queries a second | 987 | 986 | -0.2% | -11.3 to 8.28 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 149 | 130 | -13.1% | -180 to 141 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 330 | 271 | -17.8% | -556 to 438 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 28.6 | 25.1 | -12.1% | -45.7 to 38.7 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 428 | -16.3% | -182 to 15.1 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 454 | 363 | -20.1% | -210 to 28 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,832 | 248,827 | +31.1% | -12,819 to 130,808 | shown, not judged |
| host CPU busy (share of the run) | 0.134 | 0.143 | +6.6% | -0.00346 to 0.021 | EVEN, no difference beyond the noise |
| host CPU-seconds | 237 | 253 | +6.5% | -4.36 to 35.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 6.14 | 7.48 | +21.8% | 0.643 to 2.04 | power given |
| buffer pool size changes written (the knob's moves) | 0 | 17.3 |  | 4.58 to 30.1 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

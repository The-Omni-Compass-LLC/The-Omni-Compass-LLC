# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 198 | 169 | -14.9% | -85.8 to 26.9 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 988 | 988 | +0.0% | -10.2 to 10.6 | EVEN, no difference beyond the noise |
| queries a second | 988 | 988 | +0.0% | -10.2 to 10.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.32 | 3.27 | -1.5% | -1.51 to 1.41 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 10.1 | 13.2 | +31.3% | -10.6 to 16.9 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.19 | 1.31 | +9.7% | -0.517 to 0.748 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 347 | -32.1% | -266 to -63.5 | GAIN |
| pages holding data, mean (MB) | 453 | 289 | -36.1% | -272 to -54.7 | GAIN |
| pages read from disk into the pool (misses) | 188,680 | 296,180 | +57.0% | 75,099 to 139,902 | shown, not judged |
| host CPU busy (share of the run) | 0.119 | 0.126 | +5.6% | -0.0107 to 0.024 | EVEN, no difference beyond the noise |
| host CPU-seconds | 211 | 222 | +5.6% | -18.7 to 42.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.41 | 2.92 | +20.8% | -0.18 to 1.19 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 14.7 |  | 10.9 to 18.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

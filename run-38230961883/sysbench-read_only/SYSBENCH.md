# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v5 (digest 8d4f91f0dabbc9fd, 43 files) at `3132004c90de`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 292 | +0.1% | -5.23 to 5.68 | no difference beyond the noise |
| throughput (transactions a second) | 292 | 292 | +0.1% | -5.37 to 5.71 | no difference beyond the noise |
| queries a second | 4,675 | 4,678 | +0.1% | -85.9 to 91.4 | no difference beyond the noise |
| latency, 95th percentile (ms) | 4.35 | 4.35 | +0.0% | -0.194 to 0.194 | same |
| latency, 99th percentile (ms) | 6.02 | 5.84 | -3.0% | -0.332 to -0.0248 | better |
| latency, mean (ms) | 3.24 | 3.24 | +0.1% | -0.0745 to 0.078 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 487 | -4.9% | -112 to 62.4 | no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 430 | -6.7% | -111 to 48.8 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 455,050 | 498,606 | +9.6% | -94,663 to 181,776 | shown, not judged |
| host CPU busy (share of the run) | 0.198 | 0.201 | +1.6% | -0.000779 to 0.00719 | no difference beyond the noise |
| host CPU-seconds | 220 | 224 | +1.8% | -1.25 to 9.18 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.45 | 2.49 | +1.7% | -0.0622 to 0.147 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10 |  | 5.03 to 15 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

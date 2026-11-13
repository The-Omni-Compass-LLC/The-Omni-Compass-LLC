# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `afbac134f8a1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,949 | 2,945 | -0.1% | -17 to 8.59 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,956 | 2,953 | -0.1% | -5.3 to -1.64 | LOSS |
| queries a second | 2,956 | 2,953 | -0.1% | -5.3 to -1.64 | LOSS |
| latency, 95th percentile (ms) | 0.315 | 0.309 | -1.8% | -0.0193 to 0.00802 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.425 | 0.415 | -2.2% | -0.0639 to 0.0452 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.195 | 0.197 | +1.1% | -0.0183 to 0.0224 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 455 | -11.2% | -114 to -0.729 | GAIN |
| pages holding data, mean (MB) | 464 | 407 | -12.2% | -124 to 11.6 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,116 | 455,361 | +24.0% | -4,524 to 181,014 | shown, not judged |
| host CPU busy (share of the run) | 0.153 | 0.153 | -0.4% | -0.0087 to 0.00762 | EVEN, no difference beyond the noise |
| host CPU-seconds | 272 | 271 | -0.3% | -15.5 to 13.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.202 | 0.201 | -0.2% | -0.0119 to 0.011 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16.7 |  | 12.9 to 20.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `19cdd5c920e3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,942 | 2,943 | +0.0% | -9.69 to 10.9 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,963 | 2,968 | +0.2% | -9.05 to 18.7 | STEADY, no difference beyond the noise |
| queries a second | 2,963 | 2,968 | +0.2% | -9.05 to 18.7 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.25 | 0.232 | -7.5% | -0.0526 to 0.0152 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.543 | 3.7 | +581.2% | -10.4 to 16.7 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.595 | 0.724 | +21.7% | -0.376 to 0.634 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,160 | +126.6% | 605 to 691 | power given |
| pages holding data, mean (MB) | 464 | 927 | +99.9% | 434 to 493 | power given |
| pages read from disk into the pool (misses) | 365,860 | 76,967 | -79.0% | -303,451 to -274,335 | shown, not judged |
| host CPU busy (share of the run) | 0.117 | 0.115 | -1.5% | -0.0085 to 0.00499 | STEADY, no difference beyond the noise |
| host CPU-seconds | 208 | 205 | -1.6% | -15.4 to 8.75 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.155 | 0.153 | -1.5% | -0.0111 to 0.00639 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7.67 |  | 6.23 to 9.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 7.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `2be7b8f0d97f`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,945 | 2,946 | +0.1% | -11 to 14.2 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,952 | 2,954 | +0.1% | -10.6 to 14.8 | EVEN, no difference beyond the noise |
| queries a second | 2,952 | 2,954 | +0.1% | -10.6 to 14.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.357 | 0.354 | -0.7% | -0.0124 to 0.00771 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.484 | 0.478 | -1.2% | -0.0301 to 0.0187 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.217 | 0.219 | +1.0% | -0.00613 to 0.0107 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 476 | -7.1% | -92 to 19.5 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 434 | -6.5% | -84.8 to 24.6 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 366,730 | 395,359 | +7.8% | -58,019 to 115,277 | shown, not judged |
| host CPU busy (share of the run) | 0.116 | 0.117 | +0.9% | -0.00179 to 0.00387 | EVEN, no difference beyond the noise |
| host CPU-seconds | 192 | 194 | +1.0% | -2.22 to 5.91 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.143 | 0.144 | +0.9% | -0.00149 to 0.00408 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 13.3 |  | 5.35 to 21.3 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

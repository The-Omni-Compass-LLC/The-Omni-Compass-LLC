# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `a73ae3e52895`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 296 | +0.1% | -2.77 to 3.09 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 296 | 296 | +0.0% | -3.14 to 3.35 | STEADY, no difference beyond the noise |
| queries a second | 4,740 | 4,742 | +0.0% | -50.3 to 53.7 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.9 | 2.88 | -0.7% | -0.443 to 0.404 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.6 | 4.49 | -2.4% | -0.835 to 0.614 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.44 | 1.4 | -3.0% | -0.182 to 0.0961 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 545 | +6.5% | -111 to 177 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 449 | 480 | +6.9% | -98.7 to 160 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 247,827 | 237,258 | -4.3% | -57,685 to 36,545 | shown, not judged |
| host CPU busy (share of the run) | 0.11 | 0.108 | -1.9% | -0.0114 to 0.00727 | STEADY, no difference beyond the noise |
| host CPU-seconds | 66.2 | 64.9 | -1.9% | -6.85 to 4.35 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.47 | 1.44 | -1.9% | -0.16 to 0.103 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0.333 |  | -1.1 to 1.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

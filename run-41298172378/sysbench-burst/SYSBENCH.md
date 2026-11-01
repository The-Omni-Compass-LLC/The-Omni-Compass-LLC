# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `09b65edc31ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 294 | -0.7% | -6.28 to 1.91 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 296 | 294 | -0.7% | -4.94 to 0.779 | STEADY, no difference beyond the noise |
| queries a second | 4,741 | 4,707 | -0.7% | -79 to 12.5 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.78 | 2.81 | +1.2% | -0.329 to 0.397 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.29 | 4.3 | +0.4% | -0.854 to 0.892 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.33 | 1.35 | +2.1% | -0.268 to 0.324 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 778 | +52.0% | -378 to 910 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 448 | 665 | +48.7% | -229 to 665 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 242,426 | 184,520 | -23.9% | -204,773 to 88,961 | shown, not judged |
| host CPU busy (share of the run) | 0.0998 | 0.101 | +1.1% | -0.0117 to 0.014 | STEADY, no difference beyond the noise |
| host CPU-seconds | 59.9 | 60.6 | +1.2% | -6.95 to 8.35 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.33 | 1.36 | +1.9% | -0.163 to 0.213 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1.67 |  | -3.5 to 6.84 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

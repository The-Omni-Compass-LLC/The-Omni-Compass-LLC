# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `dca8d09bbaa4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 296 | +0.7% | -3.44 to 7.27 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 294 | 296 | +0.7% | -3 to 6.97 | STEADY, no difference beyond the noise |
| queries a second | 4,709 | 4,741 | +0.7% | -48 to 112 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.86 | 2.9 | +1.2% | -0.0396 to 0.108 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.38 | 4.49 | +2.4% | -0.12 to 0.329 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.36 | 1.38 | +1.9% | -0.0711 to 0.123 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 486 | +279.5% | -110 to 826 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 120 | 456 | +278.2% | -102 to 772 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 584,177 | 311,716 | -46.6% | -456,021 to -88,901 | shown, not judged |
| host CPU busy (share of the run) | 0.101 | 0.103 | +1.7% | -0.00261 to 0.00601 | STEADY, no difference beyond the noise |
| host CPU-seconds | 60.6 | 61.6 | +1.7% | -1.58 to 3.63 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.35 | 1.37 | +1.0% | -0.0238 to 0.0512 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1.33 |  | -0.101 to 2.77 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

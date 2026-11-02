# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `e5cfa2afd8ec`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 113 | 131 | +15.2% | -2.33 to 36.7 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | -0.0% | -2.44 to 2.29 | STEADY, no difference beyond the noise |
| queries a second | 3,943 | 3,941 | -0.0% | -48.8 to 45.8 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 442 | 180 | -59.3% | -579 to 54.9 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 930 | 801 | -13.9% | -2,137 to 1,879 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 84.3 | 47.4 | -43.7% | -116 to 42.3 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,289 | +907.1% | 1,064 to 1,259 | power given |
| pages holding data, mean (MB) | 122 | 1,025 | +739.6% | 896 to 910 | power given |
| pages read from disk into the pool (misses) | 1,665,556 | 83,141 | -95.0% | -1,643,847 to -1,520,983 | shown, not judged |
| host CPU busy (share of the run) | 0.213 | 0.167 | -21.9% | -0.0557 to -0.0376 | GAIN |
| host CPU-seconds | 380 | 297 | -21.9% | -100 to -66.5 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 7.45 | 5.01 | -32.7% | -4.29 to -0.588 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 13.3 |  | 11.9 to 14.8 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 12.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

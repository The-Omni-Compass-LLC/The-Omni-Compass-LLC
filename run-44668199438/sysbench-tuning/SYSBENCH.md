# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.5, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,928 | 2,928 | +0.0% | -7.7 to 8.74 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,932 | 2,932 | +0.0% | -6.34 to 8.05 | STEADY, no difference beyond the noise |
| queries a second | 2,932 | 2,932 | +0.0% | -6.34 to 8.05 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.23 | 0.225 | -2.3% | -0.0303 to 0.0197 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.414 | 0.414 | +0.1% | -0.0183 to 0.019 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.144 | 0.139 | -3.4% | -0.00832 to -0.00137 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 593 | +363.5% | -64.8 to 995 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 121 | 547 | +351.4% | -33 to 885 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 1,029,474 | 396,944 | -61.4% | -1,000,674 to -264,386 | shown, not judged |
| host CPU busy (share of the run) | 0.128 | 0.126 | -1.5% | -0.0106 to 0.00692 | STEADY, no difference beyond the noise |
| host CPU-seconds | 237 | 234 | -1.4% | -19.8 to 13 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.176 | 0.174 | -1.5% | -0.0149 to 0.00976 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1.67 |  | 0.232 to 3.1 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

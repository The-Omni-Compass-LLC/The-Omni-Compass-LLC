# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.5, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 98.1 | 121 | +23.6% | -60 to 106 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 988 | 988 | -0.1% | -4.03 to 2.51 | STEADY, no difference beyond the noise |
| queries a second | 988 | 988 | -0.1% | -4.03 to 2.51 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 78.7 | 107 | +35.9% | -30 to 86.5 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 201 | 299 | +48.8% | -186 to 382 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 13.2 | 18.9 | +43.2% | -4.81 to 16.2 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,226 | +139.4% | 689 to 739 | power given |
| pages holding data, mean (MB) | 456 | 892 | +95.4% | 405 to 466 | power given |
| pages read from disk into the pool (misses) | 193,390 | 71,407 | -63.1% | -130,765 to -113,202 | shown, not judged |
| host CPU busy (share of the run) | 0.152 | 0.14 | -7.9% | -0.0317 to 0.00779 | STEADY, no difference beyond the noise |
| host CPU-seconds | 267 | 246 | -7.8% | -54.8 to 13.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 6.1 | 4.81 | -21.1% | -5.44 to 2.86 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

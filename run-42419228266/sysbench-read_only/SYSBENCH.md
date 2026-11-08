# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 294 | -0.6% | -3.42 to -0.302 | LOSS |
| throughput (transactions a second) | 296 | 294 | -0.7% | -3.44 to -0.458 | LOSS |
| queries a second | 4,740 | 4,709 | -0.7% | -55 to -7.33 | LOSS |
| latency, 95th percentile (ms) | 4.28 | 4.2 | -1.8% | -0.266 to 0.114 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.84 | 5.64 | -3.5% | -0.463 to 0.0492 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.18 | 3.12 | -1.8% | -0.113 to -0.000443 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 815 | +59.2% | 206 to 400 | power given |
| pages holding data, mean (MB) | 463 | 732 | +58.0% | 194 to 343 | power given |
| pages read from disk into the pool (misses) | 659,424 | 234,821 | -64.4% | -503,144 to -346,062 | shown, not judged |
| host CPU busy (share of the run) | 0.251 | 0.246 | -2.0% | -0.00974 to -0.000134 | GAIN |
| host CPU-seconds | 446 | 438 | -1.9% | -17 to -0.312 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 3.29 | 3.25 | -1.3% | -0.0995 to 0.0127 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

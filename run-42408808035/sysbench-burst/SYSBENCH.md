# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 295 | +0.6% | -2.02 to 5.28 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 294 | 295 | +0.5% | -1.91 to 4.97 | STEADY, no difference beyond the noise |
| queries a second | 4,700 | 4,724 | +0.5% | -30.5 to 79.6 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.86 | 4.85 | -0.0% | -0.216 to 0.212 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.83 | 6.71 | -1.8% | -0.649 to 0.4 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.2 | 3.15 | -1.7% | -0.105 to -0.0019 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 827 | +61.6% | -183 to 814 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 457 | 721 | +57.6% | -42.5 to 569 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 245,682 | 155,477 | -36.7% | -192,547 to 12,138 | shown, not judged |
| host CPU busy (share of the run) | 0.247 | 0.244 | -1.0% | -0.00356 to -0.00135 | GAIN |
| host CPU-seconds | 147 | 145 | -1.0% | -2.04 to -0.889 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 3.27 | 3.22 | -1.5% | -0.0911 to -0.00975 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 1.33 |  | -0.101 to 2.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

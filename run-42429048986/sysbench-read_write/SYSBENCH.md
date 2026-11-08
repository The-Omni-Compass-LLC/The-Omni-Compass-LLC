# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192 | 196 | +2.2% | 1.23 to 7.35 | GAIN |
| throughput (transactions a second) | 196 | 197 | +0.1% | -2.26 to 2.67 | STEADY, no difference beyond the noise |
| queries a second | 3,929 | 3,933 | +0.1% | -45.1 to 53.3 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 8.58 | 6.71 | -21.8% | -2.47 to -1.28 | GAIN |
| latency, 99th percentile (ms) | 12.7 | 8.63 | -31.9% | -4.66 to -3.42 | GAIN |
| latency, mean (ms) | 5.17 | 4.8 | -7.2% | -0.523 to -0.218 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 997 | +94.7% | 375 to 595 | power given |
| pages holding data, mean (MB) | 463 | 890 | +92.3% | 321 to 533 | power given |
| pages read from disk into the pool (misses) | 616,842 | 136,760 | -77.8% | -529,990 to -430,173 | shown, not judged |
| host CPU busy (share of the run) | 0.276 | 0.258 | -6.8% | -0.0235 to -0.0141 | GAIN |
| host CPU-seconds | 486 | 453 | -6.8% | -41.6 to -24.9 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 5.53 | 5.04 | -8.9% | -0.66 to -0.322 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

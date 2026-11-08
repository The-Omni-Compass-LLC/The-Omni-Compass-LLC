# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 292 | +0.3% | -7.52 to 9.06 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 293 | 294 | +0.2% | -5.69 to 6.95 | STEADY, no difference beyond the noise |
| queries a second | 4,686 | 4,696 | +0.2% | -91 to 111 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.95 | 4.86 | -1.9% | -0.527 to 0.342 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.22 | 7.05 | -2.4% | -1.54 to 1.19 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.14 | 3.08 | -1.8% | -0.0899 to -0.0208 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 813 | +58.8% | 44.6 to 558 | power given |
| pages holding data, mean (MB) | 454 | 734 | +61.8% | 58.7 to 502 | power given |
| pages read from disk into the pool (misses) | 246,186 | 152,141 | -38.2% | -171,240 to -16,850 | shown, not judged |
| host CPU busy (share of the run) | 0.241 | 0.239 | -0.7% | -0.00933 to 0.00586 | STEADY, no difference beyond the noise |
| host CPU-seconds | 143 | 142 | -0.6% | -5.19 to 3.41 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.21 | 3.18 | -1.0% | -0.0603 to -0.00091 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

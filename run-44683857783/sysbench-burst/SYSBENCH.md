# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.5, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 291 | -0.3% | -5.83 to 3.8 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 292 | 292 | -0.1% | -4.26 to 3.63 | STEADY, no difference beyond the noise |
| queries a second | 4,678 | 4,673 | -0.1% | -68.1 to 58.1 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.57 | 4.6 | +0.5% | -0.282 to 0.331 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.79 | 7.08 | +4.3% | 0.134 to 0.447 | LOSS |
| latency, mean (ms) | 2.36 | 2.34 | -0.9% | -0.0948 to 0.0539 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 883 | +589.6% | 104 to 1,405 | power given |
| pages holding data, mean (MB) | 121 | 751 | +522.4% | 241 to 1,019 | power given |
| pages read from disk into the pool (misses) | 602,356 | 138,227 | -77.1% | -612,007 to -316,251 | shown, not judged |
| host CPU busy (share of the run) | 0.19 | 0.188 | -1.3% | -0.00994 to 0.00492 | STEADY, no difference beyond the noise |
| host CPU-seconds | 116 | 115 | -1.3% | -5.98 to 2.91 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.59 | 2.57 | -1.0% | -0.109 to 0.0597 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 2.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

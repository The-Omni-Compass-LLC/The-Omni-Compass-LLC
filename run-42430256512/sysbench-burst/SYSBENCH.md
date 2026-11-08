# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 291 | 292 | +0.1% | -9.58 to 9.97 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 291 | 292 | +0.3% | -10.3 to 12.2 | STEADY, no difference beyond the noise |
| queries a second | 4,663 | 4,678 | +0.3% | -165 to 195 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.08 | 4.1 | +0.6% | -0.0826 to 0.133 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.67 | 5.92 | +4.4% | -0.301 to 0.798 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.54 | 2.76 | +8.4% | -0.934 to 1.36 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 805 | +528.7% | -125 to 1,478 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 121 | 689 | +470.0% | 51 to 1,085 | power given |
| pages read from disk into the pool (misses) | 601,165 | 158,642 | -73.6% | -559,702 to -325,343 | shown, not judged |
| host CPU busy (share of the run) | 0.203 | 0.2 | -1.5% | -0.0111 to 0.00524 | STEADY, no difference beyond the noise |
| host CPU-seconds | 124 | 122 | -1.4% | -7.27 to 3.83 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.77 | 2.73 | -1.5% | -0.248 to 0.165 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

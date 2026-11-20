# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.5, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 195 | 196 | +0.8% | -3.32 to 6.46 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 198 | 198 | +0.1% | -3.14 to 3.41 | STEADY, no difference beyond the noise |
| queries a second | 3,954 | 3,957 | +0.1% | -62.8 to 68.2 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.98 | 6 | -14.0% | -2.84 to 0.885 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 12.8 | 10.3 | -19.2% | -6.95 to 2.02 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.24 | 2.97 | -8.5% | -1.04 to 0.485 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,079 | +743.3% | 939 to 964 | power given |
| pages holding data, mean (MB) | 121 | 932 | +667.5% | 749 to 872 | power given |
| pages read from disk into the pool (misses) | 1,668,820 | 221,301 | -86.7% | -1,666,126 to -1,228,910 | shown, not judged |
| host CPU busy (share of the run) | 0.151 | 0.13 | -14.2% | -0.0346 to -0.00839 | GAIN |
| host CPU-seconds | 268 | 230 | -14.2% | -61.4 to -14.7 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 3.03 | 2.58 | -14.9% | -0.737 to -0.164 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 7.67 |  | 0.495 to 14.8 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

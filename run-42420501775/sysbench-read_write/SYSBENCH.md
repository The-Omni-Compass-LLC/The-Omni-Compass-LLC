# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 184 | 197 | +6.9% | 10.5 to 14.8 | GAIN |
| throughput (transactions a second) | 197 | 197 | +0.2% | -1.02 to 1.85 | STEADY, no difference beyond the noise |
| queries a second | 3,932 | 3,940 | +0.2% | -20.4 to 36.9 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 11.5 | 6.63 | -42.4% | -5.18 to -4.59 | GAIN |
| latency, 99th percentile (ms) | 16.4 | 8.79 | -46.5% | -10 to -5.22 | GAIN |
| latency, mean (ms) | 6.28 | 4.72 | -24.9% | -3.97 to 0.842 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,032 | +706.3% | 845 to 963 | power given |
| pages holding data, mean (MB) | 121 | 921 | +660.8% | 761 to 839 | power given |
| pages read from disk into the pool (misses) | 1,665,740 | 144,440 | -91.3% | -1,533,022 to -1,509,578 | shown, not judged |
| host CPU busy (share of the run) | 0.301 | 0.255 | -15.1% | -0.0465 to -0.0442 | GAIN |
| host CPU-seconds | 529 | 448 | -15.2% | -82.4 to -78.2 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 6.28 | 4.98 | -20.6% | -1.39 to -1.21 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 5.67 |  | 0.495 to 10.8 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

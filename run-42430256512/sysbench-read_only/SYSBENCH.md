# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | -0.0% | -3.57 to 3.53 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | +0.0% | -3.36 to 3.54 | STEADY, no difference beyond the noise |
| queries a second | 4,725 | 4,727 | +0.0% | -53.8 to 56.7 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 4 | 4.1 | +2.4% | -0.00627 to 0.2 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.31 | 5.57 | +4.9% | -0.114 to 0.636 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.13 | 3.1 | -0.8% | -0.0644 to 0.0158 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 686 | +436.2% | 143 to 974 | power given |
| pages holding data, mean (MB) | 120 | 616 | +413.0% | 154 to 838 | power given |
| pages read from disk into the pool (misses) | 1,985,185 | 409,084 | -79.4% | -2,030,899 to -1,121,303 | shown, not judged |
| host CPU busy (share of the run) | 0.247 | 0.246 | -0.6% | -0.00281 to -0.000323 | GAIN |
| host CPU-seconds | 439 | 436 | -0.6% | -5.17 to -0.541 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 3.25 | 3.23 | -0.7% | -0.069 to 0.0266 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 5.41 | 12.3 | +127.5% | -11.4 to 25.2 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 985 | 986 | +0.1% | -0.974 to 2.54 | STEADY, no difference beyond the noise |
| queries a second | 985 | 986 | +0.1% | -0.974 to 2.54 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.09 | 1.69 | -19.1% | -0.778 to -0.0189 | GAIN |
| latency, 99th percentile (ms) | 3.38 | 3.08 | -9.0% | -1.11 to 0.506 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.14 | 1.04 | -8.2% | -0.247 to 0.0594 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,194 | +833.1% | 1,050 to 1,083 | power given |
| pages holding data, mean (MB) | 119 | 840 | +608.6% | 667 to 775 | power given |
| pages read from disk into the pool (misses) | 418,331 | 108,027 | -74.2% | -340,315 to -280,293 | shown, not judged |
| host CPU busy (share of the run) | 0.263 | 0.231 | -12.3% | -0.0602 to -0.00462 | GAIN |
| host CPU-seconds | 461 | 405 | -12.3% | -104 to -8.85 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 324 | 110 | -66.1% | -842 to 414 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

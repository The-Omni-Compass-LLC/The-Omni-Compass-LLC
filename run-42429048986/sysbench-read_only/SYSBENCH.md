# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 291 | 292 | +0.6% | -10.4 to 14.1 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 296 | 297 | +0.1% | -2.36 to 3.02 | STEADY, no difference beyond the noise |
| queries a second | 4,739 | 4,745 | +0.1% | -37.8 to 48.3 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.09 | 2.74 | -11.1% | -1.28 to 0.592 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 549 | 21.8 | -96.0% | -2,840 to 1,786 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 12.6 | 2.86 | -77.3% | -52.6 to 33.2 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,175 | +129.5% | 562 to 764 | power given |
| pages holding data, mean (MB) | 467 | 958 | +105.1% | 477 to 505 | power given |
| pages read from disk into the pool (misses) | 659,968 | 84,303 | -87.2% | -596,137 to -555,191 | shown, not judged |
| host CPU busy (share of the run) | 0.167 | 0.161 | -3.4% | -0.0107 to -0.000831 | GAIN |
| host CPU-seconds | 298 | 288 | -3.4% | -19.2 to -1.35 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.25 | 2.16 | -4.1% | -0.248 to 0.0635 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10.3 |  | 4.08 to 16.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 5.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

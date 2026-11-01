# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `a73ae3e52895`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 294 | -0.2% | -2.97 to 1.73 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 296 | 296 | -0.1% | -2.97 to 2.4 | STEADY, no difference beyond the noise |
| queries a second | 4,739 | 4,735 | -0.1% | -47.5 to 38.4 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.69 | 2.6 | -3.5% | -0.213 to 0.0233 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.31 | 4.47 | +3.7% | -0.0518 to 0.37 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.3 | 2.22 | -3.5% | -0.247 to 0.0853 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,099 | +758.9% | 812 to 1,130 | power given |
| pages holding data, mean (MB) | 120 | 924 | +668.0% | 723 to 885 | power given |
| pages read from disk into the pool (misses) | 2,013,277 | 173,846 | -91.4% | -2,102,443 to -1,576,420 | shown, not judged |
| host CPU busy (share of the run) | 0.163 | 0.154 | -5.6% | -0.0171 to -0.000983 | GAIN |
| host CPU-seconds | 290 | 274 | -5.5% | -31.4 to -0.484 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.16 | 2.05 | -5.3% | -0.224 to -0.00509 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 11 |  | 0.171 to 21.8 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

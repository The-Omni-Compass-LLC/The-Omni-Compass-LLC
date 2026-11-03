# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 292 | -0.3% | -3.44 to 1.63 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 294 | 294 | -0.0% | -2.67 to 2.47 | STEADY, no difference beyond the noise |
| queries a second | 4,703 | 4,702 | -0.0% | -42.7 to 39.5 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.06 | 4.97 | -1.9% | -0.688 to 0.5 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.92 | 7.34 | +6.1% | -0.0252 to 0.874 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.95 | 2.87 | -2.8% | -0.149 to -0.0162 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 849 | +563.2% | 19 to 1,423 | power given |
| pages holding data, mean (MB) | 121 | 721 | +496.3% | 163 to 1,037 | power given |
| pages read from disk into the pool (misses) | 611,583 | 149,677 | -75.5% | -610,274 to -313,540 | shown, not judged |
| host CPU busy (share of the run) | 0.231 | 0.225 | -2.6% | -0.00983 to -0.00214 | GAIN |
| host CPU-seconds | 140 | 137 | -2.6% | -5.74 to -1.6 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 3.11 | 3.04 | -2.3% | -0.0923 to -0.0494 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

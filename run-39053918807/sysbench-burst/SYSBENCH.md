# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 294 | +0.3% | -8.78 to 10.6 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | +0.1% | -9.42 to 10 | EVEN, no difference beyond the noise |
| queries a second | 4,712 | 4,717 | +0.1% | -151 to 160 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.1 | 3.02 | -2.7% | -1.05 to 0.88 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.61 | 4.6 | -18.0% | -5.89 to 3.88 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.49 | 1.45 | -2.8% | -0.454 to 0.37 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 398 | -22.3% | -178 to -50.4 | GAIN |
| pages holding data, mean (MB) | 444 | 338 | -23.9% | -168 to -43.4 | GAIN |
| pages read from disk into the pool (misses) | 244,780 | 281,426 | +15.0% | 10,729 to 62,563 | shown, not judged |
| host CPU busy (share of the run) | 0.105 | 0.106 | +0.6% | -0.0134 to 0.0148 | EVEN, no difference beyond the noise |
| host CPU-seconds | 63.3 | 63.6 | +0.5% | -8.03 to 8.69 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.42 | 1.42 | +0.3% | -0.2 to 0.209 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 5.33 |  | 0.162 to 10.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

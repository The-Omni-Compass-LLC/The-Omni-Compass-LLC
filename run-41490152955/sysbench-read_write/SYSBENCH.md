# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `5d3560eacaa2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 143 | 142 | -0.9% | -28.8 to 26.1 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | +0.2% | -0.92 to 1.85 | STEADY, no difference beyond the noise |
| queries a second | 3,932 | 3,941 | +0.2% | -18.4 to 37 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 175 | 145 | -17.6% | -188 to 127 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 363 | 301 | -17.2% | -345 to 220 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 31.9 | 27.6 | -13.4% | -30.8 to 22.2 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,302 | +154.3% | 746 to 834 | power given |
| pages holding data, mean (MB) | 462 | 1,034 | +123.9% | 535 to 609 | power given |
| pages read from disk into the pool (misses) | 618,423 | 79,214 | -87.2% | -587,712 to -490,705 | shown, not judged |
| host CPU busy (share of the run) | 0.18 | 0.162 | -10.2% | -0.0194 to -0.0175 | GAIN |
| host CPU-seconds | 320 | 287 | -10.3% | -35.3 to -30.5 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 4.93 | 4.45 | -9.8% | -1.5 to 0.536 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10.3 |  | 5.16 to 15.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 8.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 182 | 180 | -1.1% | -32.9 to 28.9 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 198 | 197 | -0.1% | -0.934 to 0.356 | EVEN, no difference beyond the noise |
| queries a second | 3,953 | 3,948 | -0.1% | -18.7 to 7.13 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 29.1 | 37.2 | +27.9% | -80.9 to 97.1 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 110 | 127 | +15.5% | -122 to 156 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 7.89 | 8.85 | +12.1% | -8.43 to 10.3 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,242 | +142.5% | 697 to 762 | power given |
| pages holding data, mean (MB) | 463 | 1,014 | +119.1% | 524 to 578 | power given |
| pages read from disk into the pool (misses) | 619,861 | 94,920 | -84.7% | -571,783 to -478,100 | shown, not judged |
| host CPU busy (share of the run) | 0.182 | 0.168 | -8.1% | -0.0213 to -0.00843 | GAIN |
| host CPU-seconds | 323 | 297 | -8.1% | -37 to -15.3 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 3.9 | 3.63 | -7.0% | -0.798 to 0.252 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8 |  | 3.7 to 12.3 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 4.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

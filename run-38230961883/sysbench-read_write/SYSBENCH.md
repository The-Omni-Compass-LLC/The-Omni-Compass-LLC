# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v5 (digest 8d4f91f0dabbc9fd, 43 files) at `3132004c90de`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 190 | 191 | +0.2% | -1.27 to 2.02 | no difference beyond the noise |
| throughput (transactions a second) | 195 | 195 | -0.2% | -0.94 to 0.00825 | no difference beyond the noise |
| queries a second | 3,900 | 3,891 | -0.2% | -18.8 to 0.165 | no difference beyond the noise |
| latency, 95th percentile (ms) | 8.84 | 8.43 | -4.6% | -1.19 to 0.373 | no difference beyond the noise |
| latency, 99th percentile (ms) | 12.8 | 12.4 | -3.5% | -1.55 to 0.655 | no difference beyond the noise |
| latency, mean (ms) | 5.48 | 5.41 | -1.4% | -0.0972 to -0.0589 | better |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 594 | +16.1% | -109 to 273 | no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 523 | +13.5% | -72 to 196 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 434,290 | 345,775 | -20.4% | -267,192 to 90,162 | shown, not judged |
| host CPU busy (share of the run) | 0.23 | 0.224 | -2.7% | -0.0106 to -0.00197 | better |
| host CPU-seconds | 250 | 243 | -2.7% | -11.2 to -2.19 | better |
| host CPU-seconds per 1,000 transactions inside the line | 4.26 | 4.14 | -2.9% | -0.167 to -0.0765 | better |
| buffer pool size changes written (the knob's moves) | 0 | 15 |  | 10.7 to 19.3 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 297 | +0.3% | -0.6 to 2.45 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 297 | +0.3% | -1.18 to 2.81 | EVEN, no difference beyond the noise |
| queries a second | 4,738 | 4,751 | +0.3% | -18.9 to 45 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.84 | 1.85 | +0.6% | -0.282 to 0.304 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.64 | 3.64 | +0.1% | -0.323 to 0.328 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.28 | 1.27 | -0.5% | -0.208 to 0.196 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 133 | +3.9% | -1.21 to 11.3 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 120 | 131 | +9.1% | -2.3 to 24.3 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 1,995,560 | 2,015,127 | +1.0% | -191,860 to 230,994 | shown, not judged |
| host CPU busy (share of the run) | 0.101 | 0.101 | +0.5% | -0.0148 to 0.0158 | EVEN, no difference beyond the noise |
| host CPU-seconds | 181 | 182 | +0.5% | -26.4 to 28.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.34 | 1.34 | +0.2% | -0.201 to 0.206 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4 |  | -0.969 to 8.97 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

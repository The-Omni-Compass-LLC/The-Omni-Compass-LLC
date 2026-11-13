# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `9a499b137e78`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 11.1 | 12.4 | +11.9% | -5.98 to 8.62 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 980 | 981 | +0.0% | -6.16 to 6.39 | EVEN, no difference beyond the noise |
| queries a second | 980 | 981 | +0.0% | -6.16 to 6.39 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.63 | 1.62 | -0.8% | -0.275 to 0.25 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 23.2 | 3 | -87.0% | -110 to 69.4 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.56 | 1.69 | -34.0% | -4.34 to 2.6 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 384 | -25.1% | -224 to -32.8 | GAIN |
| pages holding data, mean (MB) | 453 | 316 | -30.3% | -224 to -49.8 | GAIN |
| pages read from disk into the pool (misses) | 189,197 | 280,664 | +48.3% | 38,090 to 144,843 | shown, not judged |
| host CPU busy (share of the run) | 0.153 | 0.154 | +0.5% | -0.0154 to 0.0169 | EVEN, no difference beyond the noise |
| host CPU-seconds | 274 | 275 | +0.6% | -27.4 to 30.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 54.8 | 50.9 | -7.1% | -33.3 to 25.5 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 15 |  | 6.04 to 24 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

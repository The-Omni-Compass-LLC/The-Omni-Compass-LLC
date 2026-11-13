# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 273 | 272 | -0.3% | -12.8 to 11.4 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 296 | -0.0% | -3.22 to 3.02 | EVEN, no difference beyond the noise |
| queries a second | 4,734 | 4,732 | -0.0% | -51.5 to 48.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 41.9 | 50.3 | +20.1% | -119 to 136 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 286 | 308 | +7.8% | -1,107 to 1,151 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 11.1 | 12.2 | +9.3% | -30.8 to 32.9 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 346 | -32.4% | -336 to 3.85 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 447 | 297 | -33.6% | -298 to -2.58 | GAIN |
| pages read from disk into the pool (misses) | 247,150 | 317,887 | +28.6% | -9,939 to 151,413 | shown, not judged |
| host CPU busy (share of the run) | 0.165 | 0.167 | +1.5% | -0.00188 to 0.00671 | EVEN, no difference beyond the noise |
| host CPU-seconds | 98.5 | 100 | +1.5% | -1.18 to 4.16 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.37 | 2.41 | +1.7% | -0.104 to 0.185 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8 |  | 3.7 to 12.3 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

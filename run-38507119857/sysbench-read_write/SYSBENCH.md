# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 120 | 118 | -2.0% | -21.6 to 16.8 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | +0.1% | -1.98 to 2.25 | EVEN, no difference beyond the noise |
| queries a second | 3,933 | 3,936 | +0.1% | -39.6 to 45 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 348 | 347 | -0.1% | -335 to 334 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 1,572 | 1,006 | -36.0% | -4,985 to 3,852 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 83.6 | 70.9 | -15.2% | -131 to 106 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 482 | -5.8% | -115 to 55.6 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 460 | 436 | -5.3% | -89.6 to 40.4 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 616,119 | 692,311 | +12.4% | -143,157 to 295,540 | shown, not judged |
| host CPU busy (share of the run) | 0.191 | 0.194 | +1.4% | -0.00413 to 0.00932 | EVEN, no difference beyond the noise |
| host CPU-seconds | 341 | 346 | +1.4% | -8.1 to 17.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 6.24 | 6.47 | +3.7% | -1.01 to 1.48 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 20.7 |  | 16.9 to 24.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

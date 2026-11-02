# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `19cdd5c920e3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192 | 194 | +0.9% | -5.5 to 9.11 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 197 | 198 | +0.1% | -3.44 to 3.97 | STEADY, no difference beyond the noise |
| queries a second | 3,945 | 3,951 | +0.1% | -68.8 to 79.4 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.71 | 5.34 | -20.5% | -6.77 to 4.01 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 27.3 | 14.2 | -47.9% | -52.3 to 26.2 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.56 | 2.88 | -19.1% | -1.28 to -0.0861 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,184 | +131.2% | 640 to 703 | power given |
| pages holding data, mean (MB) | 462 | 988 | +113.7% | 508 to 543 | power given |
| pages read from disk into the pool (misses) | 618,034 | 127,022 | -79.4% | -517,649 to -464,376 | shown, not judged |
| host CPU busy (share of the run) | 0.133 | 0.122 | -8.2% | -0.0145 to -0.00725 | GAIN |
| host CPU-seconds | 236 | 217 | -8.2% | -25.7 to -13.1 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.7 | 2.46 | -9.1% | -0.327 to -0.165 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 7 |  | 4.52 to 9.48 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 2.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

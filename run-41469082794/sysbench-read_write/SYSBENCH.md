# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 193 | 197 | +1.8% | 2.21 to 4.7 | GAIN |
| throughput (transactions a second) | 197 | 197 | +0.1% | -0.119 to 0.44 | STEADY, no difference beyond the noise |
| queries a second | 3,936 | 3,940 | +0.1% | -2.38 to 8.81 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 8.04 | 6.28 | -21.9% | -2.7 to -0.823 | GAIN |
| latency, 99th percentile (ms) | 12 | 8.08 | -32.7% | -4.95 to -2.92 | GAIN |
| latency, mean (ms) | 4.95 | 4.57 | -7.6% | -0.555 to -0.201 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 993 | +94.0% | 402 to 561 | power given |
| pages holding data, mean (MB) | 461 | 888 | +92.6% | 340 to 514 | power given |
| pages read from disk into the pool (misses) | 617,724 | 138,104 | -77.6% | -519,980 to -439,260 | shown, not judged |
| host CPU busy (share of the run) | 0.268 | 0.249 | -7.2% | -0.0205 to -0.0179 | GAIN |
| host CPU-seconds | 472 | 438 | -7.2% | -36.2 to -31.8 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 5.33 | 4.86 | -8.8% | -0.533 to -0.408 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

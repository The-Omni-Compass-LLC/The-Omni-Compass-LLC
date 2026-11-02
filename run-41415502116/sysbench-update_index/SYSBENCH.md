# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `4b160a642eb2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 23.3 | 21.5 | -7.7% | -13.5 to 9.94 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 983 | 983 | +0.0% | -4.91 to 5.07 | STEADY, no difference beyond the noise |
| queries a second | 983 | 983 | +0.0% | -4.91 to 5.07 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.66 | 1.67 | +0.3% | -0.31 to 0.319 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.7 | 2.75 | +1.7% | -0.403 to 0.496 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.01 | 1 | -1.1% | -0.0751 to 0.0532 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,230 | +140.2% | 677 to 758 | power given |
| pages holding data, mean (MB) | 457 | 888 | +94.1% | 412 to 449 | power given |
| pages read from disk into the pool (misses) | 192,385 | 71,745 | -62.7% | -127,250 to -114,031 | shown, not judged |
| host CPU busy (share of the run) | 0.234 | 0.231 | -1.1% | -0.0357 to 0.0305 | STEADY, no difference beyond the noise |
| host CPU-seconds | 409 | 405 | -1.1% | -61.5 to 52.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 40.5 | 41.6 | +2.9% | -27.1 to 29.5 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

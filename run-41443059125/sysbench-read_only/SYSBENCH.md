# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `19cdd5c920e3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 297 | 296 | -0.3% | -3.19 to 1.33 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 297 | 296 | -0.3% | -3.11 to 1.29 | STEADY, no difference beyond the noise |
| queries a second | 4,750 | 4,735 | -0.3% | -49.7 to 20.7 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.75 | 1.77 | +1.0% | -0.305 to 0.341 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.54 | 3.64 | +2.9% | -0.55 to 0.754 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.2 | 1.2 | -0.4% | -0.217 to 0.206 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 599 | +17.0% | -287 to 460 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 537 | +16.3% | -266 to 417 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 657,388 | 573,600 | -12.7% | -410,600 to 243,024 | shown, not judged |
| host CPU busy (share of the run) | 0.0965 | 0.0956 | -1.0% | -0.0179 to 0.0161 | STEADY, no difference beyond the noise |
| host CPU-seconds | 174 | 172 | -1.0% | -32.3 to 29 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.28 | 1.28 | -0.6% | -0.244 to 0.227 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0.333 |  | -1.1 to 1.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

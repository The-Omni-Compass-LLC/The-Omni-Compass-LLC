# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `4b160a642eb2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 288 | 288 | -0.3% | -7.55 to 6.03 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 295 | 293 | -0.7% | -7.4 to 3.39 | STEADY, no difference beyond the noise |
| queries a second | 4,724 | 4,692 | -0.7% | -118 to 54.3 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.25 | 6.11 | -2.3% | -0.272 to -0.0191 | GAIN |
| latency, 99th percentile (ms) | 10.9 | 10.5 | -2.8% | -5.52 to 4.9 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.86 | 4.36 | +13.1% | -2.25 to 3.26 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,041 | +103.4% | 240 to 818 | power given |
| pages holding data, mean (MB) | 457 | 921 | +101.5% | 254 to 674 | power given |
| pages read from disk into the pool (misses) | 249,435 | 97,902 | -60.8% | -214,489 to -88,576 | shown, not judged |
| host CPU busy (share of the run) | 0.276 | 0.272 | -1.4% | -0.0143 to 0.00648 | STEADY, no difference beyond the noise |
| host CPU-seconds | 164 | 162 | -1.4% | -8.68 to 4.09 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.71 | 3.67 | -1.1% | -0.265 to 0.182 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1.33 |  | -0.101 to 2.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

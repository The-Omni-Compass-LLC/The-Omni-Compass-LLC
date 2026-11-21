# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,951 | 2,949 | -0.1% | -11.5 to 7.79 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,956 | 2,955 | -0.0% | -9.88 to 7.22 | EVEN, no difference beyond the noise |
| queries a second | 2,956 | 2,955 | -0.0% | -9.88 to 7.22 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.32 | 0.32 | +0.0% | -0.0149 to 0.0149 | EVEN, the same |
| latency, 99th percentile (ms) | 0.448 | 0.443 | -1.2% | -0.0168 to 0.00614 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.197 | 0.198 | +0.9% | 0.000939 to 0.00251 | LOSS |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 453 | -11.6% | -161 to 42.1 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 410 | -11.5% | -155 to 48.2 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,296 | 457,326 | +24.5% | -127,996 to 308,056 | shown, not judged |
| host CPU busy (share of the run) | 0.0958 | 0.0989 | +3.2% | -0.000376 to 0.00657 | EVEN, no difference beyond the noise |
| host CPU-seconds | 159 | 164 | +3.5% | -0.771 to 11.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.118 | 0.122 | +3.5% | -0.000199 to 0.0085 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 11.7 |  | 10.2 to 13.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

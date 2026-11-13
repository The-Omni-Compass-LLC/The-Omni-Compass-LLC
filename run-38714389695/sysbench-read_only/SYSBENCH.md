# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `afbac134f8a1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 296 | +0.0% | -0.645 to 0.893 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 296 | -0.1% | -0.584 to 0.0845 | EVEN, no difference beyond the noise |
| queries a second | 4,738 | 4,734 | -0.1% | -9.34 to 1.35 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.93 | 1.82 | -5.4% | -0.419 to 0.21 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.16 | 3.66 | -11.9% | -1.63 to 0.643 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.37 | 1.27 | -6.9% | -0.426 to 0.238 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 361 | -29.5% | -186 to -117 | GAIN |
| pages holding data, mean (MB) | 462 | 332 | -28.0% | -154 to -105 | GAIN |
| pages read from disk into the pool (misses) | 653,430 | 1,126,566 | +72.4% | 295,271 to 651,002 | shown, not judged |
| host CPU busy (share of the run) | 0.101 | 0.101 | -0.4% | -0.00184 to 0.00109 | EVEN, no difference beyond the noise |
| host CPU-seconds | 182 | 181 | -0.3% | -3.28 to 2.04 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.35 | 1.34 | -0.4% | -0.0288 to 0.0175 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10.3 |  | 4.08 to 16.6 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

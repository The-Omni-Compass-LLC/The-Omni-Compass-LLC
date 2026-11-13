# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `afbac134f8a1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 292 | +0.0% | -1.35 to 1.52 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 293 | 293 | +0.1% | -1.6 to 2.25 | EVEN, no difference beyond the noise |
| queries a second | 4,688 | 4,693 | +0.1% | -25.7 to 36.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.09 | 5.09 | +0.0% | -0.454 to 0.458 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.87 | 7 | +1.9% | -0.803 to 1.06 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.33 | 3.35 | +0.5% | -0.0304 to 0.0616 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 435 | -15.0% | -278 to 124 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 448 | 377 | -15.8% | -204 to 62.4 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 242,563 | 254,733 | +5.0% | -77,992 to 102,333 | shown, not judged |
| host CPU busy (share of the run) | 0.195 | 0.198 | +1.5% | -0.00485 to 0.0105 | EVEN, no difference beyond the noise |
| host CPU-seconds | 108 | 110 | +1.6% | -3.05 to 6.59 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.41 | 2.45 | +1.6% | -0.0772 to 0.154 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8.67 |  | 3.5 to 13.8 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 289 | -0.9% | -9.27 to 4.02 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 292 | -0.9% | -9.12 to 3.54 | EVEN, no difference beyond the noise |
| queries a second | 4,717 | 4,672 | -0.9% | -146 to 56.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.74 | 5.74 | +0.0% | -0.253 to 0.254 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 8.33 | 8.33 | -0.0% | -0.375 to 0.371 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.38 | 3.41 | +0.6% | -0.0956 to 0.139 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 493 | -3.8% | -66.3 to 27.5 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 447 | 408 | -8.7% | -135 to 56.5 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 246,304 | 252,117 | +2.4% | -37,140 to 48,766 | shown, not judged |
| host CPU busy (share of the run) | 0.19 | 0.194 | +2.3% | -0.0123 to 0.021 | EVEN, no difference beyond the noise |
| host CPU-seconds | 105 | 107 | +2.6% | -6.9 to 12.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.34 | 2.42 | +3.4% | -0.0749 to 0.236 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6.67 |  | 0.929 to 12.4 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

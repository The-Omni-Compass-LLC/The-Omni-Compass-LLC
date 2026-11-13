# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `63f29c3e20a5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 38.6 | 58.2 | +50.7% | -0.974 to 40.2 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 985 | 986 | +0.1% | -2.97 to 5.08 | EVEN, no difference beyond the noise |
| queries a second | 985 | 986 | +0.1% | -2.97 to 5.08 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 372 | 253 | -32.0% | -321 to 83.1 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 721 | 751 | +4.1% | -1,065 to 1,124 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 85.1 | 61.1 | -28.2% | -74 to 26.1 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 435 | -15.0% | -128 to -25.7 | GAIN |
| pages holding data, mean (MB) | 454 | 356 | -21.7% | -165 to -31.9 | GAIN |
| pages read from disk into the pool (misses) | 189,504 | 257,498 | +35.9% | 33,773 to 102,214 | shown, not judged |
| host CPU busy (share of the run) | 0.129 | 0.131 | +0.8% | -0.0143 to 0.0164 | EVEN, no difference beyond the noise |
| host CPU-seconds | 231 | 233 | +0.6% | -25.8 to 28.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 13.4 | 9.1 | -32.3% | -5.86 to -2.84 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 21.3 |  | 19.9 to 22.8 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

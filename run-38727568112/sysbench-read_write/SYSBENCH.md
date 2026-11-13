# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `63f29c3e20a5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 194 | 194 | +0.2% | -0.0346 to 0.884 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 195 | 196 | +0.3% | -1.25 to 2.51 | EVEN, no difference beyond the noise |
| queries a second | 3,908 | 3,921 | +0.3% | -24.9 to 50.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.47 | 6.83 | +5.6% | -0.159 to 0.879 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 10.1 | 10.3 | +2.5% | -1.91 to 2.41 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.79 | 3.89 | +2.5% | -0.222 to 0.409 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 468 | -8.5% | -63.1 to -24.4 | GAIN |
| pages holding data, mean (MB) | 461 | 416 | -9.9% | -64.3 to -26.5 | GAIN |
| pages read from disk into the pool (misses) | 613,981 | 751,899 | +22.5% | 57,938 to 217,897 | shown, not judged |
| host CPU busy (share of the run) | 0.178 | 0.179 | +0.3% | -0.00366 to 0.00473 | EVEN, no difference beyond the noise |
| host CPU-seconds | 321 | 322 | +0.3% | -6.5 to 8.52 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.61 | 3.61 | +0.1% | -0.0783 to 0.0852 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 17 |  | 14.5 to 19.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

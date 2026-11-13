# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 1 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `8089bdc53794`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,945 | 2,936 | -0.3% | n/a to n/a | no difference beyond the noise |
| throughput (transactions a second) | 2,952 | 2,950 | -0.1% | n/a to n/a | no difference beyond the noise |
| queries a second | 2,952 | 2,950 | -0.1% | n/a to n/a | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.23 | 0.243 | +5.7% | n/a to n/a | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.336 | 0.409 | +21.7% | n/a to n/a | no difference beyond the noise |
| latency, mean (ms) | 0.0939 | 0.126 | +34.1% | n/a to n/a | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | n/a to n/a | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 672 | +31.2% | n/a to n/a | no difference beyond the noise |
| pages holding data, mean (MB) | 470 | 566 | +20.4% | n/a to n/a | no difference beyond the noise |
| pages read from disk into the pool (misses) | 268,721 | 189,773 | -29.4% | n/a to n/a | shown, not judged |
| host CPU busy (share of the run) | 0.0766 | 0.0718 | -6.3% | n/a to n/a | no difference beyond the noise |
| host CPU-seconds | 92.1 | 86.3 | -6.2% | n/a to n/a | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.102 | 0.0963 | -5.9% | n/a to n/a | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 14 |  | n/a to n/a | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*

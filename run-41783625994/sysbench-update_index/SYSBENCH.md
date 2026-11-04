# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 19.5 | 24 | +23.1% | -22.2 to 31.2 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 985 | 983 | -0.2% | -6.97 to 3.51 | STEADY, no difference beyond the noise |
| queries a second | 985 | 983 | -0.2% | -6.97 to 3.51 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.56 | 1.48 | -4.8% | -0.368 to 0.218 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.41 | 2.27 | -6.0% | -0.692 to 0.403 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.977 | 0.956 | -2.1% | -0.122 to 0.0808 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,236 | +141.3% | 705 to 742 | power given |
| pages holding data, mean (MB) | 458 | 888 | +94.1% | 411 to 450 | power given |
| pages read from disk into the pool (misses) | 192,717 | 70,141 | -63.6% | -134,797 to -110,355 | shown, not judged |
| host CPU busy (share of the run) | 0.227 | 0.222 | -2.1% | -0.0305 to 0.0208 | STEADY, no difference beyond the noise |
| host CPU-seconds | 399 | 390 | -2.1% | -53.3 to 36.4 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 47.2 | 43.5 | -7.8% | -35.2 to 27.8 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

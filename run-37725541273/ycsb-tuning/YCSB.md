# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 2 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 1 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `64c5ae9a4d25`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,860 | 2,805 | -1.9% | n/a to n/a | no difference beyond the noise |
| throughput (operations a second) | 2,867 | 2,812 | -1.9% | n/a to n/a | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.341 | 0.342 | +0.3% | n/a to n/a | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.508 | 0.518 | +2.0% | n/a to n/a | no difference beyond the noise |
| latency, mean (ms) | 0.2 | 0.22 | +10.0% | n/a to n/a | no difference beyond the noise |
| failed operations | 0 | 0 |  | n/a to n/a | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 353 | -31.0% | n/a to n/a | no difference beyond the noise |
| bytes in the cache, mean (MB) | 416 | 291 | -30.0% | n/a to n/a | no difference beyond the noise |
| pages read into the cache (misses) | 452,928 | 597,707 | +32.0% | n/a to n/a | shown, not judged |
| host CPU busy (share of the run) | 0.21 | 0.223 | +6.2% | n/a to n/a | no difference beyond the noise |
| host CPU-seconds | 251 | 272 | +8.3% | n/a to n/a | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.286 | 0.316 | +10.3% | n/a to n/a | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | n/a to n/a | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*

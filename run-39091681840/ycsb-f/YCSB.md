# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,813 | 5,809 | -0.1% | -21.8 to 14.2 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,824 | 5,821 | -0.0% | -21.7 to 15.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.228 | 0.233 | +2.0% | -0.0111 to 0.0204 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.425 | 0.438 | +3.1% | 0.00439 to 0.0216 | LOSS |
| latency, mean (ms) | 0.115 | 0.116 | +1.3% | -0.00334 to 0.00641 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -0.9% | -7.83 to -1.44 | GAIN |
| bytes in the cache, mean (MB) | 419 | 416 | -0.6% | -5.84 to 1.16 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 698,744 | 703,884 | +0.7% | -20,359 to 30,639 | shown, not judged |
| host CPU busy (share of the run) | 0.165 | 0.166 | +0.2% | -0.0997 to 0.1 | EVEN, no difference beyond the noise |
| host CPU-seconds | 302 | 301 | -0.2% | -217 to 216 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.113 | 0.113 | -0.2% | -0.0813 to 0.0808 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

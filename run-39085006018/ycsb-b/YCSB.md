# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,935 | 2,931 | -0.1% | -10.9 to 3.91 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,937 | 2,933 | -0.1% | -9.74 to 3.16 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.212 | 0.223 | +5.0% | -0.0391 to 0.0604 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.346 | 0.36 | +3.9% | -0.0721 to 0.0995 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0829 | 0.0853 | +2.9% | -0.00938 to 0.0142 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 506 | -1.3% | -20.7 to 7.75 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 420 | 414 | -1.5% | -17.1 to 4.85 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 719,741 | 718,158 | -0.2% | -160,417 to 157,252 | shown, not judged |
| host CPU busy (share of the run) | 0.0821 | 0.109 | +33.3% | -0.0386 to 0.0932 | EVEN, no difference beyond the noise |
| host CPU-seconds | 146 | 199 | +36.7% | -73.9 to 181 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.109 | 0.149 | +36.7% | -0.0553 to 0.135 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

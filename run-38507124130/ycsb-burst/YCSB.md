# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,693 | 2,540 | -5.7% | -557 to 250 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,704 | 2,551 | -5.7% | -556 to 249 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.34 | 0.344 | +1.4% | -0.00902 to 0.0183 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.568 | 0.59 | +3.9% | -0.0771 to 0.121 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.25 | 0.28 | +12.0% | -0.0458 to 0.106 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 477 | -6.7% | -104 to 35.1 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 398 | 360 | -9.4% | -100 to 25.4 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 235,129 | 222,717 | -5.3% | -111,697 to 86,873 | shown, not judged |
| host CPU busy (share of the run) | 0.125 | 0.144 | +15.4% | -0.0642 to 0.103 | EVEN, no difference beyond the noise |
| host CPU-seconds | 87.6 | 104 | +19.3% | -48.7 to 82.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.177 | 0.222 | +25.5% | -0.0628 to 0.153 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `63f29c3e20a5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,913 | 2,912 | -0.1% | -9.74 to 6.28 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,918 | 2,917 | -0.1% | -9.84 to 6.48 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.253 | 0.264 | +4.6% | -0.00714 to 0.0305 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.41 | 0.418 | +1.9% | -0.0196 to 0.0349 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.174 | 0.177 | +1.9% | -0.0111 to 0.0175 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 501 | -2.2% | -128 to 106 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 415 | 410 | -1.3% | -105 to 94.1 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 698,869 | 734,772 | +5.1% | -114,995 to 186,802 | shown, not judged |
| host CPU busy (share of the run) | 0.157 | 0.153 | -2.2% | -0.0326 to 0.0255 | EVEN, no difference beyond the noise |
| host CPU-seconds | 283 | 275 | -3.0% | -69.2 to 52.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.212 | 0.206 | -2.9% | -0.0519 to 0.0394 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

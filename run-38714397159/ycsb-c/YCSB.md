# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `afbac134f8a1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,898 | 2,896 | -0.1% | -4.82 to 0.938 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,902 | 2,901 | -0.1% | -4.22 to 0.713 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.309 | 0.313 | +1.1% | 0.000465 to 0.0062 | LOSS |
| latency, 99th percentile (ms) | 0.57 | 0.569 | -0.2% | -0.0109 to 0.00894 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.202 | 0.203 | +0.3% | -0.00192 to 0.003 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 447 | -12.7% | -77.9 to -52.5 | GAIN |
| bytes in the cache, mean (MB) | 419 | 368 | -12.1% | -55.2 to -46.5 | GAIN |
| pages read into the cache (misses) | 737,547 | 799,914 | +8.5% | -105,166 to 229,900 | shown, not judged |
| host CPU busy (share of the run) | 0.17 | 0.189 | +11.5% | -0.0537 to 0.0927 | EVEN, no difference beyond the noise |
| host CPU-seconds | 289 | 329 | +13.8% | -110 to 190 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.217 | 0.247 | +13.8% | -0.0828 to 0.143 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

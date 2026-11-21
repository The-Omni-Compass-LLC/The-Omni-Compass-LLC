# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `8ad09824e445`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,818 | 5,818 | -0.0% | -14.1 to 13.2 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,827 | 5,826 | -0.0% | -12.7 to 10.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.226 | 0.218 | -3.4% | -0.0202 to 0.00484 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.427 | 0.409 | -4.2% | -0.0354 to -0.00061 | GAIN |
| latency, mean (ms) | 0.11 | 0.109 | -1.3% | -0.0118 to 0.0088 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,365 | 1,365 | -0.0% | -5.91 to 4.64 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 63,108 | 63,102 | -0.0% | -313 to 302 | shown, not judged |
| host CPU busy (share of the run) | 0.156 | 0.152 | -2.3% | -0.0697 to 0.0627 | EVEN, no difference beyond the noise |
| host CPU-seconds | 285 | 277 | -2.7% | -150 to 134 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.106 | 0.104 | -2.7% | -0.056 to 0.0503 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

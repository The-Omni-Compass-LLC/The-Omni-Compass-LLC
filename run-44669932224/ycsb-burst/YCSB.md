# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.38, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,937 | 2,940 | +0.1% | -0.786 to 6.16 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,940 | 2,942 | +0.1% | -0.79 to 5.68 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.234 | 0.232 | -0.9% | -0.0194 to 0.0154 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.351 | 0.342 | -2.6% | -0.0546 to 0.0366 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.0688 | 0.0675 | -1.9% | -0.0109 to 0.00836 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,523 | 1,522 | -0.0% | -3.31 to 2.2 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 77,668 | 77,708 | +0.1% | -533 to 614 | shown, not judged |
| host CPU busy (share of the run) | 0.0745 | 0.0698 | -6.3% | -0.0667 to 0.0573 | STEADY, no difference beyond the noise |
| host CPU-seconds | 54 | 50.4 | -6.7% | -51.5 to 44.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.101 | 0.0939 | -6.7% | -0.0961 to 0.0826 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 20.4 | 19.5 | -4.3% | -4.29 to 2.55 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 19.7 | 18.8 | -4.3% | -4.12 to 2.43 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.686 | 0.66 | -3.8% | -0.178 to 0.127 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 54 | 50.4 | -6.7% | -51.4 to 44.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

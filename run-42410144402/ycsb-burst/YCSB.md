# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,906 | 2,906 | -0.0% | -3.13 to 2.7 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,915 | 2,915 | +0.0% | -4.15 to 4.73 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.316 | 0.328 | +3.7% | -0.0395 to 0.0628 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.44 | 0.44 | +0.2% | -0.0284 to 0.0298 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.148 | 0.149 | +0.8% | -0.00283 to 0.00509 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,519 | 1,519 | +0.0% | -3.09 to 3.76 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 77,695 | 77,691 | -0.0% | -77.4 to 69.4 | shown, not judged |
| host CPU busy (share of the run) | 0.159 | 0.172 | +7.6% | -0.0622 to 0.0865 | STEADY, no difference beyond the noise |
| host CPU-seconds | 116 | 127 | +9.7% | -54.3 to 76.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.217 | 0.238 | +9.7% | -0.102 to 0.144 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 58.1 | 58 | -0.1% | -0.95 to 0.805 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 57.3 | 57.3 | -0.1% | -0.988 to 0.835 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.78 | 0.784 | +0.5% | -0.0753 to 0.0838 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 116 | 127 | +9.7% | -54.3 to 76.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

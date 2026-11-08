# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,876 | 2,875 | -0.0% | -4.21 to 3.41 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,887 | 2,887 | -0.0% | -4.16 to 4.08 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.525 | 0.526 | +0.1% | -0.000768 to 0.0021 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.7 | 0.705 | +0.7% | -0.00494 to 0.0149 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.222 | 0.223 | +0.4% | -0.00437 to 0.00596 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,502 | 1,501 | -0.1% | -3.22 to 1.02 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 77,578 | 77,567 | -0.0% | -290 to 268 | shown, not judged |
| host CPU busy (share of the run) | 0.191 | 0.157 | -17.8% | -0.113 to 0.0455 | STEADY, no difference beyond the noise |
| host CPU-seconds | 134 | 105 | -21.4% | -95.1 to 37.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.253 | 0.199 | -21.4% | -0.179 to 0.0705 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 76.4 | 76.2 | -0.3% | -3.85 to 3.41 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 75.4 | 75.2 | -0.3% | -3.84 to 3.37 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.01 | 1.02 | +1.6% | -0.0256 to 0.0586 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 134 | 105 | -21.4% | -95.1 to 37.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

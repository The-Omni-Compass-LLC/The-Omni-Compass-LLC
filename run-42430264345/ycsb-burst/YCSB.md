# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,899 | 2,903 | +0.1% | -3.58 to 10.9 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,912 | 2,914 | +0.1% | 0.439 to 3.88 | GAIN |
| latency, 95th percentile (ms) | 0.328 | 0.332 | +1.2% | -0.0184 to 0.0264 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.51 | 0.489 | -4.1% | -0.118 to 0.0769 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.165 | 0.163 | -1.2% | -0.0263 to 0.0222 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,512 | 1,518 | +0.4% | -10.5 to 22.6 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 77,663 | 77,715 | +0.1% | -105 to 210 | shown, not judged |
| host CPU busy (share of the run) | 0.142 | 0.148 | +4.4% | -0.0814 to 0.0938 | STEADY, no difference beyond the noise |
| host CPU-seconds | 100 | 105 | +4.3% | -66.1 to 74.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.188 | 0.196 | +4.3% | -0.125 to 0.141 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 60.7 | 60.9 | +0.4% | -1.35 to 1.8 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 59.9 | 60.1 | +0.4% | -1.3 to 1.73 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.819 | 0.827 | +1.0% | -0.0713 to 0.0869 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 100 | 105 | +4.3% | -66.1 to 74.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

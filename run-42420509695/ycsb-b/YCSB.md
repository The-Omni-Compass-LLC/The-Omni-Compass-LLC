# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7481 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,904 | 2,904 | -0.0% | -1.76 to 1.16 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,907 | 2,906 | -0.0% | -1.5 to 0.704 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.304 | 0.31 | +1.9% | -0.0123 to 0.0236 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.468 | 0.477 | +1.9% | -0.0234 to 0.0407 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.151 | 0.153 | +0.9% | -0.00376 to 0.00644 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,481 | 7,481 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,366 | 1,365 | -0.0% | -0.81 to 0.677 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 61,774 | 61,843 | +0.1% | -289 to 428 | shown, not judged |
| host CPU busy (share of the run) | 0.161 | 0.171 | +5.7% | -0.068 to 0.0864 | STEADY, no difference beyond the noise |
| host CPU-seconds | 288 | 308 | +6.9% | -147 to 187 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.216 | 0.231 | +6.9% | -0.11 to 0.14 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 142 | 143 | +1.0% | -1.93 to 4.86 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 139 | 141 | +1.0% | -1.94 to 4.59 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.51 | 2.65 | +5.7% | 0.0101 to 0.274 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 288 | 308 | +6.9% | -147 to 187 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

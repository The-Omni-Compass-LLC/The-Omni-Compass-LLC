# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7481 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `dca8d09bbaa4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,757 | 5,759 | +0.0% | -4.17 to 7.52 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,770 | 5,772 | +0.0% | -3.42 to 7.47 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.33 | 0.33 | +0.2% | -0.00937 to 0.0107 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.599 | 0.599 | -0.1% | -0.018 to 0.0173 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.154 | 0.153 | -0.6% | -0.0049 to 0.00316 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,481 | 7,481 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,363 | 1,362 | -0.0% | -3.04 to 2.53 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 63,116 | 63,022 | -0.1% | -241 to 52.6 | shown, not judged |
| host CPU busy (share of the run) | 0.199 | 0.202 | +1.2% | -0.0444 to 0.0492 | STEADY, no difference beyond the noise |
| host CPU-seconds | 359 | 364 | +1.3% | -97.1 to 106 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.135 | 0.137 | +1.2% | -0.0365 to 0.0399 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 188 | 189 | +0.3% | -2.89 to 4.21 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 184 | 185 | +0.3% | -3.14 to 4.19 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 3.89 | 4.02 | +3.4% | 0.0123 to 0.252 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 359 | 364 | +1.3% | -97.1 to 106 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

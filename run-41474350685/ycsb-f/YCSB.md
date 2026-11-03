# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,670 | 5,661 | -0.2% | -19.2 to 1.8 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,688 | 5,679 | -0.1% | -15.2 to -1.29 | LOSS |
| latency, 95th percentile (ms) | 0.436 | 0.435 | -0.2% | -0.0231 to 0.0211 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.724 | 0.721 | -0.5% | -0.0306 to 0.0239 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.244 | 0.244 | -0.3% | -0.0155 to 0.0141 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,358 | 1,359 | +0.1% | -6.59 to 9.7 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 62,816 | 62,951 | +0.2% | -612 to 883 | shown, not judged |
| host CPU busy (share of the run) | 0.31 | 0.305 | -1.6% | -0.0357 to 0.026 | STEADY, no difference beyond the noise |
| host CPU-seconds | 562 | 551 | -1.9% | -79.4 to 57.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.212 | 0.209 | -1.8% | -0.03 to 0.0224 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 316 | 315 | -0.4% | -22.9 to 20.7 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 311 | 310 | -0.4% | -22.9 to 20.6 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.45 | 4.51 | +1.4% | -0.445 to 0.568 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 562 | 551 | -1.9% | -79.4 to 57.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

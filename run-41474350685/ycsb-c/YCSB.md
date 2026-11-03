# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,888 | 2,889 | +0.0% | 0.0706 to 1.83 | GAIN |
| throughput (operations a second) | 2,892 | 2,893 | +0.0% | 0.258 to 1.56 | GAIN |
| latency, 95th percentile (ms) | 0.291 | 0.291 | +0.1% | -0.0114 to 0.0121 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.483 | 0.489 | +1.2% | 0.0017 to 0.0103 | LOSS |
| latency, mean (ms) | 0.181 | 0.182 | +0.7% | -0.00644 to 0.00885 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,349 | 1,348 | -0.0% | -0.663 to -0.0115 | GAIN |
| pages read into the cache (misses) | 61,639 | 61,622 | -0.0% | -41.8 to 7.84 | shown, not judged |
| host CPU busy (share of the run) | 0.191 | 0.191 | +0.2% | -0.0911 to 0.0917 | STEADY, no difference beyond the noise |
| host CPU-seconds | 338 | 339 | +0.1% | -194 to 195 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.254 | 0.254 | +0.1% | -0.146 to 0.146 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 174 | 175 | +0.8% | -10.5 to 13.1 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 171 | 172 | +0.7% | -10.5 to 12.9 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.41 | 2.51 | +4.4% | 0.0203 to 0.191 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 338 | 339 | +0.1% | -194 to 195 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

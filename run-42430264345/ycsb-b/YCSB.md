# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,937 | 2,939 | +0.0% | -2.22 to 4.29 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,939 | 2,940 | +0.0% | -2.14 to 4.32 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.127 | 0.128 | +0.8% | -0.0326 to 0.0346 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.302 | 0.321 | +6.2% | -0.00622 to 0.0436 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.0591 | 0.0591 | +0.0% | -0.00387 to 0.00389 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,367 | 1,367 | -0.0% | -1.25 to 0.84 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 61,819 | 61,868 | +0.1% | -171 to 269 | shown, not judged |
| host CPU busy (share of the run) | 0.0915 | 0.0782 | -14.5% | -0.0507 to 0.0242 | STEADY, no difference beyond the noise |
| host CPU-seconds | 168 | 142 | -15.3% | -100 to 48.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.125 | 0.106 | -15.3% | -0.0748 to 0.0364 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 51.8 | 50.5 | -2.4% | -3.79 to 1.35 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 49.9 | 48.6 | -2.5% | -3.83 to 1.37 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.89 | 1.9 | +0.4% | -0.0234 to 0.0376 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 168 | 142 | -15.3% | -100 to 48.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7481 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,909 | 2,912 | +0.1% | 0.955 to 3.97 | GAIN |
| throughput (operations a second) | 2,912 | 2,914 | +0.1% | 0.677 to 3.99 | GAIN |
| latency, 95th percentile (ms) | 0.167 | 0.166 | -0.6% | -0.00845 to 0.00645 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.386 | 0.39 | +1.1% | -0.0206 to 0.0292 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.103 | 0.101 | -1.8% | -0.00295 to -0.000717 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,481 | 7,481 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,349 | 1,348 | -0.0% | -2.54 to 1.59 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 61,656 | 61,648 | -0.0% | -161 to 145 | shown, not judged |
| host CPU busy (share of the run) | 0.117 | 0.126 | +8.2% | -0.0141 to 0.0332 | STEADY, no difference beyond the noise |
| host CPU-seconds | 209 | 229 | +9.8% | -28.1 to 69.1 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.156 | 0.172 | +9.8% | -0.0211 to 0.0517 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 88.9 | 87.2 | -1.9% | -2.98 to -0.438 | GAIN |
| the server's own CPU-seconds (mongod) | 86.3 | 84.5 | -2.1% | -3.06 to -0.497 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.64 | 2.71 | +2.6% | -0.0657 to 0.203 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 209 | 229 | +9.8% | -28.1 to 69.1 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

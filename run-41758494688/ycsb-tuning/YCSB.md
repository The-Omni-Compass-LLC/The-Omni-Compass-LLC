# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7481 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `e29ad045b2ac`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,905 | 2,906 | +0.0% | -4.44 to 4.91 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,911 | 2,911 | +0.0% | -3.88 to 4.47 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.3 | 0.303 | +0.9% | -0.00768 to 0.013 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.543 | 0.546 | +0.5% | -0.00113 to 0.00646 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.138 | 0.138 | -0.2% | -0.00173 to 0.00126 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,481 | 7,481 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,363 | 1,363 | -0.0% | -9.76 to 9.21 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 63,187 | 63,149 | -0.1% | -439 to 364 | shown, not judged |
| host CPU busy (share of the run) | 0.171 | 0.184 | +7.5% | -0.0247 to 0.0505 | STEADY, no difference beyond the noise |
| host CPU-seconds | 312 | 341 | +9.3% | -56.1 to 114 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.234 | 0.256 | +9.3% | -0.0423 to 0.0858 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 145 | 145 | +0.5% | -1.18 to 2.55 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 142 | 143 | +0.4% | -1.4 to 2.57 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.27 | 2.37 | +4.2% | -0.0268 to 0.216 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 312 | 341 | +9.3% | -56.1 to 114 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

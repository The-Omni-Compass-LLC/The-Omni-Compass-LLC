# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,887 | 2,886 | -0.0% | -2.61 to 1.4 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,891 | 2,890 | -0.0% | -2.71 to 1.61 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.297 | 0.297 | +0.0% | -0.0114 to 0.0114 | STEADY, the same |
| latency, 99th percentile (ms) | 0.501 | 0.505 | +0.9% | -0.0128 to 0.0221 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.184 | 0.186 | +0.7% | -0.00501 to 0.00755 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,349 | 1,348 | -0.0% | -3.23 to 2.49 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 61,659 | 61,635 | -0.0% | -153 to 105 | shown, not judged |
| host CPU busy (share of the run) | 0.168 | 0.172 | +2.4% | -0.0448 to 0.0528 | STEADY, no difference beyond the noise |
| host CPU-seconds | 287 | 294 | +2.6% | -90.1 to 105 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.216 | 0.221 | +2.6% | -0.0677 to 0.079 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 176 | 178 | +0.7% | -6.63 to 9.14 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 174 | 175 | +0.7% | -6.56 to 8.89 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.52 | 2.61 | +3.5% | -0.0697 to 0.248 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 287 | 294 | +2.6% | -90.1 to 105 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `19cdd5c920e3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,872 | 2,875 | +0.1% | -3.71 to 9.21 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,883 | 2,887 | +0.1% | -4.42 to 11.2 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.381 | 0.367 | -3.8% | -0.0398 to 0.0112 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.656 | 0.663 | +1.1% | -0.0253 to 0.0393 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.226 | 0.222 | -1.7% | -0.00885 to 0.000978 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,356 | +164.9% | 598 to 1,091 | power given |
| bytes in the cache, mean (MB) | 417 | 1,065 | +155.3% | 455 to 841 | power given |
| pages read into the cache (misses) | 671,484 | 282,377 | -57.9% | -562,316 to -215,899 | shown, not judged |
| host CPU busy (share of the run) | 0.266 | 0.261 | -1.7% | -0.0269 to 0.0178 | STEADY, no difference beyond the noise |
| host CPU-seconds | 473 | 464 | -1.9% | -64.2 to 46.4 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.357 | 0.35 | -2.0% | -0.0491 to 0.0352 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 5.33 |  | 3.9 to 6.77 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 277 | 271 | -2.1% | -13.1 to 1.21 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 274 | 268 | -2.4% | -13.7 to 0.452 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.62 | 3.29 | +25.5% | 0.505 to 0.832 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 473 | 464 | -1.9% | -64.2 to 46.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

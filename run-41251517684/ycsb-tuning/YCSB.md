# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `a73ae3e52895`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,875 | 2,877 | +0.1% | -7.44 to 12.5 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,885 | 2,887 | +0.1% | -6.33 to 9.88 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.375 | 0.359 | -4.3% | -0.025 to -0.00704 | GAIN |
| latency, 99th percentile (ms) | 0.596 | 0.577 | -3.2% | -0.0531 to 0.0144 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.225 | 0.217 | -3.4% | -0.0144 to -0.00107 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,383 | +170.1% | 665 to 1,077 | power given |
| bytes in the cache, mean (MB) | 417 | 1,085 | +160.1% | 522 to 815 | power given |
| pages read into the cache (misses) | 676,817 | 265,707 | -60.7% | -520,446 to -301,774 | shown, not judged |
| host CPU busy (share of the run) | 0.263 | 0.246 | -6.5% | -0.0794 to 0.0452 | STEADY, no difference beyond the noise |
| host CPU-seconds | 467 | 432 | -7.5% | -176 to 106 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.352 | 0.325 | -7.5% | -0.133 to 0.0802 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 6 |  | 1.7 to 10.3 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 278 | 267 | -3.8% | -16.7 to -4.1 | GAIN |
| the server's own CPU-seconds (mongod) | 275 | 264 | -4.0% | -17.2 to -4.8 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.58 | 3.17 | +22.8% | 0.423 to 0.757 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 467 | 432 | -7.5% | -176 to 106 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

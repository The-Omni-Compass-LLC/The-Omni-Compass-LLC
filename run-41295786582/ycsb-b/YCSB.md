# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `09b65edc31ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,939 | 2,942 | +0.1% | -4.17 to 10.1 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,941 | 2,944 | +0.1% | -3.92 to 9.73 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.126 | 0.117 | -6.6% | -0.0177 to 0.00107 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.318 | 0.312 | -1.7% | -0.019 to 0.00835 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.0634 | 0.0616 | -2.8% | -0.00419 to 0.000588 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 420 | 420 | +0.1% | -5.28 to 6.09 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 709,979 | 707,554 | -0.3% | -106,291 to 101,441 | shown, not judged |
| host CPU busy (share of the run) | 0.0753 | 0.0631 | -16.2% | -0.0711 to 0.0467 | STEADY, no difference beyond the noise |
| host CPU-seconds | 135 | 112 | -16.9% | -135 to 89 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.101 | 0.0838 | -16.9% | -0.101 to 0.0665 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 58.3 | 56 | -4.0% | -2.55 to -2.07 | GAIN |
| the server's own CPU-seconds (mongod) | 56.7 | 54.2 | -4.5% | -2.86 to -2.26 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.63 | 1.89 | +15.7% | -0.0504 to 0.563 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 135 | 112 | -16.9% | -135 to 89 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

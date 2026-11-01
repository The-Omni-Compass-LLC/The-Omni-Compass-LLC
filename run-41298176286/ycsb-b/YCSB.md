# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `09b65edc31ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,888 | 2,888 | +0.0% | -0.79 to 1.28 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,893 | 2,893 | +0.0% | -1.1 to 1.99 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.317 | 0.311 | -1.8% | -0.0193 to 0.00802 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.543 | 0.545 | +0.3% | -0.00981 to 0.0131 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.19 | 0.187 | -1.7% | -0.00601 to -0.000455 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 538 | +5.0% | -84.4 to 135 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 435 | +4.1% | -72.3 to 107 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 714,300 | 648,341 | -9.2% | -195,561 to 63,642 | shown, not judged |
| host CPU busy (share of the run) | 0.195 | 0.184 | -5.6% | -0.0726 to 0.0507 | STEADY, no difference beyond the noise |
| host CPU-seconds | 342 | 319 | -6.6% | -155 to 110 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.257 | 0.24 | -6.6% | -0.117 to 0.0827 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0.333 |  | -1.1 to 1.77 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 192 | 189 | -1.7% | -6.88 to 0.302 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 190 | 186 | -2.0% | -7.4 to -0.215 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.5 | 3.01 | +20.7% | 0.406 to 0.628 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 342 | 320 | -6.6% | -155 to 110 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `09b65edc31ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,847 | 5,851 | +0.1% | -8.47 to 15.9 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,855 | 5,858 | +0.1% | -8.68 to 15.5 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.152 | 0.152 | +0.4% | -0.0111 to 0.0124 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.335 | 0.35 | +4.4% | -0.0552 to 0.0845 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.0802 | 0.0796 | -0.8% | -0.00371 to 0.00239 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 630 | +23.0% | -176 to 411 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 508 | +21.2% | -130 to 308 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 699,562 | 577,534 | -17.4% | -440,691 to 196,635 | shown, not judged |
| host CPU busy (share of the run) | 0.141 | 0.121 | -14.3% | -0.105 to 0.0643 | STEADY, no difference beyond the noise |
| host CPU-seconds | 260 | 219 | -15.9% | -218 to 135 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0972 | 0.0817 | -16.0% | -0.0814 to 0.0503 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 1.67 |  | -3.5 to 6.84 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 117 | 116 | -1.0% | -5.25 to 2.82 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 114 | 113 | -1.4% | -5.57 to 2.48 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.51 | 2.84 | +13.3% | 0.0139 to 0.652 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 260 | 219 | -15.9% | -218 to 135 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

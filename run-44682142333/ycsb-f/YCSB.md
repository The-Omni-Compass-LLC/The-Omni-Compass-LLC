# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.38, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,745 | 5,700 | -0.8% | -175 to 85.6 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,763 | 5,720 | -0.7% | -169 to 83 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.325 | 0.321 | -1.3% | -0.0131 to 0.00439 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.518 | 0.532 | +2.6% | -0.0396 to 0.067 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.191 | 0.193 | +0.8% | -0.016 to 0.019 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,254 | +145.0% | 694 to 791 | power given |
| bytes in the cache, mean (MB) | 416 | 903 | +117.4% | 316 to 659 | power given |
| pages read into the cache (misses) | 699,229 | 222,194 | -68.2% | -509,508 to -444,563 | shown, not judged |
| host CPU busy (share of the run) | 0.245 | 0.256 | +4.8% | 0.000927 to 0.0224 | power given |
| host CPU-seconds | 438 | 468 | +6.9% | 7.43 to 53.1 | power given |
| host CPU-seconds per 1,000 operations inside the line | 0.164 | 0.177 | +7.8% | 0.00825 to 0.0173 | power given |
| cache size changes written (the knob's moves) | 0 | 32.3 |  | -1.58 to 66.2 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 277 | 268 | -3.1% | -11.7 to -5.37 | GAIN |
| the server's own CPU-seconds (mongod) | 273 | 264 | -3.3% | -12.2 to -6.08 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 3.69 | 4.29 | +16.2% | 0.469 to 0.727 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 438 | 468 | +6.9% | 7.45 to 53.1 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 2.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

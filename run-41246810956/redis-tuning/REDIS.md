# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `4082deec8fda`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,386 | +17.1% | 197 to 208 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0238 to 0.00655 | STEADY, no difference beyond the noise |
| cache hit rate | 0.79 | 0.925 | +17.1% | 0.132 to 0.138 | GAIN |
| latency, 95th percentile (ms) | 5.55 | 5.44 | -1.9% | -0.12 to -0.0928 | GAIN |
| latency, 99th percentile (ms) | 5.62 | 5.59 | -0.5% | -0.0389 to -0.0168 | GAIN |
| latency, mean (ms) | 1.25 | 0.527 | -57.9% | -0.741 to -0.705 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 347 | +442.0% | 271 to 295 | power given |
| memory used, mean (MB) | 61.2 | 319 | +420.7% | 250 to 265 | power given |
| keys evicted | 138,048 | 2,679 | -98.1% | -137,467 to -133,271 | shown, not judged |
| host CPU busy (share of the run) | 0.0942 | 0.0898 | -4.7% | -0.0374 to 0.0285 | STEADY, no difference beyond the noise |
| host CPU-seconds | 163 | 157 | -3.7% | -68.9 to 57 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.306 | 0.252 | -17.7% | -0.167 to 0.0587 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 17.7 |  | 14.8 to 20.5 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 196 | 175 | -10.8% | -24.7 to -17.9 | GAIN |
| the server's own CPU-seconds (redis-server) | 24.7 | 22.2 | -10.4% | -2.82 to -2.3 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 172 | 152 | -11.6% | -23.6 to -16.3 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.24 |  | 1.08 to 1.41 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.168 | 0.164 | -2.2% | -0.00672 to -0.000644 | shown, not judged |
| host CPU-seconds without steal | 163 | 157 | -3.7% | -68.9 to 57 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

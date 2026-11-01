# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `a73ae3e52895`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,466 | +15.7% | 197 to 200 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00441 to 0.0013 | STEADY, no difference beyond the noise |
| cache hit rate | 0.845 | 0.978 | +15.7% | 0.131 to 0.133 | GAIN |
| latency, 95th percentile (ms) | 5.52 | 0.168 | -97.0% | -5.36 to -5.35 | GAIN |
| latency, 99th percentile (ms) | 5.62 | 5.49 | -2.3% | -0.13 to -0.127 | GAIN |
| latency, mean (ms) | 0.963 | 0.249 | -74.2% | -0.724 to -0.704 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 337 | +426.5% | 271 to 275 | power given |
| memory used, mean (MB) | 61.3 | 313 | +410.3% | 249 to 254 | power given |
| keys evicted | 103,267 | 2,681 | -97.4% | -101,174 to -99,998 | shown, not judged |
| host CPU busy (share of the run) | 0.102 | 0.0998 | -1.9% | -0.0155 to 0.0116 | STEADY, no difference beyond the noise |
| host CPU-seconds | 178 | 177 | -0.5% | -27.1 to 25.4 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.312 | 0.268 | -14.0% | -0.0974 to 0.0104 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 28.7 |  | 27.2 to 30.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 196 | 173 | -11.8% | -24.5 to -21.7 | GAIN |
| the server's own CPU-seconds (redis-server) | 26 | 22.8 | -12.5% | -3.51 to -2.98 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 170 | 149 | -12.4% | -22.8 to -19.2 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.15 |  | 0.91 to 1.4 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.167 | 0.163 | -2.0% | -0.00785 to 0.00133 | shown, not judged |
| host CPU-seconds without steal | 178 | 177 | -0.5% | -27.1 to 25.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 15.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

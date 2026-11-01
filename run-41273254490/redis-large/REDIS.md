# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `dca8d09bbaa4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,469 | 1,470 | +0.0% | -1.11 to 1.66 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0113 to 0.0182 | STEADY, no difference beyond the noise |
| cache hit rate | 0.981 | 0.981 | +0.0% | -3.38e-06 to 5.43e-06 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.11 | 0.113 | +3.2% | -0.00519 to 0.0122 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.21 | 5.22 | +0.1% | -0.00882 to 0.0206 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.184 | 0.185 | +0.5% | -0.00267 to 0.00458 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 348 | 348 | +0.0% | -0.024 to 0.0698 | STEADY, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0506 | 0.0509 | +0.5% | -0.0578 to 0.0583 | STEADY, no difference beyond the noise |
| host CPU-seconds | 88.8 | 89.4 | +0.7% | -107 to 108 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.134 | 0.135 | +0.7% | -0.162 to 0.164 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 110 | 113 | +2.3% | 0.793 to 4.31 | power given |
| the server's own CPU-seconds (redis-server) | 14.8 | 15.4 | +3.5% | 0.0238 to 1.02 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 95.2 | 97.2 | +2.1% | 0.728 to 3.33 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.123 | 0.127 | +3.0% | -0.00704 to 0.0143 | shown, not judged |
| host CPU-seconds without steal | 88.8 | 89.4 | +0.7% | -107 to 108 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

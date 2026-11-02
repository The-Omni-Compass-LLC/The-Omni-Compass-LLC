# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `4b160a642eb2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 924 | 1,171 | +26.7% | 245 to 250 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.079 to 0.13 | STEADY, no difference beyond the noise |
| cache hit rate | 0.617 | 0.783 | +26.8% | 0.164 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.21 | -0.1% | -0.0191 to 0.00416 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.33 | 5.29 | -0.7% | -0.165 to 0.0866 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.05 | 1.21 | -41.1% | -0.871 to -0.819 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 312 | +387.7% | 244 to 252 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.5% | 196 to 198 | power given |
| keys evicted | 243,182 | 0 | -100.0% | -243,795 to -242,568 | shown, not judged |
| host CPU busy (share of the run) | 0.0607 | 0.0678 | +11.8% | -0.00831 to 0.0226 | STEADY, no difference beyond the noise |
| host CPU-seconds | 106 | 120 | +13.1% | -13.1 to 40.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.255 | 0.228 | -10.8% | -0.119 to 0.0642 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 18.3 |  | 14.5 to 22.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 131 | 124 | -5.7% | -14.1 to -0.975 | GAIN |
| the server's own CPU-seconds (redis-server) | 17.5 | 15.7 | -10.3% | -2.87 to -0.719 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 114 | 107 | -6.2% | -12.3 to -1.73 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.31 |  | 0.972 to 1.64 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.128 | 0.124 | -2.8% | -0.00888 to 0.00171 | shown, not judged |
| host CPU-seconds without steal | 106 | 120 | +13.1% | -13.1 to 40.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

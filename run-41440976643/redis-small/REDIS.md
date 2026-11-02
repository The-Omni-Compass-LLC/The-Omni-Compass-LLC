# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `159b34031f41`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 1,173 | +26.7% | 246 to 248 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00156 to 0.0181 | STEADY, no difference beyond the noise |
| cache hit rate | 0.617 | 0.783 | +26.7% | 0.165 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.7 | 5.67 | -0.4% | -0.0261 to -0.0218 | GAIN |
| latency, 99th percentile (ms) | 5.75 | 5.75 | -0.0% | -0.00741 to 0.00208 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.26 | 1.36 | -39.8% | -0.902 to -0.897 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 313 | +388.9% | 243 to 255 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.5% | 196 to 198 | power given |
| keys evicted | 243,102 | 0 | -100.0% | -243,566 to -242,638 | shown, not judged |
| host CPU busy (share of the run) | 0.147 | 0.138 | -6.3% | -0.0325 to 0.014 | STEADY, no difference beyond the noise |
| host CPU-seconds | 246 | 234 | -4.7% | -57.7 to 34.6 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.59 | 0.444 | -24.8% | -0.245 to -0.0472 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 18.7 |  | 17.2 to 20.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 310 | 276 | -11.1% | -35.5 to -33.5 | GAIN |
| the server's own CPU-seconds (redis-server) | 35.6 | 32.3 | -9.4% | -3.82 to -2.85 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 275 | 242 | -11.9% | -34 to -31.4 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.56 |  | 1.38 to 1.74 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.236 | 0.225 | -4.8% | -0.0122 to -0.0105 | shown, not judged |
| host CPU-seconds without steal | 246 | 234 | -4.7% | -57.7 to 34.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

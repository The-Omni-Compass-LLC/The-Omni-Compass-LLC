# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 1,173 | +26.8% | 247 to 249 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0169 to 0.0204 | STEADY, no difference beyond the noise |
| cache hit rate | 0.617 | 0.783 | +26.8% | 0.165 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.53 | 5.49 | -0.7% | -0.0491 to -0.0253 | GAIN |
| latency, 99th percentile (ms) | 5.59 | 5.58 | -0.1% | -0.0162 to 0.000408 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.15 | 1.27 | -40.8% | -0.884 to -0.87 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 313 | +388.3% | 245 to 252 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.4% | 196 to 198 | power given |
| keys evicted | 243,225 | 0 | -100.0% | -243,518 to -242,932 | shown, not judged |
| host CPU busy (share of the run) | 0.102 | 0.0909 | -11.2% | -0.0426 to 0.0196 | STEADY, no difference beyond the noise |
| host CPU-seconds | 177 | 157 | -11.0% | -78.6 to 39.6 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.424 | 0.298 | -29.8% | -0.278 to 0.0254 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 18.7 |  | 17.2 to 20.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 215 | 192 | -10.5% | -25.1 to -20.1 | GAIN |
| the server's own CPU-seconds (redis-server) | 25.2 | 22.5 | -10.9% | -3.18 to -2.29 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 190 | 169 | -11.1% | -24 to -18.2 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.22 |  | 0.997 to 1.45 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.166 | 0.164 | -1.3% | -0.00527 to 0.000891 | shown, not judged |
| host CPU-seconds without steal | 177 | 157 | -11.0% | -78.6 to 39.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

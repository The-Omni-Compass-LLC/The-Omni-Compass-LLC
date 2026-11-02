# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `e5cfa2afd8ec`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 1,173 | +26.8% | 246 to 250 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0769 to 0.112 | STEADY, no difference beyond the noise |
| cache hit rate | 0.617 | 0.783 | +26.8% | 0.164 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.52 | 5.48 | -0.8% | -0.0653 to -0.0264 | GAIN |
| latency, 99th percentile (ms) | 5.58 | 5.57 | -0.3% | -0.031 to 0.00156 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.15 | 1.27 | -40.8% | -0.881 to -0.875 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 313 | +388.5% | 244 to 253 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.5% | 196 to 198 | power given |
| keys evicted | 243,198 | 0 | -100.0% | -243,331 to -243,065 | shown, not judged |
| host CPU busy (share of the run) | 0.121 | 0.0999 | -17.1% | -0.0377 to -0.0035 | GAIN |
| host CPU-seconds | 212 | 175 | -17.5% | -70 to -4 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.509 | 0.331 | -34.9% | -0.242 to -0.113 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 19 |  | 16.5 to 21.5 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 215 | 192 | -11.0% | -29.1 to -18.5 | GAIN |
| the server's own CPU-seconds (redis-server) | 25.6 | 22.4 | -12.5% | -3.92 to -2.46 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 190 | 167 | -11.7% | -26.3 to -17.9 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.52 |  | 1.08 to 1.96 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.171 | 0.167 | -2.5% | -0.00924 to 0.000658 | shown, not judged |
| host CPU-seconds without steal | 212 | 175 | -17.5% | -70 to -4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

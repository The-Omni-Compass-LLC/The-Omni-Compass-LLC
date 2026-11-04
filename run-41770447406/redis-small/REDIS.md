# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 1,173 | +26.8% | 247 to 248 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.014 to 0.0184 | STEADY, no difference beyond the noise |
| cache hit rate | 0.617 | 0.783 | +26.8% | 0.165 to 0.165 | GAIN |
| latency, 95th percentile (ms) | 5.62 | 5.59 | -0.6% | -0.0699 to -0.00208 | GAIN |
| latency, 99th percentile (ms) | 5.68 | 5.67 | -0.2% | -0.0275 to 0.00292 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.18 | 1.29 | -40.7% | -0.899 to -0.874 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 314 | +389.9% | 245 to 254 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.5% | 196 to 198 | power given |
| keys evicted | 243,199 | 0 | -100.0% | -243,740 to -242,657 | shown, not judged |
| host CPU busy (share of the run) | 0.129 | 0.12 | -7.5% | -0.0642 to 0.0448 | STEADY, no difference beyond the noise |
| host CPU-seconds | 230 | 215 | -6.6% | -126 to 95.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.552 | 0.407 | -26.3% | -0.373 to 0.0823 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 18.7 |  | 14.9 to 22.5 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 223 | 196 | -11.9% | -32.6 to -20.6 | GAIN |
| the server's own CPU-seconds (redis-server) | 23.4 | 20.8 | -11.0% | -3.15 to -1.98 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 199 | 174 | -12.7% | -31.1 to -19.5 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.28 |  | 1.18 to 1.37 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.197 | 0.196 | -0.8% | -0.00264 to -0.000512 | shown, not judged |
| host CPU-seconds without steal | 230 | 215 | -6.6% | -126 to 95.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `b806aadd5bbb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 1,173 | +26.7% | 246 to 248 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | 0.00122 to 0.0154 | GAIN |
| cache hit rate | 0.617 | 0.782 | +26.7% | 0.164 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.69 | 5.66 | -0.5% | -0.0373 to -0.0219 | GAIN |
| latency, 99th percentile (ms) | 5.75 | 5.74 | -0.1% | -0.012 to 0.00233 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.26 | 1.36 | -39.8% | -0.903 to -0.896 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 313 | +388.7% | 244 to 254 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.5% | 196 to 198 | power given |
| keys evicted | 243,091 | 0 | -100.0% | -243,315 to -242,866 | shown, not judged |
| host CPU busy (share of the run) | 0.154 | 0.132 | -14.4% | -0.032 to -0.0125 | GAIN |
| host CPU-seconds | 260 | 223 | -14.2% | -57.3 to -16.3 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.623 | 0.422 | -32.2% | -0.254 to -0.148 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 18.3 |  | 16.9 to 19.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 314 | 277 | -11.8% | -41.7 to -32.3 | GAIN |
| the server's own CPU-seconds (redis-server) | 36 | 32.1 | -11.0% | -4.88 to -3.04 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 278 | 243 | -12.5% | -38.8 to -30.8 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.74 |  | 1.56 to 1.91 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.239 | 0.228 | -4.4% | -0.0171 to -0.00399 | shown, not judged |
| host CPU-seconds without steal | 260 | 223 | -14.2% | -57.3 to -16.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,327 | +23.4% | 249 to 254 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0195 to 0.0749 | STEADY, no difference beyond the noise |
| cache hit rate | 0.717 | 0.885 | +23.4% | 0.166 to 0.169 | GAIN |
| latency, 95th percentile (ms) | 6.16 | 5.63 | -8.5% | -0.563 to -0.484 | GAIN |
| latency, 99th percentile (ms) | 7.04 | 6.57 | -6.8% | -0.684 to -0.268 | GAIN |
| latency, mean (ms) | 1.78 | 0.836 | -53.0% | -0.954 to -0.931 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 246 | +283.8% | 169 to 194 | power given |
| memory used, mean (MB) | 57.2 | 200 | +249.9% | 143 to 143 | power given |
| keys evicted | 71,783 | 0 | -100.0% | -72,275 to -71,290 | shown, not judged |
| host CPU busy (share of the run) | 0.16 | 0.134 | -16.0% | -0.0712 to 0.02 | STEADY, no difference beyond the noise |
| host CPU-seconds | 112 | 93.1 | -16.8% | -56.4 to 18.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.577 | 0.39 | -32.5% | -0.373 to -0.00297 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 9.67 |  | -6.11 to 25.4 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 116 | 104 | -10.2% | -12.8 to -11 | GAIN |
| the server's own CPU-seconds (redis-server) | 13.1 | 11.9 | -9.1% | -2.2 to -0.192 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 103 | 91.9 | -10.9% | -11.9 to -10.6 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.514 |  | 0.481 to 0.548 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0824 | 0.0805 | -2.4% | -0.0111 to 0.0072 | shown, not judged |
| host CPU-seconds without steal | 112 | 93.1 | -16.8% | -56.4 to 18.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,465 | +15.7% | 195 to 201 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0127 to 0.00479 | STEADY, no difference beyond the noise |
| cache hit rate | 0.845 | 0.978 | +15.7% | 0.131 to 0.135 | GAIN |
| latency, 95th percentile (ms) | 5.76 | 0.252 | -95.6% | -5.51 to -5.5 | GAIN |
| latency, 99th percentile (ms) | 5.83 | 5.75 | -1.4% | -0.0988 to -0.0618 | GAIN |
| latency, mean (ms) | 1.06 | 0.316 | -70.1% | -0.753 to -0.732 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 338 | +427.5% | 270 to 277 | power given |
| memory used, mean (MB) | 61.3 | 313 | +411.0% | 248 to 256 | power given |
| keys evicted | 103,605 | 2,644 | -97.4% | -101,967 to -99,955 | shown, not judged |
| host CPU busy (share of the run) | 0.136 | 0.126 | -7.0% | -0.0449 to 0.0259 | STEADY, no difference beyond the noise |
| host CPU-seconds | 229 | 217 | -5.3% | -80.5 to 56.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.401 | 0.328 | -18.1% | -0.194 to 0.0485 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 28.7 |  | 27.2 to 30.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 290 | 252 | -13.1% | -39.2 to -37.1 | GAIN |
| the server's own CPU-seconds (redis-server) | 37.5 | 33.5 | -10.7% | -5.11 to -2.95 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 253 | 217 | -14.2% | -36.4 to -35.2 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.72 |  | 1.46 to 1.99 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.261 | 0.255 | -2.3% | -0.00877 to -0.00313 | shown, not judged |
| host CPU-seconds without steal | 229 | 217 | -5.3% | -80.5 to 56.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 1,172 | +26.8% | 247 to 249 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0166 to 0.021 | STEADY, no difference beyond the noise |
| cache hit rate | 0.617 | 0.783 | +26.8% | 0.165 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.51 | 5.47 | -0.7% | -0.0487 to -0.0317 | GAIN |
| latency, 99th percentile (ms) | 5.58 | 5.57 | -0.3% | -0.0235 to -0.00478 | GAIN |
| latency, mean (ms) | 2.15 | 1.27 | -40.8% | -0.885 to -0.866 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 312 | +387.0% | 246 to 249 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.5% | 196 to 198 | power given |
| keys evicted | 243,180 | 0 | -100.0% | -243,639 to -242,721 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.0983 | -11.3% | -0.0413 to 0.0162 | STEADY, no difference beyond the noise |
| host CPU-seconds | 193 | 172 | -10.9% | -78.3 to 36 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.465 | 0.326 | -29.8% | -0.235 to -0.0412 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 19.3 |  | 15.5 to 23.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 211 | 189 | -10.3% | -26.5 to -16.8 | GAIN |
| the server's own CPU-seconds (redis-server) | 24.9 | 22.3 | -10.7% | -3.26 to -2.06 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 186 | 166 | -10.9% | -24.4 to -16.1 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.29 |  | 0.986 to 1.6 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.171 | 0.166 | -2.7% | -0.0129 to 0.00357 | shown, not judged |
| host CPU-seconds without steal | 193 | 172 | -10.9% | -78.3 to 36 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,387 | +17.2% | 196 to 210 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0291 to 0.00614 | STEADY, no difference beyond the noise |
| cache hit rate | 0.789 | 0.925 | +17.2% | 0.131 to 0.141 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.68 | -1.0% | -0.0617 to -0.0526 | GAIN |
| latency, 99th percentile (ms) | 5.8 | 5.76 | -0.6% | -0.0358 to -0.0285 | GAIN |
| latency, mean (ms) | 1.34 | 0.585 | -56.3% | -0.785 to -0.727 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 350 | +447.6% | 273 to 300 | power given |
| memory used, mean (MB) | 61.2 | 320 | +423.6% | 244 to 274 | power given |
| keys evicted | 138,175 | 2,385 | -98.3% | -139,248 to -132,331 | shown, not judged |
| host CPU busy (share of the run) | 0.129 | 0.112 | -13.7% | -0.0497 to 0.0144 | STEADY, no difference beyond the noise |
| host CPU-seconds | 217 | 189 | -12.8% | -88.3 to 32.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.407 | 0.303 | -25.6% | -0.212 to 0.00367 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 17.3 |  | 15.9 to 18.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 286 | 248 | -13.1% | -42.6 to -32.2 | GAIN |
| the server's own CPU-seconds (redis-server) | 34.4 | 31.2 | -9.5% | -4.17 to -2.35 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 251 | 215 | -14.2% | -40.2 to -31.2 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.6 |  | 1.31 to 1.88 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.23 | 0.217 | -5.6% | -0.0142 to -0.0116 | shown, not judged |
| host CPU-seconds without steal | 217 | 189 | -12.8% | -88.3 to 32.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 12.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

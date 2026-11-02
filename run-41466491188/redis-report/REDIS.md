# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,327 | +23.3% | 246 to 255 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0158 to 0.0307 | STEADY, no difference beyond the noise |
| cache hit rate | 0.718 | 0.885 | +23.3% | 0.165 to 0.17 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.71 | -0.6% | -0.0453 to -0.021 | GAIN |
| latency, 99th percentile (ms) | 5.8 | 5.78 | -0.3% | -0.035 to -0.000289 | GAIN |
| latency, mean (ms) | 1.74 | 0.809 | -53.4% | -0.944 to -0.91 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 245 | +282.0% | 163 to 198 | power given |
| memory used, mean (MB) | 57.2 | 200 | +250.7% | 142 to 145 | power given |
| keys evicted | 71,756 | 73 | -99.9% | -72,540 to -70,826 | shown, not judged |
| host CPU busy (share of the run) | 0.147 | 0.114 | -22.0% | -0.119 to 0.0544 | STEADY, no difference beyond the noise |
| host CPU-seconds | 99.2 | 77.4 | -21.9% | -87.6 to 44.1 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.512 | 0.324 | -36.7% | -0.484 to 0.109 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10 |  | -5.11 to 25.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 121 | 103 | -14.5% | -18.6 to -16.3 | GAIN |
| the server's own CPU-seconds (redis-server) | 14.6 | 12.7 | -12.6% | -2.72 to -0.955 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 106 | 89.7 | -15.3% | -17 to -15.5 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.617 |  | 0.53 to 0.703 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0911 | 0.0868 | -4.7% | -0.00535 to -0.00321 | shown, not judged |
| host CPU-seconds without steal | 99.2 | 77.4 | -21.9% | -87.6 to 44.1 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,465 | +15.7% | 198 to 200 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00515 to -0.00198 | LOSS |
| cache hit rate | 0.844 | 0.978 | +15.8% | 0.132 to 0.134 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 0.233 | -95.9% | -5.52 to -5.5 | GAIN |
| latency, 99th percentile (ms) | 5.81 | 5.73 | -1.3% | -0.0994 to -0.0572 | GAIN |
| latency, mean (ms) | 1.05 | 0.308 | -70.7% | -0.75 to -0.736 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 337 | +426.9% | 271 to 275 | power given |
| memory used, mean (MB) | 61.3 | 313 | +410.0% | 249 to 254 | power given |
| keys evicted | 103,704 | 2,688 | -97.4% | -102,005 to -100,027 | shown, not judged |
| host CPU busy (share of the run) | 0.126 | 0.102 | -18.8% | -0.0815 to 0.0343 | STEADY, no difference beyond the noise |
| host CPU-seconds | 211 | 172 | -18.4% | -150 to 72.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.37 | 0.261 | -29.5% | -0.288 to 0.0698 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 29.3 |  | 27.9 to 30.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 281 | 243 | -13.6% | -45.2 to -31 | GAIN |
| the server's own CPU-seconds (redis-server) | 36.6 | 32.9 | -10.1% | -4.25 to -3.15 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 244 | 208 | -14.7% | -42.6 to -29.1 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.48 |  | 0.979 to 1.98 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.229 | 0.214 | -6.5% | -0.0246 to -0.00532 | shown, not judged |
| host CPU-seconds without steal | 211 | 172 | -18.4% | -150 to 72.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 924 | 1,171 | +26.8% | 246 to 249 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0798 to 0.0549 | STEADY, no difference beyond the noise |
| cache hit rate | 0.617 | 0.782 | +26.8% | 0.165 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.94 | 5.75 | -3.2% | -0.538 to 0.163 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.21 | 6.81 | -5.5% | -1.15 to 0.361 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.36 | 1.43 | -39.5% | -0.994 to -0.865 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 315 | +391.6% | 246 to 256 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.6% | 196 to 198 | power given |
| keys evicted | 243,285 | 0 | -100.0% | -243,843 to -242,726 | shown, not judged |
| host CPU busy (share of the run) | 0.167 | 0.142 | -15.5% | -0.034 to -0.0177 | GAIN |
| host CPU-seconds | 280 | 237 | -15.4% | -56.8 to -29.8 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.675 | 0.45 | -33.3% | -0.265 to -0.184 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 19.3 |  | 17.9 to 20.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 342 | 304 | -11.2% | -55.1 to -21.3 | GAIN |
| the server's own CPU-seconds (redis-server) | 38.9 | 34.5 | -11.4% | -6.94 to -1.9 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 303 | 267 | -11.7% | -49.9 to -21.2 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.76 |  | 1.42 to 2.09 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.258 | 0.246 | -4.4% | -0.0303 to 0.00748 | shown, not judged |
| host CPU-seconds without steal | 280 | 237 | -15.4% | -56.8 to -29.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,387 | +17.2% | 198 to 210 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.114 to 0.0556 | STEADY, no difference beyond the noise |
| cache hit rate | 0.789 | 0.926 | +17.3% | 0.132 to 0.14 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.69 | -0.8% | -0.0628 to -0.0337 | GAIN |
| latency, 99th percentile (ms) | 5.8 | 5.78 | -0.3% | -0.031 to -0.00275 | GAIN |
| latency, mean (ms) | 1.34 | 0.589 | -56.2% | -0.781 to -0.728 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 352 | +449.9% | 275 to 301 | power given |
| memory used, mean (MB) | 61.2 | 322 | +426.4% | 248 to 274 | power given |
| keys evicted | 138,192 | 2,009 | -98.5% | -138,956 to -133,410 | shown, not judged |
| host CPU busy (share of the run) | 0.132 | 0.122 | -7.7% | -0.0467 to 0.0263 | STEADY, no difference beyond the noise |
| host CPU-seconds | 222 | 208 | -6.6% | -85 to 55.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.417 | 0.332 | -20.3% | -0.221 to 0.051 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 17 |  | 17 to 17 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 287 | 254 | -11.4% | -39.5 to -25.7 | GAIN |
| the server's own CPU-seconds (redis-server) | 34.7 | 31.7 | -8.8% | -4.39 to -1.7 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 252 | 221 | -12.4% | -37.6 to -24.9 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.77 |  | 1.33 to 2.2 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.234 | 0.227 | -2.7% | -0.015 to 0.00222 | shown, not judged |
| host CPU-seconds without steal | 222 | 208 | -6.6% | -85 to 55.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 12.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

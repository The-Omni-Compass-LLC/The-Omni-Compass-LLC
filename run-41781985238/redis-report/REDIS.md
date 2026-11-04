# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,077 | 1,327 | +23.2% | 245 to 255 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | 0.034 to 0.047 | GAIN |
| cache hit rate | 0.718 | 0.885 | +23.2% | 0.164 to 0.17 | GAIN |
| latency, 95th percentile (ms) | 5.61 | 5.53 | -1.5% | -0.096 to -0.0668 | GAIN |
| latency, 99th percentile (ms) | 5.68 | 5.65 | -0.6% | -0.0526 to -0.0117 | GAIN |
| latency, mean (ms) | 1.65 | 0.745 | -54.7% | -0.921 to -0.88 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 239 | +273.1% | 168 to 182 | power given |
| memory used, mean (MB) | 57.1 | 200 | +249.3% | 141 to 144 | power given |
| keys evicted | 71,601 | 77.3 | -99.9% | -72,479 to -70,568 | shown, not judged |
| host CPU busy (share of the run) | 0.129 | 0.0924 | -28.4% | -0.0607 to -0.0126 | GAIN |
| host CPU-seconds | 93.4 | 65.4 | -30.0% | -47.8 to -8.16 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.482 | 0.274 | -43.2% | -0.313 to -0.103 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 7 |  | 4.52 to 9.48 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 83 | 71.9 | -13.4% | -13.8 to -8.42 | GAIN |
| the server's own CPU-seconds (redis-server) | 8.06 | 6.8 | -15.6% | -1.44 to -1.07 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 74.9 | 64.7 | -13.7% | -12.7 to -7.78 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.411 |  | 0.39 to 0.432 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0632 | 0.0605 | -4.3% | -0.0105 to 0.00508 | shown, not judged |
| host CPU-seconds without steal | 93.4 | 65.4 | -30.0% | -47.8 to -8.16 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,465 | +15.7% | 196 to 200 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.017 to 0.0044 | STEADY, no difference beyond the noise |
| cache hit rate | 0.845 | 0.978 | +15.7% | 0.131 to 0.135 | GAIN |
| latency, 95th percentile (ms) | 5.76 | 0.244 | -95.8% | -5.53 to -5.49 | GAIN |
| latency, 99th percentile (ms) | 5.82 | 5.75 | -1.3% | -0.0931 to -0.0607 | GAIN |
| latency, mean (ms) | 1.05 | 0.312 | -70.4% | -0.751 to -0.735 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 338 | +427.6% | 271 to 277 | power given |
| memory used, mean (MB) | 61.3 | 313 | +410.9% | 248 to 256 | power given |
| keys evicted | 103,439 | 2,638 | -97.5% | -102,064 to -99,538 | shown, not judged |
| host CPU busy (share of the run) | 0.135 | 0.115 | -15.0% | -0.0606 to 0.0202 | STEADY, no difference beyond the noise |
| host CPU-seconds | 227 | 194 | -14.4% | -111 to 45.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.398 | 0.295 | -26.0% | -0.236 to 0.029 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 29 |  | 29 to 29 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 288 | 250 | -13.3% | -40.9 to -35.7 | GAIN |
| the server's own CPU-seconds (redis-server) | 38.2 | 34.3 | -10.3% | -4.66 to -3.22 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 249 | 214 | -14.4% | -38.2 to -33.6 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.58 |  | 1.28 to 1.88 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.236 | 0.227 | -3.5% | -0.0179 to 0.00113 | shown, not judged |
| host CPU-seconds without steal | 227 | 194 | -14.4% | -111 to 45.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 1,173 | +26.6% | 246 to 247 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0358 to 0.0392 | STEADY, no difference beyond the noise |
| cache hit rate | 0.617 | 0.782 | +26.7% | 0.165 to 0.165 | GAIN |
| latency, 95th percentile (ms) | 5.71 | 5.68 | -0.4% | -0.0441 to -0.0064 | GAIN |
| latency, 99th percentile (ms) | 5.76 | 5.76 | -0.0% | -0.0152 to 0.0109 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.27 | 1.37 | -39.6% | -0.905 to -0.892 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 314 | +390.3% | 244 to 255 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.5% | 196 to 198 | power given |
| keys evicted | 243,046 | 0 | -100.0% | -243,532 to -242,561 | shown, not judged |
| host CPU busy (share of the run) | 0.156 | 0.128 | -18.0% | -0.0446 to -0.0114 | GAIN |
| host CPU-seconds | 262 | 214 | -18.3% | -79.7 to -16.4 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.63 | 0.406 | -35.5% | -0.289 to -0.157 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 18.3 |  | 16.9 to 19.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 317 | 281 | -11.3% | -39 to -32.3 | GAIN |
| the server's own CPU-seconds (redis-server) | 36.5 | 32.7 | -10.4% | -4.57 to -3.03 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 280 | 246 | -12.0% | -36.8 to -30.7 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.89 |  | 1.66 to 2.11 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.242 | 0.233 | -3.5% | -0.0194 to 0.00264 | shown, not judged |
| host CPU-seconds without steal | 262 | 214 | -18.3% | -79.7 to -16.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,387 | +17.1% | 197 to 208 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0149 to 0.00656 | STEADY, no difference beyond the noise |
| cache hit rate | 0.789 | 0.925 | +17.1% | 0.132 to 0.139 | GAIN |
| latency, 95th percentile (ms) | 5.65 | 5.53 | -2.2% | -0.181 to -0.0707 | GAIN |
| latency, 99th percentile (ms) | 5.73 | 5.69 | -0.7% | -0.0505 to -0.0277 | GAIN |
| latency, mean (ms) | 1.28 | 0.541 | -57.8% | -0.764 to -0.718 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 349 | +444.9% | 277 to 293 | power given |
| memory used, mean (MB) | 61.2 | 319 | +420.6% | 250 to 265 | power given |
| keys evicted | 138,135 | 2,701 | -98.0% | -137,841 to -133,027 | shown, not judged |
| host CPU busy (share of the run) | 0.12 | 0.121 | +0.1% | -0.0652 to 0.0655 | STEADY, no difference beyond the noise |
| host CPU-seconds | 214 | 218 | +2.0% | -130 to 139 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.402 | 0.35 | -12.9% | -0.295 to 0.191 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 17.7 |  | 14.8 to 20.5 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 212 | 183 | -13.7% | -34 to -23.8 | GAIN |
| the server's own CPU-seconds (redis-server) | 22.9 | 20 | -12.7% | -3.7 to -2.13 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 188 | 161 | -14.5% | -31.6 to -22.9 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.26 |  | 1.23 to 1.3 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.201 | 0.199 | -1.3% | -0.00894 to 0.00387 | shown, not judged |
| host CPU-seconds without steal | 214 | 218 | +2.0% | -130 to 139 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

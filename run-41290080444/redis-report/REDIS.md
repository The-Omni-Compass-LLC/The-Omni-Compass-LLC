# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `078cb4ce8aeb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,077 | 1,327 | +23.2% | 246 to 254 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0154 to 0.0132 | STEADY, the same |
| cache hit rate | 0.718 | 0.885 | +23.3% | 0.164 to 0.17 | GAIN |
| latency, 95th percentile (ms) | 5.71 | 5.68 | -0.6% | -0.0355 to -0.0277 | GAIN |
| latency, 99th percentile (ms) | 5.77 | 5.75 | -0.3% | -0.0274 to -0.0085 | GAIN |
| latency, mean (ms) | 1.72 | 0.801 | -53.5% | -0.935 to -0.909 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 245 | +282.0% | 163 to 198 | power given |
| memory used, mean (MB) | 57.2 | 200 | +250.6% | 142 to 145 | power given |
| keys evicted | 71,671 | 76.3 | -99.9% | -72,436 to -70,754 | shown, not judged |
| host CPU busy (share of the run) | 0.15 | 0.116 | -22.1% | -0.0722 to 0.00597 | STEADY, no difference beyond the noise |
| host CPU-seconds | 103 | 79.3 | -23.0% | -55.8 to 8.45 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.532 | 0.332 | -37.5% | -0.387 to -0.0118 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 10 |  | -5.11 to 25.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 116 | 99.4 | -14.1% | -16.4 to -16.1 | GAIN |
| the server's own CPU-seconds (redis-server) | 13.8 | 12.3 | -11.3% | -1.84 to -1.29 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 102 | 86.4 | -15.0% | -15.6 to -14.9 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.587 |  | 0.49 to 0.683 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0876 | 0.083 | -5.3% | -0.00585 to -0.00345 | shown, not judged |
| host CPU-seconds without steal | 103 | 79.4 | -23.0% | -55.8 to 8.45 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `078cb4ce8aeb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,466 | +15.7% | 197 to 200 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00426 to 0.00386 | STEADY, the same |
| cache hit rate | 0.845 | 0.978 | +15.7% | 0.132 to 0.133 | GAIN |
| latency, 95th percentile (ms) | 5.23 | 0.125 | -97.6% | -5.12 to -5.09 | GAIN |
| latency, 99th percentile (ms) | 5.29 | 5.23 | -1.1% | -0.106 to -0.0131 | GAIN |
| latency, mean (ms) | 0.881 | 0.198 | -77.5% | -0.69 to -0.676 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 337 | +426.0% | 271 to 275 | power given |
| memory used, mean (MB) | 61.3 | 313 | +410.3% | 249 to 254 | power given |
| keys evicted | 103,322 | 2,679 | -97.4% | -101,151 to -100,134 | shown, not judged |
| host CPU busy (share of the run) | 0.0656 | 0.0507 | -22.7% | -0.0725 to 0.0427 | STEADY, no difference beyond the noise |
| host CPU-seconds | 116 | 89.3 | -22.9% | -134 to 80.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.203 | 0.135 | -33.3% | -0.235 to 0.0995 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 28 |  | 28 to 28 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 122 | 111 | -9.1% | -13 to -9.17 | GAIN |
| the server's own CPU-seconds (redis-server) | 18.7 | 16.4 | -12.2% | -3.18 to -1.38 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 103 | 93.6 | -9.6% | -11.1 to -8.73 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.07 |  | 0.789 to 1.35 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.122 | 0.121 | -0.7% | -0.00638 to 0.00458 | shown, not judged |
| host CPU-seconds without steal | 116 | 89.3 | -22.9% | -134 to 80.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `078cb4ce8aeb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 1,173 | +26.7% | 247 to 248 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00659 to 0.0177 | STEADY, no difference beyond the noise |
| cache hit rate | 0.617 | 0.782 | +26.8% | 0.165 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.69 | 5.66 | -0.5% | -0.0311 to -0.0248 | GAIN |
| latency, 99th percentile (ms) | 5.75 | 5.74 | -0.1% | -0.00763 to -0.00551 | GAIN |
| latency, mean (ms) | 2.26 | 1.36 | -39.8% | -0.907 to -0.892 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 313 | +388.8% | 243 to 255 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.5% | 196 to 198 | power given |
| keys evicted | 243,215 | 0 | -100.0% | -243,500 to -242,930 | shown, not judged |
| host CPU busy (share of the run) | 0.154 | 0.13 | -15.7% | -0.0573 to 0.00916 | STEADY, no difference beyond the noise |
| host CPU-seconds | 260 | 220 | -15.6% | -107 to 25.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.625 | 0.416 | -33.4% | -0.341 to -0.0765 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 18.7 |  | 17.2 to 20.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 308 | 273 | -11.4% | -37.3 to -33 | GAIN |
| the server's own CPU-seconds (redis-server) | 35.1 | 31.6 | -9.9% | -4.74 to -2.18 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 273 | 240 | -12.2% | -35 to -31.7 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.67 |  | 1.42 to 1.92 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.231 | 0.22 | -5.0% | -0.0158 to -0.00731 | shown, not judged |
| host CPU-seconds without steal | 260 | 220 | -15.6% | -107 to 25.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `078cb4ce8aeb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,386 | +17.1% | 199 to 206 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0442 to 0.0127 | STEADY, no difference beyond the noise |
| cache hit rate | 0.789 | 0.925 | +17.1% | 0.132 to 0.138 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.69 | -0.9% | -0.0583 to -0.0446 | GAIN |
| latency, 99th percentile (ms) | 5.8 | 5.78 | -0.4% | -0.0406 to -0.00804 | GAIN |
| latency, mean (ms) | 1.35 | 0.595 | -55.9% | -0.761 to -0.749 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 350 | +446.3% | 278 to 293 | power given |
| memory used, mean (MB) | 61.2 | 319 | +420.8% | 250 to 265 | power given |
| keys evicted | 138,224 | 2,715 | -98.0% | -137,450 to -133,568 | shown, not judged |
| host CPU busy (share of the run) | 0.156 | 0.112 | -28.5% | -0.0585 to -0.0306 | GAIN |
| host CPU-seconds | 270 | 188 | -30.2% | -108 to -55.1 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.507 | 0.302 | -40.4% | -0.25 to -0.159 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 17.7 |  | 16.2 to 19.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 287 | 252 | -12.1% | -40.8 to -28.5 | GAIN |
| the server's own CPU-seconds (redis-server) | 34.7 | 30.9 | -11.0% | -4.42 to -3.18 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 252 | 219 | -12.9% | -38.7 to -26.3 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.66 |  | 1.39 to 1.93 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.23 | 0.223 | -3.4% | -0.012 to -0.00352 | shown, not judged |
| host CPU-seconds without steal | 270 | 188 | -30.2% | -108 to -55.1 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 12.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

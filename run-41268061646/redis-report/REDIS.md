# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `e0fab23c2615`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,326 | +23.2% | 245 to 255 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0718 to -0.0262 | LOSS |
| cache hit rate | 0.718 | 0.885 | +23.3% | 0.164 to 0.17 | GAIN |
| latency, 95th percentile (ms) | 5.76 | 5.72 | -0.7% | -0.0426 to -0.0326 | GAIN |
| latency, 99th percentile (ms) | 5.82 | 5.8 | -0.3% | -0.0362 to 0.00246 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.75 | 0.821 | -53.0% | -0.953 to -0.899 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 245 | +282.3% | 164 to 198 | power given |
| memory used, mean (MB) | 57.2 | 200 | +250.7% | 142 to 145 | power given |
| keys evicted | 71,734 | 79.3 | -99.9% | -72,576 to -70,733 | shown, not judged |
| host CPU busy (share of the run) | 0.155 | 0.105 | -32.2% | -0.131 to 0.0318 | STEADY, no difference beyond the noise |
| host CPU-seconds | 105 | 69.6 | -33.7% | -99.5 to 28.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.542 | 0.292 | -46.2% | -0.562 to 0.0616 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10.7 |  | -3.02 to 24.3 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 125 | 106 | -15.0% | -21.8 to -15.6 | GAIN |
| the server's own CPU-seconds (redis-server) | 15.3 | 13 | -15.4% | -2.66 to -2.06 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 109 | 92.1 | -15.7% | -20.4 to -13.8 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.744 |  | 0.536 to 0.951 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0956 | 0.0925 | -3.2% | -0.00717 to 0.00112 | shown, not judged |
| host CPU-seconds without steal | 105 | 69.6 | -33.7% | -99.5 to 28.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `e0fab23c2615`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,264 | 1,463 | +15.7% | 195 to 202 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00897 to 0.00589 | STEADY, no difference beyond the noise |
| cache hit rate | 0.845 | 0.977 | +15.7% | 0.131 to 0.134 | GAIN |
| latency, 95th percentile (ms) | 5.23 | 0.127 | -97.6% | -5.11 to -5.1 | GAIN |
| latency, 99th percentile (ms) | 5.27 | 5.23 | -0.7% | -0.0493 to -0.025 | GAIN |
| latency, mean (ms) | 0.897 | 0.209 | -76.7% | -0.696 to -0.68 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 336 | +425.3% | 270 to 275 | power given |
| memory used, mean (MB) | 61.3 | 312 | +409.4% | 249 to 253 | power given |
| keys evicted | 103,402 | 2,748 | -97.3% | -101,743 to -99,564 | shown, not judged |
| host CPU busy (share of the run) | 0.0541 | 0.0609 | +12.6% | -0.0231 to 0.0367 | STEADY, no difference beyond the noise |
| host CPU-seconds | 94 | 108 | +14.4% | -42.3 to 69.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.165 | 0.163 | -1.2% | -0.0882 to 0.0843 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 28.3 |  | 26.9 to 29.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 127 | 116 | -8.3% | -14.1 to -6.91 | GAIN |
| the server's own CPU-seconds (redis-server) | 17.8 | 15.8 | -11.1% | -2.64 to -1.32 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 109 | 99.3 | -8.9% | -12.8 to -6.56 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.16 |  | 0.94 to 1.38 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.128 | 0.125 | -1.7% | -0.00903 to 0.00465 | shown, not judged |
| host CPU-seconds without steal | 94 | 108 | +14.4% | -42.3 to 69.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `e0fab23c2615`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 1,173 | +26.6% | 246 to 248 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0244 to 0.039 | STEADY, no difference beyond the noise |
| cache hit rate | 0.618 | 0.783 | +26.7% | 0.164 to 0.165 | GAIN |
| latency, 95th percentile (ms) | 5.69 | 5.67 | -0.4% | -0.0367 to -0.0106 | GAIN |
| latency, 99th percentile (ms) | 5.75 | 5.75 | +0.0% | -0.0127 to 0.0151 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.26 | 1.36 | -39.7% | -0.899 to -0.895 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 314 | +390.1% | 244 to 255 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.5% | 196 to 198 | power given |
| keys evicted | 243,031 | 0 | -100.0% | -243,585 to -242,478 | shown, not judged |
| host CPU busy (share of the run) | 0.146 | 0.133 | -9.0% | -0.0591 to 0.0329 | STEADY, no difference beyond the noise |
| host CPU-seconds | 246 | 226 | -8.0% | -110 to 70.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.589 | 0.428 | -27.3% | -0.359 to 0.0366 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 18 |  | 15.5 to 20.5 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 311 | 278 | -10.7% | -35.9 to -30.3 | GAIN |
| the server's own CPU-seconds (redis-server) | 35 | 31.5 | -10.0% | -4.4 to -2.6 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 275 | 244 | -11.4% | -35.3 to -27.5 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.79 |  | 1.58 to 1.99 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.244 | 0.235 | -3.7% | -0.0193 to 0.0014 | shown, not judged |
| host CPU-seconds without steal | 246 | 226 | -8.0% | -110 to 70.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `e0fab23c2615`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,387 | +17.1% | 198 to 207 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00738 to 0.00427 | STEADY, no difference beyond the noise |
| cache hit rate | 0.79 | 0.925 | +17.1% | 0.132 to 0.138 | GAIN |
| latency, 95th percentile (ms) | 5.64 | 5.51 | -2.4% | -0.216 to -0.0553 | GAIN |
| latency, 99th percentile (ms) | 5.72 | 5.69 | -0.6% | -0.0693 to -0.00369 | GAIN |
| latency, mean (ms) | 1.27 | 0.538 | -57.7% | -0.764 to -0.705 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 349 | +444.8% | 277 to 292 | power given |
| memory used, mean (MB) | 61.2 | 319 | +420.6% | 250 to 265 | power given |
| keys evicted | 138,056 | 2,690 | -98.1% | -137,330 to -133,403 | shown, not judged |
| host CPU busy (share of the run) | 0.126 | 0.112 | -11.4% | -0.0692 to 0.0404 | STEADY, no difference beyond the noise |
| host CPU-seconds | 227 | 202 | -11.2% | -135 to 84.1 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.426 | 0.323 | -24.2% | -0.29 to 0.0837 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 17.7 |  | 14.8 to 20.5 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 205 | 181 | -11.7% | -35.2 to -12.7 | GAIN |
| the server's own CPU-seconds (redis-server) | 22.5 | 19.9 | -11.5% | -3.44 to -1.74 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 182 | 159 | -12.4% | -33 to -12.1 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.26 |  | 1.19 to 1.33 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.198 | 0.196 | -1.1% | -0.013 to 0.0085 | shown, not judged |
| host CPU-seconds without steal | 227 | 202 | -11.2% | -135 to 84.1 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

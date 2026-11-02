# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,326 | +23.2% | 246 to 254 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0809 to 0.052 | STEADY, no difference beyond the noise |
| cache hit rate | 0.717 | 0.885 | +23.3% | 0.165 to 0.17 | GAIN |
| latency, 95th percentile (ms) | 5.76 | 5.73 | -0.6% | -0.0443 to -0.02 | GAIN |
| latency, 99th percentile (ms) | 5.82 | 5.8 | -0.3% | -0.038 to 0.00351 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.75 | 0.821 | -53.0% | -0.929 to -0.921 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 245 | +282.2% | 163 to 198 | power given |
| memory used, mean (MB) | 57.2 | 200 | +250.7% | 142 to 145 | power given |
| keys evicted | 71,778 | 80.3 | -99.9% | -72,481 to -70,913 | shown, not judged |
| host CPU busy (share of the run) | 0.154 | 0.12 | -21.8% | -0.1 to 0.0332 | STEADY, no difference beyond the noise |
| host CPU-seconds | 105 | 81.3 | -22.4% | -75.9 to 28.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.541 | 0.34 | -37.1% | -0.456 to 0.0555 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10.3 |  | -4.22 to 24.9 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 123 | 106 | -13.6% | -18.3 to -15 | GAIN |
| the server's own CPU-seconds (redis-server) | 15 | 13.1 | -12.6% | -2.07 to -1.73 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 108 | 92.1 | -14.4% | -17.3 to -13.8 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.755 |  | 0.667 to 0.842 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0994 | 0.0953 | -4.1% | -0.00706 to -0.00118 | shown, not judged |
| host CPU-seconds without steal | 105 | 81.3 | -22.4% | -75.9 to 28.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,465 | +15.7% | 198 to 199 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0218 to 0.00761 | STEADY, no difference beyond the noise |
| cache hit rate | 0.845 | 0.978 | +15.7% | 0.132 to 0.134 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 0.248 | -95.7% | -5.52 to -5.49 | GAIN |
| latency, 99th percentile (ms) | 5.83 | 5.74 | -1.4% | -0.119 to -0.0441 | GAIN |
| latency, mean (ms) | 1.06 | 0.312 | -70.5% | -0.756 to -0.734 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 337 | +427.1% | 272 to 275 | power given |
| memory used, mean (MB) | 61.3 | 313 | +410.1% | 249 to 254 | power given |
| keys evicted | 103,603 | 2,694 | -97.4% | -101,506 to -100,312 | shown, not judged |
| host CPU busy (share of the run) | 0.154 | 0.109 | -29.0% | -0.08 to -0.00939 | GAIN |
| host CPU-seconds | 266 | 184 | -30.6% | -151 to -11.4 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.466 | 0.28 | -40.0% | -0.304 to -0.0688 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 28.7 |  | 27.2 to 30.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 286 | 247 | -13.6% | -46.1 to -31.8 | GAIN |
| the server's own CPU-seconds (redis-server) | 37.7 | 33.3 | -11.7% | -6.26 to -2.55 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 248 | 212 | -14.6% | -42.3 to -30.2 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.69 |  | 1.42 to 1.97 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.238 | 0.23 | -3.4% | -0.014 to -0.00226 | shown, not judged |
| host CPU-seconds without steal | 266 | 184 | -30.6% | -151 to -11.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 924 | 1,171 | +26.8% | 245 to 249 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0529 to 0.0728 | STEADY, no difference beyond the noise |
| cache hit rate | 0.617 | 0.783 | +26.7% | 0.165 to 0.165 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.21 | -0.2% | -0.0134 to -0.00651 | GAIN |
| latency, 99th percentile (ms) | 5.44 | 5.31 | -2.4% | -0.298 to 0.0354 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.06 | 1.21 | -41.2% | -0.862 to -0.838 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 312 | +387.3% | 244 to 252 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.5% | 196 to 198 | power given |
| keys evicted | 243,116 | 0 | -100.0% | -243,861 to -242,372 | shown, not judged |
| host CPU busy (share of the run) | 0.0634 | 0.0633 | -0.1% | -0.0384 to 0.0383 | STEADY, no difference beyond the noise |
| host CPU-seconds | 111 | 112 | +0.5% | -71 to 72.1 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.267 | 0.212 | -20.7% | -0.211 to 0.1 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 18.3 |  | 16.9 to 19.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 132 | 124 | -6.2% | -10.6 to -5.84 | GAIN |
| the server's own CPU-seconds (redis-server) | 17.3 | 15.5 | -10.1% | -2.14 to -1.36 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 115 | 107 | -6.7% | -9.59 to -5.81 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.23 |  | 0.909 to 1.54 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.131 | 0.127 | -3.0% | -0.0121 to 0.00417 | shown, not judged |
| host CPU-seconds without steal | 111 | 112 | +0.5% | -71 to 72.1 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,386 | +17.2% | 196 to 211 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0165 to 0.00611 | STEADY, no difference beyond the noise |
| cache hit rate | 0.789 | 0.925 | +17.2% | 0.131 to 0.141 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.69 | -1.0% | -0.076 to -0.034 | GAIN |
| latency, 99th percentile (ms) | 5.81 | 5.78 | -0.4% | -0.0552 to 0.00317 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.35 | 0.593 | -56.2% | -0.797 to -0.722 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 350 | +447.5% | 273 to 300 | power given |
| memory used, mean (MB) | 61.2 | 320 | +423.5% | 244 to 274 | power given |
| keys evicted | 138,309 | 2,371 | -98.3% | -139,160 to -132,717 | shown, not judged |
| host CPU busy (share of the run) | 0.147 | 0.12 | -18.5% | -0.0607 to 0.00611 | STEADY, no difference beyond the noise |
| host CPU-seconds | 251 | 204 | -18.8% | -112 to 17.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.471 | 0.326 | -30.7% | -0.264 to -0.0258 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 17 |  | 17 to 17 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 290 | 254 | -12.5% | -44.7 to -27.9 | GAIN |
| the server's own CPU-seconds (redis-server) | 35.4 | 31.1 | -12.0% | -5 to -3.48 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 255 | 221 | -13.2% | -41.4 to -26.1 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.64 |  | 1.45 to 1.83 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.234 | 0.226 | -3.5% | -0.0256 to 0.00917 | shown, not judged |
| host CPU-seconds without steal | 251 | 204 | -18.8% | -112 to 17.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

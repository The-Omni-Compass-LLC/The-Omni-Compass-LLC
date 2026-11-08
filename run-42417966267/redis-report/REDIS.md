# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,326 | +23.2% | 246 to 253 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00853 to 0.0182 | STEADY, no difference beyond the noise |
| cache hit rate | 0.717 | 0.885 | +23.3% | 0.165 to 0.17 | GAIN |
| latency, 95th percentile (ms) | 5.76 | 5.72 | -0.8% | -0.0611 to -0.0298 | GAIN |
| latency, 99th percentile (ms) | 5.83 | 5.79 | -0.6% | -0.0687 to -0.00594 | GAIN |
| latency, mean (ms) | 1.75 | 0.821 | -53.1% | -0.946 to -0.914 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 240 | +274.2% | 167 to 184 | power given |
| memory used, mean (MB) | 57.2 | 200 | +249.7% | 140 to 145 | power given |
| keys evicted | 71,811 | 161 | -99.8% | -72,474 to -70,826 | shown, not judged |
| host CPU busy (share of the run) | 0.145 | 0.126 | -13.5% | -0.0955 to 0.0562 | STEADY, no difference beyond the noise |
| host CPU-seconds | 97.9 | 85.2 | -12.9% | -72.6 to 47.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.506 | 0.357 | -29.4% | -0.466 to 0.169 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6.67 |  | 5.23 to 8.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 123 | 105 | -14.6% | -21.3 to -14.6 | GAIN |
| the server's own CPU-seconds (redis-server) | 14.9 | 12.9 | -13.2% | -2.52 to -1.42 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 108 | 91.4 | -15.4% | -19.6 to -13.6 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.601 |  | 0.465 to 0.738 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0955 | 0.0897 | -6.1% | -0.0123 to 0.00073 | shown, not judged |
| host CPU-seconds without steal | 97.9 | 85.2 | -13.0% | -72.6 to 47.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,265 | 1,463 | +15.7% | 195 to 201 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00571 to 0.00246 | STEADY, no difference beyond the noise |
| cache hit rate | 0.845 | 0.977 | +15.6% | 0.13 to 0.135 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 0.11 | -97.9% | -5.13 to -5.09 | GAIN |
| latency, 99th percentile (ms) | 5.25 | 5.22 | -0.6% | -0.0606 to -0.00445 | GAIN |
| latency, mean (ms) | 0.886 | 0.202 | -77.2% | -0.698 to -0.669 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 336 | +425.6% | 270 to 275 | power given |
| memory used, mean (MB) | 61.3 | 312 | +409.4% | 248 to 254 | power given |
| keys evicted | 103,251 | 2,753 | -97.3% | -102,176 to -98,821 | shown, not judged |
| host CPU busy (share of the run) | 0.0468 | 0.0578 | +23.5% | -0.0328 to 0.0549 | STEADY, no difference beyond the noise |
| host CPU-seconds | 81.5 | 102 | +25.6% | -60.5 to 102 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.143 | 0.155 | +8.6% | -0.124 to 0.148 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 28.7 |  | 27.2 to 30.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 119 | 109 | -7.9% | -18.5 to -0.297 | GAIN |
| the server's own CPU-seconds (redis-server) | 16.7 | 14.6 | -12.5% | -3.45 to -0.741 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 102 | 93.7 | -8.1% | -15.9 to -0.765 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.991 |  | 0.626 to 1.36 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.123 | 0.116 | -5.3% | -0.0145 to 0.00143 | shown, not judged |
| host CPU-seconds without steal | 81.5 | 102 | +25.6% | -60.5 to 102 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 923 | 1,171 | +26.9% | 246 to 251 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0626 to 0.0208 | STEADY, no difference beyond the noise |
| cache hit rate | 0.617 | 0.783 | +26.7% | 0.164 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.23 | 5.22 | -0.2% | -0.0248 to 0.00248 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.4 | -7.0% | -0.707 to -0.103 | GAIN |
| latency, mean (ms) | 2.08 | 1.22 | -41.5% | -0.879 to -0.845 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 313 | +388.9% | 244 to 254 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.5% | 196 to 198 | power given |
| keys evicted | 243,132 | 0 | -100.0% | -243,861 to -242,404 | shown, not judged |
| host CPU busy (share of the run) | 0.0637 | 0.063 | -1.1% | -0.0385 to 0.0371 | STEADY, no difference beyond the noise |
| host CPU-seconds | 111 | 110 | -0.5% | -70.8 to 69.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.267 | 0.209 | -21.6% | -0.202 to 0.0869 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 18 |  | 15.5 to 20.5 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 139 | 129 | -6.8% | -14.7 to -4.13 | GAIN |
| the server's own CPU-seconds (redis-server) | 17.9 | 16.2 | -10.0% | -2.38 to -1.22 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 121 | 112 | -7.5% | -13.8 to -4.19 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.42 |  | 1.29 to 1.55 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.137 | 0.134 | -1.9% | -0.00521 to 0.000124 | shown, not judged |
| host CPU-seconds without steal | 111 | 110 | -0.5% | -70.8 to 69.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,386 | +17.2% | 196 to 210 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0445 to 0.015 | STEADY, no difference beyond the noise |
| cache hit rate | 0.789 | 0.925 | +17.2% | 0.131 to 0.141 | GAIN |
| latency, 95th percentile (ms) | 5.77 | 5.7 | -1.1% | -0.07 to -0.0563 | GAIN |
| latency, 99th percentile (ms) | 5.85 | 5.81 | -0.7% | -0.0755 to -0.0112 | GAIN |
| latency, mean (ms) | 1.36 | 0.604 | -55.7% | -0.792 to -0.727 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 351 | +447.8% | 274 to 299 | power given |
| memory used, mean (MB) | 61.2 | 320 | +423.6% | 244 to 274 | power given |
| keys evicted | 138,329 | 2,371 | -98.3% | -139,101 to -132,815 | shown, not judged |
| host CPU busy (share of the run) | 0.144 | 0.116 | -19.6% | -0.0813 to 0.0251 | STEADY, no difference beyond the noise |
| host CPU-seconds | 243 | 195 | -19.9% | -156 to 59.1 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.456 | 0.312 | -31.6% | -0.337 to 0.0479 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 17.3 |  | 15.9 to 18.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 299 | 262 | -12.2% | -43.9 to -29.2 | GAIN |
| the server's own CPU-seconds (redis-server) | 36.6 | 33 | -9.9% | -5.77 to -1.46 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 262 | 227 | -13.3% | -40.7 to -28.9 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.8 |  | 1.53 to 2.08 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.246 | 0.241 | -1.8% | -0.0141 to 0.00507 | shown, not judged |
| host CPU-seconds without steal | 243 | 195 | -19.9% | -156 to 59.1 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 12.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

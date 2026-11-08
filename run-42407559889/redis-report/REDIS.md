# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `b806aadd5bbb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,326 | +23.2% | 246 to 254 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00715 to 0.014 | STEADY, no difference beyond the noise |
| cache hit rate | 0.718 | 0.885 | +23.3% | 0.165 to 0.169 | GAIN |
| latency, 95th percentile (ms) | 5.58 | 5.51 | -1.3% | -0.0725 to -0.0678 | GAIN |
| latency, 99th percentile (ms) | 5.63 | 5.61 | -0.4% | -0.0323 to -0.0164 | GAIN |
| latency, mean (ms) | 1.65 | 0.747 | -54.7% | -0.918 to -0.883 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 238 | +272.1% | 169 to 180 | power given |
| memory used, mean (MB) | 57.1 | 200 | +250.0% | 141 to 145 | power given |
| keys evicted | 71,724 | 163 | -99.8% | -72,369 to -70,751 | shown, not judged |
| host CPU busy (share of the run) | 0.116 | 0.0716 | -38.1% | -0.103 to 0.0146 | STEADY, no difference beyond the noise |
| host CPU-seconds | 81 | 49.2 | -39.3% | -74.8 to 11.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.418 | 0.206 | -50.7% | -0.384 to -0.0398 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 7.33 |  | 4.46 to 10.2 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 85.5 | 74.3 | -13.0% | -11.7 to -10.5 | GAIN |
| the server's own CPU-seconds (redis-server) | 10.6 | 9.21 | -12.8% | -1.45 to -1.25 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 74.8 | 64.6 | -13.7% | -10.9 to -9.68 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.511 |  | 0.409 to 0.613 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0675 | 0.0676 | +0.1% | -0.0014 to 0.00153 | shown, not judged |
| host CPU-seconds without steal | 81 | 49.2 | -39.3% | -74.8 to 11.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `b806aadd5bbb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,464 | +15.6% | 195 to 199 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0405 to 0.0142 | STEADY, no difference beyond the noise |
| cache hit rate | 0.845 | 0.978 | +15.7% | 0.131 to 0.134 | GAIN |
| latency, 95th percentile (ms) | 5.78 | 0.286 | -95.1% | -5.52 to -5.48 | GAIN |
| latency, 99th percentile (ms) | 5.87 | 5.78 | -1.6% | -0.0974 to -0.0921 | GAIN |
| latency, mean (ms) | 1.08 | 0.334 | -69.0% | -0.752 to -0.733 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 338 | +427.6% | 271 to 277 | power given |
| memory used, mean (MB) | 61.3 | 313 | +410.9% | 248 to 256 | power given |
| keys evicted | 103,482 | 2,646 | -97.4% | -101,731 to -99,940 | shown, not judged |
| host CPU busy (share of the run) | 0.142 | 0.123 | -13.1% | -0.0376 to 0.000418 | STEADY, no difference beyond the noise |
| host CPU-seconds | 237 | 207 | -12.5% | -67.8 to 8.56 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.416 | 0.315 | -24.3% | -0.172 to -0.0298 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 29 |  | 29 to 29 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 301 | 265 | -12.1% | -37.9 to -35 | GAIN |
| the server's own CPU-seconds (redis-server) | 38.5 | 35.4 | -8.3% | -5.16 to -1.23 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 262 | 227 | -13.4% | -38.4 to -32.1 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 2.01 |  | 1.8 to 2.22 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.287 | 0.284 | -1.1% | -0.0182 to 0.0119 | shown, not judged |
| host CPU-seconds without steal | 237 | 207 | -12.5% | -67.8 to 8.56 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

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

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `b806aadd5bbb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,386 | +17.1% | 198 to 206 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0517 to 0.0151 | STEADY, no difference beyond the noise |
| cache hit rate | 0.789 | 0.925 | +17.1% | 0.132 to 0.138 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.69 | -1.0% | -0.0611 to -0.0486 | GAIN |
| latency, 99th percentile (ms) | 5.8 | 5.77 | -0.4% | -0.0393 to -0.00944 | GAIN |
| latency, mean (ms) | 1.34 | 0.59 | -56.0% | -0.772 to -0.733 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 349 | +445.9% | 277 to 293 | power given |
| memory used, mean (MB) | 61.2 | 319 | +420.7% | 250 to 265 | power given |
| keys evicted | 138,113 | 2,701 | -98.0% | -137,449 to -133,376 | shown, not judged |
| host CPU busy (share of the run) | 0.142 | 0.118 | -16.9% | -0.0445 to -0.00357 | GAIN |
| host CPU-seconds | 242 | 201 | -16.7% | -80.3 to -0.273 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.454 | 0.323 | -28.8% | -0.197 to -0.0644 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 17.3 |  | 15.9 to 18.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 289 | 252 | -13.0% | -40 to -35 | GAIN |
| the server's own CPU-seconds (redis-server) | 35.1 | 30.7 | -12.5% | -6.96 to -1.83 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 254 | 219 | -13.7% | -36.3 to -33.1 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.6 |  | 1.34 to 1.86 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.233 | 0.221 | -5.2% | -0.0174 to -0.00695 | shown, not judged |
| host CPU-seconds without steal | 242 | 201 | -16.7% | -80.3 to -0.273 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 12.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

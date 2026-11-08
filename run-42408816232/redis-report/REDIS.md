# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,325 | +23.2% | 245 to 253 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0822 to 0.0351 | STEADY, no difference beyond the noise |
| cache hit rate | 0.718 | 0.884 | +23.2% | 0.164 to 0.168 | GAIN |
| latency, 95th percentile (ms) | 5.23 | 5.22 | -0.2% | -0.0248 to 0.00511 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.28 | 5.25 | -0.4% | -0.0665 to 0.0227 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.53 | 0.68 | -55.7% | -0.882 to -0.828 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 235 | +267.9% | 167 to 176 | power given |
| memory used, mean (MB) | 57.1 | 200 | +249.3% | 142 to 143 | power given |
| keys evicted | 71,639 | 258 | -99.6% | -71,979 to -70,783 | shown, not judged |
| host CPU busy (share of the run) | 0.0496 | 0.0421 | -15.0% | -0.0517 to 0.0368 | STEADY, no difference beyond the noise |
| host CPU-seconds | 34.3 | 29.2 | -14.9% | -37.5 to 27.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.177 | 0.122 | -30.9% | -0.205 to 0.0958 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 7.67 |  | 6.23 to 9.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 51.2 | 46.7 | -8.8% | -8.46 to -0.53 | GAIN |
| the server's own CPU-seconds (redis-server) | 7.27 | 6.31 | -13.2% | -1.48 to -0.444 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 43.9 | 39.9 | -9.2% | -7.54 to -0.539 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.507 |  | 0.409 to 0.606 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.051 | 0.0491 | -3.7% | -0.0063 to 0.00255 | shown, not judged |
| host CPU-seconds without steal | 34.3 | 29.2 | -14.9% | -37.5 to 27.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,466 | +15.6% | 195 to 201 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00956 to -0.00193 | LOSS |
| cache hit rate | 0.845 | 0.978 | +15.7% | 0.131 to 0.134 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 0.234 | -95.9% | -5.52 to -5.49 | GAIN |
| latency, 99th percentile (ms) | 5.81 | 5.73 | -1.3% | -0.0881 to -0.061 | GAIN |
| latency, mean (ms) | 1.05 | 0.307 | -70.7% | -0.749 to -0.73 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 337 | +427.2% | 270 to 277 | power given |
| memory used, mean (MB) | 61.3 | 313 | +410.9% | 248 to 256 | power given |
| keys evicted | 103,265 | 2,649 | -97.4% | -101,829 to -99,402 | shown, not judged |
| host CPU busy (share of the run) | 0.135 | 0.115 | -14.6% | -0.0651 to 0.0256 | STEADY, no difference beyond the noise |
| host CPU-seconds | 229 | 197 | -13.9% | -121 to 57 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.401 | 0.298 | -25.6% | -0.244 to 0.0385 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 29 |  | 29 to 29 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 281 | 244 | -13.3% | -39 to -36.1 | GAIN |
| the server's own CPU-seconds (redis-server) | 36.2 | 32.7 | -9.5% | -4.97 to -1.92 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 245 | 209 | -14.5% | -38.3 to -32.8 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.48 |  | 1.22 to 1.73 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.235 | 0.225 | -4.2% | -0.014 to -0.00553 | shown, not judged |
| host CPU-seconds without steal | 229 | 197 | -13.9% | -121 to 57 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 1,173 | +26.7% | 246 to 249 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0424 to 0.0426 | STEADY, the same |
| cache hit rate | 0.617 | 0.782 | +26.8% | 0.164 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.71 | 5.68 | -0.4% | -0.033 to -0.0136 | GAIN |
| latency, 99th percentile (ms) | 5.77 | 5.77 | +0.1% | -0.000752 to 0.0104 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.27 | 1.37 | -39.6% | -0.907 to -0.891 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 313 | +388.9% | 243 to 255 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.5% | 196 to 198 | power given |
| keys evicted | 243,191 | 0 | -100.0% | -243,862 to -242,519 | shown, not judged |
| host CPU busy (share of the run) | 0.158 | 0.147 | -7.4% | -0.0603 to 0.037 | STEADY, no difference beyond the noise |
| host CPU-seconds | 267 | 250 | -6.1% | -113 to 80.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.64 | 0.474 | -25.9% | -0.374 to 0.0424 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 18.7 |  | 17.2 to 20.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 321 | 286 | -10.7% | -40.9 to -27.8 | GAIN |
| the server's own CPU-seconds (redis-server) | 37.2 | 33.7 | -9.2% | -4.25 to -2.6 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 283 | 251 | -11.5% | -38.5 to -26.6 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.69 |  | 1.4 to 1.97 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.243 | 0.234 | -3.4% | -0.0129 to -0.00377 | shown, not judged |
| host CPU-seconds without steal | 267 | 250 | -6.1% | -113 to 80.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,386 | +17.1% | 197 to 209 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.055 to 0.00837 | STEADY, no difference beyond the noise |
| cache hit rate | 0.789 | 0.925 | +17.2% | 0.131 to 0.14 | GAIN |
| latency, 95th percentile (ms) | 5.77 | 5.7 | -1.1% | -0.0889 to -0.0387 | GAIN |
| latency, 99th percentile (ms) | 5.83 | 5.8 | -0.4% | -0.0586 to 0.0073 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.35 | 0.598 | -55.8% | -0.785 to -0.727 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 351 | +448.1% | 275 to 299 | power given |
| memory used, mean (MB) | 61.2 | 320 | +423.6% | 244 to 274 | power given |
| keys evicted | 138,155 | 2,395 | -98.3% | -138,729 to -132,791 | shown, not judged |
| host CPU busy (share of the run) | 0.145 | 0.132 | -9.5% | -0.0179 to -0.0099 | GAIN |
| host CPU-seconds | 245 | 225 | -8.2% | -29.8 to -10.4 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.461 | 0.361 | -21.6% | -0.106 to -0.093 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 17 |  | 17 to 17 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 299 | 260 | -12.8% | -47.4 to -29.2 | GAIN |
| the server's own CPU-seconds (redis-server) | 36.7 | 32.3 | -12.0% | -6.08 to -2.75 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 262 | 226 | -13.7% | -43.8 to -27.7 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.93 |  | 1.3 to 2.57 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.245 | 0.239 | -2.5% | -0.0165 to 0.00424 | shown, not judged |
| host CPU-seconds without steal | 245 | 225 | -8.2% | -29.8 to -10.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 12.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

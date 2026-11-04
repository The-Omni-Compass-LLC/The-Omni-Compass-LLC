# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `198314d551ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,327 | +23.2% | 246 to 255 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0145 to 0.0342 | STEADY, no difference beyond the noise |
| cache hit rate | 0.718 | 0.885 | +23.2% | 0.164 to 0.17 | GAIN |
| latency, 95th percentile (ms) | 5.56 | 5.47 | -1.6% | -0.101 to -0.0722 | GAIN |
| latency, 99th percentile (ms) | 5.61 | 5.59 | -0.4% | -0.0325 to -0.00933 | GAIN |
| latency, mean (ms) | 1.62 | 0.732 | -54.9% | -0.911 to -0.872 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 238 | +272.1% | 169 to 180 | power given |
| memory used, mean (MB) | 57.1 | 200 | +250.0% | 141 to 144 | power given |
| keys evicted | 71,663 | 159 | -99.8% | -72,414 to -70,595 | shown, not judged |
| host CPU busy (share of the run) | 0.103 | 0.099 | -4.3% | -0.0322 to 0.0232 | STEADY, no difference beyond the noise |
| host CPU-seconds | 72.1 | 70 | -2.9% | -24.4 to 20.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.372 | 0.293 | -21.2% | -0.172 to 0.0141 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 7.33 |  | 4.46 to 10.2 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 81.4 | 71.3 | -12.4% | -10.5 to -9.71 | GAIN |
| the server's own CPU-seconds (redis-server) | 9.96 | 8.72 | -12.4% | -1.56 to -0.909 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 71.3 | 62 | -13.1% | -9.43 to -9.25 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.498 |  | 0.391 to 0.605 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0662 | 0.0624 | -5.7% | -0.00432 to -0.00325 | shown, not judged |
| host CPU-seconds without steal | 72.1 | 70 | -2.9% | -24.4 to 20.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `198314d551ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,466 | +15.7% | 198 to 200 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00537 to 8.65e-05 | STEADY, no difference beyond the noise |
| cache hit rate | 0.845 | 0.978 | +15.7% | 0.132 to 0.133 | GAIN |
| latency, 95th percentile (ms) | 5.5 | 0.162 | -97.0% | -5.36 to -5.32 | GAIN |
| latency, 99th percentile (ms) | 5.61 | 5.48 | -2.2% | -0.13 to -0.12 | GAIN |
| latency, mean (ms) | 0.957 | 0.246 | -74.3% | -0.715 to -0.707 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 337 | +426.5% | 271 to 275 | power given |
| memory used, mean (MB) | 61.3 | 313 | +410.3% | 249 to 254 | power given |
| keys evicted | 103,463 | 2,669 | -97.4% | -101,224 to -100,364 | shown, not judged |
| host CPU busy (share of the run) | 0.101 | 0.0918 | -8.8% | -0.0529 to 0.0351 | STEADY, no difference beyond the noise |
| host CPU-seconds | 176 | 162 | -8.3% | -101 to 71.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.309 | 0.245 | -20.8% | -0.211 to 0.0825 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 28.7 |  | 27.2 to 30.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 193 | 172 | -11.3% | -23.5 to -20.3 | GAIN |
| the server's own CPU-seconds (redis-server) | 25.2 | 22.1 | -12.5% | -3.7 to -2.6 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 168 | 148 | -11.8% | -21.9 to -17.9 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.13 |  | 0.898 to 1.37 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.164 | 0.161 | -1.7% | -0.00676 to 0.00135 | shown, not judged |
| host CPU-seconds without steal | 176 | 162 | -8.3% | -101 to 71.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 15.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `198314d551ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 1,173 | +26.7% | 247 to 248 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.000316 to 0.0205 | STEADY, no difference beyond the noise |
| cache hit rate | 0.617 | 0.783 | +26.8% | 0.165 to 0.165 | GAIN |
| latency, 95th percentile (ms) | 5.7 | 5.67 | -0.4% | -0.0345 to -0.0159 | GAIN |
| latency, 99th percentile (ms) | 5.76 | 5.76 | -0.1% | -0.0246 to 0.0145 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.27 | 1.37 | -39.7% | -0.911 to -0.892 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 313 | +388.9% | 243 to 255 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.5% | 196 to 198 | power given |
| keys evicted | 243,172 | 0 | -100.0% | -243,674 to -242,670 | shown, not judged |
| host CPU busy (share of the run) | 0.153 | 0.136 | -11.1% | -0.0601 to 0.0262 | STEADY, no difference beyond the noise |
| host CPU-seconds | 256 | 230 | -10.3% | -111 to 58.1 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.616 | 0.436 | -29.3% | -0.363 to 0.0026 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 18.7 |  | 17.2 to 20.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 318 | 282 | -11.1% | -40.7 to -30.1 | GAIN |
| the server's own CPU-seconds (redis-server) | 36.4 | 32.8 | -10.0% | -4.13 to -3.13 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 281 | 248 | -11.9% | -38.5 to -28.3 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.62 |  | 1.36 to 1.87 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.239 | 0.229 | -4.5% | -0.0165 to -0.00497 | shown, not judged |
| host CPU-seconds without steal | 256 | 230 | -10.3% | -111 to 58.1 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `198314d551ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,387 | +17.1% | 195 to 210 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.059 to 0.0212 | STEADY, no difference beyond the noise |
| cache hit rate | 0.79 | 0.925 | +17.2% | 0.131 to 0.14 | GAIN |
| latency, 95th percentile (ms) | 5.73 | 5.68 | -0.9% | -0.0619 to -0.0437 | GAIN |
| latency, 99th percentile (ms) | 5.79 | 5.77 | -0.4% | -0.0349 to -0.0101 | GAIN |
| latency, mean (ms) | 1.34 | 0.586 | -56.2% | -0.78 to -0.723 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 350 | +446.9% | 272 to 300 | power given |
| memory used, mean (MB) | 61.2 | 320 | +423.5% | 244 to 274 | power given |
| keys evicted | 138,004 | 2,386 | -98.3% | -138,976 to -132,260 | shown, not judged |
| host CPU busy (share of the run) | 0.138 | 0.106 | -23.3% | -0.0509 to -0.0134 | GAIN |
| host CPU-seconds | 234 | 178 | -23.9% | -90.2 to -21.6 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.438 | 0.285 | -35.0% | -0.2 to -0.107 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 17.3 |  | 15.9 to 18.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 285 | 249 | -12.3% | -37 to -33.1 | GAIN |
| the server's own CPU-seconds (redis-server) | 35 | 31.2 | -10.8% | -3.97 to -3.61 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 249 | 216 | -13.2% | -34.5 to -31.1 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.51 |  | 1.16 to 1.85 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.226 | 0.217 | -4.0% | -0.0183 to 0.000374 | shown, not judged |
| host CPU-seconds without steal | 234 | 178 | -23.9% | -90.2 to -21.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 12.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

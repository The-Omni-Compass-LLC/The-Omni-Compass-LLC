# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `198314d551ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,326 | +23.3% | 247 to 254 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0409 to 0.0507 | STEADY, no difference beyond the noise |
| cache hit rate | 0.717 | 0.885 | +23.3% | 0.165 to 0.17 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.72 | -0.5% | -0.0309 to -0.0271 | GAIN |
| latency, 99th percentile (ms) | 5.81 | 5.8 | -0.2% | -0.0228 to 2.45e-05 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.74 | 0.817 | -53.0% | -0.936 to -0.911 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 245 | +282.1% | 163 to 198 | power given |
| memory used, mean (MB) | 57.2 | 200 | +250.7% | 142 to 145 | power given |
| keys evicted | 71,797 | 77.3 | -99.9% | -72,424 to -71,015 | shown, not judged |
| host CPU busy (share of the run) | 0.152 | 0.121 | -20.5% | -0.0998 to 0.0374 | STEADY, no difference beyond the noise |
| host CPU-seconds | 104 | 81.9 | -21.0% | -76.3 to 32.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.535 | 0.343 | -35.9% | -0.462 to 0.0776 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10.3 |  | -4.22 to 24.9 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 122 | 105 | -13.8% | -19.3 to -14.5 | GAIN |
| the server's own CPU-seconds (redis-server) | 15 | 13.3 | -11.5% | -2.53 to -0.939 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 107 | 91.3 | -14.8% | -17.4 to -14.2 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.655 |  | 0.604 to 0.706 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0963 | 0.0918 | -4.7% | -0.00849 to -0.000486 | shown, not judged |
| host CPU-seconds without steal | 104 | 82 | -21.0% | -76.3 to 32.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `198314d551ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,464 | +15.6% | 197 to 199 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00665 to 0.00416 | STEADY, the same |
| cache hit rate | 0.845 | 0.977 | +15.7% | 0.133 to 0.133 | GAIN |
| latency, 95th percentile (ms) | 5.76 | 0.268 | -95.4% | -5.56 to -5.43 | GAIN |
| latency, 99th percentile (ms) | 5.84 | 5.75 | -1.6% | -0.126 to -0.0602 | GAIN |
| latency, mean (ms) | 1.06 | 0.317 | -70.2% | -0.753 to -0.737 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 337 | +426.6% | 271 to 275 | power given |
| memory used, mean (MB) | 61.3 | 312 | +409.5% | 248 to 254 | power given |
| keys evicted | 103,593 | 2,770 | -97.3% | -100,958 to -100,687 | shown, not judged |
| host CPU busy (share of the run) | 0.146 | 0.109 | -25.7% | -0.0578 to -0.0173 | GAIN |
| host CPU-seconds | 249 | 183 | -26.6% | -107 to -25.9 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.437 | 0.278 | -36.5% | -0.228 to -0.0912 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 28.7 |  | 27.2 to 30.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 291 | 252 | -13.3% | -41.9 to -35.3 | GAIN |
| the server's own CPU-seconds (redis-server) | 38.8 | 34 | -12.2% | -5.65 to -3.79 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 252 | 216 | -14.1% | -38.2 to -32.8 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.63 |  | 1.28 to 1.97 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.239 | 0.232 | -3.1% | -0.0114 to -0.00347 | shown, not judged |
| host CPU-seconds without steal | 249 | 183 | -26.6% | -107 to -25.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `198314d551ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 924 | 1,172 | +26.8% | 246 to 249 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0315 to 0.0127 | STEADY, no difference beyond the noise |
| cache hit rate | 0.617 | 0.783 | +26.7% | 0.165 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.21 | 5.2 | -0.2% | -0.0117 to -0.0084 | GAIN |
| latency, 99th percentile (ms) | 5.31 | 5.25 | -1.1% | -0.0758 to -0.0396 | GAIN |
| latency, mean (ms) | 2.05 | 1.2 | -41.5% | -0.864 to -0.843 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 312 | +387.6% | 243 to 253 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.4% | 196 to 198 | power given |
| keys evicted | 243,103 | 0 | -100.0% | -243,548 to -242,658 | shown, not judged |
| host CPU busy (share of the run) | 0.0679 | 0.0659 | -3.0% | -0.0277 to 0.0236 | STEADY, no difference beyond the noise |
| host CPU-seconds | 120 | 117 | -2.6% | -52 to 45.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.288 | 0.221 | -23.2% | -0.181 to 0.047 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 18.3 |  | 15.5 to 21.2 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 129 | 120 | -7.1% | -10.3 to -8.09 | GAIN |
| the server's own CPU-seconds (redis-server) | 16.7 | 14.8 | -11.3% | -2.07 to -1.7 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 112 | 104 | -7.5% | -9.73 to -7.08 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.11 |  | 0.661 to 1.55 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.126 | 0.118 | -6.3% | -0.0191 to 0.00322 | shown, not judged |
| host CPU-seconds without steal | 120 | 117 | -2.6% | -52 to 45.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `198314d551ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,386 | +17.2% | 199 to 208 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0172 to 0.00671 | STEADY, no difference beyond the noise |
| cache hit rate | 0.789 | 0.925 | +17.2% | 0.133 to 0.139 | GAIN |
| latency, 95th percentile (ms) | 5.54 | 5.44 | -1.8% | -0.111 to -0.0907 | GAIN |
| latency, 99th percentile (ms) | 5.61 | 5.59 | -0.4% | -0.0266 to -0.0196 | GAIN |
| latency, mean (ms) | 1.25 | 0.527 | -57.9% | -0.74 to -0.708 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 349 | +444.6% | 275 to 294 | power given |
| memory used, mean (MB) | 61.2 | 320 | +422.4% | 252 to 265 | power given |
| keys evicted | 138,378 | 2,448 | -98.2% | -137,942 to -133,917 | shown, not judged |
| host CPU busy (share of the run) | 0.101 | 0.105 | +3.2% | -0.0186 to 0.0252 | STEADY, no difference beyond the noise |
| host CPU-seconds | 177 | 186 | +5.1% | -33.2 to 51.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.332 | 0.298 | -10.3% | -0.111 to 0.0426 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 17.7 |  | 14.8 to 20.5 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 197 | 177 | -9.9% | -21.1 to -17.9 | GAIN |
| the server's own CPU-seconds (redis-server) | 24.2 | 21.6 | -10.7% | -2.91 to -2.24 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 172 | 154 | -10.5% | -19.8 to -16.5 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.25 |  | 1.04 to 1.45 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.169 | 0.168 | -0.6% | -0.00629 to 0.00422 | shown, not judged |
| host CPU-seconds without steal | 177 | 186 | +5.1% | -33.2 to 51.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

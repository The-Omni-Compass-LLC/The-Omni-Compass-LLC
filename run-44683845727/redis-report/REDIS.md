# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,327 | +23.3% | 247 to 255 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0267 to -0.00128 | LOSS |
| cache hit rate | 0.718 | 0.885 | +23.3% | 0.165 to 0.17 | GAIN |
| latency, 95th percentile (ms) | 5.59 | 5.52 | -1.3% | -0.111 to -0.0369 | GAIN |
| latency, 99th percentile (ms) | 5.64 | 5.62 | -0.2% | -0.0325 to 0.00521 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.65 | 0.745 | -54.8% | -0.928 to -0.875 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 240 | +274.2% | 170 to 181 | power given |
| memory used, mean (MB) | 57.1 | 200 | +250.7% | 142 to 145 | power given |
| keys evicted | 71,694 | 72.7 | -99.9% | -72,458 to -70,784 | shown, not judged |
| host CPU busy (share of the run) | 0.115 | 0.1 | -13.0% | -0.0771 to 0.047 | STEADY, no difference beyond the noise |
| host CPU-seconds | 80.6 | 70.4 | -12.7% | -58.2 to 37.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.416 | 0.295 | -29.2% | -0.353 to 0.11 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 7 |  | 4.52 to 9.48 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 86.3 | 74.8 | -13.4% | -15.6 to -7.58 | GAIN |
| the server's own CPU-seconds (redis-server) | 10.6 | 9.35 | -12.1% | -1.57 to -0.995 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 75.6 | 64.8 | -14.3% | -14.5 to -7.12 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.524 |  | 0.416 to 0.633 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0685 | 0.0667 | -2.6% | -0.00571 to 0.00218 | shown, not judged |
| host CPU-seconds without steal | 80.6 | 70.4 | -12.7% | -58.2 to 37.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,465 | +15.7% | 196 to 201 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00889 to -0.00345 | LOSS |
| cache hit rate | 0.845 | 0.978 | +15.7% | 0.131 to 0.136 | GAIN |
| latency, 95th percentile (ms) | 5.76 | 0.266 | -95.4% | -5.51 to -5.48 | GAIN |
| latency, 99th percentile (ms) | 5.84 | 5.75 | -1.4% | -0.102 to -0.0642 | GAIN |
| latency, mean (ms) | 1.06 | 0.318 | -70.1% | -0.761 to -0.729 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 338 | +428.0% | 271 to 277 | power given |
| memory used, mean (MB) | 61.3 | 313 | +411.2% | 248 to 256 | power given |
| keys evicted | 103,578 | 2,596 | -97.5% | -102,674 to -99,290 | shown, not judged |
| host CPU busy (share of the run) | 0.144 | 0.119 | -17.7% | -0.0907 to 0.0397 | STEADY, no difference beyond the noise |
| host CPU-seconds | 245 | 202 | -17.4% | -167 to 82.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.429 | 0.307 | -28.6% | -0.317 to 0.0721 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 28.3 |  | 25.5 to 31.2 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 289 | 252 | -13.0% | -42.1 to -33 | GAIN |
| the server's own CPU-seconds (redis-server) | 38 | 33.9 | -10.7% | -6.35 to -1.79 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 251 | 216 | -14.0% | -37.8 to -32.6 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.69 |  | 1.43 to 1.95 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.24 | 0.232 | -3.0% | -0.011 to -0.00348 | shown, not judged |
| host CPU-seconds without steal | 245 | 202 | -17.4% | -167 to 82.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 1,173 | +26.8% | 247 to 249 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0169 to 0.0204 | STEADY, no difference beyond the noise |
| cache hit rate | 0.617 | 0.783 | +26.8% | 0.165 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.53 | 5.49 | -0.7% | -0.0491 to -0.0253 | GAIN |
| latency, 99th percentile (ms) | 5.59 | 5.58 | -0.1% | -0.0162 to 0.000408 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.15 | 1.27 | -40.8% | -0.884 to -0.87 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 313 | +388.3% | 245 to 252 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.4% | 196 to 198 | power given |
| keys evicted | 243,225 | 0 | -100.0% | -243,518 to -242,932 | shown, not judged |
| host CPU busy (share of the run) | 0.102 | 0.0909 | -11.2% | -0.0426 to 0.0196 | STEADY, no difference beyond the noise |
| host CPU-seconds | 177 | 157 | -11.0% | -78.6 to 39.6 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.424 | 0.298 | -29.8% | -0.278 to 0.0254 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 18.7 |  | 17.2 to 20.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 215 | 192 | -10.5% | -25.1 to -20.1 | GAIN |
| the server's own CPU-seconds (redis-server) | 25.2 | 22.5 | -10.9% | -3.18 to -2.29 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 190 | 169 | -11.1% | -24 to -18.2 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.22 |  | 0.997 to 1.45 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.166 | 0.164 | -1.3% | -0.00527 to 0.000891 | shown, not judged |
| host CPU-seconds without steal | 177 | 157 | -11.0% | -78.6 to 39.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,387 | +17.2% | 196 to 211 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0398 to 0.038 | STEADY, the same |
| cache hit rate | 0.789 | 0.925 | +17.2% | 0.131 to 0.141 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.69 | -1.1% | -0.0839 to -0.0411 | GAIN |
| latency, 99th percentile (ms) | 5.81 | 5.78 | -0.6% | -0.0543 to -0.0141 | GAIN |
| latency, mean (ms) | 1.35 | 0.592 | -56.3% | -0.8 to -0.726 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 351 | +447.8% | 273 to 300 | power given |
| memory used, mean (MB) | 61.2 | 320 | +423.5% | 244 to 274 | power given |
| keys evicted | 138,351 | 2,405 | -98.3% | -139,487 to -132,405 | shown, not judged |
| host CPU busy (share of the run) | 0.15 | 0.112 | -25.5% | -0.0413 to -0.0351 | GAIN |
| host CPU-seconds | 255 | 188 | -26.4% | -73.5 to -61.1 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.479 | 0.301 | -37.2% | -0.197 to -0.159 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 17.3 |  | 15.9 to 18.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 293 | 252 | -13.8% | -46.5 to -34.3 | GAIN |
| the server's own CPU-seconds (redis-server) | 35.8 | 31.9 | -11.0% | -6.95 to -0.904 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 257 | 219 | -14.8% | -41.3 to -34.7 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.58 |  | 1.35 to 1.81 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.238 | 0.227 | -4.6% | -0.0162 to -0.0059 | shown, not judged |
| host CPU-seconds without steal | 255 | 188 | -26.4% | -73.4 to -61.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 12.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

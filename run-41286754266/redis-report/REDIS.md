# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `507f8c2251ae`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,326 | +23.3% | 246 to 255 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0103 to 0.0314 | STEADY, no difference beyond the noise |
| cache hit rate | 0.718 | 0.885 | +23.3% | 0.165 to 0.17 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.71 | -0.6% | -0.0389 to -0.0256 | GAIN |
| latency, 99th percentile (ms) | 5.8 | 5.78 | -0.3% | -0.0303 to -0.00855 | GAIN |
| latency, mean (ms) | 1.74 | 0.811 | -53.3% | -0.938 to -0.911 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 245 | +282.0% | 163 to 198 | power given |
| memory used, mean (MB) | 57.2 | 200 | +250.7% | 142 to 145 | power given |
| keys evicted | 71,763 | 77 | -99.9% | -72,496 to -70,876 | shown, not judged |
| host CPU busy (share of the run) | 0.145 | 0.119 | -17.9% | -0.11 to 0.0576 | STEADY, no difference beyond the noise |
| host CPU-seconds | 98.4 | 81.2 | -17.5% | -82.1 to 47.6 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.508 | 0.34 | -33.1% | -0.467 to 0.131 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10 |  | -5.11 to 25.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 119 | 102 | -14.2% | -18.1 to -15.8 | GAIN |
| the server's own CPU-seconds (redis-server) | 14.5 | 12.8 | -11.6% | -2.43 to -0.942 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 105 | 88.8 | -15.2% | -16.3 to -15.5 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.602 |  | 0.515 to 0.688 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0902 | 0.0856 | -5.2% | -0.00965 to 0.000316 | shown, not judged |
| host CPU-seconds without steal | 98.4 | 81.2 | -17.5% | -82.1 to 47.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `507f8c2251ae`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,465 | +15.7% | 197 to 201 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0132 to 0.00199 | STEADY, no difference beyond the noise |
| cache hit rate | 0.845 | 0.978 | +15.8% | 0.132 to 0.135 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 0.247 | -95.7% | -5.51 to -5.5 | GAIN |
| latency, 99th percentile (ms) | 5.82 | 5.74 | -1.4% | -0.0882 to -0.07 | GAIN |
| latency, mean (ms) | 1.06 | 0.314 | -70.3% | -0.755 to -0.733 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 338 | +428.1% | 271 to 277 | power given |
| memory used, mean (MB) | 61.3 | 314 | +411.8% | 248 to 257 | power given |
| keys evicted | 103,625 | 2,579 | -97.5% | -102,070 to -100,022 | shown, not judged |
| host CPU busy (share of the run) | 0.153 | 0.113 | -26.5% | -0.0624 to -0.0189 | GAIN |
| host CPU-seconds | 264 | 191 | -27.8% | -116 to -30.7 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.464 | 0.29 | -37.6% | -0.244 to -0.104 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 29 |  | 29 to 29 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 287 | 249 | -13.1% | -40.7 to -34.6 | GAIN |
| the server's own CPU-seconds (redis-server) | 37.9 | 34.2 | -9.7% | -4.46 to -2.91 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 248 | 213 | -14.3% | -38.7 to -32.4 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.58 |  | 1.27 to 1.88 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.234 | 0.225 | -3.6% | -0.0128 to -0.00394 | shown, not judged |
| host CPU-seconds without steal | 264 | 191 | -27.8% | -116 to -30.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `507f8c2251ae`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 1,173 | +26.7% | 247 to 248 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0043 to 0.016 | STEADY, no difference beyond the noise |
| cache hit rate | 0.617 | 0.782 | +26.8% | 0.165 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.71 | 5.68 | -0.5% | -0.0322 to -0.0273 | GAIN |
| latency, 99th percentile (ms) | 5.78 | 5.77 | -0.1% | -0.0225 to 0.00552 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.27 | 1.37 | -39.7% | -0.913 to -0.89 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 313 | +389.2% | 244 to 254 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.5% | 196 to 198 | power given |
| keys evicted | 243,240 | 0 | -100.0% | -243,725 to -242,755 | shown, not judged |
| host CPU busy (share of the run) | 0.144 | 0.139 | -3.8% | -0.0345 to 0.0235 | STEADY, no difference beyond the noise |
| host CPU-seconds | 241 | 237 | -1.7% | -61 to 52.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.578 | 0.448 | -22.5% | -0.246 to -0.0136 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 19 |  | 16.5 to 21.5 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 312 | 277 | -11.1% | -39 to -30.4 | GAIN |
| the server's own CPU-seconds (redis-server) | 37.6 | 35.1 | -6.7% | -5.74 to 0.74 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 274 | 240 | -12.3% | -35.9 to -31.5 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.5 |  | 1.29 to 1.71 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.234 | 0.225 | -3.7% | -0.0173 to -0.000169 | shown, not judged |
| host CPU-seconds without steal | 241 | 237 | -1.7% | -61 to 52.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `507f8c2251ae`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,387 | +17.1% | 197 to 208 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00901 to 0.00164 | STEADY, no difference beyond the noise |
| cache hit rate | 0.789 | 0.925 | +17.1% | 0.132 to 0.139 | GAIN |
| latency, 95th percentile (ms) | 5.64 | 5.51 | -2.3% | -0.172 to -0.0823 | GAIN |
| latency, 99th percentile (ms) | 5.72 | 5.68 | -0.7% | -0.0667 to -0.00848 | GAIN |
| latency, mean (ms) | 1.27 | 0.538 | -57.7% | -0.762 to -0.707 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 349 | +444.9% | 277 to 293 | power given |
| memory used, mean (MB) | 61.2 | 319 | +420.6% | 250 to 265 | power given |
| keys evicted | 138,156 | 2,695 | -98.0% | -137,981 to -132,941 | shown, not judged |
| host CPU busy (share of the run) | 0.122 | 0.113 | -7.8% | -0.0614 to 0.0425 | STEADY, no difference beyond the noise |
| host CPU-seconds | 218 | 203 | -7.1% | -118 to 87.4 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.409 | 0.325 | -20.7% | -0.263 to 0.0943 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 17.7 |  | 14.8 to 20.5 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 205 | 180 | -12.3% | -37.5 to -12.9 | GAIN |
| the server's own CPU-seconds (redis-server) | 22.4 | 19.9 | -11.2% | -3.31 to -1.71 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 182 | 158 | -13.1% | -35.4 to -12.4 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.24 |  | 1.18 to 1.31 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.2 | 0.197 | -1.9% | -0.0183 to 0.0108 | shown, not judged |
| host CPU-seconds without steal | 218 | 203 | -7.1% | -118 to 87.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `baaf413e44d9`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,326 | +23.3% | 248 to 253 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0154 to 0.0395 | STEADY, no difference beyond the noise |
| cache hit rate | 0.718 | 0.885 | +23.2% | 0.165 to 0.169 | GAIN |
| latency, 95th percentile (ms) | 5.58 | 5.49 | -1.6% | -0.107 to -0.0693 | GAIN |
| latency, 99th percentile (ms) | 5.63 | 5.61 | -0.5% | -0.0332 to -0.0199 | GAIN |
| latency, mean (ms) | 1.64 | 0.741 | -54.8% | -0.909 to -0.891 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 238 | +271.9% | 169 to 179 | power given |
| memory used, mean (MB) | 57.1 | 200 | +250.0% | 141 to 144 | power given |
| keys evicted | 71,695 | 162 | -99.8% | -72,220 to -70,846 | shown, not judged |
| host CPU busy (share of the run) | 0.115 | 0.0931 | -19.0% | -0.0826 to 0.0389 | STEADY, no difference beyond the noise |
| host CPU-seconds | 80.7 | 65.4 | -19.0% | -63 to 32.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.417 | 0.274 | -34.3% | -0.357 to 0.0715 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 7.67 |  | 3.87 to 11.5 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 84 | 72.2 | -14.1% | -13.4 to -10.3 | GAIN |
| the server's own CPU-seconds (redis-server) | 10.5 | 9.15 | -13.2% | -2.16 to -0.627 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 73.4 | 62.5 | -14.9% | -12.2 to -9.66 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.498 |  | 0.419 to 0.577 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0668 | 0.0637 | -4.7% | -0.00496 to -0.00133 | shown, not judged |
| host CPU-seconds without steal | 80.7 | 65.4 | -19.0% | -63 to 32.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `baaf413e44d9`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,265 | 1,463 | +15.6% | 193 to 202 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.04 to 0.0606 | STEADY, no difference beyond the noise |
| cache hit rate | 0.845 | 0.978 | +15.7% | 0.131 to 0.134 | GAIN |
| latency, 95th percentile (ms) | 5.23 | 0.12 | -97.7% | -5.15 to -5.07 | GAIN |
| latency, 99th percentile (ms) | 5.26 | 5.22 | -0.8% | -0.0689 to -0.0105 | GAIN |
| latency, mean (ms) | 0.891 | 0.207 | -76.7% | -0.707 to -0.66 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 337 | +426.8% | 272 to 274 | power given |
| memory used, mean (MB) | 61.3 | 313 | +410.9% | 251 to 253 | power given |
| keys evicted | 103,231 | 2,621 | -97.5% | -101,675 to -99,547 | shown, not judged |
| host CPU busy (share of the run) | 0.0654 | 0.0537 | -17.9% | -0.0598 to 0.0364 | STEADY, no difference beyond the noise |
| host CPU-seconds | 116 | 94.5 | -18.2% | -110 to 67.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.203 | 0.144 | -29.3% | -0.199 to 0.0807 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 28 |  | 28 to 28 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 123 | 114 | -7.1% | -21.2 to 3.58 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 17.3 | 15.2 | -12.5% | -4.22 to -0.0953 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 106 | 98 | -7.3% | -17.7 to 2.29 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.09 |  | 0.714 to 1.47 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.121 | 0.12 | -0.9% | -0.0327 to 0.0305 | shown, not judged |
| host CPU-seconds without steal | 116 | 94.5 | -18.2% | -110 to 67.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 15.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `baaf413e44d9`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 1,173 | +26.7% | 247 to 248 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0303 to 0.0338 | STEADY, no difference beyond the noise |
| cache hit rate | 0.617 | 0.782 | +26.8% | 0.164 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.7 | 5.67 | -0.5% | -0.0517 to -0.00257 | GAIN |
| latency, 99th percentile (ms) | 5.77 | 5.75 | -0.3% | -0.0983 to 0.065 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.27 | 1.37 | -39.8% | -0.925 to -0.881 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 313 | +389.0% | 244 to 254 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.5% | 196 to 198 | power given |
| keys evicted | 243,172 | 0 | -100.0% | -243,652 to -242,692 | shown, not judged |
| host CPU busy (share of the run) | 0.155 | 0.127 | -17.8% | -0.053 to -0.00207 | GAIN |
| host CPU-seconds | 262 | 214 | -18.2% | -96.1 to 0.706 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.628 | 0.405 | -35.5% | -0.334 to -0.111 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 19 |  | 19 to 19 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 315 | 281 | -10.7% | -43.9 to -23.7 | GAIN |
| the server's own CPU-seconds (redis-server) | 36.4 | 32.3 | -11.4% | -6.4 to -1.87 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 279 | 247 | -11.2% | -38.9 to -23.5 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.53 |  | 1.33 to 1.72 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.237 | 0.228 | -3.9% | -0.0167 to -0.00176 | shown, not judged |
| host CPU-seconds without steal | 262 | 214 | -18.2% | -96.1 to 0.706 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `baaf413e44d9`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,387 | +17.1% | 195 to 211 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0501 to 0.0268 | STEADY, no difference beyond the noise |
| cache hit rate | 0.789 | 0.925 | +17.2% | 0.131 to 0.141 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.68 | -1.0% | -0.065 to -0.0546 | GAIN |
| latency, 99th percentile (ms) | 5.81 | 5.77 | -0.6% | -0.0384 to -0.0258 | GAIN |
| latency, mean (ms) | 1.34 | 0.588 | -56.2% | -0.786 to -0.723 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 350 | +447.5% | 273 to 300 | power given |
| memory used, mean (MB) | 61.2 | 320 | +423.6% | 244 to 274 | power given |
| keys evicted | 138,116 | 2,394 | -98.3% | -139,141 to -132,303 | shown, not judged |
| host CPU busy (share of the run) | 0.143 | 0.122 | -15.0% | -0.0502 to 0.00722 | STEADY, no difference beyond the noise |
| host CPU-seconds | 244 | 208 | -14.8% | -92.9 to 20.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.458 | 0.333 | -27.3% | -0.23 to -0.0202 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 17.3 |  | 15.9 to 18.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 284 | 250 | -12.2% | -38.1 to -31.2 | GAIN |
| the server's own CPU-seconds (redis-server) | 34.9 | 31.1 | -10.9% | -4.64 to -2.96 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 249 | 217 | -13.0% | -35.2 to -29.6 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.58 |  | 1.31 to 1.85 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.228 | 0.219 | -4.0% | -0.0137 to -0.00449 | shown, not judged |
| host CPU-seconds without steal | 244 | 208 | -14.8% | -92.9 to 20.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

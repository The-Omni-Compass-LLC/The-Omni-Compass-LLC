# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `4082deec8fda`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,075 | 1,324 | +23.2% | 245 to 254 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0695 to 0.101 | STEADY, no difference beyond the noise |
| cache hit rate | 0.718 | 0.884 | +23.2% | 0.165 to 0.168 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.21 | -0.1% | -0.0158 to 0.00337 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.27 | 5.25 | -0.4% | -0.0517 to 0.00952 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.54 | 0.683 | -55.6% | -0.879 to -0.835 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 236 | +269.5% | 170 to 175 | power given |
| memory used, mean (MB) | 57.2 | 199 | +248.7% | 141 to 143 | power given |
| keys evicted | 71,686 | 231 | -99.7% | -72,048 to -70,861 | shown, not judged |
| host CPU busy (share of the run) | 0.0586 | 0.0624 | +6.6% | -0.0874 to 0.0951 | STEADY, no difference beyond the noise |
| host CPU-seconds | 41.4 | 44.2 | +6.7% | -66 to 71.6 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.214 | 0.185 | -13.4% | -0.367 to 0.309 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 8.67 |  | 7.23 to 10.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 49.2 | 46.4 | -5.8% | -6.27 to 0.57 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 6.94 | 6.28 | -9.6% | -1.36 to 0.0291 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 42.2 | 39.5 | -6.3% | -5.29 to -0.0544 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.492 |  | 0.349 to 0.635 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0483 | 0.0468 | -3.2% | -0.00343 to 0.000311 | shown, not judged |
| host CPU-seconds without steal | 41.4 | 44.2 | +6.7% | -66 to 71.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `4082deec8fda`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,466 | +15.7% | 195 to 202 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.011 to -0.000442 | LOSS |
| cache hit rate | 0.845 | 0.978 | +15.7% | 0.131 to 0.135 | GAIN |
| latency, 95th percentile (ms) | 5.73 | 0.229 | -96.0% | -5.51 to -5.5 | GAIN |
| latency, 99th percentile (ms) | 5.8 | 5.73 | -1.2% | -0.0751 to -0.0684 | GAIN |
| latency, mean (ms) | 1.04 | 0.303 | -71.0% | -0.758 to -0.722 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 338 | +428.2% | 271 to 278 | power given |
| memory used, mean (MB) | 61.3 | 314 | +411.7% | 248 to 257 | power given |
| keys evicted | 103,483 | 2,569 | -97.5% | -102,384 to -99,445 | shown, not judged |
| host CPU busy (share of the run) | 0.132 | 0.118 | -11.0% | -0.103 to 0.0738 | STEADY, no difference beyond the noise |
| host CPU-seconds | 225 | 203 | -9.9% | -194 to 150 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.395 | 0.307 | -22.1% | -0.369 to 0.194 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 28.3 |  | 26.9 to 29.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 275 | 240 | -12.9% | -41.2 to -29.8 | GAIN |
| the server's own CPU-seconds (redis-server) | 35.4 | 31.7 | -10.4% | -4.99 to -2.37 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 240 | 206 | -13.9% | -38.2 to -28.5 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.5 |  | 1.26 to 1.74 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.227 | 0.218 | -3.9% | -0.0169 to -0.000713 | shown, not judged |
| host CPU-seconds without steal | 225 | 203 | -9.9% | -194 to 150 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `4082deec8fda`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 1,173 | +26.7% | 247 to 249 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0365 to 0.0383 | STEADY, the same |
| cache hit rate | 0.617 | 0.783 | +26.7% | 0.165 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.61 | 5.57 | -0.8% | -0.0576 to -0.0281 | GAIN |
| latency, 99th percentile (ms) | 5.69 | 5.67 | -0.4% | -0.0297 to -0.0101 | GAIN |
| latency, mean (ms) | 2.19 | 1.3 | -40.8% | -0.902 to -0.884 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 313 | +389.6% | 245 to 254 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.4% | 196 to 198 | power given |
| keys evicted | 243,136 | 0 | -100.0% | -243,379 to -242,893 | shown, not judged |
| host CPU busy (share of the run) | 0.139 | 0.114 | -18.2% | -0.0645 to 0.014 | STEADY, no difference beyond the noise |
| host CPU-seconds | 249 | 202 | -18.9% | -124 to 30.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.598 | 0.383 | -36.0% | -0.362 to -0.0689 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 18 |  | 15.5 to 20.5 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 233 | 207 | -11.1% | -32.1 to -19.4 | GAIN |
| the server's own CPU-seconds (redis-server) | 22 | 19 | -13.5% | -3.39 to -2.55 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 211 | 187 | -11.4% | -29.8 to -18 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.16 |  | 1.07 to 1.24 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.173 | 0.173 | +0.1% | -0.00181 to 0.00215 | shown, not judged |
| host CPU-seconds without steal | 249 | 202 | -18.9% | -124 to 30.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `4082deec8fda`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,386 | +17.1% | 197 to 208 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0238 to 0.00655 | STEADY, no difference beyond the noise |
| cache hit rate | 0.79 | 0.925 | +17.1% | 0.132 to 0.138 | GAIN |
| latency, 95th percentile (ms) | 5.55 | 5.44 | -1.9% | -0.12 to -0.0928 | GAIN |
| latency, 99th percentile (ms) | 5.62 | 5.59 | -0.5% | -0.0389 to -0.0168 | GAIN |
| latency, mean (ms) | 1.25 | 0.527 | -57.9% | -0.741 to -0.705 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 347 | +442.0% | 271 to 295 | power given |
| memory used, mean (MB) | 61.2 | 319 | +420.7% | 250 to 265 | power given |
| keys evicted | 138,048 | 2,679 | -98.1% | -137,467 to -133,271 | shown, not judged |
| host CPU busy (share of the run) | 0.0942 | 0.0898 | -4.7% | -0.0374 to 0.0285 | STEADY, no difference beyond the noise |
| host CPU-seconds | 163 | 157 | -3.7% | -68.9 to 57 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.306 | 0.252 | -17.7% | -0.167 to 0.0587 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 17.7 |  | 14.8 to 20.5 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 196 | 175 | -10.8% | -24.7 to -17.9 | GAIN |
| the server's own CPU-seconds (redis-server) | 24.7 | 22.2 | -10.4% | -2.82 to -2.3 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 172 | 152 | -11.6% | -23.6 to -16.3 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.24 |  | 1.08 to 1.41 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.168 | 0.164 | -2.2% | -0.00672 to -0.000644 | shown, not judged |
| host CPU-seconds without steal | 163 | 157 | -3.7% | -68.9 to 57 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `4b160a642eb2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,326 | +23.2% | 245 to 255 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00993 to 0.023 | STEADY, no difference beyond the noise |
| cache hit rate | 0.718 | 0.885 | +23.3% | 0.164 to 0.17 | GAIN |
| latency, 95th percentile (ms) | 5.77 | 5.74 | -0.6% | -0.0394 to -0.0246 | GAIN |
| latency, 99th percentile (ms) | 5.83 | 5.82 | -0.2% | -0.0235 to 0.00458 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.75 | 0.823 | -52.9% | -0.949 to -0.903 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 245 | +282.2% | 163 to 198 | power given |
| memory used, mean (MB) | 57.2 | 200 | +250.7% | 142 to 145 | power given |
| keys evicted | 71,699 | 77.3 | -99.9% | -72,630 to -70,613 | shown, not judged |
| host CPU busy (share of the run) | 0.163 | 0.121 | -25.5% | -0.162 to 0.0784 | STEADY, no difference beyond the noise |
| host CPU-seconds | 111 | 82 | -26.3% | -123 to 64.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.574 | 0.343 | -40.2% | -0.657 to 0.196 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10.3 |  | -4.22 to 24.9 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 125 | 108 | -13.8% | -19.9 to -14.7 | GAIN |
| the server's own CPU-seconds (redis-server) | 15.5 | 13.5 | -13.0% | -2.99 to -1.05 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 110 | 93.6 | -14.5% | -19.4 to -12.4 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.627 |  | 0.564 to 0.69 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0955 | 0.0911 | -4.6% | -0.00848 to -0.000249 | shown, not judged |
| host CPU-seconds without steal | 111 | 82 | -26.3% | -123 to 64.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `4b160a642eb2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,465 | +15.6% | 194 to 202 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0219 to -0.000169 | LOSS |
| cache hit rate | 0.845 | 0.978 | +15.7% | 0.13 to 0.136 | GAIN |
| latency, 95th percentile (ms) | 5.76 | 0.249 | -95.7% | -5.52 to -5.51 | GAIN |
| latency, 99th percentile (ms) | 5.83 | 5.76 | -1.2% | -0.0792 to -0.0624 | GAIN |
| latency, mean (ms) | 1.06 | 0.317 | -70.0% | -0.756 to -0.722 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 338 | +427.7% | 271 to 277 | power given |
| memory used, mean (MB) | 61.3 | 313 | +410.8% | 248 to 256 | power given |
| keys evicted | 103,502 | 2,639 | -97.4% | -102,797 to -98,929 | shown, not judged |
| host CPU busy (share of the run) | 0.137 | 0.134 | -2.0% | -0.0325 to 0.0269 | STEADY, no difference beyond the noise |
| host CPU-seconds | 230 | 232 | +0.7% | -58 to 61.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.404 | 0.352 | -12.9% | -0.146 to 0.0411 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 29.3 |  | 27.9 to 30.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 289 | 252 | -12.6% | -38.6 to -34.3 | GAIN |
| the server's own CPU-seconds (redis-server) | 38.3 | 35.3 | -7.8% | -4.56 to -1.45 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 250 | 215 | -14.1% | -38.4 to -32 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.73 |  | 1.27 to 2.19 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.239 | 0.234 | -2.0% | -0.0103 to 0.000488 | shown, not judged |
| host CPU-seconds without steal | 230 | 232 | +0.7% | -58 to 61.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `4b160a642eb2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 924 | 1,171 | +26.7% | 245 to 250 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.079 to 0.13 | STEADY, no difference beyond the noise |
| cache hit rate | 0.617 | 0.783 | +26.8% | 0.164 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.21 | -0.1% | -0.0191 to 0.00416 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.33 | 5.29 | -0.7% | -0.165 to 0.0866 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.05 | 1.21 | -41.1% | -0.871 to -0.819 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 312 | +387.7% | 244 to 252 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.5% | 196 to 198 | power given |
| keys evicted | 243,182 | 0 | -100.0% | -243,795 to -242,568 | shown, not judged |
| host CPU busy (share of the run) | 0.0607 | 0.0678 | +11.8% | -0.00831 to 0.0226 | STEADY, no difference beyond the noise |
| host CPU-seconds | 106 | 120 | +13.1% | -13.1 to 40.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.255 | 0.228 | -10.8% | -0.119 to 0.0642 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 18.3 |  | 14.5 to 22.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 131 | 124 | -5.7% | -14.1 to -0.975 | GAIN |
| the server's own CPU-seconds (redis-server) | 17.5 | 15.7 | -10.3% | -2.87 to -0.719 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 114 | 107 | -6.2% | -12.3 to -1.73 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.31 |  | 0.972 to 1.64 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.128 | 0.124 | -2.8% | -0.00888 to 0.00171 | shown, not judged |
| host CPU-seconds without steal | 106 | 120 | +13.1% | -13.1 to 40.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `4b160a642eb2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,386 | +17.2% | 200 to 207 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0152 to -0.0012 | LOSS |
| cache hit rate | 0.789 | 0.925 | +17.2% | 0.133 to 0.138 | GAIN |
| latency, 95th percentile (ms) | 5.58 | 5.46 | -2.3% | -0.132 to -0.123 | GAIN |
| latency, 99th percentile (ms) | 5.7 | 5.63 | -1.2% | -0.0919 to -0.0466 | GAIN |
| latency, mean (ms) | 1.27 | 0.539 | -57.7% | -0.75 to -0.72 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 347 | +442.5% | 272 to 294 | power given |
| memory used, mean (MB) | 61.2 | 319 | +420.7% | 250 to 265 | power given |
| keys evicted | 138,280 | 2,700 | -98.0% | -137,413 to -133,749 | shown, not judged |
| host CPU busy (share of the run) | 0.132 | 0.115 | -12.7% | -0.0399 to 0.00651 | STEADY, no difference beyond the noise |
| host CPU-seconds | 235 | 205 | -12.7% | -77.5 to 18 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.442 | 0.329 | -25.5% | -0.201 to -0.0244 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 17.7 |  | 16.2 to 19.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 209 | 183 | -12.5% | -28.2 to -24.1 | GAIN |
| the server's own CPU-seconds (redis-server) | 29.6 | 25.7 | -13.3% | -5.99 to -1.92 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 179 | 156 | -13.1% | -25.3 to -21.8 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.28 |  | 1.14 to 1.41 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.176 | 0.171 | -2.7% | -0.00955 to -7.19e-05 | shown, not judged |
| host CPU-seconds without steal | 235 | 205 | -12.7% | -77.5 to 18 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

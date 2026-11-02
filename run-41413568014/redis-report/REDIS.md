# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `abbf5f0857b3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,325 | +23.2% | 246 to 253 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0445 to 0.0295 | STEADY, no difference beyond the noise |
| cache hit rate | 0.718 | 0.884 | +23.2% | 0.165 to 0.168 | GAIN |
| latency, 95th percentile (ms) | 5.58 | 5.5 | -1.3% | -0.106 to -0.0342 | GAIN |
| latency, 99th percentile (ms) | 5.62 | 5.61 | -0.3% | -0.0407 to 0.0114 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.64 | 0.748 | -54.4% | -0.924 to -0.858 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 238 | +271.4% | 173 to 174 | power given |
| memory used, mean (MB) | 57.1 | 200 | +249.6% | 142 to 143 | power given |
| keys evicted | 71,671 | 229 | -99.7% | -71,871 to -71,012 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.105 | -5.9% | -0.117 to 0.104 | STEADY, no difference beyond the noise |
| host CPU-seconds | 77.9 | 74.2 | -4.7% | -90.1 to 82.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.402 | 0.311 | -22.6% | -0.494 to 0.312 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 8.33 |  | 6.9 to 9.77 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 84.7 | 74.3 | -12.2% | -15.1 to -5.56 | GAIN |
| the server's own CPU-seconds (redis-server) | 10.5 | 9.25 | -11.7% | -1.98 to -0.476 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 74.1 | 64.4 | -13.1% | -13.8 to -5.63 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.575 |  | 0.457 to 0.693 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0676 | 0.0666 | -1.5% | -0.00141 to -0.000587 | shown, not judged |
| host CPU-seconds without steal | 77.9 | 74.2 | -4.7% | -90.1 to 82.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `abbf5f0857b3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,466 | +15.7% | 195 to 202 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.019 to 0.0109 | STEADY, no difference beyond the noise |
| cache hit rate | 0.845 | 0.978 | +15.7% | 0.13 to 0.135 | GAIN |
| latency, 95th percentile (ms) | 5.71 | 0.217 | -96.2% | -5.5 to -5.48 | GAIN |
| latency, 99th percentile (ms) | 5.77 | 5.7 | -1.2% | -0.0721 to -0.0612 | GAIN |
| latency, mean (ms) | 1.03 | 0.297 | -71.3% | -0.749 to -0.725 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 337 | +427.0% | 270 to 277 | power given |
| memory used, mean (MB) | 61.3 | 313 | +410.1% | 247 to 256 | power given |
| keys evicted | 103,454 | 2,692 | -97.4% | -102,303 to -99,223 | shown, not judged |
| host CPU busy (share of the run) | 0.12 | 0.111 | -7.8% | -0.0485 to 0.0296 | STEADY, no difference beyond the noise |
| host CPU-seconds | 203 | 190 | -6.2% | -87.5 to 62.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.356 | 0.289 | -18.9% | -0.192 to 0.0574 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 28.3 |  | 26.9 to 29.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 267 | 232 | -13.3% | -38.6 to -32.7 | GAIN |
| the server's own CPU-seconds (redis-server) | 34.4 | 30.9 | -10.1% | -4.1 to -2.83 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 233 | 199 | -14.4% | -35.7 to -31.4 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.38 |  | 1.13 to 1.62 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.219 | 0.207 | -5.5% | -0.0163 to -0.00775 | shown, not judged |
| host CPU-seconds without steal | 203 | 190 | -6.2% | -87.5 to 62.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `abbf5f0857b3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 1,172 | +26.7% | 246 to 248 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0219 to 0.019 | STEADY, the same |
| cache hit rate | 0.617 | 0.783 | +26.8% | 0.165 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.65 | 5.62 | -0.5% | -0.0393 to -0.0211 | GAIN |
| latency, 99th percentile (ms) | 5.7 | 5.69 | -0.2% | -0.015 to -0.00421 | GAIN |
| latency, mean (ms) | 2.24 | 1.34 | -40.2% | -0.913 to -0.889 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 314 | +390.2% | 244 to 255 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.5% | 196 to 198 | power given |
| keys evicted | 243,173 | 0 | -100.0% | -243,528 to -242,818 | shown, not judged |
| host CPU busy (share of the run) | 0.157 | 0.132 | -15.9% | -0.0615 to 0.0114 | STEADY, no difference beyond the noise |
| host CPU-seconds | 273 | 229 | -16.1% | -117 to 29.6 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.655 | 0.434 | -33.8% | -0.4 to -0.0425 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 19.3 |  | 15.5 to 23.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 288 | 252 | -12.6% | -40.2 to -32.5 | GAIN |
| the server's own CPU-seconds (redis-server) | 32.3 | 28.2 | -12.9% | -5 to -3.35 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 255 | 222 | -13.2% | -36.6 to -30.9 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.59 |  | 1.29 to 1.9 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.223 | 0.215 | -3.7% | -0.0201 to 0.00354 | shown, not judged |
| host CPU-seconds without steal | 273 | 229 | -16.1% | -117 to 29.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `abbf5f0857b3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,182 | 1,385 | +17.2% | 198 to 208 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0714 to 0.0322 | STEADY, no difference beyond the noise |
| cache hit rate | 0.789 | 0.925 | +17.2% | 0.133 to 0.138 | GAIN |
| latency, 95th percentile (ms) | 5.69 | 5.65 | -0.8% | -0.0899 to 0.00385 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.75 | 5.73 | -0.3% | -0.0506 to 0.0178 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.33 | 0.586 | -56.1% | -0.787 to -0.708 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 350 | +446.2% | 278 to 293 | power given |
| memory used, mean (MB) | 61.2 | 319 | +420.7% | 250 to 265 | power given |
| keys evicted | 138,343 | 2,688 | -98.1% | -137,396 to -133,913 | shown, not judged |
| host CPU busy (share of the run) | 0.135 | 0.116 | -14.1% | -0.0523 to 0.0142 | STEADY, no difference beyond the noise |
| host CPU-seconds | 231 | 198 | -14.3% | -96.1 to 30 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.435 | 0.318 | -26.8% | -0.238 to 0.0046 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 17.3 |  | 15.9 to 18.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 266 | 239 | -10.3% | -48.9 to -6.25 | GAIN |
| the server's own CPU-seconds (redis-server) | 31.9 | 28.6 | -10.2% | -6.4 to -0.134 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 234 | 208 | -11.0% | -44 to -7.75 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.57 |  | 1.3 to 1.84 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.223 | 0.226 | +1.4% | -0.0155 to 0.0217 | shown, not judged |
| host CPU-seconds without steal | 231 | 198 | -14.3% | -96.1 to 30 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 12.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

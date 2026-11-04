# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,326 | +23.2% | 246 to 255 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0628 to 0.0402 | STEADY, no difference beyond the noise |
| cache hit rate | 0.718 | 0.885 | +23.3% | 0.164 to 0.17 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.72 | -0.6% | -0.0496 to -0.0192 | GAIN |
| latency, 99th percentile (ms) | 5.81 | 5.79 | -0.3% | -0.0234 to -0.0141 | GAIN |
| latency, mean (ms) | 1.74 | 0.817 | -53.2% | -0.943 to -0.911 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 245 | +282.0% | 163 to 198 | power given |
| memory used, mean (MB) | 57.2 | 200 | +250.7% | 142 to 145 | power given |
| keys evicted | 71,728 | 78 | -99.9% | -72,592 to -70,707 | shown, not judged |
| host CPU busy (share of the run) | 0.155 | 0.131 | -15.6% | -0.0665 to 0.018 | STEADY, no difference beyond the noise |
| host CPU-seconds | 105 | 89.3 | -15.1% | -50.8 to 19 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.543 | 0.374 | -31.1% | -0.346 to 0.00734 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10 |  | -5.11 to 25.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 123 | 106 | -14.3% | -18.2 to -17.1 | GAIN |
| the server's own CPU-seconds (redis-server) | 15 | 13.3 | -11.6% | -2.06 to -1.42 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 108 | 91.6 | -15.3% | -17.3 to -15.8 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.654 |  | 0.563 to 0.744 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0935 | 0.0883 | -5.5% | -0.00618 to -0.00419 | shown, not judged |
| host CPU-seconds without steal | 105 | 89.3 | -15.1% | -50.8 to 19 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,465 | +15.6% | 197 to 198 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00554 to -0.00243 | LOSS |
| cache hit rate | 0.845 | 0.978 | +15.7% | 0.132 to 0.133 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 0.242 | -95.8% | -5.53 to -5.48 | GAIN |
| latency, 99th percentile (ms) | 5.82 | 5.74 | -1.4% | -0.116 to -0.0499 | GAIN |
| latency, mean (ms) | 1.05 | 0.31 | -70.6% | -0.747 to -0.737 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 338 | +427.6% | 271 to 277 | power given |
| memory used, mean (MB) | 61.3 | 313 | +410.7% | 248 to 255 | power given |
| keys evicted | 103,286 | 2,645 | -97.4% | -101,061 to -100,221 | shown, not judged |
| host CPU busy (share of the run) | 0.15 | 0.106 | -29.7% | -0.073 to -0.0161 | GAIN |
| host CPU-seconds | 259 | 178 | -31.0% | -134 to -26.6 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.453 | 0.271 | -40.3% | -0.266 to -0.0993 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 29 |  | 29 to 29 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 284 | 244 | -14.0% | -50.2 to -29.2 | GAIN |
| the server's own CPU-seconds (redis-server) | 37.1 | 32.4 | -12.7% | -5.88 to -3.58 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 246 | 210 | -14.8% | -46.4 to -26.7 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.6 |  | 1.23 to 1.97 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.232 | 0.223 | -3.6% | -0.0229 to 0.00607 | shown, not judged |
| host CPU-seconds without steal | 259 | 178 | -31.0% | -134 to -26.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 1,173 | +26.8% | 247 to 248 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.014 to 0.0184 | STEADY, no difference beyond the noise |
| cache hit rate | 0.617 | 0.783 | +26.8% | 0.165 to 0.165 | GAIN |
| latency, 95th percentile (ms) | 5.62 | 5.59 | -0.6% | -0.0699 to -0.00208 | GAIN |
| latency, 99th percentile (ms) | 5.68 | 5.67 | -0.2% | -0.0275 to 0.00292 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.18 | 1.29 | -40.7% | -0.899 to -0.874 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 314 | +389.9% | 245 to 254 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.5% | 196 to 198 | power given |
| keys evicted | 243,199 | 0 | -100.0% | -243,740 to -242,657 | shown, not judged |
| host CPU busy (share of the run) | 0.129 | 0.12 | -7.5% | -0.0642 to 0.0448 | STEADY, no difference beyond the noise |
| host CPU-seconds | 230 | 215 | -6.6% | -126 to 95.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.552 | 0.407 | -26.3% | -0.373 to 0.0823 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 18.7 |  | 14.9 to 22.5 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 223 | 196 | -11.9% | -32.6 to -20.6 | GAIN |
| the server's own CPU-seconds (redis-server) | 23.4 | 20.8 | -11.0% | -3.15 to -1.98 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 199 | 174 | -12.7% | -31.1 to -19.5 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.28 |  | 1.18 to 1.37 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.197 | 0.196 | -0.8% | -0.00264 to -0.000512 | shown, not judged |
| host CPU-seconds without steal | 230 | 215 | -6.6% | -126 to 95.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,181 | 1,384 | +17.2% | 203 to 204 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0166 to 0.00864 | STEADY, no difference beyond the noise |
| cache hit rate | 0.789 | 0.924 | +17.1% | 0.135 to 0.135 | GAIN |
| latency, 95th percentile (ms) | 5.33 | 5.3 | -0.6% | -0.151 to 0.0856 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.55 | 5.5 | -0.8% | -0.558 to 0.468 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.2 | 0.496 | -58.7% | -0.768 to -0.643 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 347 | +441.7% | 277 to 289 | power given |
| memory used, mean (MB) | 61.2 | 317 | +418.0% | 255 to 256 | power given |
| keys evicted | 138,415 | 3,080 | -97.8% | -135,719 to -134,950 | shown, not judged |
| host CPU busy (share of the run) | 0.0705 | 0.0754 | +6.9% | -0.00644 to 0.0162 | STEADY, no difference beyond the noise |
| host CPU-seconds | 124 | 133 | +7.8% | -11.9 to 31.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.233 | 0.214 | -8.0% | -0.075 to 0.0377 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 18.3 |  | 16.9 to 19.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 139 | 135 | -2.9% | -47.2 to 39.2 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 18.1 | 16.7 | -7.8% | -6.45 to 3.62 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 121 | 117 | -3.1% | -42.1 to 34.5 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.19 |  | 1.09 to 1.29 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.134 | 0.142 | +6.2% | -0.0273 to 0.0439 | shown, not judged |
| host CPU-seconds without steal | 124 | 133 | +7.8% | -11.9 to 31.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,075 | 1,326 | +23.3% | 247 to 254 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0479 to 0.0186 | STEADY, no difference beyond the noise |
| cache hit rate | 0.718 | 0.885 | +23.3% | 0.165 to 0.169 | GAIN |
| latency, 95th percentile (ms) | 5.7 | 5.67 | -0.6% | -0.044 to -0.0292 | GAIN |
| latency, 99th percentile (ms) | 5.75 | 5.73 | -0.3% | -0.0255 to -0.00465 | GAIN |
| latency, mean (ms) | 1.72 | 0.796 | -53.7% | -0.937 to -0.912 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 244 | +281.9% | 163 to 198 | power given |
| memory used, mean (MB) | 57.1 | 200 | +250.7% | 142 to 145 | power given |
| keys evicted | 71,744 | 76.7 | -99.9% | -72,423 to -70,912 | shown, not judged |
| host CPU busy (share of the run) | 0.145 | 0.118 | -18.6% | -0.0752 to 0.0212 | STEADY, no difference beyond the noise |
| host CPU-seconds | 100 | 81.5 | -18.6% | -56.8 to 19.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.517 | 0.341 | -34.0% | -0.358 to 0.00696 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10 |  | -5.11 to 25.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 112 | 95.6 | -14.7% | -17.6 to -15.3 | GAIN |
| the server's own CPU-seconds (redis-server) | 13.4 | 11.5 | -14.2% | -2.46 to -1.34 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 98.6 | 83.4 | -15.4% | -16.7 to -13.6 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.636 |  | 0.559 to 0.713 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0891 | 0.0852 | -4.4% | -0.0066 to -0.00118 | shown, not judged |
| host CPU-seconds without steal | 100 | 81.5 | -18.6% | -56.8 to 19.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,465 | +15.6% | 197 to 199 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0143 to 0.00142 | STEADY, no difference beyond the noise |
| cache hit rate | 0.845 | 0.978 | +15.7% | 0.131 to 0.133 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 0.239 | -95.8% | -5.52 to -5.49 | GAIN |
| latency, 99th percentile (ms) | 5.81 | 5.74 | -1.2% | -0.0784 to -0.0602 | GAIN |
| latency, mean (ms) | 1.05 | 0.308 | -70.6% | -0.751 to -0.728 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 337 | +427.0% | 271 to 275 | power given |
| memory used, mean (MB) | 61.3 | 313 | +410.1% | 249 to 254 | power given |
| keys evicted | 103,241 | 2,689 | -97.4% | -101,276 to -99,828 | shown, not judged |
| host CPU busy (share of the run) | 0.128 | 0.109 | -14.6% | -0.0852 to 0.0478 | STEADY, no difference beyond the noise |
| host CPU-seconds | 215 | 186 | -13.6% | -156 to 97.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.378 | 0.282 | -25.2% | -0.295 to 0.105 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 28.3 |  | 26.9 to 29.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 281 | 244 | -13.3% | -45.8 to -28.8 | GAIN |
| the server's own CPU-seconds (redis-server) | 36.4 | 32.3 | -11.4% | -5.86 to -2.44 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 244 | 210 | -14.2% | -41.8 to -27.7 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.59 |  | 1.26 to 1.93 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.231 | 0.223 | -3.6% | -0.019 to 0.00229 | shown, not judged |
| host CPU-seconds without steal | 215 | 186 | -13.6% | -156 to 97.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 1,173 | +26.7% | 246 to 249 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | 0.0101 to 0.0462 | GAIN |
| cache hit rate | 0.617 | 0.782 | +26.7% | 0.164 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.69 | 5.66 | -0.5% | -0.0317 to -0.0216 | GAIN |
| latency, 99th percentile (ms) | 5.75 | 5.74 | -0.1% | -0.0141 to -0.00193 | GAIN |
| latency, mean (ms) | 2.26 | 1.36 | -39.9% | -0.911 to -0.893 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 313 | +389.0% | 243 to 254 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.5% | 196 to 198 | power given |
| keys evicted | 243,085 | 0 | -100.0% | -243,229 to -242,941 | shown, not judged |
| host CPU busy (share of the run) | 0.15 | 0.123 | -18.2% | -0.0673 to 0.0126 | STEADY, no difference beyond the noise |
| host CPU-seconds | 253 | 207 | -18.3% | -123 to 30.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.608 | 0.392 | -35.5% | -0.369 to -0.0631 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 19 |  | 19 to 19 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 311 | 275 | -11.8% | -37.6 to -35.6 | GAIN |
| the server's own CPU-seconds (redis-server) | 35.7 | 32 | -10.3% | -5.82 to -1.5 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 275 | 241 | -12.5% | -37.6 to -31.3 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.51 |  | 1.3 to 1.73 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.232 | 0.225 | -3.1% | -0.0165 to 0.00186 | shown, not judged |
| host CPU-seconds without steal | 253 | 207 | -18.3% | -123 to 30.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,386 | +17.1% | 199 to 206 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.053 to 0.0173 | STEADY, no difference beyond the noise |
| cache hit rate | 0.789 | 0.925 | +17.1% | 0.132 to 0.138 | GAIN |
| latency, 95th percentile (ms) | 5.68 | 5.62 | -1.0% | -0.0601 to -0.0486 | GAIN |
| latency, 99th percentile (ms) | 5.73 | 5.71 | -0.4% | -0.0281 to -0.0175 | GAIN |
| latency, mean (ms) | 1.32 | 0.567 | -56.9% | -0.766 to -0.731 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 349 | +445.5% | 278 to 292 | power given |
| memory used, mean (MB) | 61.2 | 319 | +420.7% | 250 to 265 | power given |
| keys evicted | 138,067 | 2,694 | -98.0% | -137,167 to -133,578 | shown, not judged |
| host CPU busy (share of the run) | 0.132 | 0.113 | -14.0% | -0.0687 to 0.0319 | STEADY, no difference beyond the noise |
| host CPU-seconds | 227 | 197 | -13.1% | -127 to 67.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.426 | 0.316 | -25.8% | -0.266 to 0.0459 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 17.3 |  | 15.9 to 18.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 259 | 224 | -13.3% | -37.3 to -31.3 | GAIN |
| the server's own CPU-seconds (redis-server) | 31.2 | 27.1 | -13.2% | -4.62 to -3.6 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 227 | 196 | -13.9% | -35.1 to -28.1 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.42 |  | 1.18 to 1.66 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.219 | 0.21 | -4.3% | -0.0104 to -0.00858 | shown, not judged |
| host CPU-seconds without steal | 227 | 197 | -13.1% | -127 to 67.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 12.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

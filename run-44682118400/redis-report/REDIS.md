# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,049 | 1,299 | +23.9% | 229 to 273 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.351 to 0.265 | STEADY, no difference beyond the noise |
| cache hit rate | 0.717 | 0.885 | +23.5% | 0.167 to 0.17 | GAIN |
| latency, 95th percentile (ms) | 7.24 | 5.62 | -22.4% | -3.31 to 0.0654 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 12.5 | 9.15 | -26.8% | -8.18 to 1.47 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.05 | 0.973 | -52.5% | -1.44 to -0.707 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 252 | +293.6% | 185 to 191 | power given |
| memory used, mean (MB) | 57.2 | 200 | +250.3% | 143 to 143 | power given |
| keys evicted | 72,179 | 0 | -100.0% | -72,628 to -71,730 | shown, not judged |
| host CPU busy (share of the run) | 0.136 | 0.111 | -18.3% | -0.0439 to -0.00584 | GAIN |
| host CPU-seconds | 95.2 | 77.7 | -18.5% | -31.2 to -3.9 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.504 | 0.332 | -34.2% | -0.243 to -0.101 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 16.3 |  | 10.1 to 22.6 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 96.4 | 82 | -14.9% | -34 to 5.25 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 11.3 | 9.61 | -15.3% | -3.26 to -0.2 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 85 | 71.8 | -15.5% | -31.2 to 4.8 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.584 |  | 0.464 to 0.703 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0745 | 0.0696 | -6.6% | -0.0358 to 0.026 | shown, not judged |
| host CPU-seconds without steal | 95.2 | 77.7 | -18.5% | -31.2 to -3.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,466 | +15.6% | 197 to 200 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00907 to 0.00216 | STEADY, no difference beyond the noise |
| cache hit rate | 0.845 | 0.977 | +15.6% | 0.131 to 0.133 | GAIN |
| latency, 95th percentile (ms) | 5.54 | 0.172 | -96.9% | -5.37 to -5.37 | GAIN |
| latency, 99th percentile (ms) | 5.63 | 5.51 | -2.1% | -0.121 to -0.116 | GAIN |
| latency, mean (ms) | 0.967 | 0.253 | -73.9% | -0.72 to -0.709 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 337 | +426.0% | 270 to 276 | power given |
| memory used, mean (MB) | 61.3 | 312 | +409.5% | 248 to 254 | power given |
| keys evicted | 103,200 | 2,765 | -97.3% | -100,877 to -99,993 | shown, not judged |
| host CPU busy (share of the run) | 0.106 | 0.0946 | -10.6% | -0.0683 to 0.046 | STEADY, no difference beyond the noise |
| host CPU-seconds | 185 | 166 | -10.1% | -131 to 93.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.325 | 0.252 | -22.3% | -0.262 to 0.117 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 29 |  | 29 to 29 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 200 | 175 | -12.3% | -26.9 to -22.3 | GAIN |
| the server's own CPU-seconds (redis-server) | 26.6 | 23.4 | -12.0% | -3.91 to -2.48 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 173 | 151 | -13.0% | -24.7 to -20.3 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.17 |  | 0.931 to 1.41 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.169 | 0.165 | -2.7% | -0.00641 to -0.00269 | shown, not judged |
| host CPU-seconds without steal | 185 | 166 | -10.1% | -131 to 93.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 15.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 1,173 | +26.7% | 246 to 248 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0354 to 0.0292 | STEADY, no difference beyond the noise |
| cache hit rate | 0.617 | 0.783 | +26.8% | 0.165 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.7 | 5.67 | -0.5% | -0.0335 to -0.0239 | GAIN |
| latency, 99th percentile (ms) | 5.77 | 5.75 | -0.2% | -0.0137 to -0.00878 | GAIN |
| latency, mean (ms) | 2.27 | 1.37 | -39.8% | -0.906 to -0.902 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 313 | +388.7% | 244 to 254 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.5% | 196 to 198 | power given |
| keys evicted | 243,296 | 0 | -100.0% | -243,984 to -242,609 | shown, not judged |
| host CPU busy (share of the run) | 0.139 | 0.125 | -10.3% | -0.0443 to 0.0155 | STEADY, no difference beyond the noise |
| host CPU-seconds | 230 | 209 | -9.2% | -78.9 to 36.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.553 | 0.397 | -28.3% | -0.259 to -0.0542 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 18.7 |  | 17.2 to 20.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 314 | 278 | -11.3% | -37.7 to -33.1 | GAIN |
| the server's own CPU-seconds (redis-server) | 35.9 | 31.8 | -11.3% | -4.71 to -3.43 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 278 | 245 | -11.9% | -35.1 to -31 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.75 |  | 1.21 to 2.29 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.238 | 0.226 | -5.3% | -0.0203 to -0.00511 | shown, not judged |
| host CPU-seconds without steal | 230 | 209 | -9.2% | -78.9 to 36.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,386 | +17.1% | 199 to 206 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0309 to 0.00146 | STEADY, no difference beyond the noise |
| cache hit rate | 0.79 | 0.925 | +17.1% | 0.132 to 0.137 | GAIN |
| latency, 95th percentile (ms) | 5.54 | 5.44 | -1.9% | -0.116 to -0.0949 | GAIN |
| latency, 99th percentile (ms) | 5.61 | 5.59 | -0.4% | -0.0311 to -0.0182 | GAIN |
| latency, mean (ms) | 1.25 | 0.524 | -58.0% | -0.737 to -0.71 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 348 | +443.5% | 275 to 293 | power given |
| memory used, mean (MB) | 61.2 | 319 | +420.8% | 250 to 265 | power given |
| keys evicted | 137,980 | 2,674 | -98.1% | -137,013 to -133,599 | shown, not judged |
| host CPU busy (share of the run) | 0.112 | 0.0847 | -24.3% | -0.123 to 0.0685 | STEADY, no difference beyond the noise |
| host CPU-seconds | 197 | 148 | -25.2% | -234 to 135 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.371 | 0.237 | -36.1% | -0.45 to 0.183 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 18 |  | 15.5 to 20.5 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 196 | 175 | -10.8% | -23.6 to -19 | GAIN |
| the server's own CPU-seconds (redis-server) | 24.7 | 21.8 | -11.5% | -3.49 to -2.18 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 172 | 152 | -11.5% | -21.4 to -18 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.22 |  | 1.03 to 1.4 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.167 | 0.165 | -1.1% | -0.00708 to 0.00325 | shown, not judged |
| host CPU-seconds without steal | 197 | 148 | -25.1% | -234 to 135 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,327 | 1,327 | -0.0% | -0.127 to 0.0951 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00563 to 0.00349 | STEADY, the same |
| cache hit rate | 0.885 | 0.885 | -0.0% | -9.2e-06 to 9.2e-06 | STEADY, the same |
| latency, 95th percentile (ms) | 5.72 | 5.72 | -0.0% | -0.00326 to -0.00134 | GAIN |
| latency, 99th percentile (ms) | 5.79 | 5.79 | -0.0% | -0.0125 to 0.00998 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.809 | 0.811 | +0.3% | -0.0027 to 0.0074 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 200 | 200 | +0.0% | 0.00444 to 0.0634 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.123 | 0.114 | -6.9% | -0.0424 to 0.0254 | STEADY, no difference beyond the noise |
| host CPU-seconds | 83.5 | 76.7 | -8.2% | -33.8 to 20.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.349 | 0.321 | -8.2% | -0.141 to 0.0844 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 104 | 104 | +0.2% | -1.1 to 1.43 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 12.8 | 13 | +1.8% | -0.391 to 0.851 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 91.3 | 91.3 | -0.1% | -1.15 to 1.02 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0905 | 0.0915 | +1.1% | -0.000931 to 0.00286 | shown, not judged |
| host CPU-seconds without steal | 83.5 | 76.7 | -8.2% | -33.8 to 20.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,468 | 1,470 | +0.1% | -4.46 to 7.89 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00659 to 0.00552 | STEADY, the same |
| cache hit rate | 0.981 | 0.981 | +0.0% | -5.13e-06 to 6.12e-06 | STEADY, the same |
| latency, 95th percentile (ms) | 0.31 | 0.235 | -24.3% | -0.224 to 0.073 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.51 | 5.53 | +0.4% | -0.118 to 0.166 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.256 | 0.251 | -2.1% | -0.0388 to 0.0279 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 349 | 348 | -0.0% | -0.136 to 0.124 | STEADY, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.105 | 0.106 | +1.1% | -0.042 to 0.0444 | STEADY, no difference beyond the noise |
| host CPU-seconds | 185 | 187 | +1.2% | -83.8 to 88 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.28 | 0.282 | +1.0% | -0.126 to 0.132 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 187 | 190 | +1.5% | -42.3 to 48 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 25 | 25.6 | +2.3% | -6.89 to 8.03 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 162 | 164 | +1.4% | -35.5 to 40.1 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.184 | 0.184 | +0.2% | -0.0415 to 0.0424 | shown, not judged |
| host CPU-seconds without steal | 185 | 187 | +1.2% | -83.8 to 88 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,172 | 1,171 | -0.1% | -1.56 to 0.288 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.049 to 0.025 | STEADY, no difference beyond the noise |
| cache hit rate | 0.783 | 0.783 | +0.0% | -3.68e-06 to 3.68e-06 | STEADY, the same |
| latency, 95th percentile (ms) | 5.2 | 5.2 | +0.0% | -0.00882 to 0.0119 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.23 | 5.24 | +0.2% | -0.0386 to 0.0646 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.19 | 1.2 | +0.6% | -0.0164 to 0.0295 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 257 | 257 | +0.0% | -0.0118 to 0.0843 | STEADY, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0565 | 0.0523 | -7.4% | -0.0526 to 0.0443 | STEADY, no difference beyond the noise |
| host CPU-seconds | 99.4 | 91.7 | -7.7% | -97.6 to 82.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.188 | 0.174 | -7.7% | -0.185 to 0.156 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 111 | 116 | +3.7% | -1.85 to 10 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 14.1 | 14.4 | +2.0% | -0.617 to 1.18 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 97.2 | 101 | +3.9% | -1.42 to 9.02 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.118 | 0.12 | +1.6% | -0.00608 to 0.00974 | shown, not judged |
| host CPU-seconds without steal | 99.4 | 91.7 | -7.7% | -97.6 to 82.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,392 | 1,392 | +0.0% | -0.2 to 0.349 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0048 to 0.00284 | STEADY, the same |
| cache hit rate | 0.929 | 0.929 | +0.0% | -6.37e-06 to 6.37e-06 | STEADY, the same |
| latency, 95th percentile (ms) | 5.45 | 5.45 | -0.1% | -0.0454 to 0.0396 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.6 | 5.6 | +0.0% | -0.0275 to 0.0297 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.509 | 0.509 | -0.0% | -0.0069 to 0.00662 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 333 | 333 | +0.0% | -0.00969 to 0.0579 | STEADY, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0875 | 0.0879 | +0.4% | -0.0251 to 0.0258 | STEADY, no difference beyond the noise |
| host CPU-seconds | 152 | 153 | +0.6% | -47.1 to 48.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.243 | 0.244 | +0.6% | -0.0751 to 0.0778 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 177 | 178 | +0.2% | -5.91 to 6.47 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 22.1 | 22.2 | +0.2% | -0.741 to 0.821 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 155 | 155 | +0.2% | -5.22 to 5.71 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.174 | 0.172 | -1.3% | -0.0116 to 0.00696 | shown, not judged |
| host CPU-seconds without steal | 152 | 153 | +0.6% | -47.1 to 48.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

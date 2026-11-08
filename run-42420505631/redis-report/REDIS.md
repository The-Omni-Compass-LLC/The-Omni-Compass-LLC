# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,327 | 1,327 | -0.0% | -1.05 to 0.656 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0105 to 0.00978 | STEADY, the same |
| cache hit rate | 0.885 | 0.885 | +0.0% | -9.2e-06 to 9.2e-06 | STEADY, the same |
| latency, 95th percentile (ms) | 5.5 | 5.5 | -0.0% | -0.0109 to 0.00629 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.61 | 5.61 | +0.0% | -0.00153 to 0.00234 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.737 | 0.739 | +0.2% | -0.00382 to 0.00715 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 200 | 200 | +0.0% | -0.00717 to 0.0637 | STEADY, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0969 | 0.0827 | -14.7% | -0.0615 to 0.033 | STEADY, no difference beyond the noise |
| host CPU-seconds | 68 | 57.2 | -15.8% | -46.5 to 25.1 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.284 | 0.24 | -15.8% | -0.195 to 0.105 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 72.8 | 73 | +0.2% | -0.674 to 0.986 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 9.06 | 9.15 | +1.0% | -0.267 to 0.44 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 63.7 | 63.7 | +0.1% | -0.874 to 1.01 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0672 | 0.0676 | +0.7% | -0.00144 to 0.00238 | shown, not judged |
| host CPU-seconds without steal | 68 | 57.2 | -15.8% | -46.5 to 25.1 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,472 | 1,471 | -0.1% | -5.93 to 3.44 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.000602 to 0.00146 | STEADY, the same |
| cache hit rate | 0.981 | 0.981 | -0.0% | -6.64e-06 to 7.18e-07 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.214 | 0.243 | +13.3% | -0.0876 to 0.144 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.65 | 5.66 | +0.2% | 0.00788 to 0.0163 | LOSS |
| latency, mean (ms) | 0.261 | 0.27 | +3.6% | -0.02 to 0.0386 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 348 | 349 | +0.0% | -0.0624 to 0.199 | STEADY, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.117 | 0.116 | -0.7% | -0.0484 to 0.0468 | STEADY, no difference beyond the noise |
| host CPU-seconds | 206 | 204 | -1.0% | -95.9 to 91.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.312 | 0.309 | -0.9% | -0.145 to 0.14 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 211 | 216 | +2.3% | -1.32 to 11.1 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 27.8 | 28.5 | +2.3% | 0.0279 to 1.25 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 183 | 187 | +2.3% | -1.35 to 9.82 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.209 | 0.212 | +1.3% | -0.00409 to 0.00949 | shown, not judged |
| host CPU-seconds without steal | 206 | 204 | -1.0% | -95.9 to 91.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,173 | 1,173 | -0.0% | -1.11 to 0.738 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00889 to 0.0104 | STEADY, the same |
| cache hit rate | 0.782 | 0.782 | -0.0% | -5.88e-06 to 4.68e-06 | STEADY, the same |
| latency, 95th percentile (ms) | 5.66 | 5.66 | -0.0% | -0.00735 to 0.00422 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.73 | 5.73 | -0.0% | -0.00508 to 0.00404 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.35 | 1.36 | +0.1% | -0.00643 to 0.0097 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 257 | 257 | +0.0% | -0.00177 to 0.062 | STEADY, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.126 | 0.128 | +1.4% | -0.0309 to 0.0344 | STEADY, no difference beyond the noise |
| host CPU-seconds | 213 | 216 | +1.4% | -59.5 to 65.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.403 | 0.409 | +1.4% | -0.113 to 0.124 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 273 | 273 | -0.0% | -3.75 to 3.54 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 31.4 | 31.3 | -0.4% | -1.25 to 1.02 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 241 | 241 | +0.0% | -2.57 to 2.59 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.228 | 0.227 | -0.4% | -0.0104 to 0.00878 | shown, not judged |
| host CPU-seconds without steal | 213 | 216 | +1.4% | -59.5 to 65.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,392 | 1,392 | -0.0% | -0.887 to 0.763 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00484 to 0.000217 | STEADY, no difference beyond the noise |
| cache hit rate | 0.929 | 0.929 | +0.0% | -3.68e-06 to 3.68e-06 | STEADY, the same |
| latency, 95th percentile (ms) | 5.21 | 5.21 | -0.0% | -0.0089 to 0.00832 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.26 | 5.26 | -0.0% | -0.0096 to 0.00726 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.452 | 0.454 | +0.4% | -0.00569 to 0.00966 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 333 | 333 | +0.0% | -0.0333 to 0.0953 | STEADY, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0515 | 0.0697 | +35.5% | -0.0209 to 0.0575 | STEADY, no difference beyond the noise |
| host CPU-seconds | 90.1 | 124 | +37.5% | -38.3 to 106 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.144 | 0.198 | +37.5% | -0.061 to 0.169 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 116 | 118 | +1.6% | 0.62 to 3.09 | power given |
| the server's own CPU-seconds (redis-server) | 15.3 | 15.5 | +0.8% | -0.182 to 0.422 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 101 | 102 | +1.7% | 0.705 to 2.76 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.139 | 0.141 | +1.7% | -0.0114 to 0.016 | shown, not judged |
| host CPU-seconds without steal | 90.1 | 124 | +37.5% | -38.3 to 106 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

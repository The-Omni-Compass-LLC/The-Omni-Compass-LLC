# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,327 | 1,327 | +0.0% | -0.191 to 0.207 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0146 to 0.0116 | STEADY, no difference beyond the noise |
| cache hit rate | 0.885 | 0.885 | +0.0% | 0 to 0 | STEADY, the same |
| latency, 95th percentile (ms) | 5.72 | 5.71 | -0.1% | -0.041 to 0.0245 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.78 | -0.2% | -0.0488 to 0.0308 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.806 | 0.805 | -0.2% | -0.0136 to 0.011 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 200 | 200 | +0.0% | -0.0237 to 0.0751 | STEADY, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.117 | 0.115 | -1.6% | -0.101 to 0.0976 | STEADY, no difference beyond the noise |
| host CPU-seconds | 79.7 | 77.7 | -2.5% | -76.9 to 72.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.334 | 0.325 | -2.5% | -0.322 to 0.305 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 104 | 103 | -1.1% | -5.62 to 3.31 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 12.9 | 12.8 | -1.0% | -1.01 to 0.757 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 91.4 | 90.4 | -1.1% | -4.79 to 2.74 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.093 | 0.0903 | -2.9% | -0.00406 to -0.0013 | shown, not judged |
| host CPU-seconds without steal | 79.7 | 77.7 | -2.5% | -76.9 to 72.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,469 | 1,470 | +0.0% | -1.31 to 1.64 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0389 to 0.025 | STEADY, no difference beyond the noise |
| cache hit rate | 0.981 | 0.981 | -0.0% | -4.03e-06 to 3.88e-06 | STEADY, the same |
| latency, 95th percentile (ms) | 0.107 | 0.099 | -7.9% | -0.0159 to -0.000954 | GAIN |
| latency, 99th percentile (ms) | 5.22 | 5.21 | -0.1% | -0.0139 to -0.000257 | GAIN |
| latency, mean (ms) | 0.182 | 0.179 | -2.0% | -0.00869 to 0.00132 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 348 | 348 | +0.0% | -0.0119 to 0.0458 | STEADY, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0582 | 0.0623 | +7.0% | -0.0478 to 0.0559 | STEADY, no difference beyond the noise |
| host CPU-seconds | 103 | 111 | +7.4% | -89.3 to 105 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.156 | 0.168 | +7.4% | -0.135 to 0.158 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 109 | 106 | -3.2% | -4.49 to -2.57 | GAIN |
| the server's own CPU-seconds (redis-server) | 14.7 | 14.1 | -4.1% | -1.76 to 0.571 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 94.6 | 91.7 | -3.1% | -3.37 to -2.49 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.125 | 0.118 | -5.0% | -0.0188 to 0.00646 | shown, not judged |
| host CPU-seconds without steal | 103 | 111 | +7.4% | -89.3 to 105 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,173 | 1,173 | +0.0% | -0.386 to 0.418 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0212 to 0.0241 | STEADY, the same |
| cache hit rate | 0.782 | 0.782 | +0.0% | -3.68e-06 to 3.68e-06 | STEADY, the same |
| latency, 95th percentile (ms) | 5.68 | 5.68 | -0.0% | -0.0136 to 0.00906 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.75 | 5.75 | -0.0% | -0.0176 to 0.0154 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.36 | 1.36 | +0.0% | -0.0117 to 0.0127 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 257 | 257 | +0.0% | -0.00889 to 0.0529 | STEADY, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.118 | 0.135 | +14.2% | -0.0453 to 0.0787 | STEADY, no difference beyond the noise |
| host CPU-seconds | 196 | 228 | +16.4% | -85.9 to 150 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.371 | 0.432 | +16.4% | -0.163 to 0.284 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 281 | 282 | +0.5% | -6.68 to 9.46 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 33 | 33.1 | +0.2% | -0.633 to 0.793 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 248 | 249 | +0.5% | -6.08 to 8.7 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.239 | 0.237 | -1.0% | -0.00708 to 0.00233 | shown, not judged |
| host CPU-seconds without steal | 196 | 228 | +16.4% | -85.9 to 150 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,392 | 1,392 | +0.0% | -0.679 to 0.734 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00413 to 0.00499 | STEADY, the same |
| cache hit rate | 0.929 | 0.929 | -0.0% | -2.62e-06 to 1.63e-06 | STEADY, the same |
| latency, 95th percentile (ms) | 5.46 | 5.46 | +0.0% | -0.0145 to 0.018 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.6 | 5.6 | +0.1% | -0.0115 to 0.0204 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.509 | 0.51 | +0.0% | -0.00753 to 0.00763 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 333 | 333 | +0.0% | -0.0467 to 0.0772 | STEADY, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0901 | 0.0874 | -3.0% | -0.0247 to 0.0192 | STEADY, no difference beyond the noise |
| host CPU-seconds | 157 | 152 | -3.3% | -46.4 to 36 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.251 | 0.243 | -3.3% | -0.0741 to 0.0575 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 177 | 179 | +0.9% | -3.67 to 6.99 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 22 | 22.1 | +0.6% | -0.804 to 1.06 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 155 | 157 | +1.0% | -2.86 to 5.92 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.172 | 0.173 | +0.3% | -0.0066 to 0.00772 | shown, not judged |
| host CPU-seconds without steal | 157 | 152 | -3.3% | -46.4 to 36 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `e5cfa2afd8ec`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,327 | 1,327 | -0.0% | -1.47 to 1.15 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0169 to 0.011 | STEADY, no difference beyond the noise |
| cache hit rate | 0.885 | 0.885 | -0.0% | -1.96e-05 to 1.22e-05 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.49 | 5.5 | +0.3% | 0.00439 to 0.032 | LOSS |
| latency, 99th percentile (ms) | 5.6 | 5.61 | +0.2% | 0.0048 to 0.0189 | LOSS |
| latency, mean (ms) | 0.737 | 0.744 | +0.9% | -0.00676 to 0.0206 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 200 | 200 | +0.0% | -0.0407 to 0.121 | STEADY, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0815 | 0.0842 | +3.3% | -0.0291 to 0.0344 | STEADY, no difference beyond the noise |
| host CPU-seconds | 56.3 | 58.3 | +3.5% | -22.2 to 26.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.236 | 0.244 | +3.6% | -0.0933 to 0.11 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 72.1 | 73.8 | +2.3% | 0.0727 to 3.24 | power given |
| the server's own CPU-seconds (redis-server) | 9.11 | 9.31 | +2.2% | -0.0208 to 0.421 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 62.9 | 64.4 | +2.3% | -0.000981 to 2.91 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0657 | 0.0673 | +2.3% | -0.00435 to 0.00739 | shown, not judged |
| host CPU-seconds without steal | 56.3 | 58.3 | +3.5% | -22.2 to 26.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `e5cfa2afd8ec`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,472 | 1,472 | +0.0% | -0.0683 to 0.0833 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.000337 to 0.000518 | STEADY, the same |
| cache hit rate | 0.981 | 0.981 | -0.0% | -2.62e-06 to 1.63e-06 | STEADY, the same |
| latency, 95th percentile (ms) | 0.161 | 0.16 | -0.7% | -0.0107 to 0.0085 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.48 | 5.47 | -0.1% | -0.0103 to 0.000451 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.228 | 0.228 | -0.1% | -0.00595 to 0.00569 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 348 | 348 | +0.0% | 0.00903 to 0.0408 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0948 | 0.0845 | -10.9% | -0.0705 to 0.0498 | STEADY, no difference beyond the noise |
| host CPU-seconds | 167 | 148 | -11.8% | -136 to 96.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.253 | 0.223 | -11.8% | -0.205 to 0.145 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 171 | 171 | -0.2% | -3.53 to 2.72 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 23.6 | 23.4 | -0.7% | -1.1 to 0.772 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 148 | 147 | -0.2% | -2.44 to 1.95 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.167 | 0.167 | -0.1% | -0.00607 to 0.00559 | shown, not judged |
| host CPU-seconds without steal | 167 | 148 | -11.8% | -136 to 96.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `e5cfa2afd8ec`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,173 | 1,173 | +0.0% | -0.521 to 0.639 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00374 to 0.0136 | STEADY, no difference beyond the noise |
| cache hit rate | 0.783 | 0.782 | -0.0% | -2.54e-06 to 1.33e-06 | STEADY, the same |
| latency, 95th percentile (ms) | 5.69 | 5.68 | -0.1% | -0.0383 to 0.0289 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.77 | 5.77 | +0.0% | -0.0322 to 0.0342 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.37 | 1.37 | -0.3% | -0.00918 to 0.00211 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 257 | 257 | +0.0% | 0.0107 to 0.0488 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.146 | 0.132 | -9.9% | -0.0191 to -0.00989 | GAIN |
| host CPU-seconds | 250 | 222 | -11.2% | -37.9 to -18 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.473 | 0.42 | -11.2% | -0.072 to -0.0339 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 287 | 284 | -0.9% | -7.95 to 2.76 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 33.9 | 33.2 | -2.0% | -1.06 to -0.325 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 253 | 251 | -0.8% | -6.91 to 3.1 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.239 | 0.241 | +0.7% | -0.00745 to 0.0108 | shown, not judged |
| host CPU-seconds without steal | 250 | 222 | -11.2% | -37.9 to -18 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `e5cfa2afd8ec`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,393 | 1,392 | -0.0% | -0.318 to 0.0849 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0175 to 0.0166 | STEADY, the same |
| cache hit rate | 0.929 | 0.929 | +0.0% | -4.08e-06 to 4.36e-06 | STEADY, the same |
| latency, 95th percentile (ms) | 5.69 | 5.69 | -0.0% | -0.0205 to 0.0151 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.78 | 5.78 | -0.1% | -0.0321 to 0.0199 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.568 | 0.567 | -0.2% | -0.0115 to 0.00878 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 333 | 333 | +0.0% | -0.0251 to 0.0765 | STEADY, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.115 | 0.106 | -7.5% | -0.0701 to 0.0529 | STEADY, no difference beyond the noise |
| host CPU-seconds | 194 | 178 | -8.3% | -132 to 99.6 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.309 | 0.284 | -8.3% | -0.21 to 0.159 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 251 | 252 | +0.2% | -7.25 to 8.36 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 31.5 | 31.4 | -0.4% | -0.997 to 0.717 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 219 | 220 | +0.3% | -6.5 to 7.9 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.23 | 0.23 | -0.2% | -0.0103 to 0.00931 | shown, not judged |
| host CPU-seconds without steal | 194 | 178 | -8.3% | -132 to 99.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

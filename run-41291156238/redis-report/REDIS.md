# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `078cb4ce8aeb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,327 | 1,327 | +0.0% | -0.0621 to 0.183 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00676 to 0.00501 | STEADY, the same |
| cache hit rate | 0.885 | 0.885 | +0.0% | 0 to 0 | STEADY, the same |
| latency, 95th percentile (ms) | 5.71 | 5.72 | +0.1% | -0.0159 to 0.0224 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.78 | 5.78 | +0.1% | -0.0081 to 0.0184 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.806 | 0.807 | +0.1% | -0.0035 to 0.00501 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 200 | 200 | +0.0% | 0.0185 to 0.0503 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.108 | -2.6% | -0.111 to 0.105 | STEADY, no difference beyond the noise |
| host CPU-seconds | 74.5 | 72.4 | -2.8% | -84.9 to 80.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.312 | 0.303 | -2.8% | -0.355 to 0.338 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 103 | 104 | +0.5% | -0.508 to 1.55 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 13 | 12.8 | -1.7% | -1.13 to 0.687 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 89.9 | 90.6 | +0.8% | 0.25 to 1.23 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0914 | 0.0914 | -0.0% | -0.000621 to 0.000533 | shown, not judged |
| host CPU-seconds without steal | 74.5 | 72.4 | -2.8% | -84.9 to 80.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `078cb4ce8aeb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,472 | 1,472 | -0.0% | -0.17 to 0.143 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00137 to 0.00153 | STEADY, the same |
| cache hit rate | 0.981 | 0.981 | +0.0% | -3.76e-06 to 4.74e-06 | STEADY, the same |
| latency, 95th percentile (ms) | 0.22 | 0.218 | -0.6% | -0.019 to 0.0166 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.72 | 5.72 | -0.0% | -0.00983 to 0.00793 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.279 | 0.278 | -0.4% | -0.00697 to 0.00455 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 348 | 348 | +0.0% | 0.0104 to 0.0238 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.107 | 0.114 | +6.0% | -0.0526 to 0.0655 | STEADY, no difference beyond the noise |
| host CPU-seconds | 182 | 194 | +6.7% | -98.7 to 123 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.275 | 0.294 | +6.7% | -0.149 to 0.186 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 239 | 238 | -0.4% | -8.48 to 6.66 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 32.4 | 32 | -1.3% | -1.53 to 0.659 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 206 | 206 | -0.2% | -7.07 to 6.14 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.224 | 0.222 | -1.0% | -0.00793 to 0.00359 | shown, not judged |
| host CPU-seconds without steal | 182 | 194 | +6.7% | -98.7 to 123 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `078cb4ce8aeb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,173 | 1,173 | +0.0% | -0.00928 to 0.0135 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00918 to 0.0146 | STEADY, no difference beyond the noise |
| cache hit rate | 0.783 | 0.782 | -0.0% | -4.1e-06 to 1.5e-07 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.66 | 5.66 | +0.0% | -0.00214 to 0.00318 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.73 | 5.73 | -0.0% | -0.0032 to 0.00319 | STEADY, the same |
| latency, mean (ms) | 1.35 | 1.35 | +0.1% | 0.000116 to 0.00252 | LOSS |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 257 | 257 | +0.0% | 0.0121 to 0.035 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.12 | 0.128 | +6.3% | -0.0137 to 0.0288 | STEADY, no difference beyond the noise |
| host CPU-seconds | 201 | 216 | +7.2% | -26.7 to 55.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.381 | 0.408 | +7.2% | -0.0506 to 0.105 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 273 | 275 | +0.6% | 0.0585 to 3.14 | power given |
| the server's own CPU-seconds (redis-server) | 32 | 32.1 | +0.5% | -1.1 to 1.41 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 241 | 242 | +0.6% | -1.32 to 4.21 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.228 | 0.227 | -0.6% | -0.00984 to 0.00711 | shown, not judged |
| host CPU-seconds without steal | 201 | 216 | +7.2% | -26.7 to 55.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `078cb4ce8aeb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,392 | 1,392 | -0.0% | -0.258 to 0.181 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00665 to 0.00409 | STEADY, the same |
| cache hit rate | 0.929 | 0.929 | -0.0% | -3.11e-06 to 1.14e-06 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.43 | 5.45 | +0.4% | -0.00583 to 0.048 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.59 | 5.6 | +0.2% | -0.000465 to 0.024 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.503 | 0.507 | +0.8% | 0.00198 to 0.00594 | LOSS |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 333 | 333 | +0.0% | 0.0151 to 0.053 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0877 | 0.0855 | -2.5% | -0.0223 to 0.0179 | STEADY, no difference beyond the noise |
| host CPU-seconds | 153 | 149 | -2.9% | -42.4 to 33.6 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.244 | 0.237 | -2.9% | -0.0677 to 0.0537 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 174 | 177 | +1.6% | 1.56 to 3.87 | power given |
| the server's own CPU-seconds (redis-server) | 22.1 | 22.6 | +1.9% | 0.177 to 0.649 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 152 | 154 | +1.5% | 1.29 to 3.32 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.17 | 0.17 | +0.2% | -0.00335 to 0.00391 | shown, not judged |
| host CPU-seconds without steal | 153 | 149 | -2.9% | -42.4 to 33.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

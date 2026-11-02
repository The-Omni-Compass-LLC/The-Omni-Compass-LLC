# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,327 | 1,327 | -0.0% | -1.31 to 0.263 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0013 to 0.00239 | STEADY, the same |
| cache hit rate | 0.885 | 0.885 | +0.0% | -9.39e-06 to 1.19e-05 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.48 | 5.48 | +0.1% | -0.0155 to 0.0255 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.59 | 5.59 | +0.0% | -0.0116 to 0.0132 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.732 | 0.736 | +0.5% | -0.00114 to 0.008 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 200 | 200 | +0.0% | -0.0182 to 0.0956 | STEADY, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0737 | 0.0782 | +6.2% | -0.0927 to 0.102 | STEADY, no difference beyond the noise |
| host CPU-seconds | 50.7 | 54.1 | +6.8% | -68 to 74.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.212 | 0.227 | +6.8% | -0.285 to 0.314 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 71.2 | 71.5 | +0.4% | -1.16 to 1.7 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 8.83 | 8.83 | +0.0% | -0.196 to 0.203 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 62.3 | 62.6 | +0.4% | -1.36 to 1.89 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0657 | 0.0655 | -0.3% | -0.00232 to 0.00192 | shown, not judged |
| host CPU-seconds without steal | 50.7 | 54.1 | +6.8% | -68 to 74.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,472 | 1,472 | -0.0% | -1.06 to 0.76 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00108 to 0.000236 | STEADY, the same |
| cache hit rate | 0.981 | 0.981 | +0.0% | -2.2e-06 to 5.16e-06 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.161 | 0.165 | +2.4% | -0.00201 to 0.00971 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.47 | 5.47 | -0.0% | -0.0137 to 0.0087 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.226 | 0.228 | +0.8% | -0.0038 to 0.00762 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 348 | 348 | +0.0% | -0.0285 to 0.0968 | STEADY, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0782 | 0.0965 | +23.5% | -0.0212 to 0.0579 | STEADY, no difference beyond the noise |
| host CPU-seconds | 136 | 171 | +25.4% | -39.2 to 108 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.206 | 0.258 | +25.4% | -0.0592 to 0.164 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 169 | 172 | +1.3% | -1.57 to 5.84 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 22.8 | 22.8 | -0.3% | -0.633 to 0.493 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 146 | 149 | +1.5% | -0.929 to 5.33 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.168 | 0.169 | +0.7% | -0.0102 to 0.0127 | shown, not judged |
| host CPU-seconds without steal | 136 | 171 | +25.4% | -39.2 to 108 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,172 | 1,172 | +0.0% | -1.04 to 1.13 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | 0.00565 to 0.012 | GAIN |
| cache hit rate | 0.783 | 0.783 | +0.0% | 0 to 0 | STEADY, the same |
| latency, 95th percentile (ms) | 5.21 | 5.21 | -0.0% | -0.0199 to 0.0153 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.29 | 5.25 | -0.7% | -0.151 to 0.0784 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.2 | 1.2 | -0.4% | -0.0229 to 0.014 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 257 | 257 | +0.0% | -0.0234 to 0.0638 | STEADY, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.054 | 0.0589 | +9.2% | -0.0362 to 0.0462 | STEADY, no difference beyond the noise |
| host CPU-seconds | 94.2 | 104 | +10.2% | -67.1 to 86.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.178 | 0.197 | +10.2% | -0.127 to 0.164 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 121 | 119 | -1.8% | -12 to 7.54 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 15.8 | 15.4 | -2.6% | -1.28 to 0.46 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 105 | 104 | -1.7% | -10.7 to 7.08 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.129 | 0.128 | -0.7% | -0.00704 to 0.00527 | shown, not judged |
| host CPU-seconds without steal | 94.2 | 104 | +10.2% | -67.1 to 86.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,393 | 1,393 | +0.0% | -0.18 to 0.284 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00943 to 0.00899 | STEADY, the same |
| cache hit rate | 0.929 | 0.929 | +0.0% | -1.63e-06 to 2.62e-06 | STEADY, the same |
| latency, 95th percentile (ms) | 5.68 | 5.67 | -0.0% | -0.0142 to 0.0112 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.76 | 5.76 | -0.1% | -0.0136 to 0.00716 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.559 | 0.56 | +0.1% | -0.00494 to 0.00655 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 333 | 333 | +0.0% | -0.0312 to 0.0573 | STEADY, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0877 | 0.117 | +33.2% | -0.0138 to 0.0719 | STEADY, no difference beyond the noise |
| host CPU-seconds | 145 | 199 | +37.6% | -25.7 to 135 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.231 | 0.318 | +37.5% | -0.0411 to 0.215 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 243 | 243 | +0.3% | -2.06 to 3.53 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 30.2 | 30.6 | +1.3% | -0.0415 to 0.828 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 212 | 213 | +0.2% | -2.64 to 3.32 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.225 | 0.224 | -0.4% | -0.00617 to 0.00424 | shown, not judged |
| host CPU-seconds without steal | 145 | 199 | +37.6% | -25.7 to 135 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

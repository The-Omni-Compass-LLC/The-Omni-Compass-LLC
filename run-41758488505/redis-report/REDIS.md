# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `e29ad045b2ac`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,327 | 1,327 | -0.0% | -0.167 to 0.104 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00837 to 0.00864 | STEADY, the same |
| cache hit rate | 0.885 | 0.885 | +0.0% | 0 to 0 | STEADY, the same |
| latency, 95th percentile (ms) | 5.7 | 5.7 | -0.0% | -0.00533 to 0.00416 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.77 | 5.77 | +0.0% | -0.00856 to 0.0138 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.801 | 0.802 | +0.1% | -0.00571 to 0.00788 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 200 | 200 | +0.0% | -0.00931 to 0.0569 | STEADY, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.11 | 0.119 | +8.8% | -0.085 to 0.104 | STEADY, no difference beyond the noise |
| host CPU-seconds | 74.1 | 81.2 | +9.6% | -64.6 to 78.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.31 | 0.34 | +9.6% | -0.27 to 0.33 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 101 | 102 | +0.4% | -1.2 to 1.94 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 12.7 | 12.6 | -0.2% | -0.4 to 0.347 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 88.7 | 89.1 | +0.4% | -1.17 to 1.97 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0886 | 0.0875 | -1.3% | -0.00204 to -0.000173 | shown, not judged |
| host CPU-seconds without steal | 74.1 | 81.2 | +9.6% | -64.6 to 78.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `e29ad045b2ac`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,472 | 1,472 | +0.0% | -0.177 to 0.231 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00326 to 0.00109 | STEADY, the same |
| cache hit rate | 0.981 | 0.981 | +0.0% | -1.14e-06 to 3.11e-06 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.241 | 0.244 | +1.0% | -0.00704 to 0.0117 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.74 | +0.0% | -0.0151 to 0.0205 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.288 | 0.288 | +0.1% | -0.00192 to 0.00244 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 348 | 349 | +0.0% | 0.00513 to 0.0553 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.113 | 0.12 | +6.6% | 0.00181 to 0.0131 | power given |
| host CPU-seconds | 190 | 205 | +7.7% | 3.51 to 25.7 | power given |
| host CPU-seconds per 1,000 requests inside the line | 0.287 | 0.309 | +7.7% | 0.00531 to 0.0387 | power given |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 250 | 249 | -0.4% | -4.92 to 2.79 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 34.3 | 33.8 | -1.6% | -1.94 to 0.847 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 216 | 215 | -0.2% | -3.01 to 1.97 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.257 | 0.257 | +0.0% | -0.0101 to 0.0103 | shown, not judged |
| host CPU-seconds without steal | 190 | 205 | +7.7% | 3.51 to 25.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `e29ad045b2ac`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,173 | 1,173 | +0.0% | -0.0222 to 0.197 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0015 to 0.00486 | STEADY, no difference beyond the noise |
| cache hit rate | 0.783 | 0.783 | +0.0% | -2.2e-06 to 5.16e-06 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.48 | 5.48 | +0.0% | -0.0119 to 0.0132 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.57 | 5.57 | -0.0% | -0.0182 to 0.0154 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.27 | 1.27 | -0.1% | -0.0063 to 0.00414 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 257 | 257 | +0.0% | 0.00571 to 0.0358 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.107 | 0.0951 | -10.7% | -0.0126 to -0.0102 | GAIN |
| host CPU-seconds | 188 | 166 | -11.8% | -23.7 to -20.5 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.356 | 0.314 | -11.8% | -0.0449 to -0.0388 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 189 | 188 | -0.3% | -4.22 to 3.17 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 22.7 | 22.6 | -0.5% | -0.667 to 0.433 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 166 | 165 | -0.2% | -3.6 to 2.79 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.167 | 0.166 | -0.5% | -0.00568 to 0.00385 | shown, not judged |
| host CPU-seconds without steal | 188 | 166 | -11.8% | -23.7 to -20.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `e29ad045b2ac`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,393 | 1,393 | +0.0% | -0.0665 to 0.0765 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00274 to 0.000735 | STEADY, the same |
| cache hit rate | 0.929 | 0.929 | +0.0% | -3.68e-06 to 3.68e-06 | STEADY, the same |
| latency, 95th percentile (ms) | 5.41 | 5.4 | -0.1% | -0.0508 to 0.0446 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.58 | 5.58 | -0.1% | -0.00968 to 0.00287 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.499 | 0.498 | -0.3% | -0.00151 to -0.00126 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 333 | 333 | +0.0% | 0.00579 to 0.0441 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0863 | 0.0785 | -9.0% | -0.0359 to 0.0203 | STEADY, no difference beyond the noise |
| host CPU-seconds | 151 | 136 | -9.8% | -68.8 to 39.4 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.241 | 0.217 | -9.8% | -0.11 to 0.0628 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 170 | 169 | -0.1% | -1.5 to 1.06 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 22 | 21.7 | -1.6% | -0.957 to 0.257 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 147 | 148 | +0.1% | -0.859 to 1.11 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.164 | 0.165 | +0.8% | -0.00215 to 0.00471 | shown, not judged |
| host CPU-seconds without steal | 151 | 136 | -9.8% | -68.8 to 39.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

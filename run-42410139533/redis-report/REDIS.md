# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,326 | 1,327 | +0.0% | -0.347 to 1.63 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0186 to 0.0307 | STEADY, no difference beyond the noise |
| cache hit rate | 0.885 | 0.885 | +0.0% | -4.08e-06 to 6.55e-06 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.65 | 5.62 | -0.4% | -0.0536 to 0.00402 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.06 | 5.81 | -4.1% | -0.81 to 0.313 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.803 | 0.781 | -2.8% | -0.0536 to 0.00918 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 200 | 200 | -0.0% | -0.0712 to 0.0546 | STEADY, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.125 | 0.104 | -16.9% | -0.084 to 0.0419 | STEADY, no difference beyond the noise |
| host CPU-seconds | 88.5 | 72.6 | -18.0% | -65.2 to 33.4 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.371 | 0.304 | -18.0% | -0.273 to 0.14 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 87.3 | 81.8 | -6.4% | -13.3 to 2.13 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 9.92 | 9.3 | -6.2% | -1.63 to 0.389 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 77.3 | 72.4 | -6.4% | -11.7 to 1.74 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0872 | 0.0839 | -3.8% | -0.0176 to 0.011 | shown, not judged |
| host CPU-seconds without steal | 88.5 | 72.6 | -18.0% | -65.2 to 33.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,471 | 1,471 | -0.0% | -0.758 to 0.185 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.000631 to 0.0015 | STEADY, the same |
| cache hit rate | 0.981 | 0.981 | +0.0% | -6.37e-06 to 6.37e-06 | STEADY, the same |
| latency, 95th percentile (ms) | 0.163 | 0.166 | +1.9% | -0.00848 to 0.0147 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.48 | 5.48 | +0.1% | -0.033 to 0.0459 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.231 | 0.233 | +0.6% | -0.00384 to 0.0065 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 348 | 348 | +0.0% | 0.00183 to 0.0532 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.082 | 0.0962 | +17.3% | -0.0471 to 0.0755 | STEADY, no difference beyond the noise |
| host CPU-seconds | 142 | 171 | +19.7% | -90.4 to 147 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.215 | 0.258 | +19.8% | -0.137 to 0.222 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 173 | 173 | -0.1% | -4.13 to 3.72 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 23.2 | 23.4 | +0.5% | -0.338 to 0.564 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 150 | 150 | -0.2% | -3.79 to 3.15 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.174 | 0.176 | +1.5% | -0.00234 to 0.0075 | shown, not judged |
| host CPU-seconds without steal | 142 | 171 | +19.7% | -90.4 to 147 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,173 | 1,174 | +0.0% | -0.0146 to 0.0329 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -8.17e-05 to 0.00316 | STEADY, no difference beyond the noise |
| cache hit rate | 0.782 | 0.783 | +0.0% | -5.68e-06 to 9.41e-06 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.62 | 5.61 | -0.1% | -0.0228 to 0.00599 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.69 | 5.68 | -0.2% | -0.0183 to -0.00119 | GAIN |
| latency, mean (ms) | 1.32 | 1.31 | -0.4% | -0.00914 to -0.00125 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 257 | 257 | +0.0% | 0.0118 to 0.0301 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.126 | 0.116 | -7.8% | -0.0383 to 0.0186 | STEADY, no difference beyond the noise |
| host CPU-seconds | 225 | 206 | -8.4% | -74.4 to 36.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.426 | 0.39 | -8.4% | -0.141 to 0.0698 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 216 | 212 | -2.1% | -8.56 to -0.689 | GAIN |
| the server's own CPU-seconds (redis-server) | 21.4 | 21 | -1.7% | -0.597 to -0.123 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 195 | 190 | -2.2% | -8.36 to -0.168 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.209 | 0.207 | -0.9% | -0.0107 to 0.00679 | shown, not judged |
| host CPU-seconds without steal | 225 | 206 | -8.4% | -74.4 to 36.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,392 | 1,392 | -0.0% | -0.743 to 0.606 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0102 to 0.0115 | STEADY, the same |
| cache hit rate | 0.929 | 0.929 | +0.0% | -3.68e-06 to 3.68e-06 | STEADY, the same |
| latency, 95th percentile (ms) | 5.44 | 5.44 | +0.0% | -0.0123 to 0.0136 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.59 | 5.59 | +0.1% | -0.00568 to 0.0141 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.506 | 0.506 | +0.1% | -0.00431 to 0.00569 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 333 | 333 | +0.0% | -0.0209 to 0.0786 | STEADY, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0896 | 0.0853 | -4.8% | -0.0338 to 0.0253 | STEADY, no difference beyond the noise |
| host CPU-seconds | 157 | 148 | -5.3% | -65.3 to 48.6 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.25 | 0.237 | -5.3% | -0.104 to 0.0777 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 176 | 177 | +0.5% | -0.257 to 2.16 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 22.1 | 22.3 | +0.9% | -0.459 to 0.865 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 154 | 154 | +0.5% | -1.09 to 2.59 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.17 | 0.17 | +0.1% | -0.0033 to 0.00349 | shown, not judged |
| host CPU-seconds without steal | 157 | 148 | -5.3% | -65.3 to 48.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

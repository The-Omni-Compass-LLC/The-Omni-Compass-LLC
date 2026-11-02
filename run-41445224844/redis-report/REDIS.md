# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `e5cfa2afd8ec`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,326 | +23.2% | 245 to 255 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0358 to 0.0138 | STEADY, no difference beyond the noise |
| cache hit rate | 0.718 | 0.885 | +23.3% | 0.164 to 0.17 | GAIN |
| latency, 95th percentile (ms) | 5.67 | 5.64 | -0.6% | -0.1 to 0.0354 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.73 | 5.75 | +0.2% | -0.105 to 0.13 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.7 | 0.791 | -53.3% | -0.925 to -0.884 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 244 | +281.3% | 162 to 198 | power given |
| memory used, mean (MB) | 57.2 | 200 | +250.7% | 142 to 145 | power given |
| keys evicted | 71,702 | 73 | -99.9% | -72,430 to -70,829 | shown, not judged |
| host CPU busy (share of the run) | 0.132 | 0.133 | +0.8% | -0.0142 to 0.0164 | STEADY, no difference beyond the noise |
| host CPU-seconds | 92.3 | 94.9 | +2.8% | -10.3 to 15.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.477 | 0.398 | -16.6% | -0.126 to -0.0319 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 10.7 |  | -3.02 to 24.3 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 98.9 | 89.6 | -9.4% | -12.5 to -6.05 | GAIN |
| the server's own CPU-seconds (redis-server) | 11.6 | 10.6 | -8.9% | -1.45 to -0.603 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 87.2 | 78.4 | -10.1% | -11.5 to -6.13 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.575 |  | 0.447 to 0.704 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0825 | 0.0828 | +0.4% | -0.00989 to 0.0105 | shown, not judged |
| host CPU-seconds without steal | 92.3 | 94.9 | +2.8% | -10.3 to 15.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `e5cfa2afd8ec`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,465 | +15.7% | 197 to 201 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00849 to 0.00596 | STEADY, the same |
| cache hit rate | 0.845 | 0.978 | +15.7% | 0.132 to 0.134 | GAIN |
| latency, 95th percentile (ms) | 5.53 | 0.18 | -96.7% | -5.37 to -5.34 | GAIN |
| latency, 99th percentile (ms) | 5.62 | 5.49 | -2.3% | -0.148 to -0.111 | GAIN |
| latency, mean (ms) | 0.972 | 0.255 | -73.8% | -0.731 to -0.705 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 338 | +427.4% | 273 to 274 | power given |
| memory used, mean (MB) | 61.3 | 313 | +411.4% | 252 to 252 | power given |
| keys evicted | 103,430 | 2,631 | -97.5% | -101,579 to -100,019 | shown, not judged |
| host CPU busy (share of the run) | 0.103 | 0.0928 | -10.3% | -0.0289 to 0.00762 | STEADY, no difference beyond the noise |
| host CPU-seconds | 180 | 163 | -9.7% | -52.7 to 17.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.317 | 0.247 | -22.0% | -0.12 to -0.0187 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 28 |  | 28 to 28 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 199 | 175 | -11.9% | -27.8 to -19.7 | GAIN |
| the server's own CPU-seconds (redis-server) | 26.3 | 23.1 | -12.4% | -3.97 to -2.54 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 173 | 151 | -12.6% | -25.9 to -17.5 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.23 |  | 0.893 to 1.57 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.172 | 0.168 | -2.6% | -0.0105 to 0.0017 | shown, not judged |
| host CPU-seconds without steal | 180 | 163 | -9.7% | -52.7 to 17.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 15.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `e5cfa2afd8ec`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 1,173 | +26.8% | 246 to 250 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0769 to 0.112 | STEADY, no difference beyond the noise |
| cache hit rate | 0.617 | 0.783 | +26.8% | 0.164 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.52 | 5.48 | -0.8% | -0.0653 to -0.0264 | GAIN |
| latency, 99th percentile (ms) | 5.58 | 5.57 | -0.3% | -0.031 to 0.00156 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.15 | 1.27 | -40.8% | -0.881 to -0.875 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 313 | +388.5% | 244 to 253 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.5% | 196 to 198 | power given |
| keys evicted | 243,198 | 0 | -100.0% | -243,331 to -243,065 | shown, not judged |
| host CPU busy (share of the run) | 0.121 | 0.0999 | -17.1% | -0.0377 to -0.0035 | GAIN |
| host CPU-seconds | 212 | 175 | -17.5% | -70 to -4 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.509 | 0.331 | -34.9% | -0.242 to -0.113 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 19 |  | 16.5 to 21.5 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 215 | 192 | -11.0% | -29.1 to -18.5 | GAIN |
| the server's own CPU-seconds (redis-server) | 25.6 | 22.4 | -12.5% | -3.92 to -2.46 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 190 | 167 | -11.7% | -26.3 to -17.9 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.52 |  | 1.08 to 1.96 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.171 | 0.167 | -2.5% | -0.00924 to 0.000658 | shown, not judged |
| host CPU-seconds without steal | 212 | 175 | -17.5% | -70 to -4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `e5cfa2afd8ec`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,386 | +17.0% | 200 to 203 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0105 to 0.0112 | STEADY, the same |
| cache hit rate | 0.79 | 0.924 | +17.0% | 0.134 to 0.135 | GAIN |
| latency, 95th percentile (ms) | 5.55 | 5.29 | -4.8% | -0.268 to -0.262 | GAIN |
| latency, 99th percentile (ms) | 5.67 | 5.62 | -0.8% | -0.0508 to -0.0367 | GAIN |
| latency, mean (ms) | 1.23 | 0.517 | -58.0% | -0.719 to -0.708 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 346 | +440.1% | 276 to 287 | power given |
| memory used, mean (MB) | 61.2 | 317 | +417.9% | 255 to 256 | power given |
| keys evicted | 137,996 | 3,083 | -97.8% | -135,522 to -134,303 | shown, not judged |
| host CPU busy (share of the run) | 0.0999 | 0.0801 | -19.8% | -0.0608 to 0.0212 | STEADY, no difference beyond the noise |
| host CPU-seconds | 178 | 141 | -20.5% | -115 to 42.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.334 | 0.227 | -32.1% | -0.244 to 0.0296 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 18.3 |  | 16.9 to 19.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 176 | 158 | -10.3% | -19.9 to -16.5 | GAIN |
| the server's own CPU-seconds (redis-server) | 20 | 17.8 | -10.6% | -2.63 to -1.62 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 156 | 139 | -11.0% | -19.4 to -15 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.14 |  | 1.05 to 1.23 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.178 | 0.177 | -0.4% | -0.00967 to 0.00814 | shown, not judged |
| host CPU-seconds without steal | 178 | 141 | -20.5% | -115 to 42.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

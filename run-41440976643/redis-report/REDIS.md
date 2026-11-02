# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `159b34031f41`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,325 | +23.2% | 247 to 253 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00204 to 0.0376 | STEADY, no difference beyond the noise |
| cache hit rate | 0.718 | 0.884 | +23.2% | 0.165 to 0.168 | GAIN |
| latency, 95th percentile (ms) | 5.58 | 5.51 | -1.3% | -0.104 to -0.0463 | GAIN |
| latency, 99th percentile (ms) | 5.63 | 5.61 | -0.3% | -0.0376 to 0.00065 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.64 | 0.75 | -54.4% | -0.922 to -0.866 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 237 | +271.1% | 173 to 174 | power given |
| memory used, mean (MB) | 57.1 | 199 | +249.1% | 141 to 143 | power given |
| keys evicted | 71,733 | 241 | -99.7% | -71,996 to -70,988 | shown, not judged |
| host CPU busy (share of the run) | 0.12 | 0.101 | -16.2% | -0.0828 to 0.0438 | STEADY, no difference beyond the noise |
| host CPU-seconds | 84.9 | 71.2 | -16.1% | -63.1 to 35.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.438 | 0.298 | -31.9% | -0.356 to 0.0766 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 8 |  | 5.52 to 10.5 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 84.9 | 74.1 | -12.8% | -15.1 to -6.54 | GAIN |
| the server's own CPU-seconds (redis-server) | 10.6 | 9.33 | -11.8% | -1.7 to -0.805 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 74.2 | 64.1 | -13.7% | -13.9 to -6.35 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.557 |  | 0.432 to 0.682 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0674 | 0.0651 | -3.3% | -0.00536 to 0.000871 | shown, not judged |
| host CPU-seconds without steal | 84.9 | 71.2 | -16.1% | -63.1 to 35.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `159b34031f41`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,268 | 1,465 | +15.6% | 197 to 198 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.018 to 0.00218 | STEADY, no difference beyond the noise |
| cache hit rate | 0.845 | 0.978 | +15.6% | 0.132 to 0.133 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 0.239 | -95.8% | -5.52 to -5.5 | GAIN |
| latency, 99th percentile (ms) | 5.82 | 5.74 | -1.3% | -0.0875 to -0.0652 | GAIN |
| latency, mean (ms) | 1.05 | 0.308 | -70.5% | -0.744 to -0.732 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 338 | +427.7% | 270 to 278 | power given |
| memory used, mean (MB) | 61.3 | 313 | +410.8% | 248 to 256 | power given |
| keys evicted | 103,121 | 2,635 | -97.4% | -100,977 to -99,997 | shown, not judged |
| host CPU busy (share of the run) | 0.135 | 0.118 | -12.2% | -0.0524 to 0.0196 | STEADY, no difference beyond the noise |
| host CPU-seconds | 228 | 202 | -11.1% | -95.8 to 45 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.399 | 0.307 | -23.1% | -0.204 to 0.0198 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 28 |  | 28 to 28 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 282 | 246 | -13.0% | -39.1 to -34.2 | GAIN |
| the server's own CPU-seconds (redis-server) | 37.1 | 32.9 | -11.3% | -4.29 to -4.1 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 245 | 211 | -13.9% | -36.7 to -31.4 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.58 |  | 1.2 to 1.97 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.23 | 0.224 | -2.5% | -0.0138 to 0.00246 | shown, not judged |
| host CPU-seconds without steal | 228 | 202 | -11.1% | -95.8 to 45 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 12.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `159b34031f41`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 1,173 | +26.7% | 246 to 248 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00156 to 0.0181 | STEADY, no difference beyond the noise |
| cache hit rate | 0.617 | 0.783 | +26.7% | 0.165 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.7 | 5.67 | -0.4% | -0.0261 to -0.0218 | GAIN |
| latency, 99th percentile (ms) | 5.75 | 5.75 | -0.0% | -0.00741 to 0.00208 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.26 | 1.36 | -39.8% | -0.902 to -0.897 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 313 | +388.9% | 243 to 255 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.5% | 196 to 198 | power given |
| keys evicted | 243,102 | 0 | -100.0% | -243,566 to -242,638 | shown, not judged |
| host CPU busy (share of the run) | 0.147 | 0.138 | -6.3% | -0.0325 to 0.014 | STEADY, no difference beyond the noise |
| host CPU-seconds | 246 | 234 | -4.7% | -57.7 to 34.6 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.59 | 0.444 | -24.8% | -0.245 to -0.0472 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 18.7 |  | 17.2 to 20.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 310 | 276 | -11.1% | -35.5 to -33.5 | GAIN |
| the server's own CPU-seconds (redis-server) | 35.6 | 32.3 | -9.4% | -3.82 to -2.85 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 275 | 242 | -11.9% | -34 to -31.4 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.56 |  | 1.38 to 1.74 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.236 | 0.225 | -4.8% | -0.0122 to -0.0105 | shown, not judged |
| host CPU-seconds without steal | 246 | 234 | -4.7% | -57.7 to 34.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `159b34031f41`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,387 | +17.1% | 196 to 210 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0726 to 0.0245 | STEADY, no difference beyond the noise |
| cache hit rate | 0.789 | 0.925 | +17.2% | 0.131 to 0.141 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.69 | -1.0% | -0.0613 to -0.0513 | GAIN |
| latency, 99th percentile (ms) | 5.81 | 5.78 | -0.5% | -0.0441 to -0.0104 | GAIN |
| latency, mean (ms) | 1.35 | 0.594 | -55.9% | -0.78 to -0.725 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 351 | +447.9% | 274 to 299 | power given |
| memory used, mean (MB) | 61.2 | 320 | +423.7% | 244 to 274 | power given |
| keys evicted | 138,228 | 2,376 | -98.3% | -139,361 to -132,341 | shown, not judged |
| host CPU busy (share of the run) | 0.135 | 0.124 | -7.9% | -0.0403 to 0.0189 | STEADY, no difference beyond the noise |
| host CPU-seconds | 227 | 212 | -6.4% | -71.9 to 42.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.426 | 0.34 | -20.1% | -0.189 to 0.0178 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 17.3 |  | 15.9 to 18.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 291 | 255 | -12.3% | -37.9 to -33.5 | GAIN |
| the server's own CPU-seconds (redis-server) | 35.3 | 31.5 | -10.6% | -4.54 to -2.95 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 255 | 222 | -13.2% | -36.1 to -31.5 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.89 |  | 1.39 to 2.38 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.251 | 0.245 | -2.5% | -0.0141 to 0.00178 | shown, not judged |
| host CPU-seconds without steal | 227 | 212 | -6.4% | -71.9 to 42.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 12.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

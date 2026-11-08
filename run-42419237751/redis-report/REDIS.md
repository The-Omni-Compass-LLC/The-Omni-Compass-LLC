# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,326 | +23.2% | 245 to 255 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0287 to 0.00314 | STEADY, no difference beyond the noise |
| cache hit rate | 0.718 | 0.885 | +23.3% | 0.164 to 0.17 | GAIN |
| latency, 95th percentile (ms) | 5.76 | 5.73 | -0.6% | -0.0461 to -0.0201 | GAIN |
| latency, 99th percentile (ms) | 5.82 | 5.8 | -0.3% | -0.0342 to -0.00253 | GAIN |
| latency, mean (ms) | 1.75 | 0.82 | -53.0% | -0.944 to -0.909 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 245 | +282.0% | 163 to 198 | power given |
| memory used, mean (MB) | 57.1 | 200 | +250.7% | 142 to 145 | power given |
| keys evicted | 71,711 | 75.7 | -99.9% | -72,531 to -70,740 | shown, not judged |
| host CPU busy (share of the run) | 0.16 | 0.136 | -15.2% | -0.108 to 0.059 | STEADY, no difference beyond the noise |
| host CPU-seconds | 109 | 92.9 | -15.1% | -83.3 to 50.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.565 | 0.389 | -31.1% | -0.51 to 0.158 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10 |  | -5.11 to 25.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 124 | 107 | -13.6% | -19.2 to -14.5 | GAIN |
| the server's own CPU-seconds (redis-server) | 15.1 | 13.3 | -11.7% | -2.63 to -0.895 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 109 | 93 | -14.6% | -17.8 to -13.8 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.741 |  | 0.654 to 0.828 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.101 | 0.099 | -2.2% | -0.00626 to 0.00189 | shown, not judged |
| host CPU-seconds without steal | 109 | 92.9 | -15.1% | -83.3 to 50.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,465 | +15.6% | 194 to 202 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0128 to 0.000853 | STEADY, no difference beyond the noise |
| cache hit rate | 0.845 | 0.978 | +15.7% | 0.131 to 0.135 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 0.238 | -95.9% | -5.52 to -5.48 | GAIN |
| latency, 99th percentile (ms) | 5.81 | 5.73 | -1.3% | -0.089 to -0.0614 | GAIN |
| latency, mean (ms) | 1.05 | 0.308 | -70.5% | -0.76 to -0.714 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 339 | +429.8% | 270 to 280 | power given |
| memory used, mean (MB) | 61.3 | 313 | +410.9% | 248 to 256 | power given |
| keys evicted | 103,446 | 2,643 | -97.4% | -102,000 to -99,608 | shown, not judged |
| host CPU busy (share of the run) | 0.125 | 0.119 | -4.8% | -0.0826 to 0.0706 | STEADY, no difference beyond the noise |
| host CPU-seconds | 210 | 204 | -3.2% | -156 to 143 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.369 | 0.309 | -16.3% | -0.318 to 0.198 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 30.7 |  | 23.5 to 37.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 281 | 245 | -12.6% | -38.9 to -31.8 | GAIN |
| the server's own CPU-seconds (redis-server) | 36.6 | 33.3 | -9.0% | -4.91 to -1.65 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 244 | 210 | -13.8% | -36.8 to -30.6 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.64 |  | 1.53 to 1.76 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.233 | 0.225 | -3.3% | -0.0195 to 0.00432 | shown, not judged |
| host CPU-seconds without steal | 210 | 204 | -3.2% | -156 to 143 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 1,173 | +26.7% | 246 to 249 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0308 to 0.0386 | STEADY, no difference beyond the noise |
| cache hit rate | 0.617 | 0.782 | +26.8% | 0.164 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.7 | 5.67 | -0.5% | -0.0328 to -0.0235 | GAIN |
| latency, 99th percentile (ms) | 5.77 | 5.76 | -0.2% | -0.0155 to -0.00481 | GAIN |
| latency, mean (ms) | 2.27 | 1.37 | -39.8% | -0.911 to -0.894 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 313 | +388.9% | 243 to 255 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.5% | 196 to 198 | power given |
| keys evicted | 243,210 | 0 | -100.0% | -243,839 to -242,581 | shown, not judged |
| host CPU busy (share of the run) | 0.158 | 0.141 | -10.7% | -0.0593 to 0.0253 | STEADY, no difference beyond the noise |
| host CPU-seconds | 268 | 241 | -10.1% | -111 to 57.1 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.643 | 0.457 | -29.0% | -0.371 to -0.00323 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 18.7 |  | 17.2 to 20.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 312 | 277 | -11.0% | -36.6 to -31.8 | GAIN |
| the server's own CPU-seconds (redis-server) | 35.6 | 32.5 | -8.9% | -4.26 to -2.05 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 276 | 243 | -11.8% | -34.2 to -30.9 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.5 |  | 1.34 to 1.65 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.235 | 0.227 | -3.5% | -0.00889 to -0.00753 | shown, not judged |
| host CPU-seconds without steal | 268 | 241 | -10.1% | -111 to 57.1 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,385 | +17.0% | 201 to 202 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0117 to 0.00674 | STEADY, no difference beyond the noise |
| cache hit rate | 0.789 | 0.924 | +17.0% | 0.134 to 0.135 | GAIN |
| latency, 95th percentile (ms) | 5.21 | 5.19 | -0.3% | -0.0182 to -0.013 | GAIN |
| latency, 99th percentile (ms) | 5.23 | 5.22 | -0.2% | -0.017 to -0.00253 | GAIN |
| latency, mean (ms) | 1.15 | 0.459 | -60.1% | -0.698 to -0.686 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 345 | +438.6% | 275 to 286 | power given |
| memory used, mean (MB) | 61.2 | 317 | +417.9% | 255 to 256 | power given |
| keys evicted | 138,097 | 3,050 | -97.8% | -135,222 to -134,873 | shown, not judged |
| host CPU busy (share of the run) | 0.0616 | 0.0503 | -18.4% | -0.057 to 0.0343 | STEADY, no difference beyond the noise |
| host CPU-seconds | 109 | 88.5 | -19.0% | -107 to 65 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.205 | 0.142 | -30.8% | -0.218 to 0.0918 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 19 |  | 19 to 19 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 112 | 103 | -8.3% | -15.6 to -2.92 | GAIN |
| the server's own CPU-seconds (redis-server) | 15 | 13.2 | -12.1% | -2.64 to -0.996 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 97.1 | 88.8 | -8.5% | -13.9 to -2.59 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.809 |  | 0.619 to 0.998 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.109 | 0.103 | -5.1% | -0.0125 to 0.00132 | shown, not judged |
| host CPU-seconds without steal | 109 | 88.5 | -19.0% | -107 to 65 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

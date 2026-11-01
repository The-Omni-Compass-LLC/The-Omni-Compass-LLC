# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `a73ae3e52895`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,326 | +23.2% | 245 to 256 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0447 to 0.0552 | STEADY, no difference beyond the noise |
| cache hit rate | 0.718 | 0.885 | +23.3% | 0.164 to 0.17 | GAIN |
| latency, 95th percentile (ms) | 5.63 | 5.55 | -1.3% | -0.0898 to -0.0524 | GAIN |
| latency, 99th percentile (ms) | 5.71 | 5.67 | -0.7% | -0.0833 to 0.000237 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.67 | 0.76 | -54.5% | -0.951 to -0.868 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 243 | +280.4% | 161 to 198 | power given |
| memory used, mean (MB) | 57.1 | 200 | +250.2% | 142 to 144 | power given |
| keys evicted | 71,658 | 77.3 | -99.9% | -72,462 to -70,699 | shown, not judged |
| host CPU busy (share of the run) | 0.129 | 0.0873 | -32.6% | -0.104 to 0.0201 | STEADY, no difference beyond the noise |
| host CPU-seconds | 91.3 | 60 | -34.2% | -79.8 to 17.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.471 | 0.251 | -46.7% | -0.453 to 0.0129 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10.7 |  | -3.02 to 24.3 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 89.9 | 77.4 | -13.9% | -18.6 to -6.31 | GAIN |
| the server's own CPU-seconds (redis-server) | 11.8 | 10.2 | -13.7% | -3.25 to 0.0165 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 78 | 66.6 | -14.6% | -18.1 to -4.68 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.566 |  | 0.495 to 0.636 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0703 | 0.0697 | -0.9% | -0.00914 to 0.0079 | shown, not judged |
| host CPU-seconds without steal | 91.3 | 60 | -34.2% | -79.8 to 17.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `a73ae3e52895`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,466 | +15.7% | 197 to 200 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00441 to 0.0013 | STEADY, no difference beyond the noise |
| cache hit rate | 0.845 | 0.978 | +15.7% | 0.131 to 0.133 | GAIN |
| latency, 95th percentile (ms) | 5.52 | 0.168 | -97.0% | -5.36 to -5.35 | GAIN |
| latency, 99th percentile (ms) | 5.62 | 5.49 | -2.3% | -0.13 to -0.127 | GAIN |
| latency, mean (ms) | 0.963 | 0.249 | -74.2% | -0.724 to -0.704 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 337 | +426.5% | 271 to 275 | power given |
| memory used, mean (MB) | 61.3 | 313 | +410.3% | 249 to 254 | power given |
| keys evicted | 103,267 | 2,681 | -97.4% | -101,174 to -99,998 | shown, not judged |
| host CPU busy (share of the run) | 0.102 | 0.0998 | -1.9% | -0.0155 to 0.0116 | STEADY, no difference beyond the noise |
| host CPU-seconds | 178 | 177 | -0.5% | -27.1 to 25.4 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.312 | 0.268 | -14.0% | -0.0974 to 0.0104 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 28.7 |  | 27.2 to 30.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 196 | 173 | -11.8% | -24.5 to -21.7 | GAIN |
| the server's own CPU-seconds (redis-server) | 26 | 22.8 | -12.5% | -3.51 to -2.98 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 170 | 149 | -12.4% | -22.8 to -19.2 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.15 |  | 0.91 to 1.4 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.167 | 0.163 | -2.0% | -0.00785 to 0.00133 | shown, not judged |
| host CPU-seconds without steal | 178 | 177 | -0.5% | -27.1 to 25.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 15.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `a73ae3e52895`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 1,173 | +26.7% | 246 to 248 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0208 to 0.00878 | STEADY, no difference beyond the noise |
| cache hit rate | 0.617 | 0.782 | +26.7% | 0.165 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.69 | 5.66 | -0.5% | -0.0362 to -0.0177 | GAIN |
| latency, 99th percentile (ms) | 5.75 | 5.74 | -0.2% | -0.0186 to 0.000367 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.26 | 1.36 | -39.8% | -0.909 to -0.891 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 313 | +388.7% | 243 to 254 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.5% | 196 to 198 | power given |
| keys evicted | 243,128 | 0 | -100.0% | -243,636 to -242,620 | shown, not judged |
| host CPU busy (share of the run) | 0.158 | 0.126 | -20.5% | -0.0439 to -0.0209 | GAIN |
| host CPU-seconds | 269 | 212 | -21.3% | -79.2 to -35 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.645 | 0.401 | -37.8% | -0.29 to -0.198 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 18.7 |  | 17.2 to 20.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 310 | 274 | -11.4% | -39.4 to -31.5 | GAIN |
| the server's own CPU-seconds (redis-server) | 35.8 | 31.8 | -11.2% | -4.64 to -3.36 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 274 | 241 | -12.1% | -37.4 to -28.8 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.71 |  | 1.34 to 2.08 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.232 | 0.224 | -3.7% | -0.0164 to -0.000655 | shown, not judged |
| host CPU-seconds without steal | 269 | 212 | -21.3% | -79.2 to -35 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `a73ae3e52895`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,182 | 1,384 | +17.1% | 201 to 203 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.041 to 0.0366 | STEADY, no difference beyond the noise |
| cache hit rate | 0.789 | 0.924 | +17.1% | 0.134 to 0.136 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.21 | -0.3% | -0.0328 to -0.00233 | GAIN |
| latency, 99th percentile (ms) | 5.28 | 5.25 | -0.6% | -0.0728 to 0.0147 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.18 | 0.48 | -59.3% | -0.711 to -0.687 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 346 | +440.9% | 281 to 284 | power given |
| memory used, mean (MB) | 61.2 | 317 | +417.9% | 255 to 256 | power given |
| keys evicted | 138,236 | 3,059 | -97.8% | -135,832 to -134,522 | shown, not judged |
| host CPU busy (share of the run) | 0.059 | 0.055 | -6.7% | -0.0372 to 0.0293 | STEADY, no difference beyond the noise |
| host CPU-seconds | 103 | 96.7 | -6.3% | -68.3 to 55.4 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.194 | 0.155 | -20.0% | -0.141 to 0.0634 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 19 |  | 19 to 19 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 125 | 116 | -7.7% | -16.1 to -3.2 | GAIN |
| the server's own CPU-seconds (redis-server) | 17.2 | 15 | -12.9% | -3.2 to -1.22 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 108 | 99.3 | -8.0% | -14.3 to -2.9 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.2 |  | 0.939 to 1.45 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.126 | 0.124 | -1.4% | -0.00682 to 0.00327 | shown, not judged |
| host CPU-seconds without steal | 103 | 96.7 | -6.3% | -68.3 to 55.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,325 | +23.2% | 246 to 254 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0374 to 0.041 | STEADY, no difference beyond the noise |
| cache hit rate | 0.718 | 0.884 | +23.2% | 0.165 to 0.169 | GAIN |
| latency, 95th percentile (ms) | 5.58 | 5.49 | -1.5% | -0.0974 to -0.069 | GAIN |
| latency, 99th percentile (ms) | 5.63 | 5.61 | -0.4% | -0.0452 to 0.00559 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.64 | 0.747 | -54.5% | -0.915 to -0.875 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 240 | +274.5% | 161 to 191 | power given |
| memory used, mean (MB) | 57.1 | 200 | +249.5% | 142 to 143 | power given |
| keys evicted | 71,719 | 240 | -99.7% | -72,092 to -70,866 | shown, not judged |
| host CPU busy (share of the run) | 0.0867 | 0.0836 | -3.6% | -0.012 to 0.0057 | STEADY, no difference beyond the noise |
| host CPU-seconds | 59.1 | 58 | -1.9% | -8.59 to 6.32 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.305 | 0.243 | -20.4% | -0.0699 to -0.0546 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 10.7 |  | 1.26 to 20.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 84 | 73.4 | -12.6% | -12.9 to -8.3 | GAIN |
| the server's own CPU-seconds (redis-server) | 10.2 | 9.09 | -11.3% | -1.67 to -0.647 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 73.7 | 63.7 | -13.5% | -11.8 to -8.06 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.529 |  | 0.415 to 0.643 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0669 | 0.0655 | -2.1% | -0.00408 to 0.0013 | shown, not judged |
| host CPU-seconds without steal | 59.1 | 58 | -1.9% | -8.59 to 6.32 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,465 | +15.8% | 196 to 204 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00945 to -0.00132 | LOSS |
| cache hit rate | 0.845 | 0.978 | +15.7% | 0.13 to 0.136 | GAIN |
| latency, 95th percentile (ms) | 5.73 | 0.227 | -96.0% | -5.52 to -5.48 | GAIN |
| latency, 99th percentile (ms) | 5.79 | 5.72 | -1.2% | -0.101 to -0.0368 | GAIN |
| latency, mean (ms) | 1.05 | 0.304 | -71.1% | -0.774 to -0.719 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 337 | +427.2% | 271 to 276 | power given |
| memory used, mean (MB) | 61.3 | 313 | +410.9% | 248 to 256 | power given |
| keys evicted | 103,612 | 2,638 | -97.5% | -103,144 to -98,805 | shown, not judged |
| host CPU busy (share of the run) | 0.143 | 0.119 | -16.8% | -0.0612 to 0.0131 | STEADY, no difference beyond the noise |
| host CPU-seconds | 245 | 205 | -16.5% | -114 to 32.6 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.431 | 0.31 | -27.9% | -0.236 to -0.00471 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 28.7 |  | 27.2 to 30.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 277 | 239 | -13.7% | -40.8 to -35.4 | GAIN |
| the server's own CPU-seconds (redis-server) | 35.8 | 31.4 | -12.2% | -4.62 to -4.13 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 242 | 206 | -14.6% | -38.3 to -32 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.45 |  | 1.17 to 1.74 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.226 | 0.211 | -6.8% | -0.022 to -0.00872 | shown, not judged |
| host CPU-seconds without steal | 245 | 205 | -16.5% | -114 to 32.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 924 | 1,172 | +26.8% | 247 to 248 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0596 to 0.0422 | STEADY, no difference beyond the noise |
| cache hit rate | 0.617 | 0.783 | +26.7% | 0.164 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.21 | -0.2% | -0.0183 to -0.00131 | GAIN |
| latency, 99th percentile (ms) | 5.36 | 5.28 | -1.5% | -0.191 to 0.0275 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.06 | 1.21 | -41.4% | -0.861 to -0.843 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 312 | +387.5% | 243 to 253 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.4% | 196 to 198 | power given |
| keys evicted | 243,076 | 0 | -100.0% | -243,155 to -242,997 | shown, not judged |
| host CPU busy (share of the run) | 0.0734 | 0.0584 | -20.4% | -0.022 to -0.00797 | GAIN |
| host CPU-seconds | 130 | 102 | -21.1% | -41.3 to -13.6 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.312 | 0.194 | -37.8% | -0.152 to -0.0843 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 17.7 |  | 12.5 to 22.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 131 | 122 | -7.2% | -13.6 to -5.39 | GAIN |
| the server's own CPU-seconds (redis-server) | 17.4 | 15.5 | -11.3% | -2.27 to -1.66 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 114 | 105 | -7.8% | -12.4 to -5.28 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.29 |  | 1.02 to 1.57 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.124 | 0.127 | +2.4% | 0.0017 to 0.00428 | shown, not judged |
| host CPU-seconds without steal | 130 | 102 | -21.1% | -41.3 to -13.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,385 | +17.0% | 198 to 206 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0442 to 0.0136 | STEADY, no difference beyond the noise |
| cache hit rate | 0.789 | 0.924 | +17.1% | 0.133 to 0.136 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.2 | -0.4% | -0.0275 to -0.0192 | GAIN |
| latency, 99th percentile (ms) | 5.26 | 5.24 | -0.4% | -0.0259 to -0.0167 | GAIN |
| latency, mean (ms) | 1.17 | 0.469 | -59.7% | -0.718 to -0.675 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 346 | +440.6% | 277 to 287 | power given |
| memory used, mean (MB) | 61.2 | 317 | +417.8% | 255 to 256 | power given |
| keys evicted | 138,224 | 3,054 | -97.8% | -136,191 to -134,150 | shown, not judged |
| host CPU busy (share of the run) | 0.0688 | 0.0524 | -23.9% | -0.0409 to 0.008 | STEADY, no difference beyond the noise |
| host CPU-seconds | 122 | 92.1 | -24.4% | -76.1 to 16.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.229 | 0.148 | -35.4% | -0.162 to -0.000206 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 18.7 |  | 17.2 to 20.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 124 | 111 | -10.8% | -15.1 to -11.8 | GAIN |
| the server's own CPU-seconds (redis-server) | 17.2 | 14.6 | -15.0% | -2.82 to -2.33 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 107 | 94.8 | -11.2% | -13.6 to -10.3 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.11 |  | 0.913 to 1.31 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.124 | 0.12 | -3.1% | -0.0105 to 0.00288 | shown, not judged |
| host CPU-seconds without steal | 122 | 92.1 | -24.4% | -76.1 to 16.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

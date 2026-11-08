# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,326 | +23.2% | 245 to 255 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0511 to 0.0391 | STEADY, no difference beyond the noise |
| cache hit rate | 0.718 | 0.885 | +23.3% | 0.164 to 0.17 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.72 | -0.6% | -0.045 to -0.0249 | GAIN |
| latency, 99th percentile (ms) | 5.81 | 5.79 | -0.3% | -0.0395 to 0.00519 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.74 | 0.815 | -53.2% | -0.936 to -0.913 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 245 | +282.2% | 163 to 198 | power given |
| memory used, mean (MB) | 57.1 | 200 | +250.7% | 142 to 145 | power given |
| keys evicted | 71,713 | 75 | -99.9% | -72,658 to -70,618 | shown, not judged |
| host CPU busy (share of the run) | 0.154 | 0.112 | -27.0% | -0.107 to 0.0233 | STEADY, no difference beyond the noise |
| host CPU-seconds | 105 | 75.3 | -28.2% | -80.6 to 21.4 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.542 | 0.316 | -41.8% | -0.474 to 0.0215 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10.3 |  | -4.22 to 24.9 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 122 | 105 | -14.1% | -18.8 to -15.7 | GAIN |
| the server's own CPU-seconds (redis-server) | 14.9 | 12.9 | -13.5% | -2.48 to -1.56 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 107 | 91.2 | -14.9% | -17.3 to -14.5 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.687 |  | 0.544 to 0.83 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0938 | 0.0886 | -5.4% | -0.0109 to 0.000707 | shown, not judged |
| host CPU-seconds without steal | 105 | 75.3 | -28.2% | -80.6 to 21.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,466 | +15.6% | 193 to 203 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00648 to -0.00385 | LOSS |
| cache hit rate | 0.845 | 0.977 | +15.7% | 0.13 to 0.135 | GAIN |
| latency, 95th percentile (ms) | 5.73 | 0.229 | -96.0% | -5.52 to -5.48 | GAIN |
| latency, 99th percentile (ms) | 5.8 | 5.73 | -1.2% | -0.0866 to -0.0482 | GAIN |
| latency, mean (ms) | 1.04 | 0.304 | -70.8% | -0.761 to -0.717 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 337 | +427.1% | 271 to 275 | power given |
| memory used, mean (MB) | 61.3 | 313 | +410.1% | 249 to 254 | power given |
| keys evicted | 103,395 | 2,703 | -97.4% | -102,517 to -98,868 | shown, not judged |
| host CPU busy (share of the run) | 0.14 | 0.114 | -18.3% | -0.045 to -0.00607 | GAIN |
| host CPU-seconds | 239 | 195 | -18.2% | -82.3 to -4.74 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.419 | 0.296 | -29.3% | -0.185 to -0.0604 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 28.7 |  | 27.2 to 30.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 278 | 241 | -13.3% | -41.4 to -32.2 | GAIN |
| the server's own CPU-seconds (redis-server) | 36.5 | 32.3 | -11.5% | -5.2 to -3.19 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 241 | 207 | -14.1% | -39.1 to -28.9 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.44 |  | 1.26 to 1.61 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.236 | 0.217 | -7.9% | -0.0531 to 0.0158 | shown, not judged |
| host CPU-seconds without steal | 239 | 195 | -18.2% | -82.3 to -4.74 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 1,173 | +26.8% | 247 to 248 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0297 to 0.0284 | STEADY, the same |
| cache hit rate | 0.617 | 0.783 | +26.8% | 0.165 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.65 | 5.6 | -0.9% | -0.192 to 0.0879 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.11 | 6.17 | +0.9% | -0.855 to 0.964 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.21 | 1.33 | -40.1% | -0.93 to -0.844 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 313 | +388.5% | 244 to 254 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.5% | 196 to 198 | power given |
| keys evicted | 243,236 | 0 | -100.0% | -243,634 to -242,839 | shown, not judged |
| host CPU busy (share of the run) | 0.134 | 0.125 | -6.5% | -0.0357 to 0.0181 | STEADY, no difference beyond the noise |
| host CPU-seconds | 236 | 222 | -6.1% | -73.2 to 44.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.567 | 0.42 | -26.0% | -0.272 to -0.0225 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 18.3 |  | 16.9 to 19.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 242 | 223 | -8.2% | -45.9 to 6.22 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 27.2 | 24.9 | -8.2% | -4.1 to -0.376 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 215 | 196 | -8.8% | -43 to 5.22 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.29 |  | 1.19 to 1.38 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.191 | 0.188 | -1.6% | -0.0189 to 0.0129 | shown, not judged |
| host CPU-seconds without steal | 236 | 222 | -6.1% | -73.2 to 44.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,182 | 1,385 | +17.1% | 200 to 205 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00975 to 0.00176 | STEADY, no difference beyond the noise |
| cache hit rate | 0.789 | 0.924 | +17.1% | 0.134 to 0.135 | GAIN |
| latency, 95th percentile (ms) | 5.23 | 5.21 | -0.4% | -0.0353 to -0.00774 | GAIN |
| latency, 99th percentile (ms) | 5.27 | 5.24 | -0.6% | -0.0537 to -0.0137 | GAIN |
| latency, mean (ms) | 1.18 | 0.474 | -59.7% | -0.715 to -0.688 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 345 | +439.0% | 274 to 288 | power given |
| memory used, mean (MB) | 61.2 | 317 | +417.9% | 255 to 256 | power given |
| keys evicted | 138,168 | 3,072 | -97.8% | -135,359 to -134,833 | shown, not judged |
| host CPU busy (share of the run) | 0.0546 | 0.0512 | -6.3% | -0.0546 to 0.0477 | STEADY, no difference beyond the noise |
| host CPU-seconds | 95 | 89.5 | -5.7% | -99.7 to 88.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.179 | 0.144 | -19.5% | -0.195 to 0.125 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 18.7 |  | 17.2 to 20.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 126 | 115 | -9.1% | -16 to -7.11 | GAIN |
| the server's own CPU-seconds (redis-server) | 17.2 | 14.6 | -14.7% | -3.23 to -1.8 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 109 | 99 | -9.3% | -14.1 to -6.06 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.06 |  | 0.674 to 1.44 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.129 | 0.12 | -6.3% | -0.0244 to 0.00809 | shown, not judged |
| host CPU-seconds without steal | 95 | 89.5 | -5.7% | -99.7 to 88.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,327 | 1,327 | +0.0% | -0.25 to 0.293 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0361 to 0.019 | STEADY, no difference beyond the noise |
| cache hit rate | 0.885 | 0.885 | -0.0% | -7.3e-06 to 4.55e-06 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.71 | 5.71 | -0.1% | -0.0152 to 0.00813 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.78 | -0.1% | -0.0144 to 0.00472 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.811 | 0.81 | -0.1% | -0.0104 to 0.00821 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 200 | 200 | +0.0% | -0.0166 to 0.0831 | STEADY, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.141 | 0.119 | -15.9% | -0.0693 to 0.0245 | STEADY, no difference beyond the noise |
| host CPU-seconds | 97.5 | 80 | -17.9% | -53.3 to 18.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.408 | 0.335 | -17.9% | -0.223 to 0.0775 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 104 | 104 | -0.1% | -0.59 to 0.284 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 13 | 13 | +0.3% | -0.15 to 0.236 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 90.7 | 90.5 | -0.2% | -0.714 to 0.323 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0911 | 0.0903 | -0.9% | -0.00385 to 0.00217 | shown, not judged |
| host CPU-seconds without steal | 97.5 | 80 | -17.9% | -53.3 to 18.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,471 | 1,471 | -0.0% | -1.32 to 1.1 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.000324 to 0.00119 | STEADY, the same |
| cache hit rate | 0.981 | 0.981 | -0.0% | -2.62e-06 to 1.63e-06 | STEADY, the same |
| latency, 95th percentile (ms) | 0.177 | 0.179 | +1.3% | -0.012 to 0.0167 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.49 | 5.49 | -0.1% | -0.0737 to 0.0629 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.235 | 0.237 | +0.5% | -0.00675 to 0.00921 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 348 | 348 | +0.0% | -0.00305 to 0.0745 | STEADY, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0978 | 0.101 | +3.5% | -0.0307 to 0.0377 | STEADY, no difference beyond the noise |
| host CPU-seconds | 173 | 179 | +3.9% | -60.9 to 74.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.261 | 0.271 | +3.9% | -0.0919 to 0.112 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 176 | 176 | +0.1% | -3.97 to 4.35 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 24.1 | 24.3 | +0.7% | -0.62 to 0.974 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 152 | 152 | +0.0% | -3.34 to 3.37 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.174 | 0.174 | -0.0% | -0.00344 to 0.00332 | shown, not judged |
| host CPU-seconds without steal | 173 | 179 | +3.9% | -60.9 to 74.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,173 | 1,173 | -0.0% | -0.376 to 0.339 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.013 to 0.0126 | STEADY, the same |
| cache hit rate | 0.783 | 0.783 | -0.0% | -5.24e-06 to 3.26e-06 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.62 | 5.62 | -0.0% | -0.00432 to 0.00353 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.68 | 5.68 | +0.0% | -0.00181 to 0.00589 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.34 | 1.34 | +0.0% | -0.00569 to 0.00684 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 257 | 257 | +0.0% | 0.0269 to 0.0564 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.138 | 0.134 | -2.5% | -0.049 to 0.0421 | STEADY, no difference beyond the noise |
| host CPU-seconds | 240 | 233 | -2.7% | -96.3 to 83.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.454 | 0.442 | -2.7% | -0.182 to 0.157 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 250 | 251 | +0.1% | -3.16 to 3.69 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 28.5 | 28.7 | +0.6% | -0.288 to 0.635 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 222 | 222 | +0.0% | -3.09 to 3.28 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.216 | 0.217 | +0.2% | -0.00229 to 0.00318 | shown, not judged |
| host CPU-seconds without steal | 240 | 233 | -2.7% | -96.3 to 83.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,392 | 1,392 | -0.0% | -0.438 to 0.365 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00252 to 0.000448 | STEADY, the same |
| cache hit rate | 0.929 | 0.929 | -0.0% | -6.12e-06 to 5.13e-06 | STEADY, the same |
| latency, 95th percentile (ms) | 5.63 | 5.63 | -0.0% | -0.0101 to 0.00998 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.71 | 5.72 | +0.1% | -0.0125 to 0.0187 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.547 | 0.55 | +0.7% | -0.00177 to 0.00928 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 333 | 333 | +0.0% | 0.0308 to 0.0462 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.117 | 0.127 | +9.0% | -0.0435 to 0.0646 | STEADY, no difference beyond the noise |
| host CPU-seconds | 203 | 223 | +10.1% | -86.6 to 127 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.324 | 0.356 | +10.1% | -0.138 to 0.203 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 225 | 227 | +1.1% | -1.08 to 5.85 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 27.7 | 27.8 | +0.4% | -0.222 to 0.462 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 197 | 199 | +1.1% | -1.31 to 5.85 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.22 | 0.219 | -0.5% | -0.00307 to 0.00108 | shown, not judged |
| host CPU-seconds without steal | 203 | 223 | +10.1% | -86.6 to 127 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,077 | 1,327 | +23.2% | 245 to 255 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | 0.034 to 0.047 | GAIN |
| cache hit rate | 0.718 | 0.885 | +23.2% | 0.164 to 0.17 | GAIN |
| latency, 95th percentile (ms) | 5.61 | 5.53 | -1.5% | -0.096 to -0.0668 | GAIN |
| latency, 99th percentile (ms) | 5.68 | 5.65 | -0.6% | -0.0526 to -0.0117 | GAIN |
| latency, mean (ms) | 1.65 | 0.745 | -54.7% | -0.921 to -0.88 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 239 | +273.1% | 168 to 182 | power given |
| memory used, mean (MB) | 57.1 | 200 | +249.3% | 141 to 144 | power given |
| keys evicted | 71,601 | 77.3 | -99.9% | -72,479 to -70,568 | shown, not judged |
| host CPU busy (share of the run) | 0.129 | 0.0924 | -28.4% | -0.0607 to -0.0126 | GAIN |
| host CPU-seconds | 93.4 | 65.4 | -30.0% | -47.8 to -8.16 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.482 | 0.274 | -43.2% | -0.313 to -0.103 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 7 |  | 4.52 to 9.48 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 83 | 71.9 | -13.4% | -13.8 to -8.42 | GAIN |
| the server's own CPU-seconds (redis-server) | 8.06 | 6.8 | -15.6% | -1.44 to -1.07 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 74.9 | 64.7 | -13.7% | -12.7 to -7.78 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.411 |  | 0.39 to 0.432 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0632 | 0.0605 | -4.3% | -0.0105 to 0.00508 | shown, not judged |
| host CPU-seconds without steal | 93.4 | 65.4 | -30.0% | -47.8 to -8.16 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

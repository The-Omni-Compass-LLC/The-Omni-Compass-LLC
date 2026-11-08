# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,327 | +23.4% | 249 to 254 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0195 to 0.0749 | STEADY, no difference beyond the noise |
| cache hit rate | 0.717 | 0.885 | +23.4% | 0.166 to 0.169 | GAIN |
| latency, 95th percentile (ms) | 6.16 | 5.63 | -8.5% | -0.563 to -0.484 | GAIN |
| latency, 99th percentile (ms) | 7.04 | 6.57 | -6.8% | -0.684 to -0.268 | GAIN |
| latency, mean (ms) | 1.78 | 0.836 | -53.0% | -0.954 to -0.931 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 246 | +283.8% | 169 to 194 | power given |
| memory used, mean (MB) | 57.2 | 200 | +249.9% | 143 to 143 | power given |
| keys evicted | 71,783 | 0 | -100.0% | -72,275 to -71,290 | shown, not judged |
| host CPU busy (share of the run) | 0.16 | 0.134 | -16.0% | -0.0712 to 0.02 | STEADY, no difference beyond the noise |
| host CPU-seconds | 112 | 93.1 | -16.8% | -56.4 to 18.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.577 | 0.39 | -32.5% | -0.373 to -0.00297 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 9.67 |  | -6.11 to 25.4 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 116 | 104 | -10.2% | -12.8 to -11 | GAIN |
| the server's own CPU-seconds (redis-server) | 13.1 | 11.9 | -9.1% | -2.2 to -0.192 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 103 | 91.9 | -10.9% | -11.9 to -10.6 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.514 |  | 0.481 to 0.548 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0824 | 0.0805 | -2.4% | -0.0111 to 0.0072 | shown, not judged |
| host CPU-seconds without steal | 112 | 93.1 | -16.8% | -56.4 to 18.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

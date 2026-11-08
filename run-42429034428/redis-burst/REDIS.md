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

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

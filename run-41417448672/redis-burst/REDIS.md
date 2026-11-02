# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `4b160a642eb2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,326 | +23.2% | 245 to 255 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00993 to 0.023 | STEADY, no difference beyond the noise |
| cache hit rate | 0.718 | 0.885 | +23.3% | 0.164 to 0.17 | GAIN |
| latency, 95th percentile (ms) | 5.77 | 5.74 | -0.6% | -0.0394 to -0.0246 | GAIN |
| latency, 99th percentile (ms) | 5.83 | 5.82 | -0.2% | -0.0235 to 0.00458 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.75 | 0.823 | -52.9% | -0.949 to -0.903 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 245 | +282.2% | 163 to 198 | power given |
| memory used, mean (MB) | 57.2 | 200 | +250.7% | 142 to 145 | power given |
| keys evicted | 71,699 | 77.3 | -99.9% | -72,630 to -70,613 | shown, not judged |
| host CPU busy (share of the run) | 0.163 | 0.121 | -25.5% | -0.162 to 0.0784 | STEADY, no difference beyond the noise |
| host CPU-seconds | 111 | 82 | -26.3% | -123 to 64.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.574 | 0.343 | -40.2% | -0.657 to 0.196 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10.3 |  | -4.22 to 24.9 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 125 | 108 | -13.8% | -19.9 to -14.7 | GAIN |
| the server's own CPU-seconds (redis-server) | 15.5 | 13.5 | -13.0% | -2.99 to -1.05 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 110 | 93.6 | -14.5% | -19.4 to -12.4 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.627 |  | 0.564 to 0.69 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0955 | 0.0911 | -4.6% | -0.00848 to -0.000249 | shown, not judged |
| host CPU-seconds without steal | 111 | 82 | -26.3% | -123 to 64.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

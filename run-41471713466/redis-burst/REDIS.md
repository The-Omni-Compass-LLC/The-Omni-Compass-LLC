# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,326 | +23.2% | 246 to 254 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0809 to 0.052 | STEADY, no difference beyond the noise |
| cache hit rate | 0.717 | 0.885 | +23.3% | 0.165 to 0.17 | GAIN |
| latency, 95th percentile (ms) | 5.76 | 5.73 | -0.6% | -0.0443 to -0.02 | GAIN |
| latency, 99th percentile (ms) | 5.82 | 5.8 | -0.3% | -0.038 to 0.00351 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.75 | 0.821 | -53.0% | -0.929 to -0.921 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 245 | +282.2% | 163 to 198 | power given |
| memory used, mean (MB) | 57.2 | 200 | +250.7% | 142 to 145 | power given |
| keys evicted | 71,778 | 80.3 | -99.9% | -72,481 to -70,913 | shown, not judged |
| host CPU busy (share of the run) | 0.154 | 0.12 | -21.8% | -0.1 to 0.0332 | STEADY, no difference beyond the noise |
| host CPU-seconds | 105 | 81.3 | -22.4% | -75.9 to 28.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.541 | 0.34 | -37.1% | -0.456 to 0.0555 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10.3 |  | -4.22 to 24.9 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 123 | 106 | -13.6% | -18.3 to -15 | GAIN |
| the server's own CPU-seconds (redis-server) | 15 | 13.1 | -12.6% | -2.07 to -1.73 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 108 | 92.1 | -14.4% | -17.3 to -13.8 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.755 |  | 0.667 to 0.842 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0994 | 0.0953 | -4.1% | -0.00706 to -0.00118 | shown, not judged |
| host CPU-seconds without steal | 105 | 81.3 | -22.4% | -75.9 to 28.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

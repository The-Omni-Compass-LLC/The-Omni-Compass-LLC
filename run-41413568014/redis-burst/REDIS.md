# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `abbf5f0857b3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,325 | +23.2% | 246 to 253 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0445 to 0.0295 | STEADY, no difference beyond the noise |
| cache hit rate | 0.718 | 0.884 | +23.2% | 0.165 to 0.168 | GAIN |
| latency, 95th percentile (ms) | 5.58 | 5.5 | -1.3% | -0.106 to -0.0342 | GAIN |
| latency, 99th percentile (ms) | 5.62 | 5.61 | -0.3% | -0.0407 to 0.0114 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.64 | 0.748 | -54.4% | -0.924 to -0.858 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 238 | +271.4% | 173 to 174 | power given |
| memory used, mean (MB) | 57.1 | 200 | +249.6% | 142 to 143 | power given |
| keys evicted | 71,671 | 229 | -99.7% | -71,871 to -71,012 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.105 | -5.9% | -0.117 to 0.104 | STEADY, no difference beyond the noise |
| host CPU-seconds | 77.9 | 74.2 | -4.7% | -90.1 to 82.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.402 | 0.311 | -22.6% | -0.494 to 0.312 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 8.33 |  | 6.9 to 9.77 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 84.7 | 74.3 | -12.2% | -15.1 to -5.56 | GAIN |
| the server's own CPU-seconds (redis-server) | 10.5 | 9.25 | -11.7% | -1.98 to -0.476 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 74.1 | 64.4 | -13.1% | -13.8 to -5.63 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.575 |  | 0.457 to 0.693 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0676 | 0.0666 | -1.5% | -0.00141 to -0.000587 | shown, not judged |
| host CPU-seconds without steal | 77.9 | 74.2 | -4.7% | -90.1 to 82.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

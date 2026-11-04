# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,390 | 1,390 | +0.0% | -3.02 to 3.71 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.219 to 0.141 | STEADY, no difference beyond the noise |
| cache hit rate | 0.929 | 0.929 | -0.0% | -4.99e-06 to 2.1e-06 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.24 | 5.2 | -0.8% | -0.139 to 0.0522 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.64 | 5.36 | -5.0% | -1.01 to 0.444 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.494 | 0.462 | -6.3% | -0.125 to 0.0623 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 333 | 333 | -0.0% | -0.186 to 0.129 | STEADY, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0729 | 0.0538 | -26.1% | -0.0293 to -0.0088 | GAIN |
| host CPU-seconds | 128 | 95.1 | -25.8% | -47.9 to -18.4 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.205 | 0.152 | -25.9% | -0.0771 to -0.029 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 143 | 116 | -18.8% | -93.2 to 39.2 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 18.1 | 14.7 | -18.5% | -10.1 to 3.47 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 125 | 101 | -18.9% | -83 to 35.7 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.14 | 0.121 | -13.6% | -0.0666 to 0.0284 | shown, not judged |
| host CPU-seconds without steal | 128 | 95.1 | -25.8% | -47.9 to -18.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,472 | 1,472 | -0.0% | -1.06 to 0.76 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00108 to 0.000236 | STEADY, the same |
| cache hit rate | 0.981 | 0.981 | +0.0% | -2.2e-06 to 5.16e-06 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.161 | 0.165 | +2.4% | -0.00201 to 0.00971 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.47 | 5.47 | -0.0% | -0.0137 to 0.0087 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.226 | 0.228 | +0.8% | -0.0038 to 0.00762 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 348 | 348 | +0.0% | -0.0285 to 0.0968 | STEADY, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0782 | 0.0965 | +23.5% | -0.0212 to 0.0579 | STEADY, no difference beyond the noise |
| host CPU-seconds | 136 | 171 | +25.4% | -39.2 to 108 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.206 | 0.258 | +25.4% | -0.0592 to 0.164 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 169 | 172 | +1.3% | -1.57 to 5.84 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 22.8 | 22.8 | -0.3% | -0.633 to 0.493 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 146 | 149 | +1.5% | -0.929 to 5.33 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.168 | 0.169 | +0.7% | -0.0102 to 0.0127 | shown, not judged |
| host CPU-seconds without steal | 136 | 171 | +25.4% | -39.2 to 108 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

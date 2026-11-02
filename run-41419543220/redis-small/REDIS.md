# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `7f74bd306bf6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,172 | 1,172 | -0.0% | -0.894 to 0.666 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0931 to 0.0564 | STEADY, no difference beyond the noise |
| cache hit rate | 0.783 | 0.783 | +0.0% | 1.48e-06 to 1.48e-06 | GAIN |
| latency, 95th percentile (ms) | 5.2 | 5.2 | +0.0% | -0.00656 to 0.00995 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.25 | 5.26 | +0.3% | -0.0499 to 0.0796 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.2 | 1.21 | +0.2% | 0.000794 to 0.00394 | LOSS |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 257 | 257 | +0.0% | 0.00223 to 0.0677 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0541 | 0.0545 | +0.9% | -0.0134 to 0.0144 | STEADY, no difference beyond the noise |
| host CPU-seconds | 94.7 | 95.7 | +1.1% | -24.7 to 26.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.18 | 0.181 | +1.1% | -0.0468 to 0.0507 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 118 | 118 | +0.3% | -2.88 to 3.65 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 14.8 | 14.7 | -0.4% | -1.02 to 0.898 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 103 | 103 | +0.4% | -2.15 to 3.04 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.123 | 0.122 | -1.2% | -0.0173 to 0.0143 | shown, not judged |
| host CPU-seconds without steal | 94.7 | 95.7 | +1.1% | -24.7 to 26.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,385 | +17.0% | 201 to 202 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0117 to 0.00674 | STEADY, no difference beyond the noise |
| cache hit rate | 0.789 | 0.924 | +17.0% | 0.134 to 0.135 | GAIN |
| latency, 95th percentile (ms) | 5.21 | 5.19 | -0.3% | -0.0182 to -0.013 | GAIN |
| latency, 99th percentile (ms) | 5.23 | 5.22 | -0.2% | -0.017 to -0.00253 | GAIN |
| latency, mean (ms) | 1.15 | 0.459 | -60.1% | -0.698 to -0.686 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 345 | +438.6% | 275 to 286 | power given |
| memory used, mean (MB) | 61.2 | 317 | +417.9% | 255 to 256 | power given |
| keys evicted | 138,097 | 3,050 | -97.8% | -135,222 to -134,873 | shown, not judged |
| host CPU busy (share of the run) | 0.0616 | 0.0503 | -18.4% | -0.057 to 0.0343 | STEADY, no difference beyond the noise |
| host CPU-seconds | 109 | 88.5 | -19.0% | -107 to 65 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.205 | 0.142 | -30.8% | -0.218 to 0.0918 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 19 |  | 19 to 19 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 112 | 103 | -8.3% | -15.6 to -2.92 | GAIN |
| the server's own CPU-seconds (redis-server) | 15 | 13.2 | -12.1% | -2.64 to -0.996 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 97.1 | 88.8 | -8.5% | -13.9 to -2.59 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.809 |  | 0.619 to 0.998 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.109 | 0.103 | -5.1% | -0.0125 to 0.00132 | shown, not judged |
| host CPU-seconds without steal | 109 | 88.5 | -19.0% | -107 to 65 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

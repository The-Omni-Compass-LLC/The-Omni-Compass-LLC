# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,182 | 1,385 | +17.1% | 200 to 205 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00975 to 0.00176 | STEADY, no difference beyond the noise |
| cache hit rate | 0.789 | 0.924 | +17.1% | 0.134 to 0.135 | GAIN |
| latency, 95th percentile (ms) | 5.23 | 5.21 | -0.4% | -0.0353 to -0.00774 | GAIN |
| latency, 99th percentile (ms) | 5.27 | 5.24 | -0.6% | -0.0537 to -0.0137 | GAIN |
| latency, mean (ms) | 1.18 | 0.474 | -59.7% | -0.715 to -0.688 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 345 | +439.0% | 274 to 288 | power given |
| memory used, mean (MB) | 61.2 | 317 | +417.9% | 255 to 256 | power given |
| keys evicted | 138,168 | 3,072 | -97.8% | -135,359 to -134,833 | shown, not judged |
| host CPU busy (share of the run) | 0.0546 | 0.0512 | -6.3% | -0.0546 to 0.0477 | STEADY, no difference beyond the noise |
| host CPU-seconds | 95 | 89.5 | -5.7% | -99.7 to 88.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.179 | 0.144 | -19.5% | -0.195 to 0.125 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 18.7 |  | 17.2 to 20.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 126 | 115 | -9.1% | -16 to -7.11 | GAIN |
| the server's own CPU-seconds (redis-server) | 17.2 | 14.6 | -14.7% | -3.23 to -1.8 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 109 | 99 | -9.3% | -14.1 to -6.06 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.06 |  | 0.674 to 1.44 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.129 | 0.12 | -6.3% | -0.0244 to 0.00809 | shown, not judged |
| host CPU-seconds without steal | 95 | 89.5 | -5.7% | -99.7 to 88.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

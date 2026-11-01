# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `a73ae3e52895`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,326 | +23.2% | 245 to 256 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0447 to 0.0552 | STEADY, no difference beyond the noise |
| cache hit rate | 0.718 | 0.885 | +23.3% | 0.164 to 0.17 | GAIN |
| latency, 95th percentile (ms) | 5.63 | 5.55 | -1.3% | -0.0898 to -0.0524 | GAIN |
| latency, 99th percentile (ms) | 5.71 | 5.67 | -0.7% | -0.0833 to 0.000237 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.67 | 0.76 | -54.5% | -0.951 to -0.868 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 243 | +280.4% | 161 to 198 | power given |
| memory used, mean (MB) | 57.1 | 200 | +250.2% | 142 to 144 | power given |
| keys evicted | 71,658 | 77.3 | -99.9% | -72,462 to -70,699 | shown, not judged |
| host CPU busy (share of the run) | 0.129 | 0.0873 | -32.6% | -0.104 to 0.0201 | STEADY, no difference beyond the noise |
| host CPU-seconds | 91.3 | 60 | -34.2% | -79.8 to 17.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.471 | 0.251 | -46.7% | -0.453 to 0.0129 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10.7 |  | -3.02 to 24.3 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 89.9 | 77.4 | -13.9% | -18.6 to -6.31 | GAIN |
| the server's own CPU-seconds (redis-server) | 11.8 | 10.2 | -13.7% | -3.25 to 0.0165 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 78 | 66.6 | -14.6% | -18.1 to -4.68 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.566 |  | 0.495 to 0.636 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0703 | 0.0697 | -0.9% | -0.00914 to 0.0079 | shown, not judged |
| host CPU-seconds without steal | 91.3 | 60 | -34.2% | -79.8 to 17.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

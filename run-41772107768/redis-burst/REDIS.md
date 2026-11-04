# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,325 | +23.2% | 246 to 254 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0374 to 0.041 | STEADY, no difference beyond the noise |
| cache hit rate | 0.718 | 0.884 | +23.2% | 0.165 to 0.169 | GAIN |
| latency, 95th percentile (ms) | 5.58 | 5.49 | -1.5% | -0.0974 to -0.069 | GAIN |
| latency, 99th percentile (ms) | 5.63 | 5.61 | -0.4% | -0.0452 to 0.00559 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.64 | 0.747 | -54.5% | -0.915 to -0.875 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 240 | +274.5% | 161 to 191 | power given |
| memory used, mean (MB) | 57.1 | 200 | +249.5% | 142 to 143 | power given |
| keys evicted | 71,719 | 240 | -99.7% | -72,092 to -70,866 | shown, not judged |
| host CPU busy (share of the run) | 0.0867 | 0.0836 | -3.6% | -0.012 to 0.0057 | STEADY, no difference beyond the noise |
| host CPU-seconds | 59.1 | 58 | -1.9% | -8.59 to 6.32 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.305 | 0.243 | -20.4% | -0.0699 to -0.0546 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 10.7 |  | 1.26 to 20.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 84 | 73.4 | -12.6% | -12.9 to -8.3 | GAIN |
| the server's own CPU-seconds (redis-server) | 10.2 | 9.09 | -11.3% | -1.67 to -0.647 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 73.7 | 63.7 | -13.5% | -11.8 to -8.06 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.529 |  | 0.415 to 0.643 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0669 | 0.0655 | -2.1% | -0.00408 to 0.0013 | shown, not judged |
| host CPU-seconds without steal | 59.1 | 58 | -1.9% | -8.59 to 6.32 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

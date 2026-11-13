# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `63f29c3e20a5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,886 | 2,883 | -0.1% | -11 to 5.51 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,896 | 2,893 | -0.1% | -9.53 to 3.24 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.371 | 0.371 | -0.1% | -0.0107 to 0.01 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.584 | 0.581 | -0.6% | -0.053 to 0.0464 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.226 | 0.224 | -0.5% | -0.00643 to 0.00427 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 450 | -12.1% | -63.6 to -60.3 | GAIN |
| bytes in the cache, mean (MB) | 417 | 369 | -11.4% | -52.2 to -43.2 | GAIN |
| pages read into the cache (misses) | 686,256 | 761,296 | +10.9% | 73,140 to 76,939 | shown, not judged |
| host CPU busy (share of the run) | 0.227 | 0.214 | -6.0% | -0.0921 to 0.065 | EVEN, no difference beyond the noise |
| host CPU-seconds | 388 | 359 | -7.5% | -195 to 137 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.292 | 0.27 | -7.5% | -0.147 to 0.103 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | -0.535 to 5.2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

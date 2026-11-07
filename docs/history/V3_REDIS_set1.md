# Redis, a cache's operator-set memory ceiling: the A/B/C confirmation

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's memory ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line, a hit inside and a miss with its store trip outside (`docs/REDIS_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **confirmed better** or **confirmed WORSE**; a run whose interval includes zero reads **no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed requests: any increase in any run is WORSE. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, losses included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 37704450300 | `467f73eba7a6` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 4 |
| B | 37704464642 | `467f73eba7a6` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 4 |
| C | 37704479534 | `467f73eba7a6` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 4 |

## tuning: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,131 | 1,304 | +15.3% (+14.2 to +16.5) | +15.2% (+14.4 to +16.0) | +15.3% (+14.3 to +16.3) | **confirmed better** |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | no difference beyond the noise (3 of 3 runs) |
| cache hit rate | 0.754 | 0.87 | +15.3% (+14.2 to +16.5) | +15.2% (+14.5 to +15.9) | +15.3% (+14.3 to +16.3) | **confirmed better** |
| latency, 95th percentile (ms) | 5.62 | 5.57 | -1.0% (-1.6 to -0.3) | -1.2% (-1.4 to -1.1) | -1.3% (-1.6 to -1.0) | **confirmed better** |
| latency, 99th percentile (ms) | 5.69 | 5.67 | -0.3% (-0.8 to +0.1) | -0.2% (-0.3 to -0.2) | -0.3% (-0.4 to -0.3) | no difference beyond the noise (1 of 3 runs) |
| latency, mean (ms) | 1.46 | 0.836 | -42.9% (-46.0 to -39.9) | -42.5% (-44.8 to -40.1) | -43.2% (-46.1 to -40.3) | **confirmed better** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 298.6 | +366.6% (+364.5 to +368.7) | +362.6% (+356.6 to +368.6) | +364.0% (+360.6 to +367.3) | **confirmed WORSE** |
| memory used, mean (MB) | 61.1 | 269.1 | +340.6% (+339.6 to +341.6) | +336.1% (+329.2 to +343.1) | +337.7% (+333.9 to +341.5) | **confirmed WORSE** |
| keys evicted | 106,700 | 28,696 | -73.1% (-75.8 to -70.4) | -72.4% (-76.2 to -68.7) | -72.0% (-73.3 to -70.6) | shown, not judged |
| host CPU busy (share of the run) | 0.119 | 0.097 | -18.4% (-33.8 to -3.1) | -7.8% (-49.2 to +33.6) | -17.8% (-74.1 to +38.6) | no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds | 140.5 | 113.7 | -19.1% (-37.2 to -1.0) | -7.6% (-53.4 to +38.2) | -18.3% (-80.1 to +43.5) | no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds per 1,000 requests inside the line | 0.414 | 0.29 | -29.9% (-46.2 to -13.5) | -19.8% (-63.8 to +24.3) | -29.1% (-87.1 to +28.9) | no difference beyond the noise (2 of 3 runs) |
| ceiling changes written (the knob's moves) | 0 | 97.0 | +97 (+92.7 to +101) | +101 (+95.5 to +106) | +98.7 (+97.2 to +100) | shown, not judged |

The ceiling handed back to the operator's and read back at the end of every omni arm in every run: yes.

## burst: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 6 1 8 1 6 × 20.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,046 | 1,200 | +14.7% (+11.3 to +18.1) | +13.9% (+11.3 to +16.6) | +13.9% (+11.2 to +16.6) | **confirmed better** |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | no difference beyond the noise (3 of 3 runs) |
| cache hit rate | 0.698 | 0.8 | +14.7% (+11.4 to +18.0) | +13.9% (+11.3 to +16.6) | +13.9% (+11.1 to +16.7) | **confirmed better** |
| latency, 95th percentile (ms) | 5.75 | 5.74 | -0.2% (-0.3 to -0.1) | -0.6% (-0.9 to -0.4) | -0.3% (-0.4 to -0.2) | **confirmed better** |
| latency, 99th percentile (ms) | 5.82 | 5.81 | -0.0% (-0.5 to +0.4) | -0.2% (-0.4 to +0.1) | -0.1% (-0.1 to -0.1) | no difference beyond the noise (2 of 3 runs) |
| latency, mean (ms) | 1.86 | 1.3 | -30.5% (-38.2 to -22.8) | -30.1% (-35.6 to -24.5) | -29.4% (-35.4 to -23.4) | **confirmed better** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 201.3 | +214.6% (+145.8 to +283.3) | +204.8% (+140.2 to +269.4) | +204.9% (+139.1 to +270.8) | **confirmed WORSE** |
| memory used, mean (MB) | 56.9 | 155.8 | +173.6% (+134.9 to +212.3) | +171.4% (+136.3 to +206.6) | +171.1% (+135.3 to +206.9) | **confirmed WORSE** |
| keys evicted | 49,913 | 9,703 | -80.6% (-92.7 to -68.4) | -77.6% (-88.6 to -66.5) | -77.5% (-88.2 to -66.9) | shown, not judged |
| host CPU busy (share of the run) | 0.141 | 0.129 | -8.7% (-38.9 to +21.6) | -2.7% (-60.0 to +54.6) | -8.5% (-38.4 to +21.5) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 63.2 | 58.1 | -8.1% (-43.5 to +27.3) | -2.2% (-67.7 to +63.4) | -8.0% (-42.9 to +27.0) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 requests inside the line | 0.504 | 0.404 | -19.9% (-53.3 to +13.5) | -14.1% (-76.7 to +48.5) | -19.2% (-50.8 to +12.4) | no difference beyond the noise (3 of 3 runs) |
| ceiling changes written (the knob's moves) | 0 | 33.0 | +33 (+12.7 to +53.3) | +30.7 (+10.4 to +50.9) | +29.7 (+11.4 to +48) | shown, not judged |

The ceiling handed back to the operator's and read back at the end of every omni arm in every run: yes.

## large: 32768 B values, working set 625 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,251 | 1,425 | +13.9% (+13.8 to +14.0) | +13.8% (+13.6 to +14.1) | +13.7% (+13.3 to +14.1) | **confirmed better** |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | no difference beyond the noise (3 of 3 runs) |
| cache hit rate | 0.834 | 0.95 | +13.9% (+13.8 to +14.0) | +13.8% (+13.6 to +14.1) | +13.7% (+13.3 to +14.1) | **confirmed better** |
| latency, 95th percentile (ms) | 5.75 | 2.52 | -56.1% (-169.8 to +57.6) | -3.4% (-4.3 to -2.5) | -6.5% (-6.7 to -6.2) | no difference beyond the noise (1 of 3 runs) |
| latency, 99th percentile (ms) | 5.82 | 5.78 | -0.6% (-0.6 to -0.5) | -0.5% (-0.8 to -0.3) | -1.1% (-1.4 to -0.9) | **confirmed better** |
| latency, mean (ms) | 1.11 | 0.469 | -57.9% (-58.1 to -57.6) | -57.8% (-59.3 to -56.3) | -60.7% (-62.8 to -58.7) | **confirmed better** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 256.4 | +300.7% (+296.8 to +304.5) | +297.0% (+285.1 to +308.8) | +294.2% (+282.2 to +306.2) | **confirmed WORSE** |
| memory used, mean (MB) | 61.2 | 221.7 | +262.0% (+258.4 to +265.6) | +257.8% (+246.4 to +269.3) | +254.6% (+242.1 to +267.1) | **confirmed WORSE** |
| keys evicted | 73,285 | 17,277 | -76.4% (-77.4 to -75.4) | -75.9% (-77.3 to -74.6) | -75.6% (-78.1 to -73.2) | shown, not judged |
| host CPU busy (share of the run) | 0.11 | 0.0928 | -15.6% (-26.3 to -4.9) | -5.3% (-42.6 to +31.9) | -17.4% (-46.9 to +12.0) | no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds | 121.0 | 102.8 | -15.0% (-27.1 to -3.0) | -3.6% (-45.4 to +38.3) | -17.5% (-49.9 to +14.9) | no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds per 1,000 requests inside the line | 0.322 | 0.24 | -25.4% (-36.7 to -14.1) | -15.3% (-54.7 to +24.1) | -27.5% (-54.9 to +0.0) | no difference beyond the noise (2 of 3 runs) |
| ceiling changes written (the knob's moves) | 0 | 159.0 | +159 (+157 to +161) | +160 (+159 to +162) | +161 (+160 to +163) | shown, not judged |

The ceiling handed back to the operator's and read back at the end of every omni arm in every run: yes.

## small: 2048 B values, working set 10,000 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 832.4 | 1,049 | +26.0% (+25.7 to +26.4) | +26.0% (+25.7 to +26.3) | +26.6% (+24.9 to +28.2) | **confirmed better** |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (+0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | no difference beyond the noise (2 of 3 runs) |
| cache hit rate | 0.555 | 0.7 | +26.1% (+25.7 to +26.4) | +26.0% (+25.7 to +26.3) | +26.5% (+25.0 to +28.1) | **confirmed better** |
| latency, 95th percentile (ms) | 5.64 | 5.6 | -0.6% (-0.8 to -0.4) | -0.6% (-0.8 to -0.3) | -0.4% (-0.5 to -0.3) | **confirmed better** |
| latency, 99th percentile (ms) | 5.7 | 5.68 | -0.3% (-0.5 to -0.1) | -0.2% (-0.2 to -0.1) | -4.9% (-12.1 to +2.3) | no difference beyond the noise (1 of 3 runs) |
| latency, mean (ms) | 2.54 | 1.75 | -31.1% (-31.1 to -31.0) | -30.9% (-31.8 to -30.1) | -30.7% (-33.0 to -28.3) | **confirmed better** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 270.4 | +322.5% (+309.6 to +335.4) | +319.9% (+307.0 to +332.7) | +325.0% (+307.2 to +342.7) | **confirmed WORSE** |
| memory used, mean (MB) | 60.3 | 210.7 | +249.2% (+248.1 to +250.3) | +248.4% (+248.3 to +248.6) | +250.8% (+244.6 to +257.0) | **confirmed WORSE** |
| keys evicted | 185,038 | 16,311 | -91.2% (-94.0 to -88.3) | -89.9% (-90.3 to -89.5) | -91.8% (-98.7 to -84.9) | shown, not judged |
| host CPU busy (share of the run) | 0.143 | 0.125 | -12.5% (-15.2 to -9.8) | -2.6% (-63.6 to +58.4) | -11.7% (-27.8 to +4.4) | no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds | 170.0 | 148.4 | -12.7% (-15.5 to -9.8) | -1.5% (-69.2 to +66.3) | -11.4% (-30.3 to +7.6) | no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds per 1,000 requests inside the line | 0.68 | 0.471 | -30.7% (-34.5 to -26.9) | -21.8% (-81.3 to +37.6) | -30.0% (-49.9 to -10.1) | no difference beyond the noise (1 of 3 runs) |
| ceiling changes written (the knob's moves) | 0 | 50.3 | +50.3 (+34.4 to +66.3) | +49.7 (+37.4 to +61.9) | +48 (+38.1 to +57.9) | shown, not judged |

The ceiling handed back to the operator's and read back at the end of every omni arm in every run: yes.

**Across 3 untouched workloads: 12 gauge-rows confirmed better, 6 confirmed worse, 0 where the runs disagree.**

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

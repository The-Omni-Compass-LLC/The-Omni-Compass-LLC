# The Redis cache in our own model, closed loop: omni-v22's candidate against omni-v21's loop and native (class S)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Our own model of the cache (`tools/redis_model.py --compare --seeds 3`, 30 October 2026, seeds 101 to 103, 30 s a notch): the harness's application, an LRU cache measured in bytes, a hit's and a miss's latency drawn from the omni-v21 native arms' own records (`docs/REDIS_PREREGISTRATION.md`, amendment 5). Native holds the operator's 64 MB; the standing wire is omni-v21's loop read from git at 29370eec0b; the candidate is the branch's own Brain (the max, the working set's floor, the application's own account of a miss, the host's room). Evidence class S, our own model, never a benchmark result. A reading leads with the word: the candidate's work inside the line GAIN in every workload (up 7.7% to 22.9%), the mean latency GAIN (down 36% to 59%), the 95th and 99th percentiles GAIN or STEADY, the memory held power given (up 220% to 367%); no LOSS.

```
== tuning
   gauge                                          native    standing   candidate   standing vs native, candidate vs standing (%)
   work inside the line (requests a second)      1247.33     1256.42     1385.60   +0.7  +10.3
   latency, mean (ms)                               1.04        1.01        0.55   -3.1  -45.6
   latency, 95th percentile (ms)                    5.55        5.55        5.41   -0.1  -2.5
   latency, 99th percentile (ms)                    5.72        5.72        5.66   -0.0  -1.0
   hit share                                        0.83        0.84        0.92   +0.7  +10.3
   ceiling held, mean (MB)                         64.00       65.81      304.23   +2.8  +362.3
   memory used, mean (MB)                          60.44       61.15      264.42   +1.2  +332.4
== small
   gauge                                          native    standing   candidate   standing vs native, candidate vs standing (%)
   work inside the line (requests a second)       938.70      937.19     1151.95   -0.2  +22.9
   latency, mean (ms)                               2.14        2.15        1.38   +0.3  -35.6
   latency, 95th percentile (ms)                    5.66        5.66        5.60   +0.0  -1.2
   latency, 99th percentile (ms)                    5.75        5.75        5.74   +0.0  -0.2
   hit share                                        0.63        0.62        0.77   -0.2  +22.9
   ceiling held, mean (MB)                         64.00       64.58      265.51   +0.9  +311.1
   memory used, mean (MB)                          59.38       59.03      208.83   -0.6  +253.8
== large
   gauge                                          native    standing   candidate   standing vs native, candidate vs standing (%)
   work inside the line (requests a second)      1351.73     1360.97     1466.18   +0.7  +7.7
   latency, mean (ms)                               0.67        0.64        0.26   -4.9  -58.9
   latency, 95th percentile (ms)                    5.48        5.46        0.27   -0.3  -95.1
   latency, 99th percentile (ms)                    5.69        5.68        5.50   -0.1  -3.2
   hit share                                        0.90        0.91        0.98   +0.7  +7.7
   ceiling held, mean (MB)                         64.00       61.94      289.19   -3.2  +366.9
   memory used, mean (MB)                          60.75       57.59      252.32   -5.2  +338.1
== burst
   gauge                                          native    standing   candidate   standing vs native, candidate vs standing (%)
   work inside the line (requests a second)      1116.96     1116.96     1313.47   +0.0  +17.6
   latency, mean (ms)                               1.51        1.51        0.81   +0.0  -46.5
   latency, 95th percentile (ms)                    5.61        5.61        5.51   +0.0  -1.8
   latency, 99th percentile (ms)                    5.74        5.74        5.71   +0.0  -0.6
   hit share                                        0.74        0.74        0.88   +0.0  +17.6
   ceiling held, mean (MB)                         64.00       62.79      201.20   -1.9  +220.5
   memory used, mean (MB)                          56.16       55.83      161.98   -0.6  +190.1
```

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

# What I measure on real Kubernetes: native against me on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The latest paired set is **set 20** (`results/live/LIVE_REPS_20.md`, benchmark-reps run 36366603505, commit 18220d4),
ten paired repetitions on kind in GitHub Actions.

| Gauge | Native | Me on top | Verdict |
|---|---:|---:|---|
| response time, mean (ms) | 126.1 | 79.4 | −37.1%, GAIN, proven |
| response time, 95th percentile (ms) | 264 | 120 | −54.6%, GAIN, proven |
| response time, 99th percentile (ms) | 374.9 | 154.4 | −58.8%, GAIN, proven |
| failed requests (%) | 0 | 0 | STEADY |
| pods the autoscaler had to start | 4.9 | 2.6 | −46.9%, GAIN, proven |
| pod start wait, mean per pod (s) | 2.73 | 1.48 | −45.9%, GAIN, proven |
| replicas, mean | 8.82 | 6.57 | −25.5%, GAIN, proven |
| workers open to new work | 6 | 4.96 | −17.4%; all stayed on, so no saving by itself |
| CPU burned by the app (cores) | 0.881 | 1.112 | +26.3%; same work, more CPU used |
| energy, idled worker fully on (100 W) | 156.0 | 158.2 | +1.4%, power given, proven |
| energy, idled worker at a declared 25 W | 158.7 | 141.2 | −11.0%, model only, no meter |

**What is proven:** I make the app answer faster, with fewer pods started and shorter waits, with zero failed requests,
and one switch puts everything back.

**What is not proven:** any energy or money saving. kind has no power meter, and every machine stayed on. That needs a
real meter, and a node autoscaler that removes the machines I idle.

**How I did it:**
- No pod was moved, evicted or restarted.
- No machine was switched off; an idle machine stays powered and Ready.
- The autoscaler alone made every pod.

**Earlier sets.** Each earlier set is recorded as measured: `LIVE_REPS_9.md`, `LIVE_REPS_11.md`, `LIVE_REPS_13.md` to
`LIVE_REPS_19.md`. Set 19's "energy" and "work done" rows carry the same caveats as above.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

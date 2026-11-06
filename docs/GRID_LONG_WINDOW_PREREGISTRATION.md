# The four stacked and the whole tower at 100 copies, the cluster inside, with a longer window: preregistration

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Written on 13 October 2026, before any of the runs it describes. Engine omni-v5 (digest `5648f290`), unchanged.

## Why

With the real Kubernetes cluster inside, an organism steps on the measured window's clock (240 steps,
`tools/run_kil.py`), and the rig's own rule is that the window is long enough for the max's arm to make every step in
time (`.github/workflows/six-kube.yml`; `tools/six_kube_report.py` marks a repetition that ends more than 5% of the
window late OFF THE CLOCK). In the grid on the card version (the 100-copy squares pooled by six-kube-pool run
38416354634), two squares did not keep that rule well enough:

- **the four stacked at 100 copies** (190,800 modelled muscles, window 3,600 s): Omni-Compass's arm fell behind the clock
  in 49 of 100 repetitions (up to 635 s late; on average 202 s, against 5 s for native);
- **the whole tower at 100 copies** (110,700 modelled muscles, window 2,400 s): behind in 1 of 100 (up to 167 s).

In both squares, at 100 repetitions, the real service's slowest responses were slower in Omni-Compass's arm (the 95th
percentile 45% and 13.5% slower, the 99th 19% and 14%), while its time over the response line was lower (8% and 11% less).
The organism's model and Omni-Compass's law for every modelled muscle run in one process on the same four-core runner as
the real cluster: in Omni-Compass's arm that process held more of the runner (the runner 92.7% busy against 89.9%), and
the service's pods used 7% less CPU at the same number of copies. On a real cluster Omni-Compass runs on its own machine.

## What changes

Only the window of these two squares, so that each of the 240 steps gets 1.5 times the wall clock and the max's arm
needs a smaller share of the runner to keep it:

| Square | Window before | Window now |
|---|---:|---:|
| The four stacked, 100 copies | 3,600 s | 5,400 s |
| The whole tower, 100 copies | 2,400 s | 3,600 s |

Everything else is protocol 2 as run in the grid: the governor at the organism's own CPU priority, its decisions
counted inside the window; the same seeds, the same open-loop load generator at 6 replicas at the organism's peak; a
fresh six-worker kind cluster for each arm; both arms of a repetition on one runner, in rotated order; a repetition whose
job fails is started again by hand, up to three times, and one that fails three times is listed.

## Runs

`six-kube` with what = runs, sizes = 100, split = no: the four stacked with durations_s = 5400, the whole tower with
durations_s = 3600, repetitions 1 to 10 first, then 11 to 100. The run names carry the window
(`... window 5400 protocol 2`). These runs are pooled only among themselves (`six-kube-pool`), never with the runs at the
earlier windows.

## Reading

The same report and the same rules as the grid (`tools/six_kube_report.py`: a gauge GAIN or LOSS only when its 95%
interval is clear of zero). The grid page shows these squares beside the earlier ones, each with its window; the earlier
squares stay exactly as they are.

- If Omni-Compass's arm keeps the clock and the 95th and 99th percentiles are no longer LOSS beyond the noise, the
  slower tail was the shared runner (the window too short for this many muscles), and it is reported so.
- If they stay higher, it is Omni-Compass's own computation competing with the service on one machine, and it is
  reported so.

Cost: GitHub's own runners (no charge). Time: each repetition about 3.6 hours (the four stacked) and 2.6 hours (the whole
tower) on one runner; ten of each about four hours of wall clock.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

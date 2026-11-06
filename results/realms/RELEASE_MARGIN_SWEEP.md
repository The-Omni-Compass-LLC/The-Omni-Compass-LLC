# Why the stacks were late more often on 2026-10-02, and the knob that settles it

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Model runs (evidence S), organism Compute / AI / Cloud (345 muscles), seeds 6000-6004, 240 steps, native against the
compass law on every muscle, handed back at 90%. Each change is Omni against native. Late: time over the service line
(the aim is lower). Energy: the aim is lower (less spent). Work: the aim is higher.

## The two knobs that moved between commit `c908054` (the first card run) and `2a9285d`

| Code | HPA target lever | Machine headroom (RELEASE_MARGIN) | Late (pp) | Energy | Work |
|---|---|---:|---:|---:|---:|
| `c908054` (first card run), seeds 6000-6002 | Omni may loosen it to 0.95 | none (1.0) | +0.25 (higher: late more often) | -0.34% (lower) | same |
| today, the target lever put back alone | Omni may loosen it to 0.95 | 0.6 | +0.06 (higher) | -0.49% (lower) | same |
| today, the headroom removed alone | held at the operator's | 1.0 | +0.16 (higher) | -0.28% (lower) | same |
| **today (both)** | **held at the operator's** | **0.6** | **-0.03 (lower: late less often)** | **-0.10% (lower)** | same |

Both knobs traded time over the line for energy. Loosening the operator's HPA target runs fewer pods, so bursts
wait; handing a machine back with no headroom leaves the next burst to wait for a machine to boot.

## The headroom dial (target held at the operator's)

| RELEASE_MARGIN | Late, mean (pp) | Late, worst seed (pp) | Energy |
|---:|---:|---:|---:|
| 0.5 | -0.033 (lower) | -0.019 (lower) | -0.086% |
| **0.6** | **-0.030 (lower)** | **-0.013 (lower)** | **-0.099%** |
| 0.7 | -0.019 (lower) | +0.002 (higher) | -0.129% |
| 0.8 | +0.012 (higher) | +0.037 (higher) | -0.173% |
| 0.9 | +0.059 (higher) | +0.081 (higher) | -0.229% |
| 1.0 | +0.160 (higher) | +0.198 (higher) | -0.275% |

0.6 is the setting that spends the least energy with no seed late more often than native (band first). From 0.7 up
at least one seed is late more often, which the founder's rule does not allow. The dial is the trade: every step
past 0.6 buys energy with lateness.

Reproduce: the scratch script in this file's commit message, or run `realms.compass_arm` with `RELEASE_MARGIN` set and
the HPA target lever on or off.

## The per-muscle sweep (2026-10-05): every node pool on its own, the compass law

The stack sweep above judged lateness at the organism. On each node pool alone (the 42 pools under a node autoscaler,
seeds 3000-3009, native against the compass law, everything else fixed):

| RELEASE_MARGIN | Energy, mean | Time over the line, mean (points) | Pools later than native |
|---:|---:|---:|---:|
| 0.6 | -2.00% | +0.157 (max +0.431) | 32 of 42 |
| 0.5 | -0.71% | +0.055 (max +0.278) | 23 of 42 |
| 0.4 | -0.11% | +0.004 (max +0.069) | 4 of 42 |
| 0.3 | -0.00% | 0.000 | 0 of 42 |

On a node pool every percent of energy saved by releasing a machine is paid in lateness: a machine boots in minutes,
and a burst that comes in the meantime is served late. Work and speed come first, so the margin is 0.3, the largest
at which no pool is later than native. It is the rule the live controller follows on real Kubernetes too: a machine goes
back only where giving it back costs no speed.

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

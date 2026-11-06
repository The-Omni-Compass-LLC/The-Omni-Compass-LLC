# Omni v14: a knob for every muscle, the operator's commands without a shell (the engine that stands since 21 October)

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Omni v14 was the engine on main on 21 October, from 04:47 UTC until omni-v15 (`docs/OMNI_V15.md`) landed that evening. The founder's orders behind it: knobs on every monitor, "to turn off and
on such a mechanism, a muscle, or tweak and turn any muscle" (20 October, evening), and, the next night, "tune the engine". It is
omni-v13 (`docs/OMNI_V13.md`) with two changes, each written before it was built and read in the model gate against omni-v13 on the
same seeds before it landed: a knob that leaves any one muscle native, and the operator's own commands run without a shell. Every
setting, gain, preset and muscle is omni-v13's, and so is every other rule. A third change, to the conveyance's reading on a
shared host, was built, tried in the gate and refused there; it is not in omni-v14 (section 3).

Its fingerprint is `OMNI_V14.json` (digest `7afba44615fcff8f`, 47 files). Forty-five files are omni-v13's bytes; two differ, the Kubernetes
governor (`omni_controller/controller.py`) and its muscles (`omni_controller/muscles.py`). Every benchmark runs again on
omni-v14, A, B and C. Every earlier table stands as its own engine's result until its three runs on v14 land, and results from
two versions are never pooled. The readings from the model gate are our own models (evidence class S), never a benchmark result.
Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

| # | Change | Where | Why |
|---|---|---|---|
| 1 | `--native MUSCLE[,...]` leaves each named muscle where native runs it: never written, the rest running as before; a name that is not a muscle is refused at the start | the governor and its muscles; the control panel's muscle button | the founder's order of 20 October: a knob for every muscle; and his rule that a muscle Omni-Compass would hurt stays native |
| 2 | The operator's own commands (the site power reading, a muscle's read command, a wall meter's `cmd:`) run without a shell unless they hold a pipe, a redirect or a variable | `run_operator_cmd` (`omni_controller/muscles.py`), `tools/wall_meter.py` | the static scan's three high findings (`docs/SECURITY_SCAN.md`); the governor's site power reading no longer reaches a shell at all |

## 1. The knob

`--native MUSCLE[,MUSCLE...]` (or `OMNI_NATIVE`) names the muscles the governor leaves native. A muscle named there is never
written: it stays where native runs it, and every other muscle runs as before. The governor still reads the whole body and
decides with all of it in view; only the write of a muscle left native is withheld, and the audit says so (`"held"`, and
`"native_muscles"` at the start). A name that is not a muscle is refused at the start, never ignored, so a misspelling can
never leave a muscle driven that the operator meant to leave native. With no name given, nothing is left native and the
governor runs exactly as omni-v13 does.

| Muscle | What is left native |
|---|---|
| `machines` | the node pool's size (the operator's node-scale command) |
| `replicas` | the pod autoscaler's target, the pod reflex's replica floor and the replica cap |
| `cpu` | the serving pods' CPU limits (the conveyance and the pod power cap) |
| `clock` | the processors' frequency ceiling |
| `gpu` | the GPU's power limit |
| `rollout` | the rollout guard (pause and undo) |
| `batch` | the batch admission and pacing |
| `rightsize`, `coldstart`, `contain`, `cooling` | the pods' rightsizing, the cold-start reserve, the namespaces' containment, the cooling setpoint |

The control panel (`tools/omni_control.py`) carries it as one more button, `POST /v1/muscle {"muscle": NAME, "on": true|false}`,
role operator, every press audited with its holder and reason, and as a row of On and Native buttons on the console. Like a
dial press it passes through native: the governor's own kill file is set, its exit awaited (every setting it wrote restored
and read back), and it starts again with the new list. Nothing is changed under a running governor. The monitor wall on the live
engine page (`docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`, `#s-wall`) points every row at these buttons; the wall itself never presses one. Tests:
`tests/test_native_muscles.py`.

## 2. The operator's commands without a shell

A command the operator configured (`--power-cmd`, a muscle's read command in the wiring file, a wall meter's `cmd:`) is split
into its words as a shell would split them and run directly when it holds nothing only a shell reads: no pipe, list, redirect,
subshell, variable, substitution, glob, home directory, comment or `NAME=value` before the command. One that does runs through
the shell as before, so no operator's wiring changes. Tests: `tests/test_operator_cmd.py`. The static scan reads two high
findings where it read three (`docs/SECURITY_SCAN.md`): the governor's own call to a shell is gone, and the two that remain are
the fallback for a command that needs one.

## 3. Refused by the gate: the conveyance's reading on a shared host

The fault it was meant to fix: on the model set from KubeRay's rig (`results/model_gate/V13_VS_V12.md`), omni-v13 raises the web
pods' CPU limits once early in the batch queue and hands them back 15 s later, and the batch's job turnaround reads +0.05%
against native, a LOSS by the key. The governor reads the host's busy share as the change in its processor counters since its
previous reading (every 15 s); the trace of that raise shows it lands on the reading the second job's pods are starting at,
before their load is in the reading.

Three rules were written and tried, each against omni-v13 on the same eight seeds:

- **No raise on any reading older than another workload's newest running pod.** Refused: the web's 95th percentile read 6.4%
  higher than omni-v13's, a LOSS.
- **No raise on the reading that opens another workload's run** (none of its pods with room running at the previous reading).
  It never fires in the model: identical to omni-v13 on every gauge, because the batch is already running when the second job
  arrives.
- **That rule, and the starting pods counted:** a pod of another workload still starting ran for none of the interval, so what
  it may use is added to the reading, and nothing is raised when the sum reaches the 70% cushion. It fires where the fault is.
  The batch turnaround returns to native's exactly, and the web's queue period is native's second by second. But the web's 95th
  percentile reads 6.4% higher than omni-v13's, a LOSS. Traced seed by seed: omni-v13's one raise costs the batch pods 15 s of
  work, which moves when every later batch pod finishes, and with it the seconds the web runs on its last pod; in six of eight
  seeds that lowered the web's 95th percentile against native. Without the raise the web's queue is native's, and the gain that
  rode on the batch's delay is gone.

By the gate's rule a LOSS row is not carried into a real run, so none of the three is in omni-v14. They are kept on the branch
`v14-convey-study` with their tests and the model's readings. The next version's list (`docs/CHANGE_CONTROL.md`) carries the
work that comes first: the model's web model set from a real run's own files (its record already says it is out of its regime on
the 3-core batch host), then the third rule read again. The gate found one fault in the model itself and it is fixed for both
engines: a batch pod was listed as Running from the moment it was made; a cluster lists it as Pending until its container runs
(the rig's own pod start, about 3 s).

## 4. The model gate against omni-v13

`results/model_gate/V14_VS_V13.md`: the shipped controller on the model cluster in the cloud setting at 60 and 15 s and with every
worker out of service for two minutes, the conveyance on one kind host (readable quota, unreadable quota, a quota that refuses
every raise, and the batch muscle of KubeRay's rig beside the serving one), and the verdict on noisy work, eight seeds each, the
same seeds for both engines. Every one of the 57 gauges reads identical between omni-v14 and omni-v13, and the verdict allows the
same share of give-back steps at every cost: no LOSS. That is what both changes should read there: with no muscle named, the
knob leaves nothing native, and no model calls an operator's command. The knob's own behaviour is proven in its tests (a muscle
named is never written, an unknown name is refused, every other muscle runs as before), and the commands' in theirs.

## 5. What stays omni-v13's

Every other engine file; every rule, gain and guard, the conveyance and its hand-back of omni-v13 among them; the verdict byte
for byte. The next version's list (`docs/CHANGE_CONTROL.md`) carries what is still to fix. The GPU governors
(`omni_controller/gpu_governor.py`, `gpu_compass.py`) keep their own two levers, the power limit and the clock, and take the
per-muscle knob with the version that next changes them.

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

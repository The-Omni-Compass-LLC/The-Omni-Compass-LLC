# Omni v15: the power cap's request through the line's own clear time, every wire in the fingerprint (the engine that stood 21 to 22 October)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Omni v15 was the engine on main from 21 October, evening, until omni-v16 (`docs/OMNI_V16.md`) landed on 22 October, under the founder's standing order that every fault found is
fixed and every fix lands as the next version, told, not asked (19 October), and his word of 21 October ("push, push, push on
GitHub, update, enhanced engine"). It is omni-v14 (`docs/OMNI_V14.md`) with one change to the brain and one to the fingerprint,
each written before it was built and read in the model gate against omni-v14 on the same seeds before it landed: the brain's
request for the power cap trims only while the response line has been clean for the governor's own clear time, and every wire
that holds a governor's rules is inside the fingerprint. Every gain, guard, preset and muscle is omni-v14's, and so is every
other rule. A third item declared with it is not an engine change: the kill test's reading after the kill is 300 s wide
(section 3). A second form of the first change, a dwell with a glide, was built, read in the gate and refused there; it is not
in omni-v15 (section 1).

Its fingerprint is `OMNI_V15.json` (digest `0a53cdd7a558f803`, 55 files). Forty-five of its files are omni-v14's bytes; two
differ, the brain (`omnicompass/adapter.py`) and the card governor (`omni_controller/gpu_governor.py`); eight are the wires
taken into the fingerprint with this version, their bytes as they stood (`tools/run_redis.py`, `run_kafka.py`,
`run_pgbench.py`, `run_sysbench.py`, `run_ycsb.py`, `run_swarm.py`, `run_mujoco.py`, `run_cpu_power.py`). The C++ twin of the
brain (`cpp/src/governor.cpp`) carries the same change and is proven equal to the Python again (`tests/test_cpp_governor_parity.py`,
on an observation stream that now carries the line's clear flag; `results/SEAL.json`). Every benchmark was to run again on omni-v15,
A, B and C; none started before omni-v16 replaced it, because the grid's conductor read omni-v15's commits as no engine (its own
copy of the version tool's scope predated the eight wires; fixed on 22 October, `CHANGELOG.md`). Every earlier table stands as its own engine's result until its three runs on v15 land, and results from two
versions are never pooled. The readings from the model gate are our own models (evidence class S), never a benchmark result. Run
and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

| # | Change | Where | Why |
|---|---|---|---|
| 1 | The brain trims the power cap to demand only while the response line has been clean for the governor's own clear time; a breach, or a line not yet clean, releases the request to the start limit in the same decision | `omnicompass/adapter.py` (the `power` rule, `observe_vector`'s `clean`), its C++ twin `cpp/src/governor.cpp`; the card governor hands the brain its clear flag (`omni_controller/gpu_governor.py`) | on the omni-v11 long run the request switched between the start limit and the trim at 126 of 350 decisions and turned back at 123 of them, at the one threshold on the queue and the state (`docs/CHANGE_CONTROL.md`, "the next version's list") |
| 2 | Every wire that holds a governor's rules is in the fingerprint | `tools/omni_version.py` (`SCOPE`; a version declared before them is read without those eight wires and only those) | a rule in a wire outside the fingerprint could change without the version changing (the swarm's reflex did, in omni-v12) |
| 3 | Declared, not an engine change: the kill test reads the 300 s after the kill, where it read 120 s | `tools/live_reps.py`, `docs/ROBUSTNESS_PREREGISTRATION.md` ("On omni-v15"), `tests/test_robust.py` | the one tail rise of the omni-v11 kill test came 140 to 190 s after the kill, past the window declared |

## 1. The request through the clear time

**The fault.** The brain (`omnicompass/adapter.Governor`) asks for a power cap at every decision: when the queue is under its
guard (q < 0.05) and the state's U is at or over the gate (0.85 in the fleet law), the request is the trim to demand,
clamp(cap_now × load × (1 + margin), cap_min, 1); otherwise it is the start limit, 1. On the omni-v11 long run (run
39173420146, the robustness long scenario: three paired repetitions of two hours on real Kubernetes, the wandering load) the
governor's own audit shows the request switching between 1.0 and 0.695 (the fleet law's floor, which the trim reached at every
calm decision) at 126 of its 350 decisions, and turning back the other way at 123 of them (41 of 116, 36 of 118 and 49 of 116 in
the three repetitions; `results/STEERING.md` reads it as moves and reversals an hour). Each switch was the line breached (the
controller folds the response-time pressure into the queue reading) and the next decision calm again. On Kubernetes the power
wire is off, so nothing was written; but the card governor reads the same request for the GPU's power limit, and a request that
hammers at one threshold is not the compass law's way (a band with cushions, smooth, not hammering).

**The rule.** The Kubernetes governor already declares the reflex: while the response line is breached, and for its clear time
after (`--slo-clear-s`, 180 s), Omni-Compass may not pack replicas tighter than the HPA's target and may not cap power. It
handed that flag to its muscles and not to the brain, whose request kept trimming the moment one decision read calm. The card
governor applied the same gate outside the brain (`cap = requested if slo_clean else 1.0`, its `--slo-clear` 3 decisions).
omni-v15 puts it inside: the observation vector carries the line's clear flag (`slo_clean`; a caller that senses no line is
clean), and the trim is asked for only while it is set. A breach, or a line not yet clean for the clear time, releases the
request to the start limit in the same decision; the spread under backlog at the power envelope and the backlog bound are
untouched. No constant is added to the law: the clear time is each governor's own, as it already declared it.

**Read on the run's own decisions.** The three audits' decisions (their queue reading, state U, clear flag and the request
recorded) are kept as a fixture (`tests/fixtures/robust_long_39173420146_decisions.json`, the source files' SHA-256 inside).
The recorded request is omni-v14's rule on the recorded queue and state, decision for decision. On the same decisions, read
with the recorded clear flag, omni-v15's rule leaves 35 moves of 126, 32 reversals of 123, and 28% of the travel
(`tests/test_cap_band.py`). A fault's fix is read first where the fault was found.

**Refused by the gate.** A second form was written first: a dwell of three calm decisions and a glide of 0.05 a decision toward
the trim, the release at once. On the run's own decisions it reads 67 moves and 33 reversals; but in the model gate, where the model
cluster's calm stretches are long, the glide turned each trim into seven small moves (the request's moves in a day 149 against
omni-v14's 38 on one seed, the travel the same), and on the model card it wrote the limit 25 times against 16 for the same travel
and 0.17% more energy. More writes of smaller size is not the fix the fault asked for; by the gate's rule it is not carried.
The clear-time gate alone is in omni-v15.

**The card.** With the flag inside the brain the card governor's own gate becomes a second reading of the same rule: the model
card reads omni-v15 identical to omni-v14 on every gauge (section 4), as it should, and the GPU's run on Lambda starts from
`gpu-omni-v15`, one exact commit.

## 2. Every wire in the fingerprint

`tools/omni_version.py` hashes every file whose bytes decide what Omni-Compass does. Up to omni-v14 the scope held the brain,
the live governors, the realms and three outside-simulator wires (`tools/run_kil.py`, `run_citylearn.py`, `run_pandapower.py`);
the data stores' wires (`run_redis.py`, `run_kafka.py`, `run_pgbench.py`, `run_sysbench.py`, `run_ycsb.py`) and `run_swarm.py`,
`run_mujoco.py` and `run_cpu_power.py` were versioned by git and tested but did not move the digest, and one of them carried a
fault fixed in omni-v12 without the digest moving (`docs/CHANGE_CONTROL.md`, "Gaps this page names"). From omni-v15 every one
of them is in the scope: a change to any rule changes the version. A version declared before them is read without those eight
wires and only those: a commit carrying omni-v14's 47 files byte for byte reads omni-v14 whatever those eight wires hold,
because its fingerprint never covered them, while any other file omni-v14's list does not name (a new rule, a new module)
still makes the tree a different engine (`tests/test_omni_version.py`); and the tool prints a version's own digest and file
count as its fingerprint records them.

## 3. The kill test's reading: 300 s after the kill

Declared before omni-v15's runs, as `docs/ROBUSTNESS_PREREGISTRATION.md` ("On omni-v11") proposed: the kill scenario's paired
gauges, the time over the line and the failed requests after the kill, are read over the 300 s after the kill mark, where they
were read over 120 s (`tools/live_reps.py`, `ROBUST_AFTER_KILL_S`). The one tail rise of the omni-v11 kill test came 140 to
190 s after the kill, past the old window. The omni-v11 kill table stands as read then; omni-v15's kill runs are read over 300 s
from their first. The rig is unchanged (the probe runs through the whole 900 s window).

## 4. The model gate against omni-v14

`results/model_gate/V15_VS_V14.md`: the shipped controller on the model cluster in the cloud setting at 60 and 15 s and with every
worker out of service for two minutes, the conveyance on one kind host (readable quota, unreadable quota, a quota that refuses
every raise, and the batch muscle of KubeRay's rig beside the serving one), the verdict on noisy work, and, new with this version,
the GPU governor on the modelled card (the card whose voltage falls with its clock and the card near its voltage floor), eight
seeds each, the same seeds for both engines. Every service gauge of every model reads identical between omni-v15 and omni-v14:
machine-hours, energy, pending-pod minutes, the HPA's shortfall, the 95th percentile and the alert minutes on the cluster models;
requests served, start waits, the 95th percentile, host busy, limits given, pod seconds and writes on the conveyance models; the
batch queue and turnaround; requests served, the 95th and 99th percentiles, energy, peak temperature and the limit's writes,
moves, reversals and travel on both card models (the card governor applied the same gate outside the brain, so the brain's gate
inside changes nothing there: 17 writes, 16 moves and 15 reversals a run on the card whose voltage falls with its clock, 35, 34
and 33 on the card near its floor, the same in both engines); and the verdict allows the same share of give-back steps at every
cost. The request's own wear is the one place the two engines differ, and it reads STEADY: on the model cluster, where the response
line is breached in about 27 of a day's 1,440 minutes and the calm stretches between are long, the request moved 67.3 times a day
against 64.9 (+3.7%, STEADY), turned back 66.1 times against 63.8 (+3.7%, STEADY) and travelled 20.4 against 19.6 (+3.9%, STEADY) at a
decision every 60 s; at a decision every 15 s 98.8 moves against 100.1 (−1.4%, STEADY), 96.1 reversals against 97.5 (−1.4%, STEADY),
29.3 travel against 29.7 (−1.4%, STEADY); with the blink, +3.0%, +2.9% and +3.0%, STEADY. The small rise at 60 s is the gate doing
what the governor declares: omni-v14 kept trimming while the line was breached by less than the queue guard's 5% (a pressure
between 0 and 0.05), and omni-v15 releases there too, so in a regime of rare, light breaches it releases a little more often. The
fault was found in the opposite regime, the long run's clustered breaches (126 switches in 350 decisions), where the same gate
leaves 35 (section 1); the cluster model's regime is the cloud setting's, set from a real run's own files, not the long run's, and
the next long run on omni-v15 reads the request's moves and reversals an hour in `results/STEERING.md`. No LOSS anywhere: the
change lands.

## 5. What stays omni-v14's

Every other engine file, byte for byte; every gain, guard and preset; the conveyance and its hand-back; the verdict. The next
version's list (`docs/CHANGE_CONTROL.md`) carries what is still to fix, first among them the Redis harness's brain in its own
process (its model, `tools/redis_brain_probe.py`, is read before the harness changes, with the version that changes it) and the
model's web model set from KubeRay's after-queue files. The GPU governors keep their own two levers; the brain they call now
reads the line's clear flag from them.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

# Omni v24: the factory beat for its place: a decision every 10 s on site, every 60 s through a cloud

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Omni v24 (`OMNI_V24.json`, digest `66c8f2d94b3e4725`, 65 files) stood on main from 1 November, night, to 3 November, night, when omni-v25
(`docs/OMNI_V25.md`, the Kafka wire's producer started before the governor's thread) took its place. It is omni-v23 with one change in the Kubernetes governor
(`omni_controller/controller.py`, `factory_beat`): the heartbeat it ships with, its full decision, is read from the place it
runs in, a decision every 10 s on site and every 60 s through a cloud. On the founder's orders:

> "Whatever is the best one out of all that helps the best system is the factory set one." (23 October)
>
> "60 seconds is a disadvantage, it's not a benefit ... we have to have the basic line engine tuned to what we call the basic
> setting, and then we lock that, and anybody can turn and tweak it to another scenario." (31 October)
>
> "You pick and find out." (31 October, night)
>
> "Update, push, build, wire, and give me my new version engine and everything." (1 November)

64 of its 65 files are omni-v23's bytes. No gain, guard, preset, card or law moves; do no harm keeps its strictest form. Every
rule of the governor counts seconds (omni-v16), so the beat changes only how often the governor looks, never how long any rule
waits; the fast checks (the scheduling floor, the pod reflex, the conveyance's clock) stay every 5 s at every beat.

## What changes in the engine

- With no `--interval` set, the governor reads the cluster's nodes once, at its start. A node whose `spec.providerID` names a
  public cloud's machine (`azure://`, `gce://`, `aws://`, `oci://`, `digitalocean://`, `linode://`, `ibm://`, `alicloud://`,
  `hcloud://`, `scaleway://`, `vultr://`) makes the place "through the cloud", and the beat is 60 s. Every other node (kind's
  `kind://`, the owner's own machines, a private cloud the owner runs, a node with no providerID) makes it "on site", and the
  beat is 10 s. A reading that fails, or finds no node, keeps the longer beat, 60 s: a blind reading decides nothing (omni-v11).
- `--interval` set by hand always wins. The heartbeat stays a dial (any beat from 5 to 120 s; the live engine's six buttons,
  10, 15, 30, 60, 90 and 120 s), and every beat a person sets is that person's tune, its results its own.
- The audit's first record names the place, the beat and the reason (`factory_beat`), so every run says which beat it ran at
  and why.
- `--print-factory-beat` prints the beat for the cluster the kubectl reaches and exits. Every rig asks the engine through it
  (`scripts/factory_beat.sh`), so the rule is written once, in the engine.

## Why these two beats: the pick, before the gate

The rule that picks the factory beat was frozen before any reading was seen (`docs/PACE_PREREGISTRATION.md`, amendment 4): a beat
is admissible when no gauge reads LOSS against native (in a cloud the machine-hours stand for the bill and may not rise); among
the admissible beats the factory beat is the one no other dominates on the service gauges; where none is admissible the factory
beat stays 60 s. Amendment 6 read the twelve beats, 5 to 120 s, again on the corrected model (its stand-in cluster gives every
pod its own object and metadata), in both places, on the tune study's development seeds 101 to 108, one day each (our own models,
evidence class S; the record `results/model_gate/V23_LADDER_CORRECTED.md`, written by `tools/beat_ladder.py` from its source report
`results/model_gate/V23_LADDER_CORRECTED_SOURCE.json`, which names the tree each place ran on):

- **On site** (the kind rig's own machines, made at the start, no cluster autoscaler): every beat admissible, and 10 s the one
  beat no other dominates (rule 2). Against 60 s at 10 s: the minutes over the response line down 65.5%, from 6.9 to 2.4 a day
  (fewer, GAIN); the 95th percentile response down 9.9%, from 59.3 to 53.4 ms (faster, GAIN); the pod autoscaler short of its
  target down 6.2% (GAIN); the power-cap request's moves down 47.2% and its reversals down 53.1% (GAIN); the machine-hours
  identical (on site the machines are already made and paid for). What it costs: the governor reads the cluster 6,897 times an
  hour where it read 2,317 (up 197.7%, power given), and its own processor works 10.3 s an hour where it worked 1.3 s (power
  given).
- **Through a cloud** (the plant with the cloud's own autoscaler, Omni-Compass at the max on top): no beat admissible. Every
  beat raised the machine-hours against native, up 7.8% to 33.7% (up 14.7% at 60 s): the bill, which the rule does not let rise
  in a cloud; and every beat but 90 s raised the pods waiting for a place (LOSS, up 15.4% at 60 s). By rule 4 the factory beat
  stays 60 s, and those rows go on the next version's list with their cause: the autoscaler target held ahead of the load buys
  machines the cloud bills, and a pod waits while the cloud makes a machine (the next design: ask the cloud for a machine
  without making a real pod wait).

## The model gate

`results/model_gate/V24_VS_V23.md` (our own models, evidence class S; `tools/model_gate.py`, seeds 1 to 8, one day each, the engine
that stood, omni-v23, against the candidate, omni-v24): no LOSS against omni-v23 in any model. Eleven of the twelve models read identical
on every gauge and every seed (the verdict model among them): every model that sets its own beat, and the shipped cloud model (`cluster_shipped`), where both engines
decide every 60 s because the model's nodes are a cloud's machines.

The new on-site model (`onsite_shipped`: each engine at its own default beat on the kind rig's own machines, no cluster autoscaler, the
5 s plant) is the preregistered reading of the pick on the untouched seeds (amendment 4: omni-v23 at its shipped 60 s against the
pick; the same seeds, plant and beats as `--pace-periods 60,10`). omni-v24 at its 10 s against omni-v23 at its 60 s:

- the minutes over the response line down 60.7%, from 7.0 to 2.8 a day (fewer, GAIN);
- the 95th percentile response down 8.2%, from 61.0 to 56.0 ms (faster, GAIN);
- the pod autoscaler short of its target down 5.1% (GAIN);
- the power-cap request's moves down 53.3% and its reversals down 58.5% (GAIN);
- the machine-hours identical; no pod waited for a place in either engine; no error, no held reading, and no trial abandoned
  (omni-v23 abandoned 6).

Against native on site, omni-v24: the minutes over the line down 89.8%, the 95th percentile down 29.7%, the autoscaler's shortfall
down 10.4% (GAIN), the machines the same. What it costs: the governor reads the cluster 6,079 times an hour where omni-v23 read 2,131,
and its own processor works 10.7 s an hour where it worked 1.3 s (power given).

The rows that read LOSS against native in the cloud and card models (pods waiting for a place, a pod's start wait, the batch's
requests and minutes over the line, the card's 95th percentile) are omni-v23's own, identical seed for seed on omni-v24: the beat
does not reach them. Each stays on the next version's list with its cause (`docs/CHANGE_CONTROL.md`).

## The tests

`tests/test_pace_clocks.py`, `test_the_factory_beat_is_the_places`: a cluster of kind nodes gets 10 s; nodes of Azure, Google
and Amazon get 60 s; nodes with no providerID get 10 s; a reading that fails, or finds no node, gets 60 s; a beat set by hand
is kept; the install files set no beat. `tests/test_cloud_cadence.py`: every cloud rig's beat is 60 s. The unit-test suite, the
function tests and the release check pass on the tree; no C++ twin changes (the Kubernetes governor has none).

## What changes in the rigs and the install files, not the engine

- The kind rigs ask the engine for the beat (`scripts/kind_bench.sh`, `kind_full.sh`, `kind_pilot.sh`, `pilot_shadow.sh`),
  so a kind run decides every 10 s and a managed cluster's run (Azure) every 60 s; each run writes its beat beside its files
  (`omni_interval.txt`), as every run has since omni-v16. The pace arms of `scripts/kind_paired.sh` still set their own beat;
  the robustness test's second governor reads the first one's beat from the run's own file (`scripts/kind_robust.sh`); the
  levers' mechanism proof keeps the 60 s beat its checks were written at, set by hand (`scripts/kind_levers.sh`).
- The install files set no beat (`deploy/install/omni-compass.yaml`, `omni-compass-cloud.yaml`, `deploy/controller.yaml`), so
  an installed governor reads its own place.
- `tools/model_gate.py`: the model's stand-in nodes carry a providerID as a real cluster's do (a cloud's machine in the cloud
  setting, kind's elsewhere), and the gate reads a new model, `onsite_shipped`: each checkout at its own default beat on site,
  on the 5 s plant.
- `tools/live_reps.py`: a run without its beat file is older than omni-v16 and is read at the 60 s it ran at.

## What is run again

Every benchmark runs again on omni-v24 from 01:30 UTC on 2 November 2026 (`scripts/reruns.txt`, A of every entry, then B, then C; the
conductor's campaign, `scripts/dispatch_grid.py`). The omni-v23 runs started before that moment run to their end as omni-v23's
record; nothing is cancelled. On kind, which is on site, the compass arm decides every 10 s; on Azure, through the cloud, every
60 s, as on omni-v23. The real runs of the pace preregistration (amendment 3's arms) read the factory beat beside the dial's
other beats. The card governor on the chips (`omni_controller/gpu_governor.py`) keeps its own clock and is unchanged.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

# Omni v5 — the engine fingerprint

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

**omni-v5** is a distinct engine, its own tree, no longer read as v3. It is fingerprinted file by file in `OMNI_V5.json`
(`tools/omni_version.py`); `python3 tools/omni_version.py` prints `omni-v5` on this checkout. v1, v2 and v3 stay frozen,
each kept for its own results; no result is ever read across versions.

## The default brain: the max (12 October)

The founder's order of 12 October: "We're going to show a benchmark that shows it to the max. And we're going to show
one native... anybody can tune it from the max down." v5's default (`V5CFG`) is therefore **the max**: every muscle
pushed toward its own limit for the most work, faster, never past its limit and never below native. The energy that
takes is reported as **LOSS**, beside the work and the speed it bought; the max never shaves (nothing is taken
from one muscle to give to another). The dial turns it down: **the tune-down** (`V5SAVE`, the save setting described
below) is native's work on the least energy, kept and tested on every muscle.

- **A pool** gets the machines its forecast needs before the rush lands: the recent peak arrivals widened by the largest
  rise the pool has shown within one machine start, at 95% utilisation, plus any **work waiting in line** cleared within
  one machine start, through a floor under its own autoscaler, never fewer than its **twin** runs (the brain's model of
  native: the same pool under its own autoscaler alone, on the same arrivals). The machines it added and no longer needs
  go back at once (a ceiling at the larger of its need and its twin's count; the autoscaler's own scale-down would hold
  them for its window). Its power cap and admission stay native: full clock, every request admitted.
- **A room** is cooled ahead of the heat as it nears its limit or its cooling nears flat out, never warmer than native.
- **A battery site** clips its line from its charge, native plus: the operator's own reserve while nothing would cross,
  and below it, down to its band's floor, exactly the draw that would cross; a UPS lends only the charge above its outage
  floor.
- **A motion axis alone**, while tasks are waiting, runs at **its own peak speed** (`s_peak`, `realms/presets.py`: the
  head the machine itself has above the everyday profile native runs: a joint's drive and a multirotor's airframe 1.25, a
  road vehicle's drive 1.25, a ship's engine to its maximum continuous rating 1.15), never past it, back to the everyday
  setting at once when its motor passes 80% of its heat rise or its tracking error passes half its line. A reaction
  wheel's saturation, a train's line speed and an elevator's overspeed governor are their limits: those stay native.
  Inside a body an axis keeps its everyday speed (see the bone). Torque (effort) limits stay native: in these models a
  higher one changes nothing.
- **A process loop** native already runs flat out (the full actuator): wired, watched, native.
- **At its limit on native.** Every power limit at full, every admission gate open, a loop's actuator at its full range:
  native already runs these at the top of their range, the max writes nothing, and the tables say so in those words
  (`native_at_limit`).
- **The bone.** Inside an organism the body's lines (each site's grid line, each room's cooling and its degrees to its
  limit) are loaded by the whole body, so the max grants machines and cooling only out of the room the most loaded line
  has left, one decision ahead (its latest reading plus the larger of 3.09 of its own wobbles and the largest single climb
  it has shown, counted on the line without the max's own machines: its own steps are not the line's wobble). A machine
  is started only if the lines can still carry it when it is ready (the climb grown by the square root of its start time:
  one started and then cancelled only burns its start). A site with flexible load waiting gives its catch-up the room
  first. With no room, what the max added goes back, as much as the shortfall needs, the pools with the most extra first
  and the machines started last first, never below a pool's twin. An axis inside a body keeps its everyday speed: at the
  peak hour the organisms run, the bone almost never has room for its worst case, and in the development runs its peak
  gave the body nothing while its changed rhythm crossed neighbours at their own limits.
- **One pedal.** Push for more, lift off for less; lifting hands the setting back toward native. At idle the
  pool lifts all the way to its breathing floor (two machines) and wakes straight to the work. **The lease**: at 80% of
  every modelled run the brain is cut and the plug walks every setting back to native over 24 decisions (no jump the body
  must absorb at once); a floor that only held a pool at its twin's count adds nothing to walk back and is let go at once
  (a walking floor would hold machines native had already released). The security kill switch is instant.
- **Wear** is metered beside the work, never judged: a pool's machine-hours, a room's cooling unit-hours, a battery's kWh
  cycled, an axis's motor heat (degree-hours above ambient), a loop's actuator duty-hours.
- **Three loads**, fixed before the preregistered run (seeds 3000-3009): each organism's own load, **the climb** (the load
  stepping 1 2 3 2 3 4 ..., up to twice its own), and **the line** (`LINE` in `realms/harness.py`: work already waiting
  when the run starts, a quarter of the work the run itself brings; a pool's jobs, an axis's tasks, a site's held-over
  flexible load; a room's heat and a loop's demand cannot wait and have none). Every muscle alone runs its own load and
  the line; the organisms run all three. Speed is judged where there is a line: the arm that clears it sooner is faster.
- **The live controllers** carry the same dial (`--dial max`, the default): the Kubernetes controller holds the service
  well inside its line (the compass at 0.3) and never gives back a machine the cluster had on its own; the GPU compass
  keeps the card's clock ceiling at the top while it serves (the card already runs flat out on its own power limit).

The organisms run the hour around each battery site's daily peak, where the UPS lines carry most of their rating: there
the bone is tight and the max gives only what the lines can carry. Every muscle alone has no body around it, so the max
gives it everything its own limits allow. `results/realms_v5/REALMS_V5.md` shows both, and the climb (the load stepping
1 2 3 2 3 4 ..., up to twice the organism's own) where native breaks first.

## What v5 is

v5 is **a combination of everything**: it takes v3's proven engine (its live controllers, its realms and organisms, its
runners) and adds the **v5 compass law** (`realms/compass_arm_v5.py`) and its arm in the harness (`realms/harness.py`). The
goal is to be equal to or ahead of native and every prior version on every measure, and never behind on any — *do no
harm*.

The v5 muscle catalog (`realms/catalog_v5.csv`) is **1,107 muscles in 70 families** — v3's 945, then a first wave of six
new families of real control points: **Linux Kernel & OS Control** (cgroups, the CFS scheduler, DVFS/cpufreq, transparent
hugepages, the I/O scheduler, NUMA balancing, dirty-ratio writeback, swappiness, TCP buffers, …), **Serverless & Functions
(FaaS)**, **Virtualization & Hypervisor**, **Content Delivery & Edge Cache**, **Gut** (data-plane intake and waste), and
**Skin** (perimeter and admission); then a second wave (12 October) of 95 muscles: five new families, **Financial Markets
& Trading Systems** (matching engines, order gateways, pre-trade risk, market-data fan-out), **Media Streaming & CDN**
(transcoders, packagers, origin shields, player buffers), **Game Servers & Real-Time Interactive** (Agones fleets, tick
rates, matchmaking, relays), **Blockchain & Ledger Nodes** (a node's cache, mempool, peers and validation threads; never a
consensus rule) and **CI/CD & Build Farms** (runner scale sets, build concurrency, caches, test shards), plus additions to
seven families already there: security engines (an intrusion-detection system's capture threads and ring buffer, a web
firewall's inspection workers, a SIEM's ingest), MQTT brokers, DNS and mail caches, ROS 2 executors, humanoids and
manipulators, warehouse robot fleets, PX4 and ArduPilot drones and swarm spacing, and edge sites. The GPU family is named
for the hardware, not one vendor (**GPU Hardware**), and the eight audited families carry numbers (64 to 71) like every
other family. Each is a distinct real-world knob, modelled on the matching plant template, exactly as v3's 945 already
share five templates. A third wave (12 October, night) adds the founder's nine open-source pieces as ten muscles, each in
the spine family its knob belongs to (`docs/THE_SEAT.md`): Kepler's energy reading driving a pool's target (Kubernetes
Workload Scaling), Climatik's inference power cap, Adaptive GPU Power Capping and NVIDIA's platform power budget (GPU
Hardware), EAR's CPU frequency policy and global energy budget and the Kubernetes Power Manager's core profiles (Host CPU &
Memory), CruiseKube's and Goldilocks's request rightsizing (Container Resources) and PEAKS's power-aware placement
(Kubernetes Placement & Scheduling). The organisms on v5: Compute / AI / Cloud 540, Physics / Robotics / Autonomous 404,
Energy / Facility / Industrial 480, Distribution / Specialized 484, the four stacked 1,908, the whole tower 1,107; the spine
all four realms share is 267. (v3's own catalog `realms/catalog.csv` stays 945, frozen for v3's results.)

Two math-only guardrails, and otherwise free arms:

- **The edge** — a per-knob cushion that widens at once when service climbs and narrows slowly when it falls
  (`cushion = climb × reaction + z × wobble`), so nothing riding its own limit falls off.
- **The centre / the hole** — nothing is eased into a pit it cannot climb out of. A cooled zone is eased only by the
  degrees its cooling can still recover (the Lindley reach), and not at all while its cooling headroom is falling toward
  empty faster than the cooling can answer. A process loop's setpoint never sits closer to its band's edge than the
  loop's own largest swing toward that edge (the loop reach, read from the historian's low and high over each decision,
  carried ahead for a slow loop). A serving pool is never capped below the largest jump in demand it has shown (the drop
  floor) nor so far that a burst would push its responses over the line where native's would not (the latency floor).
  And nothing permanent: a machine handed back to a cloud is the cluster autoscaler's own decision, because the
  autoscaler shrinks from wherever it is left, so an early hand-back would leave the pool a machine short of native for
  good; and a motion axis is slowed only while the wake forecast over a whole deadline (the most that can arrive in one
  deadline at the recent peak rate) still finishes inside that deadline at the slowed speed, so a delay is always
  recovered before a later rush could make it permanent. When work comes, every muscle wakes straight to the level the
  work needs (the founder's rule: from idle straight to 99, never past 100).

Every other knob is free to move both ways inside its physical cover, generating units included (a unit's steam,
speed or gate loop eased inside its band serves the same load with less effort), and **a knob stays native only where its
own physics says moving it cannot help without harm**: an interactive pool's power cap (its response line is shorter
than one decision, so a cap's one decision of slower service cannot be seen and undone inside the line; the metered GPU,
class P, is where that cap is proven), a battery's peak-shave (round-trip energy bought for service), and a cloud pool's
machine hand-back. A batch queue's, a training job's or a terminal's power cap is free under the drop and latency floors.

**Amendment, 12 October.** The first v5 table (commit `c0e80a852`, the whole tower +0.0%) ran an engine that held every
generating unit's loop, every power cap and every inverter native by blanket gates. The gate on generating units alone
threw away almost all of what v5 saves: on the tower, 1.09% with it off against 0.04% with it on, on development seeds.
v5 was re-declared with the gates replaced by the physics floors above, developed on seeds 7100-7209 only, and the
preregistered seeds 3000-3009 were run again unchanged.

**Amendment 2, 12 October.** The catalog's second wave (95 muscles, five new families and additions to seven) took it to
1,097 muscles in 70 families; the engine's law is unchanged, its fingerprint re-declared because the catalog is part of
it. Developed on seeds 7100-7109 only (0 of 1,097 LOSS or power given, all six organisms superior); the preregistered seeds 3000-3009
were run again unchanged on commit `04d9eb3b3`, with the same savings on the whole tower, the four stacked and Energy /
Facility (3.0 times v3's).

**Amendment 3, 12 October (night): the living body.** The founder's order of 12 October: "whatever one muscle is having
a problem, the other muscles kick in ... the brain and nervous system to activate its immune system ... nothing can be
locked." The engine now carries, as properties of the code (`docs/FORMAL_V5.md`, section 4): a native twin of every room
(the brain's sense of the temperature native would leave it at, exact by construction), the room's own knob curing it
where it can and the body's heat debt handing back the max's machines where it cannot (V8, V11), every battery's charge
counted as room only while it lasts and its discharge timed for its line (V6, V12), no machine taken from a queue that
needs it (V7), a pull-down handed back gradually and granted only where it can be held (V9, V10), and every forecast
starting at the plant's first reading (V13: a lock that kept every battery's timed discharge shut for the whole run, and
a room twin that started wrong, both removed). The catalog's third wave took it to 1,107 muscles. Developed on seeds
7100-7199 only: under the climb, plants with less work or more misses inside the four realms fell from 19 to 0 in 400 organism runs while the
misses fell about twice as far as before; on seeds 7100-7109 every muscle alone and the six organisms on all three loads
showed 0 muscles and 0 plants with less work or more misses. Fingerprint re-declared (digest `9be48445438943c2`); the preregistered seeds
3000-3009 were run again unchanged.

**Amendment 4, 13 October: every muscle its own card.** The founder's question of 12 October, night: does every muscle
have its own tuning, maxed to its own benefit, instead of one global setting for a thousand muscles? The brain stays one;
its settings are now each muscle's own (`docs/FORMAL_V5.md`, section 5). A muscle's card (`realms/muscle_cards_v5.csv`)
holds what the max uses for it: a machine pool's edge utilisation and window, a battery's line margin and, wired by its
power, its hold window and hold margin. The cards were found by an automatic search over every muscle whose settings can
change what the max does (`tools/tune_cards.py`), on development seeds only, today's global setting always one of the
choices, and kept only where the card beat the global setting beyond the noise on seeds 7100-7109 and again on seeds
7200-7209 and never behind native on any of their seeds under any load (never over its line more often, never less
work, never its line cleared later): 364 muscles (333 machine pools, 31 batteries); every other muscle runs the global
setting. Inside a body, a battery wired by its power keeps the body's margins on its line (V14: its card was
chosen alone; the line carries the whole body's swing). In development, 360 organism runs on the two sets: 0 plants with less
work or more misses, the misses removed 1.7 times the global setting's. Fingerprint re-declared (digest `5648f2902f1fae68`, 44 files,
the cards among them); the preregistered seeds were run again unchanged. Every card is printed in plain words in the
muscle catalog (`docs/MUSCLE_CATALOG.md`).

**Amendment 5, 13 October (evening): every muscle from 1 up to one click under its own capacity, read live.** The
founder's order of 13 October: "you can write it in code ... to show one, two, whatever a muscle's capacity is able to
handle, guardrailed and skimmed on its border, one click down probably, so it never goes beyond. And, of course, can all
scale right back down. It can never go be less than one." No top or floor in the live controllers is a number written
down for a muscle any more; each muscle reads its own from the system it runs on:

- **Machines** (the Kubernetes controller): the top is the operator's own `--max-nodes` where given; else every ready
  worker plus what the cluster's own autoscaler may still add (its published status); where Omni-Compass resizes the
  pool with the operator's own command and no autoscaler reports, there is no top but the one the pool shows: one under
  the first count it refuses, read from the command's own refusal. Before: a fixed 1,000. The floor stays the founder's
  two machines, and cruise climbs toward the top one step a decision.
- **Replicas** (the replica room): at the autoscaler's cap with the compass pressing, the cap rises to the replicas the
  autoscaler's own arithmetic asks for, never past what the machines can hold of the service's pods, one pod under it,
  read live (the allocatable CPU of every ready worker and of the machines the system can still add, less what every
  other pod asks for); where every node is a container on one machine (kind), each reports the whole machine's CPU as its
  own, so that machine's CPU counts once (on 4 October the room raised to 30 on kind served no more requests and ran 78%
  more pods, `results/live/REPLICA_ROOM.md`: the cap was never kind's limit, the machine was); `--replica-ceiling N` is
  the operator's own; 0 keeps the cap unmoved. Before: off unless the operator gave a number.
- **The power cap at the max is never set under native**: each machine's idle CPU goes to the capped service's pods
  (one click under the machine: its last 5% is never handed out, and no pod gets less than its operator gave it), and the
  frequency ceiling and the GPU limit stay at their top. Before: the governor's trim to demand could set the pods' CPU
  limit and the frequency ceiling as low as 69.5% even at the max (never on the sets with a response-time probe, where the
  muscle already conveyed). The tune-down trims as before, with no fixed floor: the pod's own request and its use plus
  headroom (before: a fixed 65%), and the card's own minimum power limit, read live.
- **GPU**: the clock ceiling's floor is the card's own lowest supported clock (before: 35% of the top); one degree under
  the card's own slowdown temperature reads as full heat where the card reports it (before: a fixed 83 C for every card).
- **Batch**: held work is admitted while load and power stress are under the compass's wall less one cushion
  (0.95 - 0.05 = 0.90, the nervous system's own admit gate; before: load 0.80).
- **The nervous system's site power envelope** is the living band of the device's own range, [0.05, 0.95] (before:
  [0.65, 0.95]); the C++ twin the same, re-proven equal value for value and re-sealed.
- **Words**: the engine's own files say which way a number went (the founder's order of 13 October); the older result
  label "WORSE" is "AWAY FROM ITS AIM", the GPU benchmark's own.

The modelled organisms are unchanged: their code differs only in comments, file headers and that one label's name, so
the 1,107 muscles, the cards and the max give the same numbers on the same seeds. The test rig with the real cluster
inside changes beside the engine (protocol 3, `docs/K8S_COMPASS_PREREGISTRATION.md`): the model of the organism on the
runner's last core and the kind nodes on the others, and the window set from the heavier arm's measured step.
Fingerprint re-declared (digest `6093b2b88aa911b9`, 44 files); the mechanism identity's actuator part re-recorded (the
core, the law, the observation map, the governor, the time step and the shield unchanged); every result runs again on it.

## The no-harm proof (modelled, class S)

On a fixed seed, for **every** muscle in the catalog, the v5 default does no less work than native, is over its line no
more often, and hands every knob back to native on the kill (the dead-man lease); the energy it takes is power given,
shown beside the work and the speed it bought. On the preregistered seeds 3000-3009 (commit `eea291501848`, digest
`5648f2902f1fae68`, every muscle its own card): **0 of 1,107 muscles LOSS or power given or mixed** (527 toward their aims, 421 at their limit on
native, 159 the same), every organism ahead of native under all three loads, and **not one plant with less work or more misses inside any
organism under any load**; the misses fall 1.9% to 7.5% under each organism's own load, 1.4% to 7.2% under the climb and
1.1% to 8.3% with work waiting in line, against 1.6% to 6.4%, 0.9% to 3.5% and 1.0% to 7.2% with one global setting
(digest `9be48445438943c2`), with less power given and less wear. This is checked in `tests/test_compass_arm_v5.py` and run in full by
`tools/run_realms_v5.py` (`results/realms_v5/`). Models are class S: a model's energy is not a meter's, and a plant written
by the same people who wrote the law is not an independent test.

## In development

While v5 is in active development its fingerprint is **re-declared on each engine change** (`python3 tools/omni_version.py
--write v5`), and **no v5 result is published** until the v5 freeze. At the freeze, every benchmark is rerun on v5, A/B/C,
the founder hears each result before it goes up, and the fingerprint is final.

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

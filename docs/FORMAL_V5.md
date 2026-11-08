# The max, formally: definitions, what the code guarantees, and what the runs measure

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

This page states the engine's default brain, the max (`realms/compass_arm_v5.py`, `V5CFG`, engine omni-v5 by
`tools/omni_version.py`), in definitions and properties. Each property carries its class: **V** a property of the code,
proved by reading the code path named beside it and checked by the runs; **S** measured on our own models; **L**
measured on real software; **P** measured by a physical meter. A V property is a statement about what the governor
writes; it is not a statement that a measured outcome follows. Measured outcomes are stated with their numbers and their
limits, and nothing on this page is claimed beyond them. The earlier formal results (`docs/TRACKING_THEOREM.md`,
`docs/FORMAL_STATUS.md`) belong to the earlier core engine's channels and are not restated here.

## 1. Setting

A **body** is a set of plants p₁, ..., pₙ run on one clock of decisions k = 0, 1, 2, ... (15 s each in the
organisms). Each plant i has

- a template τᵢ (compute_pool, thermal_zone, energy_storage, motion_axis, process_loop: `realms/plants.py`),
- one knob κᵢ (capacity, setpoint, power or admission: the muscle's single wire),
- a **native controller** Nᵢ, the plant's own law, unchanged by Omni-Compass: the pod autoscaler or the cluster
  autoscaler of a pool, the PI loop and staging of a cooled room, the dispatch of a battery site, the servo profile of
  an axis, the PI loop of a process,
- a state xᵢ,ₖ and an exogenous input wᵢ,ₖ (arrivals, heat from its own load, the site's own load, disturbance),
  drawn from the plant's seed, the same in every arm.

The plants are coupled through the body (`realms/harness.py`, `Body.couple`): with Sₖ the body's source power (every
plant that is neither a room nor a battery site) and Zₖ the rooms' power, room z receives heat h[z] · Sₖ₋₁ and battery
site s receives load gₛ · (Sₖ₋₁ + Zₖ₋₁ − its nominal), where h[z] and gₛ are fixed by the body's calibration.

An **override** oᵢ,ₖ is a set of key-value pairs that bounds what Nᵢ may do at decision k: a floor and a cap on the
machines a pool's autoscaler may ask for, a setpoint for a room's loop, a reserve or a defended ceiling for a battery's
dispatch, a speed scale for an axis. The plant then steps by its own law under that bound:
xᵢ,ₖ₊₁ = fᵢ(xᵢ,ₖ, Nᵢ(xᵢ,ₖ; oᵢ,ₖ), wᵢ,ₖ, coupling_k). The empty override leaves Nᵢ exactly as shipped.

**Definition 1 (the two arms).** The native arm writes oᵢ,ₖ = ∅ for every i and k. The Omni arm writes
oₖ = G(y₀, ..., yₖ) for k < K, where yₖ is what the governor reads at decision k and K is the decision at which the
governor goes silent (in every run, K = 0.8 × the run's decisions), and the lease's walk back after K (Property V5).
Both arms run the same plants, the same seeds and the same inputs.

**Definition 2 (a governor, and a collection of tools).** A rule G is a **collection of separate tools** if there are
maps g₁, ..., gₙ with oᵢ,ₖ = gᵢ(yᵢ,₀, ..., yᵢ,ₖ) for every i and k: each muscle's bound depends on that
muscle's readings alone. G is **one governor over the body** if for some plant i the bound oᵢ,ₖ depends on the
readings of another plant j ≠ i.

**Definition 3 (a twin).** The twin Tᵢ of a plant i is the same plant model, built from the same row and seed, fed the
same exogenous input, run under Nᵢ alone with no override. The pools' twins run inside the governor
(`Bone.__init__`, `Bone.advance_twin`); a twin is the governor's model of what native does with that plant.

**Definition 4 (room on a line).** The lines of a body are the battery sites' connections and the rooms' cooling. For a
line ℓ with distance to its limit gap_ℓ (the connection's limit plus what its battery can still clip, less its import;
or a room's cooling capacity less its command, and its degrees in hand), one-decision climb up_ℓ (the larger of line_z
times its step-to-step spread, the largest climb it has shown, and a prior of 5% of the line) and load per W of the
body's power a_ℓ, the room over r decisions is

  R(r) = min over ℓ of (gap_ℓ − √r · up_ℓ) / a_ℓ   (`Bone.room`, `Bone.room_for`),

the power the body may still add, read r decisions ahead.

## 2. What the code guarantees (class V)

**Proposition 1 (V). The max is one governor over the body.** In `max_body_step`, the floor written on a pool is
max(now + can, base), where can is the number of machines whose idle power fits in min(R(1), R(r) − used); R reads
every battery site and every room of the body, and `used` is what was granted to the pools decided before it in the
same decision. So the bound on one pool depends on the readings of the body's sites, rooms and other pools: by
Definition 2, the max is one governor, not a collection of tools. No set of separate tools has this property, however
many run at once. ∎

**Property V1 (one wire).** Every override the max writes uses only its muscle's own key: {floor, cap} on a pool wired
by capacity or setpoint; {setpoint} on a room wired by its setpoint; {setpoint} or {capacity} on a battery site wired by
that knob; {capacity} on an axis alone (inside a body an axis keeps its everyday speed); nothing on any other muscle.
Proof: every branch of `max_apply`, `max_hold` and `max_body_step` writes only these keys. ∎

**Property V2 (never fewer machines than native asks for).** For every pool i with a twin, at every decision k < K, the
count its autoscaler is asked for is never below the twin's: a floor written is ≥ m(Tᵢ,ₖ), and a cap written is
≥ max(m(Tᵢ,ₖ), n[min]), where m counts machines in service and starting. Proof: `max_ask` sets base = m(Tᵢ,ₖ) and
want = max(forecast, base); `max_body_step` writes floor = max(now + can, base), and on a shortfall keep ≥ base. The
pool's own law is a function of its own arrivals and settings only, so its twin runs exactly as the native arm's pool
does: m(Tᵢ,ₖ) is the count native asks for at that decision. ∎

**Property V3 (native at its limit is left alone).** Under the max, the override of every muscle wired by power or
admission, of every process loop, and of every axis whose machine has no speed above its everyday setting is empty at
every decision: native already runs them at the top of their range. Proof: `max_ask` returns nothing for them and
`max_body_step` writes ∅. ∎

**Property V4 (grants come out of the room the lines have).** At a decision with R(1) ≥ 0, the idle power of the
machines the max adds, summed over the body, is at most R(1), and the machines of a pool that take r decisions to start
are granted only out of R(r) less what was already granted. With R(1) < 0, what the max added goes back, the pools
holding the most first, never below each pool's twin (V2), and no room is pulled below its operator's setpoint. Proof:
`_units`, the running decrements of r[src], r[all] and used, and the shortfall branch of `max_body_step`. ∎
*Limit, stated with it:* R is a forecast. A line that climbs further within one decision than any climb it has shown,
while power granted earlier is still in service (power is handed back one decision after a line shows the need), can
still be carried over its limit. Section 4 gives how often that happened.

**Property V5 (the lease: everything handed back).** If the governor goes silent at decision K, every override moves
1/(K + W − k) of the way to its native value at each decision k ≥ K and is native from decision K + W − 1, W = 24
(`walk_back`; a floor that only held a pool at native's own count is let go at once). Every run checks every knob on
every seed (`restore_ok`); a muscle or organism that fails is labelled INVALID. In the official table every muscle and
every organism passed. ∎

**Property V6 (the live ranges: from 1 up to one click under the system's own capacity; amendment 5).** In the live
Kubernetes controller, with n the machines in service, m the floor (two), T the machine lever's top and P the ready
workers: T is the operator's `--max-nodes` where given; else P plus the room the cluster's own autoscaler publishes
(the sum over node groups of maxSize less registered); else, where Omni-Compass resizes the pool with the operator's
command, T = f − 1 for the smallest count f the pool's command has refused, and T = ∞ before any refusal; else T = P.
Every machine count written lies in [m, T], moves at most the rate limit a decision (shield I5), and cruise writes
min(T, n + step). The replica cap c of a sensed service never exceeds C = max(1, ⌊(A − Q)/r⌋ − 1), A the allocatable CPU
of the ready workers and of the machines the system can still add (by T), or, where every node is a container on one
machine (kind), that machine's CPU once; Q the requests of every other pod and r one pod's request: one pod under what
the machines hold. At the max, every pod CPU limit written is ≥ the operator's own,
and no frequency ceiling or GPU limit is written below its top; on the tune-down, a CPU limit is never written under the
pod's request nor its use × (1 + headroom), and a GPU limit never under the card's own minimum. Proof:
`Controller._machine_room`, `_max_nodes`, `_pool_command`, `_live_ceiling`, `Muscles.push`, `_power_cap`, `_hardware`
and `convey` (`omni_controller/`); `tests/test_compass_controller.py`, `tests/test_omni_controller.py`,
`tests/test_muscles.py`. ∎ *Limit, stated with it:* T = ∞ refuses no count in advance: machines are still added only by
the controller's own rules (the scheduling floor while pods wait for a place, one more past the compass's wall, the
governor's law, cruise while a queue waits), within the rate limit; the first refusal by the pool, or by the cloud's
quota behind it, sets the top from then on.

**Definition 5 (the readings).** For each seed s, the paired difference is dₛ = Omni_s / native_s − 1 for work and
energy, and Omni_s − native_s (percentage points) for the share of decisions over the line. Over n seeds, the 95%
interval is mean ± t[0.975, n−1] · sd / √n. A gain or a loss is a row whose interval is clear of zero; otherwise the
row reads no difference beyond the noise. Across runs A, B and C: the same sign in all three with every interval clear
of zero reads "lower (or higher) in all three of our runs"; an interval across zero reads "no difference beyond the
noise"; clear intervals of opposite signs read "the runs disagree" (`tools/readings.py`, `tools/confirm_abc.py`).

## 3. What the runs measure (classes S, L, P)

- **S, the muscles alone, 1,107 muscles, preregistered seeds 3000-3009, both loads** (omni-v5's run, commit
  `eea291501848`, digest `5648f2902f1fae68`, every muscle its own card, section 5; its record is `docs/OMNI_V5.md`, the no-harm
  proof): 527 GAIN, 421 STEADY at their limit on native (V3: the max writes nothing), 159 STEADY, no difference beyond the
  noise, **0 LOSS or power given, 0 mixed**. `results/realms_v5/REALMS_V5.md` now holds the run on omni-v8 of 17 October,
  read again by the one key on 24 October: 530 GAIN, 421 at their limit on native, 156 STEADY, the same as native, 0 LOSS.
- **S, inside the organisms, the same seeds, three loads**: every organism with fewer misses as a whole under every load, and
  **0 plants with less work or more misses** in every organism under every load (0 of the 1,908 in the four stacked). Misses (the share of
  plant decisions over their line) fall 1.9% to 7.5% under each organism's own load, 1.4% to 7.2% under the climb (the
  load stepping 1 2 3 2 3 4 ... to twice its own) and 1.1% to 8.3% with work waiting in line, against 1.6% to 6.4%,
  0.9% to 3.5% and 1.0% to 7.2% with one global setting for every muscle (digest `9be48445`, the same seeds), and the
  power given and the wear fall with them (`docs/OMNI_V5.md`; on the omni-v8 run, an engine that no longer stands (omni-v26 stands), Compute under its own load
  takes 0.01% more energy than native and 0.06% more wear, power given). Every row of that run is reported in
  `results/realms_v5/REALMS_V5.md`.
- **L, real software**: `docs/THE_RECEIPTS.md`, receipt by receipt.
- **P, a physical meter on a real chip**: the card's own meter on the Lambda runs (`results/gpu/`); on one A10 on omni-v23
  the energy for each request served fell 0.8% to 1.8%, less energy for the same work, GAIN in all three of our runs
  (`results/gpu/V23_A10_CAP_FULL_ABC.md`).

## 4. The living body: why plants read LOSS, and the version that cures them (the engine since 12 October, night)

Found on development seeds only (7100-7299), never on the preregistered ones. Under the climb, rooms and UPS lines
reach their limits in both arms; a plant read LOSS when the Omni arm reached a limit a moment sooner, or when a sense
the brain read was wrong. Each cause, and the property of the code that removes it:

1. **A room snapped back.** A room cooled ahead of the heat, then returned at once to its operator's setpoint when the
   lines ran short: its own PI loop overshot warm of native, and once its cooling ran flat out the difference was frozen
   in. *V9 (the pedal lifted, never snapped):* a pull-down is handed back toward the operator's setpoint over the
   cooling's own reaction time. *V10 (no pull-down that cannot be held):* a new pull-down is granted only out of the room
   the lines have for that reaction time.
2. **A battery's charge counted as room after it ran out.** *V6:* a site whose battery covers its draw, but whose charge
   above its floor runs out within r + 1 + T decisions (T = 2: the heat of machines handed back reaches the rooms a
   decision later and their cooling answers over its own averaging, one more), has as room on its line only its limit
   less its whole draw, read at the draw's own climb.
3. **Machines handed back while a queue needed them.** *V7:* on a shortfall, a pool is never held below
   ⌈(λₖ₋₁ + Qₖ / Δt) / μ⌉.
4. **A room left warmer than native.** *V8:* every room has a twin: the same room under its operator's settings, warmed
   by native's heat (the body's source power with each pool's power replaced by its twin's). A room wired by its
   setpoint that reads warmer than its twin by e > 0 has its setpoint written at most t[set] − e, unless its cooling is
   already flat out.
5. **A room that cannot cure itself.** *V11 (the body cures what a muscle cannot):* a room wired by its cooling units,
   a power or an admission gate, or whose cooling is flat out, and that reads warmer than its twin by e > 0, puts a heat
   debt e · C / (Δt · h) on the body (C its heat capacity, h its share of the body's source heat); the room the bone
   grants is bounded by minus that debt, so the machines the max added go back until no such room is warmer than
   native's.
6. **A battery that never timed its discharge.** *V12:* a battery wired by its power holds its charge while its line has
   room after the largest climb it has shown, line_z of its wobbles and a twentieth of its limit, and gives native's full
   power once the line could need it; it holds nothing until it has read its line for a window of decisions (20).
7. **A lock in the senses.** *V13 (a forecast starts at the first reading):* a plant shows its initial values before its
   first step; the jump from them to the first reading was taken as the line's largest climb ("never forgotten") and
   kept every battery's timed discharge shut for the whole run. Every forecast of a line now starts at the plant's first
   real reading, and the bone reads nothing before the body's first step.
8. **A twin that started wrong.** The body reads its sources at their nominal power before the first step; the room twins
   read zero, so for the first ten or so decisions they ran up to 0.3 °C apart from native's rooms and the body cured
   differences that did not exist. The twins now start from the body's own reading (V8, the definition above), and with
   the max writing nothing every room twin equals its room to the last digit, every decision
   (`tests/test_compass_arm_v5.py`).

The battery's admission gate stays native: deferring a site's flexible load to keep its line clear left part of that
work not caught up by the end of a run (work first).

Measured on development seeds 7100-7199, the four realms under the climb, 400 organism runs each way:

| | Plants with less work or more misses | Misses (pp), the four realms | Work, the four realms |
|---|---:|---|---|
| the engine before (omni-v5, 8d4f91f0) | 19 | −0.109, −0.125, −0.005, −0.144 | +0.0013%, +0.0016%, +0.0000%, +0.0022% |
| V6-V10 only | 7 | −0.104, −0.110, −0.005, −0.137 | kept |
| **this version (V6-V13)** | **0** | **−0.206, −0.187, −0.143, −0.212** | +0.0008%, +0.0010%, +0.0000%, +0.0016% |

The misses fall about twice as far as before (in the Energy / Facility / Industrial body, from almost nothing to 0.14
points), and no plant in any of the 400 runs did behind native. The work gained is about two thirds of the version
before: the heat debt hands back machines while a room that cannot cure itself is warmer than native's.

One lock is left, said plainly: a line that once jumped (a battery that stopped covering its site) is read as able to
jump that far again for the rest of the run, which keeps the max from adding machines on that line. Removing it (every
line's climb read on the site's whole draw) roughly triples the misses removed on the same seeds (−0.34 points), but in
36 of the 400 runs a machine pool whose queue sat at its limit then did more work and took one decision longer to clear
it, which our decision count reads as LOSS. That is the next version's work, and it enters the engine only as a new
version, every result run again on it, the founder told first.

## 5. Every muscle its own card (the engine since 13 October)

The founder's question of 12 October, night: does every muscle have its own tuning, maxed to its own benefit, instead of
one global setting for a thousand muscles? It does, and the engine now carries it.

**Definition 6 (a card).** For muscle i, a card θᵢ is the brain's settings for that muscle: for a machine pool, its edge
utilisation uᵢ (how full it runs on its forecast before it calls for more) and its window wᵢ (decisions of history it
reads); for a battery, its line margin zᵢ (wobbles kept under its line) and, wired by its power, its hold window and
hold margin. The brain is one (the same law, the same bone, the same body); only these numbers differ by muscle. A muscle
without a card runs the global setting θ₀ (u = 0.95, w = 20, z = 3.09, the hold window equal to w, a hold margin of a
twentieth of the line). The tune-down never reads cards.

**The search (development seeds only, `tools/tune_cards.py`).** Every muscle whose settings can change what the max does
(458 machine pools, 44 batteries, 48 axes) tries every candidate in a declared grid on seeds 7100-7109, alone, under its
own load and with work waiting in line; θ₀ is always among the candidates. Pools: u ∈ {0.70, 0.75, ..., 0.95} × w ∈
{10, 20, 40, 60}; batteries wired by their power: z ∈ {0, 0.5, 1, 2, 3.09} × hold window ∈ {3, 5, 10, 20} × hold margin
∈ {0, 0.02, 0.05, 0.10}; other batteries: z ∈ {0, 0.25, ..., 4}; axes: heat head × strain. A candidate is kept if it
beats θ₀ beyond the noise on those seeds (fewer misses, more work or faster: a 95% interval of the paired difference clear
of zero), read LOSS than θ₀ nowhere, and is never behind native: on no seed and under no load over its line
more often than native, doing less work or clearing its line later (the engine's own no-harm tests, seed by seed); among
those, the fewest misses, then the most work, the fastest, the least energy. It is then run again against θ₀ on seeds 7200-7209 and enters the engine only
if it wins there too: a card must win twice. The preregistered seeds 3000-3009 are never read by the search.

**V14 (the body has the last word on a line it shares).** Inside a body, a battery wired by its power keeps the body's
margins on its line: its z and its hold margin are never slimmer than θ₀'s; its own window stays. A card is chosen for
the muscle alone, and a battery's line inside a body carries the whole body's swing, which the battery alone never saw:
the one plant behind native that the cards produced in development (a rack's power allocation, one extra decision
over its line in the whole tower with work waiting, one seed of ten) was exactly that case, and V14 removes it.

What the search found: 409 of the 550 searched muscles beat θ₀ on the first seeds; 364 won again on the second (45 fell
back to the global setting, none LOSS); the engine's cards are those 364 (`realms/muscle_cards_v5.csv`: 333 machine
pools, 31 batteries). No axis setting beat the global one. A first set of cards was chosen by the mean over the seeds
alone (371 cards); the engine's own no-harm test then caught one of them (an electrolyzer battery, one decision over its
line on one seed), and the rule became the seed-by-seed one above. The cards are the ones it chose. A room alone and a process loop alone have nothing for a card
to fix (native almost never misses there), and the 421 knobs native already runs at their limit have nothing above native
to give: their help comes from the body. Every card is printed in plain words in the muscle catalog
(`docs/MUSCLE_CATALOG.md`).

Inside the six organisms, on both development sets (360 organism runs, every plant against native): 0 plants with less work or more misses, and
the misses removed against native 1.7 times the global setting's over the three loads (1.2 times under each organism's
own load, about 1.9 under the climb, 1.7 to 1.8 with work waiting in line):

| Seeds | Own load: global → cards | The climb: global → cards | Work in line: global → cards | Plants with less work or more misses |
|---|---|---|---|---:|
| 7100-7109 (the cards chosen here) | 0.078 → 0.094 points | 0.153 → 0.293 points | 0.088 → 0.161 points | 0 |
| 7200-7209 (the cards checked here, on untouched seeds) | 0.074 → 0.087 points | 0.145 → 0.282 points | 0.086 → 0.149 points | 0 |

Work is unchanged within a millionth, and the power given is lower than the global setting's in the organisms where it
moves at all (Compute under its own load, from 0.058% to 0.011% more energy than native's). The preregistered result, on seeds the search never read,
is section 3.

## 6. Limits, stated plainly

- A card is chosen for its muscle alone. Inside a body the bone shares the lines and V14 keeps a battery wired by its
  power to the body's margins; the organisms were checked with every card on both development sets (0 plants with less work or more misses)
  and on the preregistered seeds (section 3), but a card is not tuned for the body it sits in.
- Many machine pools chose the most aggressive edge the search offered (256 of 333 cards at 0.70): their own limit may
  lie further out. Searching further is the next version's work, a new version with every result run again.
- V properties bound what the governor writes. They do not by themselves bound an outcome on a line the governor does
  not control (section 4).
- R is a forecast (V4). A climb no line has shown before can beat it within the one decision power takes to be handed
  back.
- S results are our models. They are never presented as proof of a physical saving; the physical receipt is a P run.
- The twin is exact for a pool (its law reads only its own inputs) and for a room (its heat is the body's own source
  reading with each pool's power replaced by its twin's, so with the max writing nothing it equals the room to the last
  digit); with the max writing, a room twin is native's room under native's heat as the brain reconstructs it, not a
  meter.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

# The room: every muscle's band, native's point in it, and what Omni-Compass may take

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The founder's law of 23 October 2026, in his words: "if a muscle doesn't gain any benefit with OmniCompass in it and in
actuality has negative when everything else is a benefit, then that simply means that muscle is at its fullest limit";
native "just means not doing anything on there, and there can be no reason that anything native can be better than the
mathematics and physics of OmniCompass in it, unless it is because the muscle itself has its own limitations". This page
writes that law as the theory and the mathematics the engine is held to, names what the catalog already reads by it, and
sets the order of the work it calls for: the theory first, then the tuning, then the muscles Omni-Compass builds itself.
Words and mathematics only; no code changes here. Run and scored by The Omni-Compass LLC's own code. No outside party has
reviewed or approved these results.

## 1. The band, native's point, the room

A muscle is one setting on one machine that already has its own control (`docs/MUSCLE_CATALOG.md`). Its lever moves in a
band, the **cover**, from lo to hi: the device's or the buyer's lowest and highest setting, outside which nothing is written
(`omnicompass/compass_law.py`, `Plug`). Native holds the lever at one point in it, xₙ, by its own rule.

  the room upward    rᵤ = hi − xₙ
  the room downward  r_d = xₙ − lo
  the room           r = rᵤ + r_d, and r = 0 exactly when the band is one point

Omni-Compass acts on the lever only inside the cover, so every write x satisfies lo ≤ x ≤ hi, and every change it can make
is bounded by the room: |x − xₙ| ≤ max(rᵤ, r_d).

## 2. What the room is worth

Let g be the organism's gauge the muscle moves (work done, time waited, energy spent), read against native as the key
reads it (`tools/readings.py`): a rise in work is GAIN, a fall in waiting is GAIN, a fall in a resource spent is a cut and a
rise is power given. Let g(x) be the gauge at lever x with everything else the same. The **worth of the room** is the most
the gauge can move inside the cover:

  Wᵤ = sup { g(x) − g(xₙ) : xₙ ≤ x ≤ hi },  W_d = sup { g(x) − g(xₙ) : lo ≤ x ≤ xₙ }

in the gauge's own direction of aim. Two statements follow from the definitions alone:

1. **The gain on a muscle is bounded by the worth of its room.** Whatever law Omni-Compass runs, its reading on that gauge
   satisfies Δg ≤ max(Wᵤ, W_d). A muscle with r = 0 has W = 0 and can only read STEADY. The catalog's own word for it is
   **at its limit on native**: native already runs the knob at the top of its range, Omni-Compass reads it and leaves it.
2. **A LOSS on a muscle is never the muscle's.** With the lever inside the cover and the law pulling the reading toward
   the band's centre with a bounded force, the gauge can fall below native in only two ways: the lever was pushed **past**
   a limit the law was not wired to (a wall the sense never saw), or the wire reads or writes wrong (a sense that is blind
   or late, a write the device did not take, a read-back that lies). Both are the wiring's, and both are the brain's,
   nerves' and immune system's to catch, because they are wired to every muscle's limit. A LOSS is therefore always a
   fault to find in the wiring and fix in the next version (`docs/CHANGE_CONTROL.md`), never a number to live with.

## 3. The three readings a muscle can give, by this law

| reading | what it says about the room | what Omni-Compass does |
|---|---|---|
| **GAIN** | r > 0 and the law took some of its worth | holds it; the next version asks whether more of the worth is reachable |
| **STEADY, at its limit on native** | r = 0: native is at the wall of the band | reads the knob and leaves it native; nothing can be gained here by any law |
| **STEADY, the same as native** | r > 0 but the law took none of its worth | the room exists and is not taken: this is the room to reverse-engineer (section 5) |
| **LOSS** | a limit was crossed or a wire is wrong | root-caused and fixed, through the model gate, as the next version; never carried |

## 4. What the catalog reads today, by this law

The realms result on the engine that stands (`results/realms_v5/REALMS_V5.md`, our own models, class S, every muscle
under its own load and the line), all 1,107 muscles:

| reading | muscles |
|---|---:|
| GAIN | 527 |
| STEADY, at its limit on native | 421 |
| STEADY, the same as native | 159 |
| LOSS | 0 |

So 421 muscles have no room by construction (admission knobs native already opens fully, power limits native already runs at
full, and the like: `docs/MUSCLE_CATALOG.md`, the aims), and 159 have room the engine does not yet take. The 159 are the
first work of section 5.

## 5. The order of the work this law calls for

1. **The room of every family, written.** For each of the 70 families: the band (lo, hi) and where it comes from (the
   device, the vendor's documents, the operator); native's point xₙ and the rule that puts it there; rᵤ and r_d; the gauge
   g the muscle moves; the worth Wᵤ and W_d read from the family's own model or its live receipts; and, for each wall,
   whether the wall is the **design** (a vendor's default, a published cap, a protocol's rule: movable by a muscle of our
   own) or the **physics** (a core does one thing at a time, a disk has one bandwidth, a chip has one power ceiling: not
   movable by any muscle). That table is `docs/THE_ROOM_TABLE.md`, built by `tools/room_table.py` from the catalog, each
   muscle's preset and the realms result, one row a family, plant and knob (235 rows), and it is what the next engine
   version tunes against.
2. **The 159 same-as-native muscles, one by one.** Each has room and no gain. The first reading, from the result file's
   own columns (the writes the governor made a run, the work and the misses against native, `results/realms_v5/MUSCLES_V5.csv`):
   - **111 are process loops' setpoints, and the governor never wrote one** (0 writes a run). The law's loop rule holds the
     setpoint native whenever the loop's own reach, the excursion its disturbance already makes from the setpoint plus its
     climb, fills the band (`realms/compass_arm_v5.py`, `loop_clamp`: room = (1 − reach) × half-band, native once that room
     is gone). These loops use their whole band under their own controller; a setpoint moved toward the calm end would be
     carried across the line by the next swing. Omni on top of such a loop can take nothing without harm. The wall here is
     **the loop's own controller**, which is design, not physics: a tighter loop (the same actuator, less swing) opens room
     the law can then take. These 111 are the first muscles for Omni-Compass to build itself (section 5.3).
   - **36 are thermal zones** (19 setpoints, 17 capacity knobs): the governor writes (39 setpoint writes a run), the work
     is the plant's own fixed load and the misses are none in both arms, so no aim moves; what Omni buys is margin ahead of
     the heat, power given by the key. No room on the aims to take; the gauge that moves is energy, and the max does not
     shave it.
   - **12 are batteries' power knobs**: the governor writes (27 a run) and the misses fall 0.11 points, inside the noise.
     Room taken, worth too small to read at this size; the lever itself is the question (section 5.3 for a bigger store).
   Each answer is a change to the engine, to a muscle card or to a muscle of our own, through the model gate, as the next
   version.
3. **Omni-Compass's own muscles, where the wall is the design.** Where a family's wall is the vendor's design and not the
   physics, the muscle is rebuilt from its published mechanism with the wall as a dial and the compass law inside it
   (the orchestrator of 23 October, `docs/OMNI_ORCHESTRATOR.md`, is the first: Kubernetes' scheduler, autoscaler, node
   agent and service address rebuilt), benchmarked against the original two arms by the one key, and used in the organism
   only where it reads no LOSS and some GAIN against the original.
4. **The joined organism.** Omni-Compass's muscles, its brain over them, its governance over the collected clusters and its
   seat in the chip, run as one organism against native at every layer: the stacked run (`docs/WHOLE_SYSTEM_PREREGISTRATION.md`),
   every gauge, nothing paid for with another.

## 6. The orchestrator's LOSS of 23 October, read by this law

The showing of Omni-Compass's own orchestrator read work −11.1% and the 95th percentile +23.8% LOSS against the yardstick
while cutting machines 26.5% (`docs/OMNI_ORCHESTRATOR.md`). By section 2 that is a crossed limit or a wrong wire, and it was
a crossed limit: the muscle at its wall was the **processor core**; the room rule counted paper requests and saw room where
the core had none; two units busy at once on one core each took twice as long. The brain had no wire to that limit. With the
limit wired (a machine's room measured as the processor it can still give at full speed, the engine's own 75% rule), the
same showing read work STEADY, the 95th percentile STEADY and the machines cut 5.4%: the harm gone, the cut kept. The law held;
the wall had to be wired.

## 7. The second wall of 23 October: the unit's own paper quota, and the engine's conveyance

With the busy rule wired the showing read STEADY on work and on the 95th percentile, and STEADY is the reading of a room not taken
(section 3). The files said where the room was. In both arms no request ever waited in line (the front's line read 0 at every
second of every step), so the response time was not a shortage of units; it was the unit's own wall: a request of about 40 ms
of processor inside a quota of 250 millicores (25 ms of every 100 ms period) takes 115 ms or more of wall-clock time, and
sometimes a second period. The yardstick (Kubernetes' rule) answers a slow response by adding units, each walled the same, so
each answer stays as slow; and Omni's brain, holding the yardstick's own count (the twin floor) with a force that never fired
under the 800 ms line, was the same mechanism with packing. The wall here is **the design**: a paper quota the operator wrote,
on a machine with processor to spare. The engine already has the muscle that moves it, **conveyance** (omni-v7 and omni-v13,
`omni_controller/muscles.py`): a unit's wall is raised to the room its machine can still give under 75%, shared among the
units on it, never under the request, and handed back at the top. Put into Omni's own orchestrator (23 October, evening): a
lone unit on a half-processor machine stands at 370 m instead of 250 m and answers at the machine's speed. By section 2 the
gain is bounded by the worth of the room: the response time can fall at most to the unit's own service time at machine speed,
and the work (closed-loop clients) can rise at most by the same factor; neither can move further, because the clients' 100 ms
of thought between requests is the organism's own limit.

Read on the quick form (six steps of 15 s, one run of each arm, class L): the 50th percentile 90 → 79 ms, the 95th 176 → 146 ms
(down 13%, STEADY at six pairs), the work up 3.6% (STEADY), machines down 6.6% (STEADY), units up 23% (power given: the twin follows
the work; see section 8), 0 failed, 0 wrong. The full form is read next. The same mechanism stands in the engine on top of
Kubernetes (the kind rigs: the pods' limits conveyed), so this is one mechanism read at two levels, by itself and on top of
native, as the founder's order of 23 October requires.

## 8. The unit count's own edge, in mathematics

Kubernetes' rule holds the units at u_K = ⌈u × b ÷ 0.5⌉, b being the processor the units use over their requests. At its
equilibrium b = 0.5, so u_K = 2a, where a is the **offered load**: the mean number of units working at once (the Erlangs of
the service, a = λ × s, arrivals a second times the service time). The organism's own edge is the fewest units at which a
request still almost never waits. For arrivals at random and u units, the share of requests that wait is Erlang's C formula,

  C(u, a) = [ aᵘ/u! × u/(u − a) ] ÷ [ Σₖ₌₀^{u−1} aᵏ/k! + aᵘ/u! × u/(u − a) ]

and the count that holds C near a small constant as the load grows is the square-root law, u* = ⌈a + β√a⌉ (Halfin and Whitt;
the staffing rule of every call centre). With β = 2:

| offered load a | Kubernetes' count 2a | waiting share at 2a | the edge u* = ⌈a + 2√a⌉ | waiting share at u* | units the edge cuts |
|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 0.333 | 3 | 0.091 | none (one more) |
| 2 | 4 | 0.174 | 5 | 0.060 | none (one more) |
| 4 | 8 | 0.059 | 8 | 0.059 | 0% |
| 8 | 16 | 0.009 | 14 | 0.039 | 12.5% |
| 16 | 32 | 0.000 | 24 | 0.043 | 25.0% |
| 32 | 64 | 0.000 | 44 | 0.029 | 31.2% |
| 64 | 128 | 0.000 | 80 | 0.035 | 37.5% |
| 128 | 256 | 0.000 | 151 | 0.030 | 41.0% |
| 256 | 512 | 0.000 | 288 | 0.031 | 43.8% |

So the room on the unit count against Kubernetes' rule is

  r(a) = 1 − (a + β√a) / 2a = ½ − β / (2√a),  which rises to ½ as the load grows;

and the mean wait a request pays at the edge, C(u*, a) ÷ (u* − a) service times, is 2% of one service time at a = 2 and 0.1%
at a = 128. Two things follow for the showing of 23 October and for the engine:

1. **On the showing's rig the count has no room.** Its clients offer a ≈ 1 to 3 (one to four clients, each working about half
   the time): there u* is at or above 2a, the yardstick's count is already the edge, and the only room was the quota (section
   7). That is why the units read power given (the twin follows the work: faster answers bring more requests from closed-loop
   clients, more processor is used, and Kubernetes' rule asks for more units) and why a cut in machines cannot come from the
   count at this size. The edge is a property of the load, not of the brain.
2. **At the scale a company runs, the count's room is close to half.** A service carrying 64 units of work holds 128 units
   under Kubernetes' rule and 80 at the edge with 3.5% of requests waiting a mean of a thousandth of a service time; its
   machines fall with the units. The brain takes that room live not by assuming random arrivals but by the verdict
   (`omnicompass/verdict.py`): one unit fewer than the twin is tried on the service's own response times under the same
   traffic, kept only where it reads no LOSS within 2%, one step at a time, and a request waiting in line hands a step back.
   The square-root law says where the trials will end; the verdict measures it on the organism itself.

The order of the work stands as in section 5: the theory first (this section), the tuning next (the verdict's pace and the
reflex, read in the full showing and then in three runs), and the muscles Omni-Compass builds itself where the wall is the
design.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

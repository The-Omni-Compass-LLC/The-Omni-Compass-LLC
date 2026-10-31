# The Unified Circle Principle

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Omni-Compass begins with one idea: a system that is closed, bounded and pulled toward a center cannot run away, and
everything it does is a return. I call this the closed circle. This chapter states the principle as I hold it, in its
mathematical form, and then says plainly which parts of it the software uses and which parts belong to the wider theory
the software grew out of.

## The statement

    dX/dt = G(X),        X(0) in Omega, a subset of R^n
    G(X) . n(X) <= 0     on the boundary of Omega
    grad L(X) . G(X) <= 0
    =>  lim (t -> infinity) X(t) in M*, a subset of F

Read line by line:

1. **dX/dt = G(X).** The state X moves according to one law G. There is no outside hand: every change comes from the
   law and the state it is in.
2. **X(0) in Omega.** The state starts inside the admissible region Omega: the set of states that are physically and
   operationally allowed.
3. **G(X) . n(X) <= 0 on the boundary.** At the wall of Omega, the flow never points outward (n is the outward normal).
   Nothing that starts inside can cross out. In control theory this is the Nagumo condition: Omega is forward
   invariant.
4. **grad L(X) . G(X) <= 0.** There is a function L, the energy of the compass, that never increases along the motion.
   This is a Lyapunov condition.
5. **=> X(t) settles in M*.** Together, an invariant container and a non-increasing energy force every path into the
   set M* where the energy stops falling: the bottom of the compass.

The power of the statement is that it does not depend on the particular disturbance. Every input up to the size the
container is built for has the same answer before it is asked: the state stays inside and returns. That is what I mean
when I say that a closed circle holds the answer to every question that can be put to it.

## Closure, admissibility, boundedness

The theory sets five requirements on any law that claims to close the circle:

| Requirement | Meaning | In the engine |
|---|---|---|
| Finite deviation | the distance from the admissible state has a ceiling, abs(E) <= E[max] | the deviation state E drains faster than it can fill |
| Finite curvature | the landscape the state moves on has no infinite slopes or pits | the drive is bounded by tanh; the authority is clipped |
| Global conservation | what flows in is matched by what flows out | the drain and the bath's friction match the drive |
| Recurrence | a disturbed state returns arbitrarily close to where it was | convergence to the target pole at rate K[P] |
| One law | every subsystem obeys the same law, no special cases | one engine, one compass, every muscle |

## The closed circle tested

The canonical evolution law has four parts: deviation is damped nonlinearly and coupled to alignment and to the basin;
alignment relaxes toward unity and responds to deviation; the basin's curvature evolves with internal structure; damping
absorbs excess growth and redistributes energy. Bounded random noise is permitted; divergence is not. A cycle is
identified when the system returns arbitrarily close to a prior state within a bounded tolerance under noise. The state
advances stepwise under a stable numerical integrator with boundedness checks. Under parameter sweeps the test is
always the same three checks: no divergence, bounded, recurring.

## Symmetry and conservation in the closed circle

Every conservation law is the shadow of a symmetry (Noether). The closed circle carries four:

| Symmetry | Conserved | In Omni-Compass |
|---|---|---|
| Temporal (the law does not change with time) | energy | the same law governs every decision; the receipt compares like with like |
| Spatial (the law does not depend on where) | momentum | the same law governs every muscle in every realm |
| Rotational | angular momentum | the compass is symmetric about its center; the engine is symmetric between its poles |
| Internal alignment | alignment invariance | the alignment state is pulled to its pole whichever pole it is |

Around them sit the boundary conditions of the circle: maximum deviation (the boundary limit), topological closure
(bounded wholeness), nonlinear dynamics (complex interactions), resonant reversal (feedback return), energy-momentum
conservation, and cross-scale invariance (scale-independent patterns).

## Scale invariance

The theory claims that one bounded nonlinear action has the same form at every scale: cosmological (curvature
geometry, compression and expansion, thermodynamic cycling), galactic (rotation curves, mass-energy distribution),
stellar (gravitational compression, fusion equilibrium, radiative transport), atomic (electron displacement, orbital
coherence, radiative damping) and quantum (localized deviation wells, bounded oscillation, finite amplitude). The
universal criteria for such a law are that it operates at every scale and preserves bounded deviation, finite curvature
and recurrence. The state vector carries the same meaning at every scale: E the deviation magnitude, U the coherence or
flow alignment, S the structural curvature or basin geometry, B the redistribution or damping.

## The lineage of unification

Each step in the history of physics unified two things that had been separate: geometry formalized structure; motion
was unified across earth and sky; astronomy revealed recurrence; fields replaced action at a distance; curvature unified
gravity, though singularities remained; symmetry came to govern the quantum realm. The closed circle is offered as the
next step: unity without divergence, a single bounded law with no singularity and no runaway.

## What is tested and what is theory

The software uses the engineering core of this principle, and every part of that core is checked:

- The six-state engine, its bounded control command held through the integration step, and the convergence of its
  alignment state to its pole are proved (`docs/TRACKING_THEOREM.md`) and tested against a C++ twin.
- The invariance and boundedness of each engine state were checked state by state (Chapter "Closing the Circle").
- The compass law pulls every muscle's service reading to the middle of its band under a bounded, smooth force, and its
  behavior is measured in simulation and on real software.

The wider claims - one law across every physical scale, the cosmological and quantum readings, the candidate unified
action - are the theory from which Omni-Compass was built. They are stated here so that the engineer understands where
the design comes from. They are not claims that the software has measured, and no result in this book depends on them.

# The Four-Piece Engine

The engine is built in four pieces, stacked like the stages of a press, each feeding the next:

| Piece | Name | What it establishes |
|---|---|---|
| 1 | Foundational Engine | the base laws, the states and the boundaries: a closed, bounded, nonlinear adaptive engine with a four-state dynamical structure (misalignment, alignment recovery, coherence potential, path interaction), bounded convergence and persistence with decay, intrinsic feedback and stabilization, and an empirical validation framework for recovery |
| 2 | Geometric Response | geometric alignment and response dynamics: a geometric coherence field, a unified potential governing geometric deformation, and the propagation mechanism of that response |
| 3 | Coherence Evolution | coherence through response and adaptation: the coherence-response envelope, the system response field, and the coupling of coherence state with response propagation |
| 4 | Unified Master Field Law | one coherent field structure: it integrates pieces 1-3 into one closed dynamical structure with a unified potential governing all subsystems, bidirectional propagation between engine state, geometry and response, bounded convergence across the whole system, and no external authority: all evolution emerges from internal coupling |

The four pieces compress every domain through one center core. The compression process has four stages: the domains
unordered; compression in progress; coherence achieved; return to equilibrium. The result has four properties:
coherent, bounded, admissible, stable - one law, one return, one cycle.

**The 24 domains.** The theory gathers 24 domains into four quadrants around that core:

| Quadrant | Domains |
|---|---|
| 1. Foundational structures | Newtonian gravity; Maxwell electromagnetism; Einstein relativity; Schrodinger quantum mechanics; Shannon information theory; Dirac quantum field theory |
| 2. Dynamics and symmetries | Noether symmetry laws; Hamiltonian dynamics; Lagrangian mechanics; thermodynamics; topology; differential geometry |
| 3. Coherence evolution | gauge field theory; fluid dynamics; field theory; discrete mathematics; solid-state physics; plasma physics |
| 4. Complex systems and integration | astrophysics; consciousness and information integration; biological systems and self-organization; universal mathematical structure; systems theory and complex adaptive systems; the unified Omni-Compass domain (the unified admissible state) |

**In the software,** the four pieces appear as the engine's state equations (piece 1: deviation, alignment, memory and
basin), the basin potential and its flow (piece 2), the bath that absorbs and redistributes (piece 3), and the one
governor that couples every muscle to one law with no outside authority (piece 4).

# The Compass

The Omni-Compass rose is the whole mechanism drawn as one picture.

**The ring.** Twenty-four letters, the complete Greek alphabet from Alpha to Omega: the complete set, nothing missing,
one letter for each domain. On a ring the end runs back into the beginning: after the last letter the ring returns to
Alpha. That is the closed circle: identity, return, cycle.

**The four points.** Four letters are lifted out of alphabetical order and set on the four points of the rose:

| Point | Letter | Mark | Meaning in the engine |
|---|---|---|---|
| North | Alpha, the first | + | the positive pole of the alignment's double well, U = +1 |
| South | Omega, the last | - | the negative pole, U = -1 |
| East | Beta | > | the drive coming in (the beta terms that fill the deviation) |
| West | Gamma | < | the coupling that carries energy out to the bath, where friction absorbs it |

The north-south line is polarity; the east-west line is flow in against flow out. A system stays inside its circle
exactly when what flows out can always match what flows in.

**The inner marks.**

| Mark | Meaning | In the mechanism |
|---|---|---|
| + and - | the two polarities | the two poles of the double well |
| > and < | push out, pull in | the antagonist pair: the up force and the down force |
| the double arrow | exchange both ways | the two-way wire: read in, write out |
| the up-tack | the ceiling | the cover: nothing goes past the top |
| approximately-equal | the wave, the tolerance | the band and its cushion: hold near the center |
| the star | the guiding star | the target the needle points to |

**The center.** The spiral at the middle is the attractor: every path winds inward to one point.

**Opposite letters.** Across the center, zeta faces xi: both are the engineer's symbol for the damping ratio, and a
damping ratio of one is the critical glide to the center with no overshoot. Lambda faces psi: the eigenvalue and the
wave function of the eigenvalue equation.

# Basins, Polarity and the Dual-Basin Engine

## Geometric funneling and basin formation

A basin forms in three stages. While the driving tension T is low, curvature is weak and there is no dominant basin:
flows spread outward. As T increases, curvature concentrates and a positive feedback loop begins. Then a stable
geometric funnel forms: self-reinforcing curvature, finite depth, bounded deviation, with the boundary abs(E) <= E[max]
respected. Structure emerges from fluctuation through curvature concentration and feedback.

In the engine, the basin state S rolls down its potential Phi(S) to a stable bottom; in the compass, every muscle's service
reading is pulled into the bottom of its own funnel.

## Polarity

Two like charges repel without anyone pushing them: the force comes from the shape of the field. A wall built of like
polarity at the edge of a band pushes the state back harder the closer it comes (as one over the distance squared),
and two such walls cancel at the center, where the state comes to rest. This is the boundary condition of the closed
circle written as a force: the field itself points inward at the wall.

The repulsion does not create energy: the field stores what it took to bring the charges together. What is gained in
the computer is that the force is computed rather than spent: the brain computes it at no physical cost, and the
machine's energy is saved because its knob no longer fights itself.

A symmetric pair of repelling walls was tested on the modelled GPU card. It raised work per energy but also raised the
time spent past the service line, because the lower wall pushed capacity away when the card was calm. It was removed.
The upper wall alone remains a candidate.

## The dual-basin engine

The dual-basin engine is a recursive transform with five stages:

1. **Compression.** Two outer basins of positive polarity draw matter and energy inward in a spiral; rotation organizes
   the flow; compression increases toward the center.
2. **Saturation.** At the center, two cores of negative polarity meet back to back; the basin structure S reaches its
   critical value and the curvature reaches its maximum.
3. **Transition (ignition).** Where the cores touch, the transition operator T(X) = sigma(S - S[c]) T(X) activates:
   compression halts and redistribution begins.
4. **Redistribution.** Two axial jets carry the excess out along the axis, with opposite helicity to the inflow.
5. **Reset and recurrence.** The domain relaxes and the cycle repeats.

The core mathematics is a bounded flow: dX/dt = G(X, t) with abs(G(X)) <= C[G], a curvature envelope K(X) <= K[max], and
a redistribution term that activates only at saturation. The state X = (E, U, S, B) stays in its admissible domain,
whose horizon boundary is forward invariant (the Nagumo condition again).

**For an engineer,** the transform reads: pull toward the center (compression); a wall where the muscle saturates;
and, when one muscle saturates, move the excess to its siblings rather than hammering it (redistribution). The first two
are built into the compass. Redistribution across muscles is designed and not yet built; it is on the roadmap.

# The Reflex Rule: One Body, One Brain

A body does not decide in advance how much force a muscle will need. It sends a signal, the muscle moves, the nerves report
what the movement did, and only then does the brain choose the next signal. Nothing in that loop is a forecast. The decision
is made on the reaction, after the reaction, and from the reaction. The founder's order of 10 October 2026 puts the whole of
it in one sentence: what the brain sends to a muscle has to coincide with what the muscle sends to itself and where it is
at. This chapter is the theory of that sentence, and the reason it is the whole mechanism rather than one more rule beside
the others.

## The reflex, not the forecast

The compass of the earlier chapters is a force: where a reading sits in its band, how hard the two opposing forces push it
back toward the middle, and how smoothly. A force alone does not say when it may become a new setting. A governor that
turns every urge straight into a move is a governor that guesses, and a guess made on a machine that is already working is
a guess paid for by that machine. The reflex rule closes the gap: a new setting is earned by a trial on the muscle itself,
and the trial is read from the muscle's own reaction. The urge proposes; the reaction disposes.

## A trial runs to its end

The rule that taught this was broken in a measured run. On 10 October the message broker's consumer group was given a spend
trial: one more consumer, then measure. The extra consumer drained the waiting messages so fast that the service went calm
at once, and the harness of that day ended the trial the moment the calm arrived, before the measurement it existed to
take. Every spend was abandoned by the success it caused. A trial that can be ended by the calm it creates can never prove
that it was worth it. Hence the first rule: a trial runs to its full measurement and is never ended by the calm it causes;
only the wall, a service reaching its line, or the engine's own time limit ends it early. In the one repetition of that day
in which the brain allowed the third consumer early, the whole of the earlier gain came back at a fraction of the spend:
the slowest five percent of messages from 2,450 ms to 57 ms, the queue from 3,375 waiting messages to 253, the work done
inside the line up 17%, with 2.5 consumers on average where the earlier law had spent six to eight. The gain is real and
cheap; what was missing was a fair trial of it.

## No forcing: the need and the urge

A spend is tried only when the muscle's own reading says there is something to buy: messages waiting, a cache missing,
clients queued at a pool. A give-back is tried only when the whole body is calm. The compass force is the urge, smooth and
bounded; the muscle's own condition is the need. The brain never moves a muscle because it wants to. It moves it because the
muscle has shown that a move can pay, and then only by trial.

## One body, one brain, one tick

A muscle judged alone can be read GAIN by pushing its neighbour away from its own: a cache that takes memory from the database beside
it, a consumer that takes processor time from the service it feeds. So the brain reads the whole body first, every
muscle's state, every service's speed and work, the host's processor, memory and energy where a meter exists, and judges
the body's cost: the Omni index's own arithmetic over all the work, all the speed, all the machines and all the resources.
On top of the body's total stands a guard for every part. A step is refused if any one service read LOSS beyond its cushion,
even when the total improved. Pushing one thing to a LOSS to move another toward its own is refused by rule, not by luck.

That guard is do no harm in its strictest form, and it is the form the engine that stands keeps. The founder's words of
19 October 2026 give do no harm its meaning (`DISCLOSURES.md`, section 3): the real goal is the organism, to strengthen it
and keep it healthy, working at the best state its own muscles can carry, turning whatever is fed into it into the most
and best output it can make. Harm is the organism turning out less than native makes it turn out, or made less healthy: a
muscle past its own limit, a service over its own line, anything made to fail. Within that, the muscles are one body: where
one muscle's strength cannot be used without straining another, the brain offsets and engages them together, and it may
use one muscle less, or leave it native, so that another can carry more, whenever the whole organism comes out ahead and
every muscle stays healthy. The guard above refuses every such trade, the good with the bad; the next engine version
replaces it with that judgment of the whole organism and of every muscle's health, through the model gate first, and every
result is run again on it.

## One trial at a time, nothing permanent, the wall belongs to the body

If two muscles move together, the brain cannot tell which one caused what it feels. Inside a body, one new trial runs at a
time, granted to the muscle asking loudest whose own condition holds; every other muscle keeps acting inside what it has
already proven, so nothing is frozen and only new trials wait their turn. Every allowed step is tried again on the recheck
and pulled back when it stops paying, and a muscle at native is asked again whenever its signal returns: native is where the
brain stands when it has not yet been shown a reason, never a verdict. And if any service reaches its line, the trial
stops, that step is undone, and every force in the body lifts off. The wall is the body's, not the muscle's.

## Why this is the closed circle again

The Unified Circle Principle says that a system closed on itself, bounded, and pulled toward its center cannot run away:
everything it does is a return. The reflex rule is that principle carried into time. The loop is closed through the system's
own reaction; every excursion is bounded by the trial's limits, the cover and the wall; and every allowance is pulled back to
native unless the body keeps proving it. The compass holds each reading in the middle of its band. The reflex holds each
decision in the middle of what has been shown.

## What it means for the evidence

Omni v3, the engine on main, already tries a slow knob on the muscle itself before it moves it, and the live harnesses carry
the same verdict around every live knob. Omni v4 is the engine written to make the rule hold on every wire by construction:
one body that every muscle's wire passes through, the trial's rules inside the verdict, and no wire that can write around
them. Because that changes the engine, v4 carries its own fingerprint, the package version follows it, and every result in
this book is run again on it. No result is read across engines.

# Closing the Circle in the Engine

Each state of the engine was checked against the closed-circle conditions:

| State | Closed? | Why |
|---|---|---|
| E, deviation | closed | it drains at rate α[E] while its inputs are bounded (the drive is capped by tanh) |
| U, alignment | closed | the cubic term μ U (1 − U²) pushes back hard from far out |
| I[U], memory | closed | it forgets at rate λ[I] |
| B, the bath | closed | the friction ω[B] / Q[B] settles it |
| S, the basin | closed on the positive side; open on the negative side below an unstable ridge | Φ(S) carries a cubic term, so the landscape falls away below the ridge (at S = −3.5 with the default parameters) |

Three openings were found and each has its closure:

1. **The basin's negative side.** A quartic term in Φ(S) would give the compass a wall on both sides. This changes the
   frozen engine and is a new version with its own proof.
2. **The outer loop.** The frozen live governor computes the push and pull u and uses it as a convergence signal; it
   does not send u to a lever. The compass closes this loop: reading, force, plug, lever, read-back. On the modelled card
   this is the difference between +0.1% and several percent of work per energy (the one-wire governor against the
   corrected two-wire compass, `results/sim/gpu_two_wire/`).
3. **The corner.** clip() is a hard stop; tanh is its smooth form. The compass uses tanh.

**What closing the loop has shown since.** The compass law of the second opening is the law every result in the manual
was made on: it was frozen as Omni v1 on 5 October 2026 with its proofs untouched, grown to the 945-muscle catalog as v2,
and given one gate as v3, the slack gate on speed knobs, after the v2 realms read a service tradeoff on the Physics realm
and the tower. That gate is the closed circle applied to a muscle's physics: an axis that is busy more than half the time
at full speed has no slack to spend, and a law that spent it anyway would be spending energy for nothing; with the gate,
every organism reads superior within its guardrails and zero muscles read LOSS (`results/realms/REALMS.md`). On real
software the same law, read through the plug and the read-back, is the law of the Kubernetes, database, broker and cache
tables, with their gains and their losses. The first opening, the basin's negative side, remains open and documented: it
would be a new version with its own proof, and no result depends on it.

# The Physics of a Processor

A GPU's firmware raises its clock one step at a time whenever there is work and room; each higher clock needs a higher
voltage, and dynamic power rises with the clock times the square of the voltage, so the top of the clock range is where
each extra step of speed costs the most watts. When the draw crosses the power limit, the firmware knocks the clock down
several steps; with room again, it climbs again. On a busy card this repeats many times a second. The clock saws against
the limit, the overshoots burn watts before the limiter catches them, and the card spends its time at the steepest part
of its power curve. The power is the burner; the cooling removes the heat at its own pace; the limiter turns the burner
down so the cooling can catch up, and the boost turns it back up.

The firmware does not aim at a balance point because it cannot see the job: it does not know whether the work is a
response due in milliseconds or a batch due overnight, the right point moves with the workload, the room and the chip,
and a limiter is simple to prove safe. The vendor default is set for maximum performance, and the electricity bill is the
customer's.

Omni-Compass sits on the customer's side, where the job's service line is known. It holds two wires: the clock ceiling
sets how high the boost may climb, and the power limit becomes a lid set just above what that ceiling draws. The boost
stops at the bottom of the compass instead of slamming into the wall; the limiter rarely needs to act. Every watt kept off
the chip is saved twice in a data center: once at the chip and again at the chillers that would have carried its heat.

# The Seven Organisms and the Benchmark Grid

Omni-Compass is benchmarked on seven organisms, each run native and with Omni-Compass on top of native on the same seed,
the same load and the same clock. An organism is a set of muscles stepped together on one clock, each muscle from its own
plant model with its own native controller, the whole fed one demand from one seed, so that the heat the machines make is
load on the rooms, the body's power swing is load on every site's line, and one brain judges every step against every other
muscle's cushion. On the 1,107-muscle catalog the engine that stands carries (`realms/catalog_v5.csv`) the seven are: the
**spine**, the 267 muscles every real stack runs on, every one in all four realms, an organism in its own right since 16
October and the base of the other six, as an operating system is the base of every program (`docs/THE_SPINE.md`); the four
realms, each its own trade's families on the spine, Compute / AI / Cloud (540 muscles), Physics / Robotics / Autonomous
(404), Energy / Facility / Industrial (480) and Distribution / Specialized (484); the four stacked with every duplicate of
the spine kept (1,908); and the whole tower with every muscle once (1,107). Earlier catalogs' organisms and counts stay
with their own results in `docs/history/`.

Every organism runs under three loads: its own load; the climb, the demand stepping by one, up and down (1 2 3 2 3 4 …),
past what native can carry, so that the most each arm can do shows; and work waiting in line when the run starts. Every
receipt shows work, the time over the service line (misses), the energy the max took as power given beside the work it
bought, wear, and whether every knob was handed back; the reading is GAIN, STEADY or LOSS by the key at the front of this
manual, judged by what each gauge is for and never by the sign of its number. The spine read beside a realm shows what that
realm's trade adds to the base it stands on; the spine read alone shows whether the governor helps the machines every
stack runs on before any trade is put on them.

**The grid.** Each organism runs at 1, 10 and 100 copies of itself on one clock and at 1, 10 and 100 paired runs, modelled
and with the real cluster inside, both arms shown in every square; on GitHub's own machines the 500 tier runs too (the
ladder of the Python's 500-run Monte Carlo, the founder's order of 25 October), a cell beyond a free runner's memory or time listed as pending runner capacity and
never rented, while paid cloud and GPU runs stay at 1, 10 and 100 copies with at most 100 repetitions. The two axes answer
two questions. Copies is the size of the body one brain governs: at 100 copies of the four stacked the law computes a force
for about 190,000 muscles from one reading of one clock, and the question is whether it stays coherent, whether the decision
is made inside the decision period, and whether the cluster inside it is still served on time. Runs is the number of
independent paired trials, each from its own seed, and the question is statistical: how wide the interval of the paired
difference is and whether it moves as the trials multiply. The grid's readings on the engine that stands are
`results/grid_v5/GRID.md` and the standing block of `docs/STATE_OF_PLAY.md`, every square shown, the spine's squares filled
by the conductor as they land; the number is small because the native controllers in the models are well tuned and leave
little room, it is real within the model, and it is never counted in the Omni index, which is made of real stacks only.

On a GPU machine the real card is wired into each organism as one more muscle of its GPU Hardware family, a spine family,
so the card is in the spine and in every organism built on it; its own power meter and its requests are counted in the
organism's receipt, kept apart from the modelled plants and also added to them. Real Kubernetes is benchmarked separately
on real clusters, and it is also wired into the organisms as one more muscle (`tools/run_kil.py`): at 1, 10, 100 and, on
GitHub's own machines, 1,000 copies, the organism's own compute demand drives a real load generator against a real service
on a real cluster, and the cluster's watts come back into the organism as heat and load. Those runs are labelled "L + S":
the cluster is live software, the organism around it a model.

The seven organisms are models (evidence class S). They show how the law behaves across hundreds of kinds of machine at
once and whether its effect is stable as the count and the size grow. Real Kubernetes, the real database, the real broker,
the real cache and the real card are the anchors measured on real software and, for the card, a real meter; their results
and their losses are in the manual's section 16.

# The Economics of a Receipt

Run the stack native and print the receipt. Run the same stack with Omni-Compass and print the receipt. The difference
is the gain, read from either side: more work for the same energy, or the same work for less energy and fewer machines.

The license fee is set against the measured gain on the customer's own receipt. On a stack that costs one hundred, a
measured gain of ten is worth ten; the fee is a share of that ten, and the customer keeps the rest. Percentages from
different parts of a stack are not added into one bill: the invoice is one gain, measured once.

The value a customer sees comes in three forms, each on its own line of the receipt:

1. **Work per energy** - more finished work per kilowatt-hour.
2. **Capacity** - the same work on fewer machines in service; it becomes a cost reduction when the released machines are
   returned to the cloud or switched off by the platform around Omni-Compass.
3. **Service** - faster responses and fewer breaches at the same load.

The babysitting tax - the people and tools kept on the clock to set caps, answer pages and turn knobs back after a run
or a crash - is the cost Omni-Compass removes by holding the knobs and returning them itself.

**The receipt's arithmetic, and the one number.** With the work held equal, a gain G in productivity is the same
measurement as a saving S = G / (1 + G) in resources: a third more work is a quarter off the bill (manual, section 3.4).
Across every real stack the one number is the Omni index (`results/OMNI_INDEX.md`): each test's work, speed, machines and
energy as ratios, combined by geometric means so that a gain and an equal loss cancel exactly, each real category weighed
the same, and only rows the same in all three of our runs counted. The index is honest in both directions by construction.
As this edition is written it reads +30.2%: real Kubernetes +25.5%, the database +14.2%, messaging +166.9%, and the cache
−24.9%, the last negative because the memory the governor holds for a wide working set is the resource it trades and
reads power given by rule, even as the cache's work and hit rate read GAIN. A buyer reads the category that matches their
stack, and reads its losses in the same table as its gains.

**What a receipt is not.** A receipt is not a forecast. It is the measured difference between two arms on one system at
one time, with its interval. The only number that applies to a customer's system is the one their own paired runs produce,
and the method of those runs is the manual's section 13, the same method every table in this book was made with.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

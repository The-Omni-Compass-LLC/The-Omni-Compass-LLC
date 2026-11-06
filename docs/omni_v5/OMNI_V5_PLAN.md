# Omni v5 — the living cyborg engine (the whole mechanism of action; the v5 engine is declared omni-v5)

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. Evaluation and Simulation use only. Any commercialization or
monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the
USA. www.omni-compass.com

Founder's orders, 11 Oct. This file is the record of the whole mechanism of action, so the engine can be built, rewired
and pushed on his word. It is pushed on branch v5; what is built and what is still to build is marked in §10, §26, §27
and `docs/omni_v5/BUILD_STAGES.md`.

## 1. The goal (changed)
- Not only SAVE (least energy for the work). Also MAX (the most work the same hardware can do inside its edge), with a
  DIAL between them, judged by **net benefit** (value of work − energy − wear − risk), never by energy cut alone.
- "Use the maximum that every muscle and every watt already has." Push to the limit, hold at the limit, never past it.
- Two numbers per organism, plus the curve between, with native marked: **Save** and **Max**, each with its full bill.

## 2. The only two limits — both written in mathematics, nothing else set
- **The edge.** Each muscle's own boundary (deadline, queue limit, temperature-limit, power limit, the chip's own
  throttle point). The cushion before it moves in real time per machine: the muscle's climb within its own reaction time
  + z × its wobble. A barrier the controller may never cross, whatever it wants. (v5 law: `Edge`, `safe_speed`,
  `drop_floor`, `cooling_hole_ceiling`, `band_position`.)
- **The centre.** No muscle ever enters a state it cannot climb back out of: a queue growing faster than it drains, a
  room whose cooling has saturated, a battery run flat. Sized from queue math (Lindley) and heat math. (`release_safe`,
  `cooling_hole_ceiling`'s Lindley reach table.)

Everything else is Omni's mathematics pushing coherence. Nothing is hardwired.

## 3. The body (brain + nervous system + immune system)
- **Never sleeps, one eye open.** The body idles at a breathing floor (never zero); the brain watches every muscle at
  full rate (cheap — only reads meters) and wakes the body before work lands, jumping idle→needed (1→≤99, never 100),
  then the compass settles it smoothly.
- **Nervous system.** Every muscle reports, every few seconds: where it sits in its band, how fast it heads to its edge,
  its wobble. Early-warning = act on the projection, not the reading (already in v5 for motion deadlines, cooling
  headroom, burst room; extend to every muscle).
- **Immune system.** Learn each muscle's normal physics; anything that breaks it is foreign:
  - impossible reading (dead sensor), foreign writer (one-writer rule already catches), unknown workload (miner on a
    GPU: busy power + ~zero work), a part going bad (fan moving less air per watt).
  - Response: local reflex → neighbours help → **quarantine to native** → named alarm → remember (faster next time).
  - Specificity is the law: it flags only the sick muscle, never healthy ones (the autoimmune failure). shown in the model (class S, not proof)
    (`docs/omni_v5/study/immune.py`): injected one runaway, flagged exactly it, quarantined, body returned to healthy, 0 false
    positives. Detector = busy-level power AND served-work ≈ 0 together (neither alone fires).
  - **Fever:** if inflammation spreads, the whole body goes native until it calms.
  - **Cancer:** a part of the body itself turned bad and spreading (leak, runaway, dying disk, compromise). Omni can
    contain and work around it (quarantine, protect neighbours, alarm) but cannot repair hardware — a person replaces it.
- **Health / wear (so the super-athlete doesn't die at 25).** Every muscle has a wear gauge; the rule: never age a part
  faster per unit of work than native, unless the owner turns the dial past it. a gauge shown in the model (class S, not proof) (`maxarm.life_used`,
  Arrhenius, life halves ~every 10 °C). Models: silicon Arrhenius (Ea≈0.5 eV), thermal-cycle fatigue (Coffin–Manson,
  swing²), battery cycle+calendar aging, motor/fan bearing+insulation.

## 4. Chip heat (the founder's specific question)
- Omni cannot burn a chip up: it only moves settings inside the ranges the chip's firmware allows; the chip throttles
  itself before damage. Omni's job is to stay far enough from the throttle point to lose no speed.
- Read each chip's own limits (current temp, throttle temp, shutdown temp, power limit) + the room's cool-to temp and
  spare cooling. Running 1–2 °C warmer: ~1–2 °C warmer chip, no speed lost while below throttle with margin, a little
  more leakage power + faster fans. Keep the change only if net benefit is positive. Cost is not a limit; net benefit is.
- The boundary is the chip's own **junction temperature**: its slowdown (throttle) point and its shutdown point above it,
  both read from the chip itself (nvidia-smi and amd-smi report them), never assumed. Omni keeps the junction a learned
  margin below the slowdown point — the edge: how fast the junction has climbed times how long the cooling takes to
  answer, plus z times its wobble — pushes to that limit, holds there and never goes past it. The room's cool-to
  temperature and the cooling's spare capacity decide how close the junction may run; the chip's own shutdown and
  protection stay the machine's (§8), never Omni's.

## 5. The dial (owner's choice, shown with its bill)
- Default we ship: **Balanced** — strong, fast, pushing hard never shortens life.
- Settings: **Long-life → Balanced → Edge → Sprint** (Sprint = burn for speed, life rule relaxed). The manual states
  plainly an owner may tune past health for their own economics (run organisms like pawns, replace and continue). Omni
  shows the numbers; the owner decides. shown in the model (class S, not proof) (`maxarm.DIAL`, `sweep.py`): at 2× load, misses −20%→−23% for
  +1%→+4% chip-life, +5%→+16% energy.

## 6. The cyborg wiring — gauges & knobs, by body part (full instrumentation)
All wired OUT to monitors + one outside panel (green/yellow/orange/red), on the screens companies already use
(Prometheus/Grafana, NVIDIA DCGM, OPC UA / Modbus, Kubernetes metrics).
| Body part | World | Gauges | Knobs |
|---|---|---|---|
| Skeleton | servers, racks, PDUs, UPS, switches, storage, building | BMC/IPMI (fans, PSU, temps, volts), power & net meters, inlet temp | node power caps, fan policy, outlet on/off, UPS mode |
| Nerves | signal paths | telemetry pipeline, cgroups, RAPL/energy counters, DCGM, logs/traces; arrival latency | the two-way plug (k8s, cloud, device APIs) |
| Food (energy) | grid, price, carbon, batteries | meters, RAPL, DCGM power, price/carbon signals | battery charge/discharge, power caps, flexible-work timing |
| Water (cooling) | chillers, CRAH/CRAC, liquid loops, fans, pumps | supply/return temp, flow, pressure, cooling in use | setpoints, fan/pump speed, valves |
| Muscles | CPU, GPU, mem, disk, net, containers, k8s, DB, queues, AI serving, robots, motors, process lines | load, queue, wait, throughput, errors, temp, power | DVFS/sleep states, GPU power/clocks, cgroup limits, autoscaler, scheduler, DB pools/caches, queue consumers, batch size, motor speed/torque, process setpoints |
| Exercise | keep every muscle proven | does it still answer its knob; wake time | load steps (1 2 3 2 3 4), burst drills, failure drills, warm spares, a small test move if a muscle sat idle too long |
| Immune + monitors | §3 | brain vitals, outside watcher | the dial, the physical switch |
- **Balance dial** per body: tilt toward work/speed vs energy/wear/cost.

## 7. Stacked levels (founder's hunch — likely gains more)
Omni on the muscle, on the organism, AND on the chip/cloud, stacked. Each level sees what others can't (muscle: own edge
fastest; organism: shared heat/power/load between muscles; chip/cloud: hardware limits). Rule: one hand per knob — each
level owns different knobs, or the level above sets the edges for the one below. TEST: one muscle, five ways (native;
Omni on muscle; on organism; on chip; all stacked) on identical plants/seeds. Expectation: stacking wins where muscles
share heat/power/load, ties where a muscle stands alone. NOT YET RUN.

## 8. What never changes — the DNA / seed
Two-way plug (one wire in, one out); snapshot-once, restore-to-native; one hand per knob; heartbeat lease (brain silent →
all native within a known time); decision log; kill switch; and one line no mode crosses: the machine's own safety
systems (shutdown temps, protective relays, battery fire protection) — Omni never touches those, only native knobs inside
their ranges. **Seed** = engine fingerprint + dial setting + wiring map → same seed, same machines, same organism (same
bloodline); every result names its seed; seeds can be crossed.

## 9. Kill switch & self-watch (tainted brain)
- Physical switch outside the body cuts Omni without asking the brain; lease then snaps all native within a known time —
  a sick/hijacked brain cannot stop it. (Today: software switch + lease exist; physical switch + outside watcher to build.)
- Brain checks its own picture vs physics; disagreement → go native. Outside watcher checks results vs native → cut if
  below native. Fingerprint proves which brain runs. Even a mad brain can't move a knob past its native-set range.

## 10. State & build order
- **Pushed:** v3 (main). v4 (own branch). v5 on branch v5: declared omni-v5 with the v5 law in the engine, the
  1,097-muscle catalog, the official v5 realms table (0 of 1,097 behind native) and the benchmark code for every
  platform (§26, §27).
- **v5 SAVE shown in the model (class S, not proof; 12 fresh runs, 6 organisms):** beats every version + native on energy & misses; work = native; the
  one exception Physics vs v1/v2 energy is inside the noise and v1/v2 bought it with late trains/ships.
- **v5 MAX/dial/wear/immune shown in a quick model (class S, not proof; the Max dial, with its tradeoffs)**
  (`docs/omni_v5/study/`): +14% load at equal quality, −23% misses at 2×, dial
  tradeoff, Arrhenius wear, specific immune quarantine with 0 false positives.
- **Built 12 Oct:** the v5 edge inside the live Kubernetes controller and the GPU governor, and the v5 law in the six
  organisms with a real cluster or card inside. **NOT built yet:** the databases' adapters on v5 (stage 11); sleep/wake
  floor on every muscle; outside watcher + monitor panel; physical switch; stacked levels;
  combined GPU+k8s+cloud+data-center organism; full early-warning on every muscle.
- **Build order on GO:** (1) wiring map per body part; (2) v5 engine = edge+centre+health+immune+dial+seed, both open
  harms (data-hall precool, robot-joint lateness) at zero; (3) modelled test all organisms + combined, 4 dial settings,
  Save+Max+bill+wear, zero-harm per muscle, kill drill; (4) founder review; (5) write into engine as next version, rerun
  all, verifier 0 FAIL under 3.12, push; (6) real clusters — GitHub (free), AKS, GCP; (7) GPU on Lambda, one exact commit.
- **Files to touch when pushing:** `omnicompass/compass_law.py`, `omnicompass/verdict.py`, `realms/compass_arm.py`,
  `realms/plants.py`, `realms/harness.py`, `realms/presets.py`, `tools/run_scale.py`, new omnicompass/immune.py +
  omnicompass/wear.py + watcher/panel, `OMNI_V5.json`, docs/OMNI_V5_PLAN.md, manual chapter "The brain you build",
  `tools/omni_version.py`, `tools/legal.py` headers. Commit trailers: no model identifier (CLAUDE.md).

## 12. Switches, the real security threat, and a brain that breaks down
- **Per-muscle switch (optional):** a human can force any one muscle off or native from its tile. Rarely needed — Omni
  already cuts a bad muscle itself — but it's there.
- **The switch that matters: the whole-organism kill switch.** A physical switch that takes Omni *completely* off; the
  lease then returns every knob to native within a known time. Its real purpose is not a muscle fault (Omni handles those)
  but a **bad actor hijacking the brain** — whoever controls the brain controls the system — or **the brain itself
  breaking down**. Even a hijacked or broken brain cannot stop the physical switch, and cannot move any knob past the
  range the native system set.
- **The health of the whole organism has three separate layers that can each fall ill: the BRAIN (the decision logic),
  the NERVOUS SYSTEM (the signal paths in and out), and the MUSCLE (the plant). Each has its own ailments, its own
  computational meaning, its own detection and its own response. Named in human terms so the tech world reads the
  interpretation; each is a real check in code.**

  BRAIN ailments (the decision logic):
  - **Hijack / bad actor** (the true security case): someone takes the brain; whoever owns the brain owns the system.
    Defense: engine fingerprint, one-writer rule, every knob clamped to the native-set range, outside watcher cuts Omni if
    results fall below native, physical switch above all.
  - **Amnesia / Alzheimer's** = learned state corrupts or is lost. Response: distrust memory, run native, re-learn in
    watch-mode; never act on a memory it can't verify.
  - **Schizophrenia / hallucination** = the brain acts on a reality the meters do not show (a false or poisoned world
    model; it "sees" demand or risk that isn't there). Detection: **every action must be reconstructable from the raw
    meters** — if the brain's intended move is not justified by what the sensors actually read (the physics residual),
    it is hallucinating. Response: that move is refused and the muscle goes native.
  - **Sleepwalking** = acting while idle — jumping from idle to full with nothing really arriving. Detection: a wake must
    be backed by a metered trigger (real arriving work or a real risk signal); a wake with no cause is refused. Response:
    wake-gating — no ramp without a metered cause. (Ties to "never sleeps, one eye open": the eye must see a real reason.)
  - **Mania / runaway** = pushing ever harder with no payback (chasing its tail). Detection: action escalating while net
    benefit is flat or negative. Response: futility + backoff (already in v4's verdict).
  - **"A psychopath doesn't know he's crazy."** A broken brain cannot judge itself, so judgment must come from OUTSIDE the
    brain — this is the cyborg part. The outside watcher, the physics ground-truth, and the native twin do not depend on
    the brain's own opinion; the organism can be proven unhealthy even while the brain believes it is fine. That is why the
    watcher and the "results vs native" check live outside the brain and above it.

  NERVOUS-SYSTEM ailments (the signal paths, separate from the brain — the brain can be fine and these still fail):
  - **Signal never reaches the muscle** (like ALS/MS): a command issued but not applied. Detection: read-back shows the
    knob didn't move. Response: that path native + alarm.
  - **Reversal / mis-signal:** a sensor path corrupts or a feedback sign inverts (reads the opposite of reality).
    Detection: physics-sanity (brain's picture vs the energy/queue/heat balance). Response: drop the path, go native; a
    reversed signal can't drive a knob because every write is read back and checked against physics first.
  - **Mis-routed signal:** a command or alarm for muscle A reaches muscle B. Detection: per-path identity + read-back on
    the intended muscle. Response: drop, native, alarm. **Inflammation must land on the muscle whose physics actually
    broke, never where a mis-routed signal points** — the immune alarm is cross-checked against the physics residual at
    that muscle before any response.
  - **Blocked / stale pathway:** telemetry or command stalls or times out. Detection: reading age (the `stale` signal).
    Response: a stale reading is never acted on — native until the path is live again.

  MUSCLE ailments (the plant itself — a muscle, like any muscle, with its own full list):
  - **Sprain** = transient overload, recoverable (a brief queue spike or thermal excursion, pushed a touch past safe).
    Detection: a short edge breach that is already easing. Response: ease the load, let it recover; no quarantine.
  - **Tear** = partial failure under load (degraded throughput, errors climbing, a worker half-dead). Detection: output
    drops below its healthy band while still drawing load. Response: shed load off it, route around, alarm.
  - **Break** = full failure (crashed process, dead GPU, failed drive — the muscle is down). Detection: no output / no
    heartbeat. Response: take it out, redistribute its work, native, alarm.
  - **Cramp** = seizes and won't release (deadlock, connection-pool or thread exhaustion, stuck lock, long GC pause, I/O
    hang, a throttle that latched). The muscle is contracted and frozen. Detection: load present, output ~0, but NOT the
    runaway signature — it is stuck, not busy-burning. Response: **relieve the cramp** like a real one — back its load off,
    release the lock / drain the pool / cancel the stuck request so it can unclench; if it won't release, cycle it
    (restart) and run native meanwhile. (A cramp is distinct from cancer: cramp = stuck and silent; cancer = busy and
    producing nothing.)
  - **Malnutrition / starvation** = the muscle lacks its supply and so cannot perform no matter the command (CPU-starved,
    memory pressure, I/O or network starved, power-capped too hard). Detection: output low while its own inputs
    (CPU/mem/IO/power grant) are the binding limit, not its command. Response: **feed it** (lift the cap, grant memory/IO,
    move neighbours off its supply); never blame or quarantine a starved muscle — the fault is upstream supply.
  - **Nutrition is a first-class reading:** every muscle reports whether its supply (power, cooling, memory, I/O, network)
    is adequate; a muscle starved of supply is diagnosed as starved, not broken.
  - **Fried actuator (nerve-into-muscle at the muscle end)** = the driver/actuator that takes the command is dead.
    Detection: read-back shows the knob never moves though the path upstream is live. Response: native, alarm.
  - Dying part, runaway/cancer, foreign workload — detected and quarantined by the immune system (§3, shown in the model, class S, in
    `docs/omni_v5/study/immune.py`).

  SKELETON ailments (the frame everything is built on and that bears the load — the layer that was missing; computational
  = servers/chassis, racks, power distribution (PDU/UPS/transformer/phase), network backbone, cooling plant, the building,
  and for a vehicle the vessel's frame). A muscle lives on a bone; if the bone fails, everything on it falls, so the
  skeleton's limit is a **shared edge above every muscle on it** — a muscle is never pushed past what its rack's power or
  its switch's bandwidth can bear, even when the chip itself could take more.
  - **Fracture / break** = a structural node fails (rack power lost, PDU trips, a backbone link dies, a power phase drops,
    an availability zone/region goes down). Detection: a whole group of muscles on one bone loses supply or signal at once.
    Response: stand the body on the rest of the skeleton — fail the muscles over to sound bones (rebalance across
    racks/AZs), alarm; Omni can't mend the bone (a human does) but keeps the body standing on what's left.
  - **Osteoporosis / weak bone** = the frame is near capacity and brittle (thin power/cooling/network headroom).
    Detection: structural headroom gauges — rack power vs breaker, backbone vs capacity, cooling plant vs IT load (PUE).
    Response: don't pile more on a weak bone; the edge already includes the skeleton's limit.
  - **Posture / load-bearing** = weight must be spread so no one bone carries too much. Response: balance rack power,
    spread muscles across racks/AZs/switches (anti-affinity), never stack the body on one bone.
  - Skeleton gauges & knobs are in `CONNECTORS.md` (BMC/IPMI/Redfish, PDU meters, SNMP backbone, BMS) — read board/rack
    power, phase balance, link health, structural temps; knobs are node power caps, outlet on/off, failover/rebalance,
    spread policy. The vessel's own frame (car/boat/plane/train/rocket chassis) is the skeleton in a vehicle.
- Because any layer can go wrong, the manual explains plainly what brain an owner is building (the dial), and that the
  kill switch, the native-range clamps, and the outside watcher are the guardrails that keep even a sick brain, a crossed
  nerve, or a cancerous muscle from harming the body.

## 13. Self-wiring — the owner wires almost nothing (the manual's whole point)
- The manual is a deliverable as important as the engine: wire it wrong and the output is wrong. So the design removes the
  wiring from the human wherever it can.
- **Auto-discovery + AI onboarding:** dropped on a native stack, Omni probes what's there (Prometheus, k8s API, DCGM,
  OPC UA browse, SMART, cloud APIs, SNMP), matches each muscle to its adapter, snapshots, and comes up in watch-mode. An
  AI onboarding agent (an assistant like this one, run once at install) reads the stack and writes the small per-muscle
  adapter config automatically — the human confirms, does not hand-wire a thousand muscles.
- **Never acts on a muscle it cannot read, write AND read back.** An unmappable muscle is shown on the screen and left
  native, not guessed at — this is the rule that stops the wrong-output problem at its root.

## 14. Different vessels, one DNA
The same brain + nervous system + immune system (the DNA/seed) drops into different vessels — a data center, a car, a
boat, a plane, a train, a rocket, a factory, a grid. Each vessel is a different assembly of muscles with different edges,
but the mechanism and the seed are identical, the way the same genome builds different bodies. Each vessel's edges and the
safety-of-life exclusions (§ CONNECTORS) are what differ, written per vessel in the manual.

## 15. Manual chapters to write (deliverable)
Front matter + legal; What Omni is (governor on top of native); The brain you build (the dial, genius↔sprint, what never
changes); Wiring (auto-discovery, the adapter catalog, one screen, colors, override); The two limits (edge, centre, the
math); The body (nervous, immune, cancer, fever, wear, sleep-one-eye-open); Security (kill switch, hijack, amnesia, nerve
reversal, native clamps); Vessels (data center, car, boat, plane, train, rocket, factory, grid — edges + exclusions each);
Reading the numbers (evidence classes, three-run reading, native-vs-Omni, no wrong output); Results (Save + Max + bill +
wear, every row incl. losses); Back matter (glossary, file map, troubleshooting, seed/replication).

## 16. Digestion, metabolism and waste — the gut (the layer the founder added last)
A body takes input through the mouth, breaks it down, sends the good parts to the muscles that need them, and pushes the
waste out. If waste sits in the belly it turns to poison. The organism does the same, and it must heal its own indigestion.
Plain English first, then the engineer's word.
- **Mouth / intake** = where work comes in. *Engineer:* ingress / API gateway / load balancer / message intake / sensor
  feed. Omni reads the rate and shape of what's arriving.
- **Stomach / digestion** = breaking raw input into work the muscles can act on. *Engineer:* parse, validate, queue,
  batch, schedule. Omni paces intake so the stomach isn't overwhelmed.
- **Liver / kidneys / where the nutrients go** = deciding what goes where — which work to which muscle, and which
  resources (power, memory, I/O, cooling — the "iron and vitamins") to which muscle. *Engineer:* the scheduler / placement
  / resource allocator. This is Omni's brain deciding where the iron goes; it ties straight to the muscle's **nutrition**
  reading (a starved muscle is fed, not blamed — §12).
- **Waste detection and elimination (the new, important part).** Not all input is good, and **you don't fully know what's
  waste until it's been through the system** — so Omni processes, watches the result, and eliminates what proves useless or
  toxic, and remembers it (immune memory) so it's caught earlier next time.
  - *Waste, in engineer terms:* invalid / malformed / poison messages, duplicate and retry storms, zombie jobs, orphaned
    connections, leaked memory, dead-letter messages, stale queue items, and disk buildup (logs, temp, cache).
  - *Constipation / toxic buildup:* waste that sits and backs up — a dead-letter queue filling, disk filling, memory
    leaking, zombies piling, a retry storm feeding itself. Left alone it poisons the body (fills disk, exhausts memory,
    clogs queues) and cascades into failure.
  - *Elimination (push it out):* dead-letter and drop poison, garbage-collect, reap zombies, evict caches, rotate and ship
    logs, clear temp, cap retries (circuit breaker), TTL-expire stale items. Omni watches the buildup gauges and clears
    them **before** they poison the body.
- **Indigestion / heartburn / diarrhea — self-heal, then tell the human.** Bad input can throw the body into disarray even
  while the brain works fine (a bad batch, a slow query, a hot partition, a thundering herd = heartburn; dropping work and
  cascading timeouts, over-shedding = diarrhea). Omni steadies intake, isolates the bad batch, rebalances, stops
  over-shedding — resolves the disarray on its own — and then **reports it on the one screen** the way a person feels the
  heartburn after a big meal: "the body had indigestion from this input; here is what it did."
- **Metabolism = the nutrition↔waste balance:** good in → to the muscles; bad → out. This closes the loop with the muscle
  nutrition reading and the immune memory.
- **Gut gauges & knobs** are added to `CONNECTORS.md`: read intake rate, queue & dead-letter depth, disk/log/temp use,
  memory-leak slope, retry/duplicate rate, zombie count; knobs are intake pacing / admission, dead-letter & drop, GC,
  cache eviction, log rotation, retry caps (circuit breaker), TTL.

## 17. Tone and the manual's opening (founder's order)
- **Two registers, always:** the engineer's / CTO's / physics term AND plain English a 10th-grade reader follows. Every
  concept carries both. The body words (mouth, gut, waste, cramp, bone) are the bridge, not decoration.
- **The manual opens, before any wiring, with a full referee-level chapter: "What a system, a stack, a cluster and an
  organism really are"** — translating the whole machine world into the body (skeleton, muscle, nerves, brain, gut,
  immune system, nutrition, waste) so an engineer reads the wiring through the biology. Front matter and back matter in
  full (legal, standards, glossary, file map, troubleshooting, seed/replication).
- **Positioning (front matter):** putting Omni on a system turns an ordinary body into a super-athlete / superhero — not
  one power but all of them at once (speed, strength, endurance, healing, reflexes) — while it stays healthy and lives as
  long as, or longer than, native. The dial lets the owner choose how far past healthy to push, with the bill shown.

## 18. The joint registry — a logged checkpoint at every intersection (chain of custody)
The organism must tell itself, at every joint, what happened: what came in, what ailment it caused, what Omni did about
it, and what went out. A body carries a signal mouth → neck → stomach → shoulder → elbow → wrist → hand → each knuckle,
back and forth; every joint is a checkpoint that records the pass.
- *Engineer:* distributed tracing with a signed, append-only record at every hop (ingress, scheduler, each service, each
  resource grant, each actuator write, each output), carrying one trace id end to end — the way OpenTelemetry spans, a
  service mesh, and an audit log work, unified into one. (v5 already keeps a decision log; this makes it a full chain of
  custody at every joint, not just the brain's own decisions.)
- Each joint record holds: the input it received, its own health at that moment, any ailment it saw (sprain/cramp/
  starvation/indigestion/foreign), the action Omni took, and the output it passed on. The one screen can replay any
  input's whole journey through the body and show exactly where and why it caused trouble and how it was fixed.
- This is also what lets a hurt muscle not slow the body: the registry shows the brain which joints are degraded, so work
  routes around them without a reaction nobody needs — a hurt muscle is worked around, not panicked over.

## 19. Self-repair and the cyborg difference (software heals free; metal wears and a human replaces it)
The organism is half living, half machine, so repair has two kinds, and the manual must make the difference plain:
- **The software/living half heals itself at no wear cost:** restart a crashed process, fail over, re-queue, clear a
  cramp (release a lock, drain a pool), garbage-collect, re-learn a lost memory, route around a degraded joint. These cost
  only a moment, like flesh knitting — Omni does them on its own and logs them.
- **The hardware/metal half wears and cannot be un-worn:** a fan, a disk, a battery, a solder joint, a bearing age with
  heat, cycles and time (the wear gauges, § 3). Omni cannot repair metal — it can only slow the wear (stay cooler, cycle
  less), work around a failing part, and raise the "send a person" alarm. A human replaces the metal.
- The honest line (manual + engine): Omni **contains, works around, and slows** hardware failure, and **fully self-heals**
  software failure; it never claims to mend metal. This is exactly the cyborg: the machine half gives strength and long
  life, the living half gives self-healing, and the brain knows which kind of fix each ailment needs.

## 20. They are muscles, not competitors (the framing correction)
Every "serious player" named in a competitive scan — Karpenter, KEDA, VPA, Oracle Autonomous DB, a data-center cooling AI,
MPC in industry, Autobidder, a chip power manager — is a **native controller**, i.e. a muscle's own reflex. Omni-Compass is
never standalone and never their rival; it is the **supervisory governor that sits on top of each of them** and moves each
to a larger GAIN than it reaches on its own. So they are not competitors to the governor — they are the muscles the governor governs. The
only thing that could be a true competitor is another governor-on-top-of-all-natives across every domain, and none is known.
- **What Omni adds on top = whatever the native left on the table.** On a plain native (fixed HPA target, static power cap,
  a fixed setpoint) there is a lot untapped, so Omni adds a lot. On an already-smart native (a tuned cooling AI, a good
  autoscaler) there is less untapped, so Omni adds less — **and by Do No Harm, where it cannot improve a knob it stays
  native, never below it.** The gain is never negative; it is only ever "how much was left to take."
- This is the honest completion of "Omni makes everything ahead of native": ahead or equal, on every muscle, on top of
  whatever native is there — dumb or smart. The headline number is bigger on the dumb ones; the guarantee holds on all.

## 21. Wire everything, watch everything — push a signal only where it helps (corrected)
EVERY muscle gets wired and watched, always — no muscle is ever dropped from the body. The reason is the same reason there
is a kill switch on things that look 100% solid: **you never know.** What goes in the mouth decides how any limb reacts,
and it can react any way — the wrong input can swell a foot, ache a head, cramp a gut on a muscle that "never needed" Omni.
So the wire must already be there, watching, the instant that muscle is hit.
- What's conditional is only the **active signal**, not the wire. Where a muscle has no headroom to gain right now, Omni
  stays silent on it (near-zero cost — it doesn't tell a finger to scratch when it's already there), but it keeps watching
  at full rate (one eye open), and the moment bad input or a fault makes that muscle need help, the wire is already live
  and Omni acts.
- So: **wire all, watch all, act where it pays.** Do-No-Harm and low overhead come from withholding the *signal* on
  no-gain muscles, never from un-wiring them. "Never behind native" is kept because a watched-but-silent muscle runs
  exactly native until the instant Omni has a reason to move it.

## 22. What is really open to benchmark ON TOP OF (honest source map — so we never claim a closed scalp we didn't take)
The whole method needs the REAL native underneath, not our model of it. Here is what is actually gettable and what is not.
- **Truly open, real code on GitHub — build Omni on top and benchmark for real (no model):**
  Kubernetes HPA / VPA / Cluster Autoscaler / **Karpenter** / **KEDA** (Apache-2.0); GPU serving **vLLM / Triton /
  TensorRT-LLM**; databases **PostgreSQL / MySQL / MongoDB / Redis**; data/stream **Spark / Kafka / OpenSearch / Nginx /
  fio**; observability & immune stand-ins **Prometheus / Alertmanager / Grafana / OpenTelemetry**; cooling/building
  **EnergyPlus / BOPTEST / CityLearn / Sinergym**; battery **PyBaMM**; grid **GridLAB-D / pandapower**; spacecraft
  **NASA F´ (F Prime) / cFS** (open). These are the real muscles; Omni rides them on real clusters/CI/GPU.
- **Closed — the real thing is NOT gettable; we ride an OPEN equivalent and say so plainly (never claim we beat the named
  product):** Google/DeepMind's actual data-center cooling AI (paper only; the trained model + Google's DC telemetry are
  not released → we use EnergyPlus/BOPTEST/Sinergym as the advanced-cooling stand-in); Datadog / Dynatrace Davis /
  New Relic / Moogsoft (commercial SaaS → Prometheus/OTel + open anomaly detection as the stand-in); Oracle Autonomous
  Database (Oracle Cloud only → Postgres auto-tuning as the stand-in); Tesla Autobidder (commercial → open grid/battery
  simulators as the stand-in).
- **The honest rule for the manual and every result:** when the native under Omni is an open stand-in for a famous closed
  system, the result says "on top of <open system>", never "beat <closed product>". We take the scalps we actually take.

## 23. Never assume — closed loop, every step (the first law)
Omni **never assumes a push or a pull worked.** It knows only because the nervous system sends the signal back: it writes
a knob, reads the knob back, then reads the service and the physics the move produced, and only then does it trust and
count the move. No open-loop guessing, ever — if the return signal doesn't come, or doesn't match physics, the move is not
trusted and that muscle goes native (ties to read-back, stale-path, and the physics-sanity checks). Everything is real
time: a living, breathing loop — sense → decide → act → sense the result — running every step, on every muscle that has a
live signal. This is why the whole thing is a **comprehension / convergence control-core-plane engine**: it comprehends
(reads and understands the real state), converges (moves toward the edge without crossing it), and controls from the core
plane over every native muscle — breathing at every step, assuming nothing.
- Consequence for the results: a gain is only ever counted from a *measured* return, never from an intended action. This
  is also what keeps "never behind native" honest — a move that didn't land, or landed wrong, is caught by its own
  return signal and undone, not booked as a win.

## 24. Distributed body — local reflexes, muscle identity, anticipation, signal speed (so it scales and never waits)
The signal moving back and forth through every muscle, nerve, organ, bone and fiber is a huge amount of traffic. It cannot
all round-trip the central brain every tick — that would be slow and would never scale to a million muscles. So the body is
distributed, the way a real one is:
- **Local reflexes (the spinal reflex).** Each muscle and limb has its OWN small brain and its own nerves: it reads itself,
  computes, and acts at the edge, instantly, WITHOUT asking the central brain — a hand pulls off a hot stove before the
  brain hears about it. *Engineer:* a local control loop at each muscle / a sidecar per node, a regional coordinator per
  group (a ganglion), and the central governor (the brain) only for the big picture and the slow decisions. The brain
  sends a signal into the nervous system now and then; the nervous system does its own calculating and proving in between.
  This is what makes it real-time at scale AND answers the overhead concern — most work never reaches the center.
- **Muscle identity (a hand is only a hand).** Every muscle carries its declared type and its one function and its own
  edges, known from the start. A signal built for one type can never be applied to another — anything outside a muscle's
  function is rejected as foreign (this is the hard stop on a mis-routed signal, § 12). Typed muscles, pre-loaded with
  their own job, so none is blind out the gate.
- **Anticipation (ready before it comes).** A muscle does not wait for input to think — it forecasts its own next demand
  (the early-warning model) and pre-positions, so when work arrives the muscle is already set for it. One eye open, leaning
  into where the work is going.
- **Signal speed (the tanh / c bound).** Local reflexes fire in microseconds-to-milliseconds, regional fast, central
  slower — the signal moves as fast as its medium allows, "near the speed of light." The engine's own law bounds how fast a
  knob may move with the tanh/`c` term (compass_law core eq. 4, `c = 1.0`): fast, but never faster than the physics, so it
  converges to the edge without overshooting it. Speed with no overshoot.

## 25. The parts still unmapped — blood, skin, heart, senses (and a completeness check for the lock)
Body map, now complete, before the repo is locked:
- **Skeleton** = physical infra (racks, chassis, power distribution, network backbone, building, vessel).
- **Muscles** = the workers (five abstract types cover essentially every controllable subsystem: a queue/pool, a thermal
  mass, a store, a motion/trajectory, a feedback loop — so a new domain is a new preset, rarely a new type).
- **Nerves** = the signal paths (telemetry in, control out) + the local reflexes and ganglia of § 24.
- **Brain** = the central governor (big picture, slow cadence).
- **Blood** = the data/control plane circulating through everything — the payload data, the telemetry, and the power that
  fuels it, flowing continuously and carrying waste back out. *Engineer:* the message/data bus + the power feed. If the
  blood stops (bus down, power lost), the body is starved — watched as a vital.
- **Heart** = the pump/clock that keeps the blood moving at a steady beat. *Engineer:* the control-loop clock / scheduler /
  broker driving the tick; its rate is the pulse, watched for arrhythmia (missed beats, jitter).
- **Skin** = the boundary between inside and outside — keeps the inside in, the outside out, and feels a touch at the edge.
  *Engineer:* the security perimeter (firewall/WAF, access control, TLS, network boundary) and edge intrusion detection.
- **Senses (eyes/ears)** = the outside signals the body reads to anticipate: demand forecast, price, carbon, weather,
  traffic. Feed the anticipation of § 24.
- **Gut, immune system, wear/health, seed/DNA, kill switch** = as in §§ 3, 12, 16, 8.
- **Honest completeness verdict (corrected against the real catalog, not the scratch sim).** The muscle coverage is
  ALREADY built and broad: **945 muscles in 59 families** across the four realms (`docs/REGISTER.md`, `realms/catalog.csv`,
  `docs/MUSCLE_CATALOG.md`). **AI is front and centre, not an afterthought: family 1 = AI Inference Serving (24 muscles),
  family 2 = AI Training (18 muscles, compute_pool/gpu_batch) — the two biggest AI loads are #1 and #2.** The 59 families
  already span: cloud VM/containers/Kubernetes scaling-placement-scheduling-Karpenter-OpenShift, HPC, GPU hardware/fabric/
  RDMA/DPU, quantum, host CPU/memory, admission shaping; EV/aviation/elevator/marine/rail/robot-fleet/robot-joint/
  spacecraft; agriculture/HVAC/cooling/district-heat/energy-storage-microgrid/facility-grid/grid-T&D/healthcare-env/
  industrial-PLC/mining/oil&gas/pharma-food/power-turbine/renewable-inverter/semiconductor-fab/water; cache/commerce/
  analytics-ETL/database/medical-imaging/messaging-streaming/network-routing/observability/ports/reliability-security/
  runtime/search-vector-DB/service-mesh/storage/telecom-RAN/workflow. The proof program (`docs/REGISTER.md` rows to 63)
  also reaches FHIR/MONAI healthcare, FASTSim EV, Kueue/Volcano AI-batch, swarms, spacecraft (cFS/F´).
- **My earlier error, logged so it isn't repeated:** I said "add AI training as one preset." Wrong — it is already family 2.
  I was speaking from the 5-preset *scratch* organisms (compute/physics/energy/distribution + stack/tower) used only to
  tune the v5 law fast, not from the real 945-muscle catalog. The catalog is not thin; the five *types* are the abstract
  bases, and the 59 families/945 muscles are the real presets already in the repo. A genuinely new domain is a new preset
  under an existing type, rare.
- **What v5 actually ADDS is not muscle coverage (that's done) — it's the body organs and laws:** blood, skin, heart,
  senses, local reflexes/distributed control, the gut/waste, the immune system, wear/health, the dial, Max mode, the joint
  registry, the connectors + one pane + self-wiring. Safety-of-life stays watch-only. With these the body is complete to
  lock and build against; the muscle catalog was already complete.

## 26. The count — 1,097 muscles in 70 families on v5 (built)
Repo truth on branch v5: v5's catalog (`realms/catalog_v5.csv`) is **1,097 distinct muscles in 70 families** — v3's 945 in
59 families (`realms/catalog.csv`, frozen for v3's results) plus two waves. The first wave, **57 new muscles in six new
families**:
- **Linux Kernel & OS Control** (20): cgroup CPU weight, CPU quota and memory.high; the CFS scheduler's latency; the
  cpufreq/DVFS governor; C-states; transparent hugepages and the hugepage pool; the I/O scheduler's depth and the block
  queue; NUMA balancing; dirty-ratio writeback; swappiness; zswap; page-cache reclaim; KSM; irqbalance; TCP buffers;
  receive coalescing; the CoDel queue target.
- **Serverless & Functions (FaaS)** (9), **Virtualization & Hypervisor** (9), **Content Delivery & Edge Cache** (6),
  **Gut: Data-plane Intake & Waste** (8), **Skin: Perimeter & Admission** (5).
The second wave (12 October), **95 muscles**: five new families, **Financial Markets & Trading Systems** (14: matching
engine threads, order gateways and their admission, pre-trade risk workers, market-data fan-out and conflation, FIX
heartbeats, kernel-bypass poll cores, the tick store, settlement, the end-of-day risk batch, the colocation rack's
cooling), **Media Streaming & CDN** (14: the bitrate ladder, the player's buffer, transcoder pools and their clocks and
batch power, packagers, origin shields, edge TTLs, segment length, request coalescing, DRM licence servers),
**Game Servers & Real-Time Interactive** (12: Agones fleet buffer, minimum and maximum, tick rate, players per server,
matchmaking admission and wait window, relays, voice mixers, the game node pool, replay renders, cloud-gaming clocks),
**Blockchain & Ledger Nodes** (10: a node's database cache, mempool, peers, script-validation threads, block relay, the
RPC queue, the UTXO cache flush, indexers, the archive tier, the validator host's power profile; never a consensus rule),
**CI/CD & Build Farms** (10: runner scale sets, build concurrency, build cache, test shards, job admission, artifact
retention, build nodes' clock, remote execution, the warm runner pool); and additions to seven families: security engines
(6, in Reliability, Security & Recovery: an IDS's capture threads, ring buffer and rule groups, a web firewall's
inspection workers, a SIEM's ingest, endpoint scan scheduling), MQTT brokers (4, Messaging & Streaming), DNS and mail
caches (4, Runtime & Application), ROS 2, humanoids and manipulators (8, Robotics Motion Control), warehouse robot fleets
(2), PX4 and ArduPilot drones and swarm spacing (8, Aviation & Autonomous Flight), and edge sites (3, Cross-Cluster,
Multi-Region & Edge). The GPU family is named for the hardware (**GPU Hardware**), and the eight audited families carry
numbers 64 to 71 like every other family.
Each is a distinct real-world knob, modelled on the matching plant template, as v3's 945 already share five templates; AI
Inference and AI Training stay the two biggest compute families. The organisms on v5: Compute / AI / Cloud 530, Physics /
Robotics / Autonomous 394, Energy / Facility / Industrial 470, Distribution / Specialized 474; the stack (all four realms,
the 257-muscle spine counted in each) is **1,868** on v5 (v3: 1,716). The "1,000" elsewhere in the docs is the
1,000-**copy** scale, not a muscle count.
The do-no-harm check runs on all 1,097 (`tests/test_compass_arm_v5.py`); the official table is
`results/realms_v5/REALMS_V5.md` (all six organisms superior within guardrails, 0 of 1,097 behind native; the whole tower saves 0.99% of its energy against v3's 0.33% on the same seeds (3.0 times), the four stacked 0.99% against 0.33% (3.0 times), Energy / Facility 1.00% against 0.33% (3.0 times)). More
families — the SDN/load-balancer fabric beyond routing, more of the body's vitals — raise the count again when built.

## 27. The benchmark program — every run, nothing left out
The map is `docs/omni_v5/BENCHMARKS_V5.md`; one button starts them all (`.github/workflows/v5-all-benchmarks.yml`).
- **The v5 law, modelled:** `realms-v5` — all 1,097 muscles and the six organisms, with the no-harm check.
- **23 free benchmarks on GitHub's machines:** Kubernetes (steady, every lever, full, shadow, add-ons, 50/500/1,000 nodes),
  the six organisms at 1, 10, 100 and 1,000 copies with and without the real cluster inside, the v3 table, CPU power,
  PostgreSQL, MySQL, MongoDB, Redis, Kafka, buildings and grid (CityLearn), the power grid (pandapower), robot arms
  (MuJoCo), drones (PX4 swarms), robustness (Omni killed mid-run, the long run, Omni's own cost).
- **The GPU:** GitHub's T4; **one chip**, the whole preregistered test (`scripts/gpu_rented_run.sh`); **the 1,000 copies**
  of the six organisms with the real card inside; **eight chips** at once (`scripts/gpu_8card.sh`); the **AMD APU** and
  AMD GPUs (`scripts/apu_run.sh`).
- **The clouds:** **Azure AKS**, **Google GKE**, **Amazon EKS** (the same paired design, the bill counted every 15 s at
  list price), and the big organisms on a rented Azure machine.
- The plain truth: the live Kubernetes controller, the GPU governor and the six organisms with a real cluster or card
  inside run v5 (the v5 edge, `omnicompass/edge.py`); the databases' adapters keep their live laws until their own port
  (`docs/omni_v5/BUILD_STAGES.md`, stage 11).

## 28. The babysitting tax — one screen, counted as a benefit
A thousand muscles can mean a thousand dashboards and an engineer babysitting each. Omni collapses that to one screen of
tiles (green, yellow, orange, red) that a couple of engineers watch, with a human override on every tile; the engineer-
hours saved are a counted line on the bill beside energy, work and wear (`docs/omni_v5/CONNECTORS.md`, "One screen, not
a thousand").

## 11. Where the law and its study live
- The law, in the engine (omni-v5): `realms/compass_arm_v5.py`, run by the v5 arm in `realms/harness.py`.
- The study it came from: `docs/omni_v5/study/` (`v5_law.py`, `maxarm.py`, `sweep.py`, `immune.py`).
- The runner `tools/run_realms_v5.py`, the test `tests/test_compass_arm_v5.py`, the table `results/realms_v5/`.

© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. Evaluation and Simulation use only. Any commercialization or
monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the
USA. www.omni-compass.com

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

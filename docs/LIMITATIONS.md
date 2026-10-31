# Limitations and threats to validity

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

What the newest three-run tables (omni-v11's; omni-v23, the engine that stands since 31 October, runs every benchmark again)
can and cannot support, written the way a referee reads a
study: who ran it, what could bias a comparison, what a gauge really measures, how often the reading rule could be fooled,
and how far a result travels. Each limitation names what would remove it. Run and scored by The Omni-Compass LLC's own
code. No outside party has reviewed or approved these results.

## 1. Independence

- **Every run is ours.** The harnesses, the runs, the tables and this page are The Omni-Compass LLC's own; no outside party
  has run, reproduced or reviewed them. What reduces the dependence on us: every table is rebuilt from its raw receipts by a
  public command and compared byte for byte (`tools/reproduce.py`, `reproduce.yml`), every rule was written before its
  runs (`docs/DEVIATIONS.md` lists every later change with its timing), and every raw file carries its SHA-256.
- **What would remove it:** an outside party running the same workflows from a fork, or the paired protocol on its own
  system (`docs/PILOT_PROTOCOL.md`).

## 2. Internal validity: could something other than Omni-Compass explain a difference?

- **Pairing and order.** Each repetition runs native and Omni-Compass back to back on the same machine, alternating which
  goes first. With three pairs a run (the data stores) the order cannot balance (two to one). Where it was checked (the
  Redis tail, `docs/TAIL_LATENCY.md`) the difference held in both orders.
- **The machine moves between runs.** GitHub's free machines differ from run to run. On MySQL's update workload the
  throughput was +0.3% in every pair of run B and −0.4% in every pair of run C, so the row reads "the runs disagree": a
  machine-level effect larger than the change, under an offered rate that pins throughput near 98% of what is offered.
- **One machine under kind.** Every Kubernetes node in the kind tests is a container on one runner; the governor counts that
  machine's processor once (omni-v6) and the served image is pulled onto every worker before each arm (18 October). A
  multi-machine cluster (Azure) is the test of the cloud's own behaviour.
- **The measuring process.** In the Redis harness the brain runs as a thread inside the load generator's own Python
  process, and its once-a-second work shares Python's interpreter lock with the request threads. The 99th percentile there
  reads about 6 µs higher with Omni-Compass in two of three runs. A controlled test shows the cause: the brain's presence in
  the process, with nothing else changed, lengthens the timed requests (99th percentile +101 µs, 10 of 12 pairs; mean +5 µs,
  11 of 12) (`docs/TAIL_LATENCY.md`, section 4). The bias weighs against Omni-Compass, because only its arm carries the
  brain, and no deployment runs the brain inside the application. The next version's harness runs it in a process of its
  own. The other data stores' load generators already run as processes of their own.
- **Simulators that do not reproduce exactly.** CityLearn's comfort score moved by up to 3.6 × 10⁻⁵ between runs in both
  arms alike; PyBullet (the drone swarm) reproduces to about one part in a thousand across GitHub's machines. Rows that do
  not reproduce read "the runs differ", and the tables say when the paired change was exactly zero.

## 3. Construct validity: does each gauge measure what its name says?

- **Energy in the Kubernetes and swarm tables is a declared model**, not a meter (evidence class S inside a live test).
  No physical meter has measured Omni-Compass yet (class P: none), so less energy is **undetermined**.
- **Node-hours on kind are not a bill.** The cloud bill is measured only in the cloud (Azure, running).
- **The modelled muscles and organisms are our own models** (class S): 1,107 muscles, 527 GAIN, 0 LOSS
  (`results/realms_v5/REALMS_V5.md`) say what our models do, never what a real plant does.
- **A margin no gauge judges, and a fault it hid.** In the drone swarm the judged safety gauge is the near miss (two drones
  under half the 0.3 m keep-out, 0.15 m). The closest approach is shown, not judged. With Omni-Compass on top it fell from
  about 0.30 m to as low as 0.156 m (run C, the short cell). There was no near miss and no collision in any counted run, but
  the margin native keeps was spent to fly faster. On mission draws outside the preregistered seeds it read LOSS: on the mixed
  cell with draw 214, the omni-v11 wire let two drones come within 0.083 m, with 5 near-miss ticks and 3 collision ticks, where
  native flew the same draw with none (`results/model_gate/V12_SWARM_REFLEX.md`). A preregistered set of seeds could not show
  it, and only flying draws the wire was never tuned on did.
- **The cause is in the wire, not the brain.** The proximity reflex is written to return the planner's cruise at once. The
  code lowered the speed by 0.01 a tick instead, so a drone that saw a neighbour within 0.5 m flew fast for about a second more.
- **The fix**: the reflex at once, reaching out with the square of the speed, as the stopping distance does. In our own
  flights it held every drone at or outside the full keep-out (the least, 0.304 m), with no near miss and no collision, on all
  ten cells and draws tried, the four preregistered cells and six untouched draws. It kept 49% to 92% of the energy cut.
- **What came with it.** The fix landed in omni-v12 (`docs/OMNI_V12.md`), and the same version's preregistration amendment
  (`docs/SWARM_PREREGISTRATION.md`, amendment 2, written before its runs) makes a collision with Omni-Compass on top a judged
  LOSS row, voids a cell only when native itself collides, and adds three mission draws no wire was ever run on.

## 4. Statistical conclusion validity: how often could the reading rule be fooled?

- **The three-run rule is strict.** A row reads GAIN or LOSS only when three separate runs all move the same way with every
  95% interval clear of zero. With no true change, and runs independent, one run's interval is clear of zero on a given side
  with probability 0.025, so a false GAIN or LOSS in a row has probability 2 × 0.025³ ≈ 3.1 × 10⁻⁵. Over the 1,039 judged
  rows of the omni-v11 tables the expected number of false readings is at most 0.03. Of those rows, 613 are in tests that
  carry noise; the other 241 are in deterministic simulators, which reproduce to the digit. Over the 613 the expectation is
  0.02. Runs share the harness, so they are not fully independent of it; the number is a guide, not a guarantee.
- **STEADY is not zero.** A row reads STEADY when the test could not resolve a change; `docs/POWER.md` gives, for every judged
  row, the smallest change all three runs would detect. Many data-store rows (three pairs a run) cannot resolve a change
  under 10% of native; STEADY there means "no change larger than that", and nothing finer is claimed.
- **Rows where the runs disagree** (omni-v11): MySQL's update throughput (above), CityLearn's comfort score in two districts
  (CityLearn's own drift; the paired change exactly zero), and the drone swarm's closest approach, tracking error and
  cruise override (PyBullet's reproduction; the first is the margin of section 3, the other two are shown, not judged).
- **A fixed set of seeds is a sample, not a guarantee.** Every preregistered test runs on seeds written before its runs, so a
  reading holds for those draws. The swarm's collisions (section 3) appeared only on a draw outside them. The swarm's omni-v12
  runs add three draws never flown (amendment 2); the other tests still run on their fixed seeds alone.

## 5. External validity: how far does a result travel?

- **Loads.** Open-loop load generators on synthetic schedules, one public day of demand (Google 2011) on kind, and the data
  stores' published benchmark workloads (sysbench, YCSB, pgbench). No production traffic.
- **Size.** kind clusters of six workers on one machine; an Azure cluster of four workers. No large production fleet.
- **Undetermined:** the cloud bill (Azure running, Google and Amazon gated by their $0 checks), energy (no meter), the GPU
  (no run on the engine that stands), production readiness (no deployment). These are written as undetermined wherever
  they appear, never as results.

## 6. The engine changed often

Twelve versions in twelve days (omni-v5 to omni-v16, `docs/CHANGE_CONTROL.md`), each through omni-v15 a fault found in a real
run and fixed, and omni-v16 the decision pace made a clean setting on the founder's word.
No table mixes engines, and each benchmark runs again on every version; the cost is that each version's three-run tables
take a day or more to land, so the newest tables of some benchmarks are an older engine's until they do.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

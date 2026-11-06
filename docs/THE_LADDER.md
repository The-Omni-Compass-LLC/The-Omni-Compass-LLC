# The ladder: 1, 10, 100 and 500, for runs and for organisms alike

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The founder's order of 25 October: "the 1, 10, 100, 500 is really nothing more than the 500 run broken into 100 and then a 10 into
a 1. So it's the full 500. When somebody says 100 clicks, they only get the 100. They click a 10, they only get 10. They click 1,
they get the 1. The same thing with the 500 organisms. It's a whole stack of organisms that got cut down to 100, a 10 and a 1."

## 1. In plain words

There is one set of 500 runs and one stack of 500 copies of an organism. Every smaller rung is the front of the same thing: the
first 100, the first 10, the first 1. Nothing at a smaller rung is drawn, seeded or built apart from the 500. Press 100 and you
get those 100 and no others; press 10, those 10; press 1, that one.

## 2. The rungs

    L = {1, 10, 100, 500},   1 < 10 < 100 < 500

## 3. The runs

Run k has the seed of the jump generator and the stream the live engine's page uses (`tools/engine_runs.py`):

    seedₖ = (base + k · 0x9E3779B9) mod 2³²,   k = 0, 1, …, 499

The rung of N runs is the set of the first N:

    R_N = { 0, 1, …, N − 1 },   R₁ ⊂ R₁₀ ⊂ R₁₀₀ ⊂ R₅₀₀

Each run k leaves one receipt rₖ (the brain's final state after 288 decisions integrated by RK4, the compass law's 80 steps, one
give-back trial judged by the verdict). The canonical line canon(rₖ) writes its numbers in one order, six decimals. Each rung has
its own digest:

    D_N = SHA-256( canon(r₀) ‖ "\n" ‖ canon(r₁) ‖ "\n" ‖ … ‖ canon(r_{N−1}) )

The proof of the three engines is that the three digests agree at every rung:

    D_N(Python) = D_N(C++) = D_N(the page),   for every N ∈ L

Because R₁ ⊂ R₁₀ ⊂ R₁₀₀ ⊂ R₅₀₀, the rung of 100 is not a separate experiment: it is the first 100 lines of the 500-run record, and
its digest is computed from those lines alone.

## 4. The organisms

An organism is a set of muscles drawn from the catalog (the spine, a realm, the four stacked, the whole tower). Its copy c is the
same muscles with c written into each muscle's name (`muscle_id~c`, copy 0 the bare name), every plant seeded from the run's seed
and its own name, so copy c is the same plant whatever the size of the stack it sits in. With B the organism's muscles in catalog
order, the stack of M copies lists them copy by copy:

    S_M = [ B₀, B₁, …, B_{M−1} ],   Bc = B with each name marked ~c

and the stacks nest exactly as the runs do:

    S₁ ⊂ S₁₀ ⊂ S₁₀₀ ⊂ S₅₀₀,   S_M = the first M · |B| muscles of S₅₀₀

(`tests/test_run_scale.py`, `TheStackCutDown`, checks it muscle for muscle.)

## 5. Two readings of a rung of copies, both from the same stack

**The organism of M copies on its own clock** (the grid's square of M copies): the first M copies of the stack, run as one body.
Copies inside one body are coupled on every step (`realms/harness.py`, `Body.couple`: the body's shared supply and its immune
system), so this is the M-copy organism living by itself.

**The stack cut down** (the founder's reading): the 500-copy stack run whole, then read at its first M copies, plant for plant:

    work_M = mean over the plants of S_M of (work with Omni-Compass ⁄ work with native)
    energy_M = Σ_{plants of S_M} energy with Omni-Compass ⁄ Σ_{plants of S_M} energy with native
    misses_M = (Σ violations with Omni-Compass ⁄ Σ steps) − (Σ violations native ⁄ Σ steps), in points, over S_M

Every run of more than one copy writes both: its own reading and its cuts at each smaller rung (`tools/run_scale.py`, `cuts_of`,
the table "The stack cut down"). The two can differ, and the difference is physics, not error: inside the 500-copy body the first
100 copies share the body with 400 more.

## 6. Where it is coded

| Place | Runs ladder | Organisms ladder |
|---|---|---|
| The Python (`tools/engine_runs.py`) | the record's `ladder`: D_N for N ∈ L, the Python's and the C++ harness's | — |
| The C++ harness (`cpp/tools/engine_runs.cpp`) | one canonical line a run, so D_N(C++) is its first N lines | — |
| The live engine page | the ladder buttons 1 · 10 · 100 · 500 on its own run of the Python's set, and the ladder table (the three digests a rung) | the grid monitor: 1, 10, 100 and 500 copies × 1, 10, 100 and 500 runs |
| The grid (`scripts/dispatch_grid.py`, `six.yml`, `six-kube.yml`) | nested runs 1, 10, 100, 500 | copies 1, 10, 100, 500 on GitHub's free runners |
| The organism runner (`tools/run_scale.py`) | the first N runs of a set | the stack cut down: the first 1, 10, 100 copies of every larger run |

Paid cloud and GPU runs stay at 1, 10 and 100 copies with at most 100 repetitions (the founder's order of 12 October, kept for
everything that costs money).

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

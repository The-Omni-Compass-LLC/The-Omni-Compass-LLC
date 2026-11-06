# The two bills: four arms, the bill and the work done inside it

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The founder's design of 1 November 2026: the same work measured against what it cost, on the two bills a customer pays. **A**, the chip native, and **B**, the chip with Omni-Compass on native: a rented graphics card run directly, its bill the rental. **C**, the cloud native, and **D**, the cloud with Omni-Compass on native: Kubernetes on Azure's machines, its bill Azure's own at list price. The question for each bill: is it the same, and is more work done inside it. Each arm's runs are labelled run 1, 2 and 3 so the run letters never meet the arm letters. Every number is read from a table the repository already holds, each place on its own engine; nothing here is a new measurement.

## The one equation: work for the bill

The founder's words of 2 November: what the receipts of the chips and the clouds show in the end is how much work is done inside the bill natively and how much with Omni-Compass on native, and the one thing to prove is more work for the bill. For a place p (the chip, run directly; or the cloud) and an arm a (native, or Omni-Compass on native), on the same offered load over the same window:

- W(p, a): the work done (the requests served, the jobs finished);
- B(p, a) = Σₖ c(p, a, k): the bill, every cost component k inside the place's own boundary (on the chip, the rental for the arm's window; in the cloud, every machine it bills at the cloud's own price);
- E(p, a) = W(p, a) / B(p, a): the work for each dollar.

The benefit in a place is

    G(p) = E(p, Omni-Compass) / E(p, native) − 1 = (1 + ΔW(p)) / (1 + ΔB(p)) − 1,

where ΔW(p) = W(p, Omni-Compass) / W(p, native) − 1 is the work Omni-Compass added and ΔB(p) = B(p, Omni-Compass) / B(p, native) − 1 is the bill it moved. In logarithms the two sides add:

    ln(1 + G) = ln(1 + ΔW) − ln(1 + ΔB),

so every benefit lives on one side or both: more work inside the bill (ΔW above zero), or the same work for a smaller bill (ΔB below zero). A bill that rises is power given, and the place gains only where the work rises more (G above zero).

**The four arms.** A is the chip native, B the chip with Omni-Compass on native, C the cloud native, D the cloud with Omni-Compass on native, so G(chip) = E(B) / E(A) − 1 and G(cloud) = E(D) / E(C) − 1.

**Where each place's benefit can live.**

- **On the chip** (a card rented directly): the price of an hour is fixed and both arms rent the same window, so ΔB is near zero and G(chip) is near ΔW: the benefit is the work the card does in the time already paid for.
- **Through the cloud**: B is the sum over the machines it bills of machine-hours times the cloud's price for each, with the cloud's own services inside that price; Omni-Compass moves the machines kept in service (a machine parked while idle leaves the bill) and the work each machine does, so both sides can move.
- **The places are never added or set against each other.** The same work carries a different bill in each place (a cloud's price holds its own services and margin over the silicon), so each G is a ratio inside its own place, read the same way in both, and one place's price never enters another's reading.

**Layers inside one place.** Where Omni-Compass governs two layers of one stack (the software end on top of the chip it runs on), the work for the bill composes, 1 + G(stack) = (1 + G(software end)) × (1 + G(chip)), when the two layers' effects do not overlap. That product is a composition of two measurements and is written as one; the stack's own run is the measurement.

**The bill's line items** (the founder's checklist of 2 November: build each place's receipt line by line, so the two bills compare like for like). B is the sum of the place's own line items for the window; what each place charges for each, and what these runs meter:

| Line item k | On the chip, run directly (a rented card) | Through the cloud | Metered in these runs |
|---|---|---|---|
| the machine (compute) | a flat rate for the hours rented, the same whether the card runs full or idle | an hourly rate for every hour each machine is on, billed by the second | yes: the rental for each arm's window; the machine-hours at the cloud's list price |
| data out (egress) | a large allowance or a flat port in the rental | a fee for every gigabyte that leaves the cloud | not metered: both arms serve the same offered load, so the same data leaves in both |
| storage and its speed (IOPS) | the drives inside the rented machine, in its rate | a fee a gigabyte stored, and one for the speed provisioned | not metered: both arms hold the same data on the same disks |
| the labor to run it | the operator's own staff | much of it inside the cloud's price | not counted; Omni-Compass's own processor is counted, as power given, beside each run |

**What Omni-Compass can move, term by term.** The work done in a window is W = C × (1 − V) × U: C the work one chip can do in the window fed all through it, V the share the place's own software layer takes before the work reaches the chip (a cloud's virtual machines and orchestration; none on a card run directly), U the chip-time kept fed in the window, counted in chip-windows (one chip fed all through the window is 1; a machine parked is fed none of the time it is parked). Inside one place both arms run the same chips under the same layer, so C and V are the same in both and cancel: ΔW = U(Omni-Compass) / U(native) − 1, the utilization Omni-Compass wins (the chip fed, the queue drained, the machines in service doing work). The bill, line by line: on a card rented directly B = the rate × the hours rented, the same in both arms, so ΔB = 0 and G(chip) = U(B) / U(A) − 1; through a cloud B = R × H + (data out × its rate) + (storage × its rate) + the cloud's other metered services, and of these Omni-Compass moves H, the machine-hours kept on (a machine parked while idle leaves the bill and takes no fed time with it), the others the same in both arms for the same workload, so G(cloud) = (U(D) / U(C)) × (B(C) / B(D)) − 1: the same work for fewer machine-hours is a GAIN, and so is more work for the same hours. Omni-Compass moves no C (the chip's own speed) and no V (the place's own layer, and the path the data takes through it). C and V differ between places and are why the same work carries a different bill in each: the places are never set against each other, and a figure for any place's V or price that this repository did not measure is never written as one of its own.

A line item the same in both arms adds the same dollars to both bills: it leaves ΔW as it is and draws ΔB toward zero, so a receipt drawn inside a wider boundary reads a smaller bill change for the same work change. Each table names its boundary; a line item not metered stays written as not metered, never filled with a guessed price.

**How a G is judged.** Each run's G is read by the one key across the three runs (`tools/readings.py`): from 0.5% up, GAIN where the work for the bill rose and LOSS where it fell, in all three runs or by their mean; STEADY under the floor; the runs disagree where clear runs point opposite ways.

**The equation's cells today**, each read from its place's own table on its own engine:

| Place and arms | Run | W, native → Omni-Compass | ΔW | B ($), native → Omni-Compass | ΔB | E (work per $), native → Omni-Compass | G |
|---|---|---|---|---|---|---|---|
| the chip, A against B (omni-v23) | 1 | 2,616 → 2,656 | +1.51% | 0.1194 → 0.1195 | +0.04% | 21,909 → 22,229 | +1.46% |
| the chip, A against B (omni-v23) | 2 | 2,270 → 2,286 | +0.73% | 0.1189 → 0.1189 | ±0.00% | 19,089 → 19,229 | +0.73% |
| the chip, A against B (omni-v23) | 3 | 2,255 → 2,239 | −0.70% | 0.1189 → 0.1189 | −0.01% | 18,964 → 18,833 | −0.69% |
| the cloud, C against D (omni-v18, Azure) | one set of 97 | not counted in that set | | 0.05626 → 0.05694 | +1.21%, inside the noise | not read | not read |
| the cloud, C against D (Google, Amazon) | | not yet run | | | | | |

**What it reads today.** On the chip the three runs' G read **the runs disagree**: the work for the bill has not yet been shown to rise. In the cloud the work was not counted in the set that stands, so G is not read. The runs that read it next are started or queued: the card fully loaded with the seven organisms, the eight-card machine, and the cloud at the max with its work meter, each read by this equation as it lands.

## The chip: A against B (an NVIDIA A10 on Lambda, omni-v23, three runs)

From `results/gpu/V23_A10_CAP_FULL_ABC.md` (runs 41243352339, 41243355485, 41243358705): the full load, more requests offered than the card serves in its window, so the work done can rise inside the same rented time. The bill is the rental for each arm's own window (its energy over its mean power) at $1.29 an hour, the price each launch printed (`docs/RUN_LEDGER.md`); Lambda's billing page is the exact figure. Beside it, the same runs' fixed job (`results/gpu/V23_A10_CAP_ABC.md`, a set number of requests in each window, so the work cannot rise): requests served STEADY, the same; energy STEADY, under the floor (the three runs' mean 0.38%).

| Gauge | Three runs | Run 1 | Run 2 | Run 3 |
|---|---|---|---|---|
| bill ($, the rental for the arm's window) | **STEADY, under the floor (the three runs' mean 0.01%)** | STEADY, 0.04% | STEADY, 0.00% | STEADY, 0.01% |
| work done (requests served) | **the runs disagree** | GAIN, 1.51% | GAIN, 0.73% | LOSS, 0.70% |
| work per dollar (requests served per $) | **the runs disagree** | GAIN, 1.46% | GAIN, 0.73% | LOSS, 0.69% |
| energy, GPU (J) | **GAIN in all three of our runs** | STEADY, 0.31% | GAIN, 0.63% | GAIN, 1.48% |
| energy per served request (J) | **GAIN in all three of our runs** | GAIN, 1.79% | GAIN, 1.35% | GAIN, 0.78% |
| response time, 95th percentile (ms) | **the runs disagree** | GAIN, 3.68% | GAIN, 1.38% | LOSS, 2.25% |

| Run | Arm | Window (s) | Bill ($) | Requests served | Requests per $ |
|---|---|---:|---:|---:|---:|
| 1 | A, native | 333.2 | 0.1194 | 2,616 | 21,908.8 |
| 1 | B, Omni-Compass on native | 333.4 | 0.1195 | 2,656 | 22,229.5 |
| 2 | A, native | 331.8 | 0.1189 | 2,270 | 19,089.3 |
| 2 | B, Omni-Compass on native | 331.8 | 0.1189 | 2,286 | 19,229.1 |
| 3 | A, native | 331.9 | 0.1189 | 2,255 | 18,963.8 |
| 3 | B, Omni-Compass on native | 331.8 | 0.1189 | 2,239 | 18,832.8 |

## The cloud: C against D (Kubernetes on Azure's AKS, omni-v18, one set of 97 paired repetitions)

From `results/live/AKS_STEADY_100_OMNI_V18.md`, the newest cloud set with a metered bill. The engine that stands has not yet run in the cloud: its set starts when Azure's current long set ends, and this row is then read again on it.

| Gauge | C, native | D, Omni-Compass on native | The change | 95% interval | Beyond the noise |
|---|---:|---:|---|---|---|
| bill at list price ($ a window) | 0.05626 | 0.05694 | 1.21% (power given, inside the noise) | -0.00071 to +0.00208 | no |
| machines billed (machine-hours a window) | 0.5860 | 0.5931 | 1.21% (power given, inside the noise) | -0.0074 to +0.0216 | no |

This set counted no work done: the cloud's work meter came with the cloud sets after 31 October, so its work per dollar is not read here; the set on the engine that stands reads it.

## The seven organisms in the four arms

Each organism runs native and with Omni-Compass on native in each place: on the chip, A against B, and through the cloud, C against D. Every cell is a three-run reading by the one key of the card's own receipts with the organism running around it: the requests the card served (the work), the rental for the arm's window (the bill) and the two together (work per dollar); the organism's modelled plants are in each place's own table, never in these cells.

### The chip: eight A100 cards on Lambda, each organism on its own card

From `results/gpu/V23_A100_8CARD_STACKS_ABC.json` (omni-v23; runs 41271477833, 41279081905, 41271481737). The card governor's writes, from its own audit in each Omni-Compass arm: A 0 in 15 arms, B 0 in 12 arms, C 0 in 12 arms; it wrote nothing on the card, so on the card the two arms were one system, and a change read in these cells is the order of the arms and the card's own drift, not the engine.

| Organism | Copies | work done (requests served) | bill (the rental for the window) | work per dollar |
|---|---:|---|---|---|
| Compute / AI / Cloud | 1 | one repetition in a run: shown, not judged | one repetition in a run: shown, not judged | one repetition in a run: shown, not judged |
| Compute / AI / Cloud | 10 | one repetition in a run: shown, not judged | one repetition in a run: shown, not judged | one repetition in a run: shown, not judged |
| Compute / AI / Cloud | 100 | one repetition in a run: shown, not judged | one repetition in a run: shown, not judged | one repetition in a run: shown, not judged |
| Physics / Robotics / Autonomous | 1 | one repetition in a run: shown, not judged | one repetition in a run: shown, not judged | one repetition in a run: shown, not judged |
| Physics / Robotics / Autonomous | 10 | one repetition in a run: shown, not judged | one repetition in a run: shown, not judged | one repetition in a run: shown, not judged |
| Energy / Facility / Industrial | 1 | no value | no value | no value |
| Energy / Facility / Industrial | 10 | no value | no value | no value |
| Energy / Facility / Industrial | 100 | no value | no value | no value |
| Distribution / Specialized | 1 | no value | no value | no value |
| Distribution / Specialized | 10 | no value | no value | no value |
| Distribution / Specialized | 100 | no value | no value | no value |
| The four stacked | 1 | one repetition in a run: shown, not judged | one repetition in a run: shown, not judged | one repetition in a run: shown, not judged |
| The four stacked | 10 | one repetition in a run: shown, not judged | one repetition in a run: shown, not judged | one repetition in a run: shown, not judged |
| The whole tower | 1 | one repetition in a run: shown, not judged | one repetition in a run: shown, not judged | one repetition in a run: shown, not judged |
| The whole tower | 10 | one repetition in a run: shown, not judged | one repetition in a run: shown, not judged | one repetition in a run: shown, not judged |

### The chip: one A10 on Lambda, the card fully loaded inside the organism (docs/GPU_PREREGISTRATION.md, amendment 16)

From `results/gpu/V23_A10_STACKS_FULL_ABC.json` (omni-v23; runs 41271470803, 41271473309, 41271475877). The card governor's writes, from its own audit in each Omni-Compass arm: A 0 in 62 arms, B 0 in 62 arms, C 0 in 62 arms; it wrote nothing on the card, so on the card the two arms were one system, and a change read in these cells is the order of the arms and the card's own drift, not the engine.

| Organism | Copies | work done (requests served) | bill (the rental for the window) | work per dollar |
|---|---:|---|---|---|
| The spine | 1 | LOSS by the mean of our three runs, beyond the noise in 0 of 3 | STEADY, under the floor (the three runs' mean 0.01%) | power given by the mean of our three runs, beyond the noise in 0 of 3 |
| The spine | 10 | STEADY, under the floor (the three runs' mean 0.12%) | STEADY, under the floor (the three runs' mean 0.00%) | STEADY, under the floor (the three runs' mean 0.13%) |
| The spine | 100 | one repetition in a run: shown, not judged | one repetition in a run: shown, not judged | one repetition in a run: shown, not judged |
| Compute / AI / Cloud | 1 | STEADY, under the floor (the three runs' mean 0.01%) | STEADY, under the floor (the three runs' mean 0.01%) | STEADY, under the floor (the three runs' mean 0.00%) |
| Compute / AI / Cloud | 10 | STEADY, under the floor (the three runs' mean 0.18%) | STEADY, under the floor (the three runs' mean 0.01%) | STEADY, under the floor (the three runs' mean 0.17%) |
| Compute / AI / Cloud | 100 | one repetition in a run: shown, not judged | one repetition in a run: shown, not judged | one repetition in a run: shown, not judged |
| Physics / Robotics / Autonomous | 1 | STEADY, under the floor (the three runs' mean 0.30%) | STEADY, under the floor (the three runs' mean 0.01%) | STEADY, under the floor (the three runs' mean 0.29%) |
| Physics / Robotics / Autonomous | 10 | LOSS by the mean of our three runs, beyond the noise in 0 of 3 | STEADY, under the floor (the three runs' mean 0.00%) | power given by the mean of our three runs, beyond the noise in 0 of 3 |
| Physics / Robotics / Autonomous | 100 | one repetition in a run: shown, not judged | one repetition in a run: shown, not judged | one repetition in a run: shown, not judged |
| Energy / Facility / Industrial | 1 | STEADY, under the floor (the three runs' mean 0.03%) | STEADY, under the floor (the three runs' mean 0.01%) | STEADY, under the floor (the three runs' mean 0.04%) |
| Energy / Facility / Industrial | 10 | STEADY, under the floor (the three runs' mean 0.23%) | STEADY, under the floor (the three runs' mean 0.00%) | STEADY, under the floor (the three runs' mean 0.22%) |
| Energy / Facility / Industrial | 100 | one repetition in a run: shown, not judged | one repetition in a run: shown, not judged | one repetition in a run: shown, not judged |
| Distribution / Specialized | 1 | STEADY, under the floor (the three runs' mean 0.01%) | STEADY, under the floor (the three runs' mean 0.00%) | STEADY, under the floor (the three runs' mean 0.01%) |
| Distribution / Specialized | 10 | STEADY, under the floor (the three runs' mean 0.16%) | STEADY, under the floor (the three runs' mean 0.00%) | STEADY, under the floor (the three runs' mean 0.16%) |
| Distribution / Specialized | 100 | one repetition in a run: shown, not judged | one repetition in a run: shown, not judged | one repetition in a run: shown, not judged |
| The four stacked | 1 | STEADY, under the floor (the three runs' mean 0.02%) | STEADY, under the floor (the three runs' mean 0.01%) | STEADY, under the floor (the three runs' mean 0.03%) |
| The four stacked | 10 | STEADY, under the floor (the three runs' mean 0.03%) | STEADY, under the floor (the three runs' mean 0.00%) | STEADY, under the floor (the three runs' mean 0.03%) |
| The four stacked | 100 | one repetition in a run: shown, not judged | one repetition in a run: shown, not judged | one repetition in a run: shown, not judged |
| The whole tower | 1 | STEADY, under the floor (the three runs' mean 0.00%) | STEADY, under the floor (the three runs' mean 0.01%) | STEADY, under the floor (the three runs' mean 0.01%) |
| The whole tower | 10 | LOSS by the mean of our three runs, beyond the noise in 0 of 3 | STEADY, under the floor (the three runs' mean 0.00%) | power given by the mean of our three runs, beyond the noise in 0 of 3 |

### Through the cloud: Azure, one rented machine with the real cluster inside each organism

Not yet read: big-organism-detached, run 41269562586 (100 copies, three repetitions).

### Through the cloud: Google Cloud

Not yet run: its key is not in the repository's secrets (docs/GOOGLE_SETUP.md).

### Through the cloud: Amazon Web Services

Not yet run: its key is not in the repository's secrets and the account is on the Free plan (docs/AMAZON_SETUP.md).

## What the two bills say today

- **The chip:** the bill STEADY, under the floor (the three runs' mean 0.01%) (the same rented window in both arms); the work done inside it the runs disagree; the work per dollar the runs disagree; the energy for each request served GAIN in all three of our runs.
- **The cloud:** the bill 1.21% higher with Omni-Compass on native, inside the noise; the work done was not counted in that set, so the work per dollar waits for the set on the engine that stands.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

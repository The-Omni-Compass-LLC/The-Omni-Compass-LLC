# Work for the Bill: the One Number the Receipts Prove

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

What the receipts of the chip and of the clouds must show is how much work is done for the bill, native against Omni-Compass on native (the founder's words of 2 November). This page writes it as one equation, reads every term from a receipt the repository holds, and says where the benefit lives and where it is counted. Nothing here is a new measurement.

## The equation

    E(p, a)  = W(p, a) / B(p, a)                       work done for each dollar of the bill, in place p, arm a
    G(p)     = E(p, omni) / E(p, native) − 1           the benefit in place p: more work for the bill when G(p) > 0
             = (1 + w(p)) / (1 + b(p)) − 1             w = ΔW(p): the change in the work done; b = ΔB(p): in the bill
             ≈ w(p) − b(p)                             for small changes; exactly ln(1 + G) = ln(1 + w) − ln(1 + b)
    G(total) = Σₚ S(p)·(1 + w(p)) / Σₚ S(p)·(1 + b(p)) − 1
                                                       for an owner who runs work in both places: S(p) the owner's own
                                                       native spend in place p over one period, never the benchmark
                                                       windows; a system in one place reads that place's G alone
    B        = Σₖ cₖ,   b = Σₖ sₖ·bₖ,   sₖ = cₖ(native) / B(native)   the bill as the sum of its components

The letters are those of `results/TWO_BILLS.md` ("The one equation"), with w and b short for ΔW and ΔB. W is the work done as each place's own receipt counts it: on the chip the requests served within the arm's fixed window (the card's receipt counts no response line); through the cloud the requests answered inside the response line (the work meter). B is the bill: on bare metal the card's metered window at Lambda's launch price, $1.29 an hour (seconds × the price, computed by `tools/two_bills.py`, not a billing statement; the same window bills nearly the same, so b ≈ 0 and G ≈ w); through the cloud the cloud's own bill at list price (machine-hours × the price). A bill that rises is power given; there is more work for the bill when the work rises more than the bill (w > b, G > 0). G(total) is the places' own G weighted by the owner's spend, so it always lies between them.

**Why the places' prices do not move G.** A cloud usually bills far more than bare metal for the same work on the same silicon (its margin, the software it wraps around the machine, egress and storage fees, paying only for the hours used). Inside one place both arms pay the same prices, so the price level cancels in G(p): with the bill B = Σₖ πₖ·qₖ (prices πₖ, quantities qₖ), b = Σₖ sₖ·(qₖ(omni)/qₖ(native) − 1) depends on the quantities alone. A component Omni-Compass does not move (egress, storage, a managed service's fee) has bₖ = 0 and only dilutes b toward 0; the cloud receipt read so far prices the machine-hours alone, at list price, so its b is the compute bill's. The places' price levels enter only G(total), through the owner's spend S(p), and the owner's choice of place, which Omni-Compass does not make.

## Where the benefit lives and where it is counted

| | Bare metal (arms A and B) | Through the cloud (arms C and D) |
|---|---|---|
| What Omni-Compass writes in the receipts read so far | the card's own power limit and clock ceiling, under the operator's cap, through the card's published interface (the service's queue is its signal, not a knob it writes) | the machines alone, at the tune-down (the omni-v18 set); the sets at the max add the cluster's pods and their room, with the cloud's own autoscaler under them |
| Where the benefit shows | the requests the card completes in the same metered window | the requests answered inside the line, on the machines the cloud bills |
| The bill B | the card's rental for the window (the same hours in both arms) | the cloud's own bill at list price |
| The work W | requests served in the window (the card's own receipt; no response line) | requests answered inside the line (the work meter) |
| The second receipt | the card's own meter: energy for each request served | the machine-hours beside the bill |

**What a place sets and what Omni-Compass moves.** Write the work as W = C·(1 − Vₒ)·U·t: C the chip's raw capacity, Vₒ the share a place's own software layer takes (0 on bare metal; a hypervisor's and an orchestrator's share in a cloud), U how much of what is left becomes served work, t the time. Write the cloud's bill as B = R·H + E·Rₑ + S·Rₛ + I (the hourly rate × the hours on, egress × its rate, storage × its rate, the metered extras) and bare metal's as B = M + L (the lease and the owner's own staff). Inside one place C, Vₒ, t and every rate are the same in both arms, so they cancel: w = U(omni)/U(native) − 1, and b moves only through the quantities Omni-Compass changes, the hours H in a cloud (E only as the work grows) and nothing of M + L on bare metal (so b = 0 there and G = w). The place sets C, Vₒ and the prices; Omni-Compass moves U and, in a cloud, H. Which place costs less for the same work (a cloud for a few hours a month, bare metal for a box busy all day) is the owner's choice of place, not a benefit of Omni-Compass.

**How Omni-Compass can lower a cloud's bill, and what it does not do.** A cloud bills every hour a machine is on, busy or idle. Omni-Compass's levers there are the ones the Kubernetes API already accepts (the Operator's Manual, 14.5): it closes to new work and parks machines the cloud's own autoscaler made but the work does not need, so the autoscaler can remove them and the idle hours stop being billed (b falls); it moves the autoscalers' targets so pods are ready ahead of the load, and it gives a pod the processor its machine can spare, so less work waits and more is answered inside the line (w rises). It holds no cloud credential and asks the cloud for no machine. It does not reorder data in memory, fill a chip's cache, change a network or make silicon faster; and no cut of a cloud's hours has been measured yet (the one set read so far moved its machine-hours up 1.21%, inside the noise).

## The bill, line by line

The bill is the sum of its line items, B = Σₖ cₖ, and each item's change counts by its share of native's bill, b = Σₖ sₖ·bₖ. Which items Omni-Compass can move, and which the receipts read so far have priced:

| Line item | Through the cloud: how it is billed | Moved by Omni-Compass? | Bare metal: how it is billed | Moved by Omni-Compass? |
|---|---|---|---|---|
| The server (compute) | by the second: machine-hours × the hourly price | yes: the machines it parks and wakes, the pods it places (priced in the cloud receipt read so far, at list price) | a flat lease or a rental by the hour for the same box | no: the same box in both arms, so this item holds and G ≈ w (priced in the chip receipt: the metered window at $1.29 an hour) |
| Electricity | inside the price | no line of its own | paid by the owner where the box sits on its own meter | yes: the card's own meter reads the energy for each request served (GAIN in all three A10 runs); not priced in the receipt, a line an owner adds at its own rate |
| Data out (egress) | per gigabyte that leaves the cloud | only through the work: more requests served can send more data out, a rise proportional to the work (not priced in the receipt read so far) | an allowance or a flat port | no, inside the allowance |
| Storage and its speed | per gigabyte stored, plus the speed tier bought | no (not priced) | inside the box | no |
| The people who watch and tune the stack (on call, triage, hand tuning) | the owner's staff (a cloud's own operations sit inside its price) | through the pages: the alert minutes (the minutes an on-call page would be open) fell 7.4% over 41 real Kubernetes tests on omni-v25, fewer in 15, to none in 3 (`results/OVERSIGHT.md`); the hours and pay are the owner's own line, on no receipt | the owner's staff | the same |

So the receipts read so far price the item Omni-Compass moves most in each place (the cloud's machine-hours; the chip's window), and leave out items it does not move. An item it does not move has bₖ = 0 and only pulls b toward 0, so an owner's full bill shows a smaller b than the compute line alone; an item that grows with the work (egress) takes back a share of w in the cloud, and an owner's own electricity rate gives bare metal a second line where the card's energy cut is paid back.

## Reading your own bill: a worked example

The prices below are an owner's example (a three-node cluster, the founder's illustration of 2 November), not a result; the changes put through them are only what the receipts measured. Each place is read on its own.

| Example | Its bill, line by line (native) | What Omni-Compass can move | Read through the equation |
|---|---|---|---|
| Bare metal, always on | the lease $500 a month (egress and storage inside the box) | none of the bill: the same boxes in both arms, b = 0 | G = w, the work the same boxes serve: on the A10's receipts w was +1.51%, +0.73%, −0.70%; at native's price per unit of work that is $7.53, $3.66, −$3.50 of work a month out of the same $500, and the three runs disagree |
| Through the cloud, always on | compute 720 h × $4.50 = $3,240, egress 500 GB × $0.08 = $40, storage $30: $3,310 | the hours (the machines it parks and wakes), 97.9% of this bill; egress only as the work grows; storage not at all | b ≈ 0.979 × the change in machine-hours; the one cloud set read so far moved its machine-hours +1.21% (inside the noise, at the tune-down on the machines alone) and did not count its work, so G is not read |
| Through the cloud, weekends only (40 h) | compute 40 h × $4.50 = $180, egress 50 GB × $0.08 = $4, storage $30: $214 | the hours, 84.1% of this bill | the same reading: b ≈ 0.841 × the change in machine-hours |

Which place is cheaper for the same work (the weekend cluster in a cloud, the always-on one on bare metal) is the owner's choice of place, and a cloud's hypervisor share is the same in both arms: neither is a benefit of Omni-Compass. What Omni-Compass changes is the work the same machines serve and, in a cloud, the hours billed (`owner_bill` in `tools/work_per_bill.py` reads any owner's line items the same way).

## A $100 million budget, read by the equation

The $100 M is an example, the founder's of 2 November: a company whose IT infrastructure costs 2.9% of its revenue (the example's own figure, of the order public surveys of IT spending report for large firms, about 3% of revenue), so the budget stands for a revenue of about $3.45 B ($100 M / 0.029). The 2.9% is the size of the budget against the revenue; it is not a cost Omni-Compass removes.

An owner's budget is read the same way, place by place, from the receipts and nothing else. Split the owner's native spend into the places it runs in, S(cloud) + S(bare metal) = $100 M, and read each place's G from its own receipt; G(total) is their spend-weighted mean and lies between them. The scale is plain arithmetic: each point of G on a $100 M spend is $1 M of work at native's price per unit of work, about 0.029% of the example's revenue. What can be written today:

| Place | Its bill with Omni-Compass | The work with Omni-Compass | What the receipts let an owner write today |
|---|---|---|---|
| Bare metal (a lease of $100 M) | the same $100 M: the same boxes in both arms, b = 0 | w, the work the same boxes serve | the A10 receipt's own ratios applied to the spend (arithmetic, not a measurement of a fleet): +$1.51 M, +$0.73 M, −$0.70 M of work at native's price per unit of work, out of the same $100 M; the three runs disagree, so no figure is claimed |
| Through the cloud ($100 M a year) | b, read from the cloud's own bill: only the hours Omni-Compass parks or adds move it | w, the work answered inside the line (the work meter) | the one set read so far moved the compute bill +1.21% (inside the noise) and did not count its work; our own model at the max reads the machine-hours up 8% to 34% across the beats, 15% at the main engine's 60 s, with the work fixed by the model's own load (`results/model_gate/V23_LADDER_CORRECTED.md`, class S): the cloud's bill may rise where the work rises more, so a smaller cloud bill is not what the record points to |

**The arithmetic at the founder's aim, an example and not a result.** The founder's words of 31 October state the aim the cloud is judged by: "We're pushing 1% more bill, but we're getting ~12% more work." Put through the equation on the example's $100 M a year in a cloud: ΔB = +1%, ΔW = +12%, G = 1.12 / 1.01 − 1 = +10.9%, the work for each dollar up 10.9%. In dollars, each at native's price per unit of work (native's $100 M bill for native's year of work): the bill is $101 M and the work 1.12 times native's, worth $112 M, so $12 M more work for $1 M more bill; at that work for each dollar, $100 M of bill buys $10.9 M more work than native's $100 M did; read the other way, native's year of work costs $100 M / 1.109 = $90.2 M. On bare metal the bill holds (ΔB = 0), so G = ΔW: each 1% more work from the same boxes is $1 M of work a year on the example's $100 M. These are the equation's arithmetic on an aim; the receipts above are what has been measured, and a page that shows the example says so beside it.

**What no budget may show.** Three limits come from the engine and from physics, not from the receipts:

- No line item called a "stack tax" falls to zero. The share a place's own software layer takes (Vₒ above: a hypervisor's, an orchestrator's) is the same in both arms, because Omni-Compass sits on top of that layer and removes nothing; it cancels in G and is never a saving.
- No machine runs at 100% of its silicon. Every muscle is driven to its own limit and never past it, and the compass law keeps a 5% cushion at each line; and in any queue the waiting grows without bound as the busy share nears one (for one server, the mean time in the system is 1/(μ − λ), which diverges as the arrival rate λ nears the service rate μ). A budget that turns 75% of a fleet's capacity into 100% of it contradicts the engine's own rule.
- Idle hours are not "eliminated". Omni-Compass parks machines the cloud's own autoscaler made and the work does not need, so that autoscaler can remove them; it keeps the cushion the response line needs, and it wakes a machine before the line is crossed. How many hours that removes is what the cloud sets are measuring.

## What the receipts say today

**Bare metal** (The card on omni-v23, the power cap at 70% of the card's top, the full load (cap-full): three runs on an A10; omni-v23 (digest c96ea4105d8747db, 65 files); `results/TWO_BILLS.json chip (results/gpu/V23_A10_CAP_FULL_ABC.json)`):

| Run | Work, native → Omni-Compass | w | Bill, native → Omni-Compass | b | Work per dollar, native → Omni-Compass | G (its own word) |
|---|---|---:|---|---:|---|---|
| run 1 | 2,616.2 → 2,655.6 requests | +1.51% | $0.1194 → $0.1195 | +0.04% | 21,909 → 22,229 | +1.46% GAIN |
| run 2 | 2,269.6 → 2,286.2 requests | +0.73% | $0.1189 → $0.1189 | ±0.00% | 19,089 → 19,229 | +0.73% GAIN |
| run 3 | 2,255.2 → 2,239.4 requests | −0.70% | $0.1189 → $0.1189 | −0.01% | 18,964 → 18,833 | −0.69% LOSS |

The three runs together, by the one key: **the runs disagree** (the mean of the three G +0.50%). No interval is carried for a run's work per dollar, so no run is counted beyond the noise; each run's word is its own size against the 0.5% floor.

**Through the cloud** (omni-v18, 97 paired repetitions, Omni-Compass on top of native at the tune-down (dial save) on the machines alone (OMNI_MACHINES_ONLY=1), the rule of 14 October struck on 31 October; `results/TWO_BILLS.json cloud (results/live/AKS_STEADY_100_OMNI_V18.md)`): the bill $0.0563 → $0.0569 a window, b +1.21%, inside the noise; the work done was not counted, so G(cloud) is not read: the set counted the bill and the machine-hours but not the work done (its load sent a fixed rate of requests, so its work could not grow); the work per dollar waits for the sets at the max with the work meter (scripts/azure_queue.txt), on the engine that stands.

**Not yet read:**

- the chip: eight A100 cards on Lambda, each organism on its own card: read (lambda-gpu 8card pooled, runs 41271477833, 41279081905 and 41271481737); tools/two_bills.py reads its card rows (requests served, energy) as the A10's
- the chip: one A10 on Lambda, the card fully loaded inside the organism (docs/GPU_PREREGISTRATION.md, amendment 16): read (lambda-gpu 1card stacks-full, runs 41271470803, 41271473309 and 41271475877); tools/two_bills.py reads its card rows (requests served, energy) as the A10's
- through the cloud: Azure, one rented machine with the real cluster inside each organism: not yet read (big-organism-detached, run 41269562586 (100 copies, three repetitions)); no reader yet writes its W and B: tools/two_bills.py reads card rows only
- through the cloud: Google Cloud: not yet run (its key is not in the repository's secrets (docs/GOOGLE_SETUP.md)); no reader yet writes its W and B: tools/two_bills.py reads card rows only
- through the cloud: Amazon Web Services: not yet run (its key is not in the repository's secrets and the account is on the Free plan (docs/AMAZON_SETUP.md)); no reader yet writes its W and B: tools/two_bills.py reads card rows only

**Both places, for an owner who runs work in both**, G(total): read only for an owner's stated native spend in each place, never from the benchmark windows; and only once every place's G is read on the engine that stands (the cloud's work is not yet counted).

## Is it proven

Not yet, said plainly. On bare metal two runs of three gave more work for the bill and the third gave less, so the three runs disagree; the card's energy for each request served fell in all three (GAIN in all three of our runs). Through the cloud the work was not counted in the one set read so far. The sets that will decide it are running or queued on the engine that stands, and each lands here by itself when its table does (`python3 tools/two_bills.py`, then this page).

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

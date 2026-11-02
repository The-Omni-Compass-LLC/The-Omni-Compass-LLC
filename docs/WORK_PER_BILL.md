# Work for the Bill: the One Number the Receipts Prove

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

What the receipts of the chip and of the clouds must show is how much work is done for the bill, native against Omni-Compass on native (the founder's words of 2 November). This page writes it as one equation, reads every term from a receipt the repository holds, and says where the benefit lives and where it is counted. Nothing here is a new measurement.

## The equation

    Y(p, a)  = W(p, a) / B(p, a)                       work done for each dollar of the bill, in place p, arm a
    G(p)     = Y(p, omni) / Y(p, native) − 1           the benefit in place p: more work for the bill when G(p) > 0
             = (1 + w(p)) / (1 + b(p)) − 1             w: the change in the work done; b: the change in the bill
             ≈ w(p) − b(p)                             for small changes; exactly ln(1 + G) = ln(1 + w) − ln(1 + b)
    G(total) = Σₚ S(p)·(1 + w(p)) / Σₚ S(p)·(1 + b(p)) − 1
                                                       for an owner who runs work in both places: S(p) the owner's own
                                                       native spend in place p over one period, never the benchmark
                                                       windows; a system in one place reads that place's G alone
    B        = Σₖ cₖ,   b = Σₖ sₖ·bₖ,   sₖ = cₖ(native) / B(native)   the bill as the sum of its components

W is the work done as each place's own receipt counts it: on the chip the requests served within the arm's fixed window (the card's receipt counts no response line); through the cloud the requests answered inside the response line (the work meter). B is the bill: on bare metal the card's metered window at Lambda's launch price, $1.29 an hour (seconds × the price, computed by `tools/two_bills.py`, not a billing statement; the same window bills nearly the same, so b ≈ 0 and G ≈ w); through the cloud the cloud's own bill at list price (machine-hours × the price). A bill that rises is power given; there is more work for the bill when the work rises more than the bill (w > b, G > 0). G(total) is the places' own G weighted by the owner's spend, so it always lies between them.

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

## The bill, line by line

The bill is the sum of its line items, B = Σₖ cₖ, and each item's change counts by its share of native's bill, b = Σₖ sₖ·bₖ. Which items Omni-Compass can move, and which the receipts read so far have priced:

| Line item | Through the cloud: how it is billed | Moved by Omni-Compass? | Bare metal: how it is billed | Moved by Omni-Compass? |
|---|---|---|---|---|
| The server (compute) | by the second: machine-hours × the hourly price | yes: the machines it parks and wakes, the pods it places (priced in the cloud receipt read so far, at list price) | a flat lease or a rental by the hour for the same box | no: the same box in both arms, so this item holds and G ≈ w (priced in the chip receipt: the metered window at $1.29 an hour) |
| Electricity | inside the price | no line of its own | paid by the owner where the box sits on its own meter | yes: the card's own meter reads the energy for each request served (GAIN in all three A10 runs); not priced in the receipt, a line an owner adds at its own rate |
| Data out (egress) | per gigabyte that leaves the cloud | only through the work: more requests served can send more data out, a rise proportional to the work (not priced in the receipt read so far) | an allowance or a flat port | no, inside the allowance |
| Storage and its speed | per gigabyte stored, plus the speed tier bought | no (not priced) | inside the box | no |
| The hidden labour | inside the cloud's premium | no | the owner's staff | no |

So the receipts read so far price the item Omni-Compass moves most in each place (the cloud's machine-hours; the chip's window), and leave out items it does not move. An item it does not move has bₖ = 0 and only pulls b toward 0, so an owner's full bill shows a smaller b than the compute line alone; an item that grows with the work (egress) takes back a share of w in the cloud, and an owner's own electricity rate gives bare metal a second line where the card's energy cut is paid back.

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

- the chip: eight A100 cards on Lambda, each organism on its own card: not yet read (lambda-gpu 8card pooled, runs 41271477833, 41279081905 and 41271481737); tools/two_bills.py reads its card rows (requests served, energy) as the A10's
- the chip: one A10 on Lambda, the card fully loaded inside the organism (docs/GPU_PREREGISTRATION.md, amendment 16): not yet read (lambda-gpu 1card stacks-full, runs 41271470803, 41271473309 and 41271475877); tools/two_bills.py reads its card rows (requests served, energy) as the A10's
- through the cloud: Azure, one rented machine with the real cluster inside each organism: not yet read (big-organism-detached, run 41269562586 (100 copies, three repetitions)); no reader yet writes its W and B: tools/two_bills.py reads card rows only
- through the cloud: Google Cloud: not yet run (its key is not in the repository's secrets (docs/GOOGLE_SETUP.md)); no reader yet writes its W and B: tools/two_bills.py reads card rows only
- through the cloud: Amazon Web Services: not yet run (its key is not in the repository's secrets and the account is on the Free plan (docs/AMAZON_SETUP.md)); no reader yet writes its W and B: tools/two_bills.py reads card rows only

**Both places, for an owner who runs work in both**, G(total): read only for an owner's stated native spend in each place, never from the benchmark windows; and only once every place's G is read on the engine that stands (the cloud's work is not yet counted).

## Is it proven

Not yet, said plainly. On bare metal two runs of three gave more work for the bill and the third gave less, so the three runs disagree; the card's energy for each request served fell in all three (GAIN in all three of our runs). Through the cloud the work was not counted in the one set read so far. The sets that will decide it are running or queued on the engine that stands, and each lands here by itself when its table does (`python3 tools/two_bills.py`, then this page).

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

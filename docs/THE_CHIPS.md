# The chips: where the GPU proof stands, what the card shows, and what it still needs

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Written 30 October 2026 from the run records (`docs/RUN_LEDGER.md`, GitHub's own run pages), the card's three-run tables
(`results/gpu/`) and the card governor's own files; every number here is a table's, read by the one key (`tools/readings.py`:
GAIN, STEADY, LOSS by what the gauge is for, the floor at 0.5%, the word before the number). The card's meter is class P; the
organisms modelled around the card in the stacked box are class S and are never presented as proof. Run and scored by The
Omni-Compass LLC's own code. No outside party has reviewed or approved these results. This page is kept current with every
chip run; the ledger of every rental, hour and dollar is `docs/RUN_LEDGER.md`, section 1.

## 1. What the chip has to prove, and why it is the missing piece

Omni-Compass lives in three places: the software end (Kubernetes and the orchestrators, the data stores, the services), the
cloud's wire between the two ends, and the bare metal at the hardware end (the processor, the card, the rack). The record is
strong at the software end: on real Kubernetes the three-run tables read more work and a faster service on the same
machines, GAIN in all three of our runs (`docs/STATE_OF_PLAY.md`). On the cloud's wire alone the benefit can only be a small
cut in the bill, because a tenant cannot touch the cloud's own metal (the README: the cloud is a wire). The hardware end is
where the rest of the headline is read: the energy, the watts, the heat, on a meter that belongs to the device. The card is
the first muscle at that end, and until the card has a GAIN of its own in all three of our runs, the organism's proof stops
at the software end. That is the piece the founder named, and this page says exactly where it stands.

**The muscle and the governor.** The card's native controller is its own firmware: the power limit the operator sets and the
clock the firmware runs under it. The card governor (`omni_controller/gpu_governor.py`, inside omni-v22's fingerprint since
omni-v15) sits on top: it reads the device's own meter (power drawn, temperature, utilization, the enforced power limit,
the clock-limit reasons), may lower the power limit inside the operator's start limit and never above it, writes nothing
new until the last write is read back from the device, fails up to the start limit at once on a response-time breach or a
thermal or hardware slowdown, and hands the limit back at the end. The dial: the max (the factory tune) and the tune-down
(`save`). The preregistration is `docs/GPU_PREREGISTRATION.md`; the three-run reading is `tools/gpu_abc.py`.

## 2. Every chip run so far

All on Lambda's rented cards, started from the GPU branch of the engine that stood (`gpu-omni-v21`, one exact commit). The
hours are the machine's rented hours from GitHub's run records; the A10 price is the $1.29 an hour each launch printed;
the A100 price is on Lambda's billing page.

| Run (GitHub) | Date (UTC) | Engine | Card | What | Hours | What came back |
|---|---|---|---|---|---:|---|
| 40079645681 | 24 Oct | omni-v18 | A100 SXM4 40 GB | one card, the factory dial | 6.7 | every gauge STEADY; 0 writes in 3,050 decisions: both knobs already at their top on native |
| 40143765437, 40143770324, 40143775773 | 24 to 25 Oct | omni-v18 | A10 ×3 | the stacked box, A, B, C | 25.1, 25.1, 25.0 | the wire check and the smoke only: the watcher fetched packed files alone (fixed 26 Oct, `8e62252e1f`) |
| 40394988327, 40394992822, 40394997159 | 26 to 28 Oct | omni-v21 | A10 ×3 | the stacked box, A, B, C | 33.1 each | sizes 1 and 10 complete (5 and 3 repetitions a run), 100 copies one repetition a run: `results/gpu/V21_STACKS_A10_ABC.md` |
| 40461604089 | 27 Oct | omni-v21 | A100 SXM4 40 GB | one card, the factory dial, 10 paired repetitions | 7.1 | every gauge STEADY, under the floor; 0 writes |
| 40485597269, 40485602065, 40485605739 | 27 Oct | omni-v21 | A100 SXM4 40 GB | one card, the tune-down, A, B, C, 10 paired repetitions each | 6.9 each | `results/gpu/V21_A100_SAVE_ABC.md` |
| 40485609401, 40485613546, 40485617318 | 27 Oct | omni-v21 | A100 SXM4 40 GB | one card under the operator's power cap at 70% of its top, A, B, C, 5 paired repetitions each, the normal load and the card fully loaded | 4.6 each | `results/gpu/V21_A100_CAP_ABC.md`, `results/gpu/V21_A100_CAP_FULL_ABC.md` |

Rented so far: about 176 A10 hours (about $227) and about 48 A100 hours (6.7 on omni-v18, 41.6 on omni-v21). Nothing is
rented before the founder's word; every launch prints its price first and rents nothing on a dry run (`docs/LAMBDA_SETUP.md`).

## 3. What the card shows, by the one key (class P, the card's own meter, omni-v21)

| Tune, three runs | Work per energy | Requests served | Response time | Writes |
|---|---|---|---|---|
| The factory dial (the max), one run | STEADY, under the floor (up 0.12%) | STEADY, the same | STEADY | 0 |
| The tune-down (dial save) | **GAIN by the mean of our three runs** (up 0.84%, 0.71%, 0.69%; beyond the noise in 1 of 3); the energy a cut, GAIN (down 0.85%, 0.70%, 0.68%) | STEADY, the same in every run | STEADY, under the floor: the mean, the 95th and the 99th percentile | 312, 540, 485 |
| The cap at 70%, the normal load | STEADY, under the floor (0.11%) | STEADY, the same | the mean **LOSS by the mean of our three runs** (A 1.87% slower, B STEADY, C 0.79% slower; beyond the noise in 0 of 3); the 95th percentile: the runs disagree (A 3.21% slower, B 1.20% faster, C STEADY) | 7 to 78 |
| The cap at 70%, the card fully loaded | STEADY, under the floor (0.07%) | STEADY, under the floor; requests not served **LOSS by the mean** (A 2.18% more, B and C STEADY; 0 of 3) | the 95th percentile **LOSS by the mean** (A 1.50% slower, B and C STEADY; 0 of 3) | 7 to 78 |
| The stacked box, an A10 inside the seven organisms, sizes 1 and 10 | the card STEADY, under the floor, in every organism | STEADY, the same | STEADY, under the floor; the card's 95th percentile LOSS by the mean in three rows (none beyond the noise): Energy at 1 copy (A 0.79% slower, B STEADY, C 0.69% slower), Physics at 10 (1.22%, 0.97%, 1.79% slower), the tower at 10 (1.05%, 0.74%, 5.81% slower) | the factory max: 0 |

Two readings carry the power the card held: the share of samples at the power limit fell in every tune-down run (down 7.0%,
16.9%, 18.2%, a cut, GAIN) and under the cap by the mean (GAIN, beyond the noise in 2 of 3). Every row of every table is in
`results/gpu/`; no row is left out here.

## 4. What the card's own files say about the mechanism

**At the factory dial the card benefit is zero, and that is the mechanism reading right.** The A100 as Lambda ships it runs
with its power limit at the top of its range (400 W) and its clock at the top under load. Omni-Compass's max pushes a muscle
to its own limit and never past it; a knob native already runs at the top of its range is "at its limit on native". So the
governor read 3,050 decisions on omni-v18 and 10 repetitions on omni-v21 and wrote nothing: STEADY, under the floor, no harm,
and no benefit, because there was none to be had on an uncapped card running flat out. This is not a fault in the wire; it is
what do no harm requires there.

**Where the governor acted, the energy fell and the service did not move.** The tune-down wrote 312, 540 and 485 times in
10 repetitions, lowering the power limit while the response stayed inside its line, and the card drew 0.68% to 0.85% less
energy for the same requests at the same speed. The size is small because the load used little of the card's headroom:
every write lowered the limit and nothing slowed, which says the card had power it was not spending on this work. The knob
had little leverage at this load; the load, not the knob, bounded the gain.

**Under the operator's power cap the record is run A's.** With the cap at 70% the firmware's limiter holds the card; the
governor wrote 7 to 78 times in 5 repetitions. Every LOSS row of both cap tables comes from run A alone (the mean 1.87%
slower, fully loaded 2.18% more requests not served and the 95th percentile 1.50% slower); B and C read STEADY or faster,
and none of the three is clear of the noise. Five repetitions is few: the card's own spread at the cap is wider than the
effect being read, and run A's files on `raw` (`run-40485609401/`) are where its cause is to be found before another
dollar is spent there.

**In the stacked box the card reads its spread, not a mechanism.** The card sat at its factory max (0 writes), the
organisms around it (class S) read STEADY, and the three 95th-percentile rows that read LOSS by the mean are 1% to 2% in
two runs and 5.8% in one, none beyond the noise, in a box where the card is not the organism's limit.

So the chip has two doors, and the record has opened each once. The **energy door**: with energy the aim (the tune-down),
the card gives back watts the work does not need, GAIN by the mean of our three runs, every service gauge STEADY. The **budget
door**: under an operator's power budget (the cap), Omni-Compass must serve as much, as fast, inside the same budget as the
firmware alone, and today that door reads LOSS by the mean from one run of three, none beyond the noise. At the factory max
on an uncapped card there is no door: the firmware is already at the top.

## 5. What the chip proof still needs, step by step, with what each step costs

Each step starts from the GPU branch of the engine that stands (`gpu-omni-v23`, one exact commit), prints its price first,
and rents nothing before the founder's word.

1. **Run A's cause, then the cap at the stopping rule's repetitions.** Read run A's files (`raw`, `run-40485609401/`): the
   governor's audit against the card's meter, decision by decision. A fault in the wire is fixed as the next version through
   the model gate (`tools/model_gate.py`, the card models). Then the cap again, A, B and C at 10 paired repetitions, not 5:
   about 7 hours a run on an A100, three runs, about 21 A100 hours.
2. **The tune-down as the card's factory dial.** The one tune that read GAIN against native with no LOSS is admissible under
   the declared tune rule (`docs/THE_TUNE.md`); on a chip the aim is work per energy. It lands only as the next version,
   through the model gate, on the founder's word (told, never taken), and the card runs again on it: three runs, about 21
   A100 hours.
3. **A load that makes the card the limit.** The tune-down's gain was bounded by a load that left the card's headroom
   unused. The same three runs at the request rate that holds the card at its line read what the governor does when the
   knob carries the service; one A100 run of 10 paired repetitions finds the rate, about 7 hours, before the three.
4. **The stacked box's 100-copy size rented alone.** Sizes 1 and 10 spent the 33 rented hours; 100 copies got one
   repetition a run and is shown, not judged. Rented alone: about 33 hours on each of three A10s, about $128.
5. **Eight cards pooled** (`8card pooled`, every stage on eight A100 cards, repetitions pooled across the cards): the whole
   design at once, never rented; about 10.5 hours, about $165 at most at Lambda's list price.

Steps 1 and 3 are the chip proof's own; 2 is the founder's call; 4 and 5 widen it. Nothing here is written as a result
before the result exists.

## 6. The clouds, read the same day

- **Azure** (`aks-metered`, the machines alone at the tune-down, native's cap, `OMNI_MACHINES_ONLY=1`): the omni-v18 set of
  100 paired repetitions ran from 24 to 29 October: 97 passed, 3 failed (repetitions 82, 90 and 93); it stands as omni-v18's
  record, read in no omni-v21 or omni-v22 table. The omni-v21 steady set (run 40940616527, 100 paired repetitions under the
  stopping rule) started 29 October at 19:29 UTC: 16 of 100 done by 16:27 UTC on 30 October, 14 passed, 2 failed
  (repetitions 3 and 10, each in the compass arm's own last minutes; their files are the run's artifacts `aks-3` and
  `aks-10`, on `raw` when the run ends), about 68 minutes a repetition, one at a time: about four more days to the cap
  unless a look of the stopping rule (at 10, 20, 40 and 70) reads the bill first. Behind it in the queue: the two bursts and
  the real day (Google 2011), each behind Azure's own $0 check.
- **Google Cloud and Amazon**: wired as Azure's sets are and switched off (`scripts/google_queue.txt`,
  `scripts/amazon_queue.txt`, `switch=off`); no key of either is stored in the repository's secrets (`cloud-check` reads
  all four absent); nothing has ever been rented on either. Each goes on with the founder's word once its key is stored
  (`docs/GOOGLE_SETUP.md` section 4; `docs/AMAZON_SETUP.md` section 1a, the account on the Paid plan).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

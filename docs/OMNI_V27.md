# Omni v27: a pod is placed before it is asked for; the scale-up looks forward; the conveyance gives what is owed

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Omni v27 (`OMNI_V27.json`, digest `34548e45437a05bd`, 65 files) is omni-v26 with four faults fixed in the Kubernetes governor
(`omni_controller/controller.py`, `omni_controller/muscles.py`), landed as one version on the founder's order of 14 November: "it
surely cannot be worse ... if it's worse, then it's supposed to result to native"; "one whole new version of engine with all these
new metrics as one shot instead of all these pieces". Do no harm keeps its strictest form.

## 1. Place before asking: no pod is asked for that has no machine to run on

**The fault**, read from the omni-v26 Azure work meter's own audits (runs 43005182097, 43177138720 and 43364393684,
`results/live/V26_AKS_WORK_METER.md`). Work per dollar read GAIN in all three of our runs (up 28.3%, 34.2% and 28.8%), and the pods
waiting for a machine stood about three to four times native's in every run (up 295.3%, 233.6% and 295.4%; shown, not judged). The replica room, the lever
that raises the autoscaler's cap while the service stands at it under pressure, read the most replicas the machines can hold
including the machines the cluster autoscaler may still add (`_live_ceiling`), and it raised the cap again while the pods it had
asked for still waited: 10, 11, 16, 19, 22, 25, 31, 35, with 47 asked. Every pod asked for on a machine not yet made waited for
that machine's boot, and a pod with no machine serves nothing.

**The change** (`_replica_room`, `_live_ceiling(h, in_service=True)`, `_own_pod_counts`):

- R1, place before asking: the cap is raised only while none of the service's pods waits, and only up to the pods the machines
  in service can take now (the live ceiling without the machines still to come). The machines the cloud may still add are its own
  autoscaler's to add, as on native.
- R2, back to native while pods wait: while one of the service's pods has no machine and the cap stands above the operator's,
  the cap is set back to the pods already placed, never below the operator's own cap, and the audit says so
  (`"replica_room": "back while pods wait"`). The pods Omni-Compass asked for that have no machine are withdrawn (Kubernetes
  removes an unplaced pod first), and native's own scaling stands.
- R3, native's count while pods wait: Omni-Compass's other push for pods is the autoscaler's target, held below native's (the
  fail-up and the compass), so the autoscaler asks for more pods than native's would. While one of the service's pods has no
  machine and the target stands below native's, the cap is set to the larger of native's own count (the replicas native's
  autoscaler asks for at the operator's own target, inside the operator's range) and the pods already placed: every pod
  Omni-Compass asked for beyond native's count that has no machine is withdrawn, and native's own pods wait exactly as they
  would on native. The operator's range is recorded first, and once no pod waits the cap goes back up as the machines in
  service can place the pods, to the operator's own (`_live_ceiling(h, in_service=True)`); the reset restores it.
- Machines first, for the pods withdrawn (`_machines_first`): a waiting pod is also what asks the pool for a machine (the
  scheduling floor counts its request), so before R2 or R3 withdraws one, the machines the cluster's requests need, the waiting
  pods' included, are ordered by the floor's own arithmetic. The machines still come; the pods follow as they land. Found by
  the model gate on the first form of R3: without it one seed in the cloud's setting at 60 s made 7.6% fewer machines than
  omni-v26 and its 95th percentile rose 5.5%.

## 2. The scale-up looks forward, never back

**The fault**, put by the founder on 15 November: "if it's scaling up, it should be looking forward 3 steps ... history is what
makes the future, which is bullshit." The immune memory (omni-v19) kept the largest rise in demand it had ever seen, inside two
decisions, as a reserve from then on: the fail-up asked only the pods the machines in service could place after a rise of that
size, and a machine was given back only when the rest held the requests and that rise. It never let go: one burst in the morning
held room all day, whether the demand was flat, falling or rising, and the machines the room asked for were Omni-Compass's
reserve, not the demand's. And it counted its window in readings, so at a faster beat it looked back less than a machine takes
to come (30 s at 15 s, where a machine takes about two minutes), and a rise over the boot found no room: in the model gate's
cloud setting at 15 s, omni-v26's pods waited 58.2% longer than native's.

**The change** (`LOOK_AHEAD_BEATS = 3`, `DELIVERY_S = 120.0`, `_slope`, `_horizon_s`, `_delivered`): each decision reads how fast
the service's demand and the cluster's requests are rising now, the least-squares slope of their readings over the last three
beats, the time the decisions' own count times the beat, and projects that rate ahead over the look-ahead: three beats, never
nearer than a machine's delivery, since a machine ordered now serves nothing sooner. The pods the fail-up asks leave room for the
projected rise (`_placeable_target`'s rise, the demand ahead over the demand now), and a machine is given back only when the
machines left hold the requests and the larger of one machine and the projected rise. While the demand is flat or falling,
nothing is projected and no reserve is held. The delivery is the cloud's own, read live: each machine order Omni-Compass writes
is timed from the order to the machines open to work reaching the count ordered, and the look-ahead follows it (half the last
measure, half the new); 120 s stands only until the first order lands. A machine delivered in four minutes makes the look-ahead
four minutes; a cloud's own limits on the pool (its maximum, read live from its autoscaler) bound every order, as before.

## 3. The conveyance gives what is owed, and steps by the band

**The faults**, read from omni-v25's Koordinator rigs (`docs/LOSS_CAUSES_2026-11-07.md`), built and gated on 7 November and held
on the branch `v27-convey-study` by the founder's order of that evening until omni-v26's tables stood (they stand: the release on
omni-v26). Koordinator's best-effort pods ask for their processor only in its batch resources, so the conveyance read them as
using nothing and raised the web pods' limits into processor the queue was owed; and one raise jumped the shared host from 70% to
75% busy, whereupon the hand-back put every limit back at once, a cycle.

**The change** (`omni_controller/muscles.py`): a best-effort pod is counted by what it may use, with room of its own; while
another workload's pods wait for a place (unplaced, of no workload an HPA scales, a DaemonSet's aside) nothing is raised and each
limit given steps back by half its raise at every pass; beside another workload's room on a shared host a raise gives the serving
pods together no more than the host's room under the band's cushion line, and at the top each limit gives back half its raise at
each pass, never all of it at once.

## 4. The stand-ins: the cloud is asked for a machine ahead, and no real pod waits for it

**The fault**, found by the model gate on the forms above and put by the founder on 15 November: "we don't want to make pods
scale up when we can't give it to them". In a cloud, Omni-Compass's machine lever opens and parks machines that exist
(`scripts/kind_nodepool.sh`); a new machine is made by the cloud's own autoscaler, and only for a pod that waits. omni-v26 got its
machines ahead by letting the pods its target asked for wait (pods waiting three to four times native's on the Azure work meter);
sections 1 and 2 stop every such wait, and with them the only signal that had the cloud make a machine early: in our own cloud
model at 60 s omni-v27 without the stand-ins read the 95th percentile and the alert minutes LOSS against omni-v26.

**The change** (`_headroom`, `standin_count`, `deploy/kind/omni-headroom.yaml`, the grant in `deploy/kind/rbac-omni.yaml` and
`deploy/install/rbac-cloud.yaml`). The mechanism Kubernetes itself provides for it: a priority class below every real pod (−5,
above the cluster autoscaler's cutoff of −10, so the cloud makes a machine for it; it never displaces anything) and one
deployment of pause pods, 250m each, made at the install with none. At the end of each decision, through a cloud only, the
governor sets their count: the room looked ahead (the rise of the cluster's requests over the look-ahead, section 2) and the pods
held back until a machine can take them (R1 and the release, section 1) beyond the room the machines in service have free and the
pool's parked machines hold (the floor opens those first), never past what the cloud's autoscaler may still add. The stand-ins
fill the free room first, so only the shortfall waits, and the cloud's autoscaler makes the machine for it; any real pod displaces
a stand-in at once, so the machine is up before the demand and no real pod waits for it. With nothing rising and nothing held back
there is none, and an empty machine goes back to the cloud by its own rule. On site, where no machine is made, never; at the
tune-down, on the cloud's give-back-only and where the machines are left native, never, since the bill may not rise there. The
governor's reading, its fast check and the harness's own counts (`fleet/capture/kube_capture.sh`, `pilot/bench_report.py`,
`scripts/kind_nodepool.sh`) never count a stand-in as a pod that waits or as a request; the reset sets them back to none.

**The C++ twin.** The look-ahead's rate, its horizon, the delivery measured and the stand-in count are written once more in C++
(`cpp/src/lookahead.cpp`, `cpp/tools/run_lookahead.cpp`), sealed with the other twins (`tools/seal.py`) and held to the Python
to the last bit by `tests/test_cpp_lookahead_parity.py` (verify runs it, with a negative control: C++ stand-ins that ask the
cloud for machines the pool already has parked must be caught).

## The tests and the model gate

`tests/test_place_before_asking.py`: on the stand-in cluster, a cap raised to 18 with 14 pods placed and 4 waiting goes back to
14 (omni-v26 raised it on to 33); a cap of 12 with 6 placed goes back to the operator's 10, never below; no raise while pods
wait; with two machines in service and two the autoscaler may add, the raise goes to the 14 pods the machines in service hold, not
the 18 asked; with the target at 30% where native's is 50%, 14 pods placed and 4 waiting, the cap goes from the operator's 20 to the
14 placed (native's own count is 11), and with 8 placed and 10 waiting to native's 11; once nothing waits it goes back to the
operator's 20; and the immune memory's window at each beat. `tests/test_compass_controller.py` reads the in-service ceiling.
`tests/test_convey_owed.py` (six cases) and `tests/test_convey_handback.py` read the conveyance. `tests/test_standins.py`:
through a cloud, two machines of 2 cores with 2 free and 3 cores rising, 12 stand-ins (1 core's worth waits for the cloud's
machine); 10 for 2.5 cores held back; none where a parked machine holds the rise, 20 beyond it; none at the pool's top, on site,
at the tune-down or on give-back-only; a waiting stand-in is never a pod waiting in the reading or the fast check; none after the
reset. `tests/test_place_before_asking.py` reads the pods held back for the stand-ins (4 of 200m where the machines in service
hold 14 of the 18 asked).

**The model gate** (`results/model_gate/V27_VS_V26.md`, `.json`: seeds 1 to 8, twelve models; our own models, evidence class S, never
proof). Each reading is the mean change over the seeds, with whether it stands beyond the seeds' noise.

| Model | Against | Pods waiting | 95th percentile | Alert minutes | Autoscaler short of pods | Machine-hours |
|---|---|---|---|---|---|---|
| the cloud, a decision every 60 s (its factory beat) | native | GAIN, down 19.3% | GAIN, down 4.0% | GAIN, down 15.0% | LOSS, up 0.8% (inside the noise) | power given, up 13.8% |
| | omni-v26 | GAIN, down 28.4% (beyond the noise) | LOSS, up 5.0% (inside the noise) | LOSS, up 9.7% (inside the noise) | LOSS, up 2.2% (inside the noise) | power given, up 3.6% |
| the cloud, every 15 s | native | GAIN, down 62.3% | GAIN, down 19.5% | GAIN, down 68.5% | GAIN, down 3.3% | power given, up 66.5% |
| | omni-v26 | GAIN, down 76.2% | LOSS, up 8.5% | LOSS, up 67.5% | LOSS, up 8.6% | power given, up 27.5% |
| on site, every 10 s (its factory beat) | native | STEADY (none waits in either) | GAIN, down 28.7% | GAIN, down 80.5% | GAIN, down 9.5% | STEADY (the same) |
| | omni-v26 | STEADY | LOSS, up 1.4% | LOSS, 5.25 against 2.75 minutes a day (inside the noise) | LOSS, up 1.0% (inside the noise) | STEADY |

The cloud with machines blinking out and the cloud at each checkout's own beat read as the cloud at 60 s. The conveyance, the card and
the verdict models read omni-v26's numbers to the digit: none of their paths changed, and their rows against native are omni-v26's own,
LOSS among them (the conveyance models' pod start wait up 9.0%, the batch model's requests served down 2.1% and its alert minutes up
9.8%, the card's 95th percentile up 2.4%), each on the next version's list. Against native the cloud and on-site models read GAIN or
STEADY on every service gauge, but the one row inside the noise. Against omni-v26 the pods waiting fall in every cloud model, and the speed
and the alert minutes rise: omni-v26 bought them with the two things the founder ordered out on 14 and 15 November, the pods it asked
for waiting on machines the cloud had not yet made, and the largest rise ever seen held as a reserve from then on. The forward look
holds no reserve while the demand is flat or falling, and a single jump in the load is met as native meets it.

Two forms were refused on the way, both read in the same models. The least-squares line through the last three beats projected a
single jump again as a climb: pods waiting near none, but 22% to 86% more machine-hours than omni-v26 for demand that never came.
A window matched to the whole look-ahead (eight beats at 15 s) was cheaper, but one seed at 15 s read pods waiting and alert minutes
above native's: the rule "never worse than native" refused it, and the three beats the founder named stand.

## What is run again

Every benchmark runs again on omni-v27 from 18:30 UTC on 15 November (`scripts/reruns.txt`, A of every entry, then B, then C; the
conductor's campaign, `scripts/dispatch_grid.py`) on GitHub's own machines. Nothing runs in a paid cloud or on a rented chip
until the founder says the mechanism is the one he wants (his order of 15 November: "you don't run no chip and no cloud until you
make sure you got the mechanism right that I want"): the Azure, Amazon and Google queues read `switch=off`, and the one-card chip
on Amazon (`.github/workflows/aws-gpu.yml`: one card at 1, 10 and 100 copies; the eight-card machine not now) starts only by
hand. The omni-v26 runs started before that moment run to their end as omni-v26's record; nothing is cancelled.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

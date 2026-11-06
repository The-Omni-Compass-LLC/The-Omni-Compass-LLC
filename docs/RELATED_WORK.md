# Related work: where the idea of Omni-Compass comes from, and what it adds

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

`docs/COMPARISON.md` sets Omni-Compass beside the systems that run data centres today (the Kubernetes autoscalers, Borg,
Twine, Turbonomic, the power managers). This page sets it beside the published ideas it is built from, so a referee can
see which parts are known technique and which part is the claim. Each idea is named with the work that stated it.

## 1. A supervisory layer over a controller that already works

Omni-Compass never replaces the native controller. It moves the same settings native moves, inside bounds the system and
its operator set, and native keeps running underneath.

- **Advanced process control over regulatory control.** In process industries the fast loops (PID controllers on valves
  and pumps) are left in place and a supervisory layer, usually model predictive control, moves their setpoints
  (S. J. Qin and T. A. Badgwell, "A survey of industrial model predictive control technology", *Control Engineering
  Practice* 11(7), 2003). Omni-Compass has the same layering: the native autoscaler, pool or firmware is the regulatory
  loop; Omni-Compass is the supervisory layer.
- **Reference and command governors.** A governor modifies the reference given to a loop that is already stable, so that
  constraints hold, and leaves the loop itself alone (E. Garone, S. Di Cairano and I. Kolmanovsky, "Reference and command
  governors for systems with constraints: a survey on theory and applications", *Automatica* 75, 2017). This is the
  closest formal relative of Omni-Compass: it moves a setting, inside a cover, on top of native.

**What differs.** Reference governors are usually designed from a model of the closed loop and prove constraint
satisfaction from it. Omni-Compass carries no model of the system it governs: it reads the system, steps, and lets each
step stand only if a paired trial on the system itself shows it did no harm (section 3). Its own law is proved bounded,
monotone and Lipschitz (`docs/ENGINE_PROOFS.md`, C1 to C8), but the safety of a step in a given system rests on the trial
and the cover, not on a model of that system.

## 2. A fallback that is always there

- **The Simplex architecture.** A high-performance controller runs beside a simple, verified safety controller, and a
  decision module hands control to the safety controller whenever the system leaves a recoverable region (L. Sha,
  "Using simplicity to control complexity", *IEEE Software* 18(4), 2001).

Omni-Compass's fallback is native itself. Every setting is snapshotted before the first write and handed back at the end,
on the kill switch (instantly) and, if Omni-Compass dies, by the lease's walk back (`docs/SAFETY_CASE.md`,
`omnicompass/master.py`). The fallback is not a second controller written for the purpose; it is the controller the
system was already trusted with.

## 3. Changing a live system one tested step at a time

- **Online controlled experiments.** A change is shown to a share of live traffic and kept only if a paired comparison says
  it helped (R. Kohavi, R. Longbotham, D. Sommerfield and R. M. Henne, "Controlled experiments on the web: survey and
  practical guide", *Data Mining and Knowledge Discovery* 18, 2009).
- **Safe exploration and shielding.** A learning controller may explore only inside a set a shield has proved safe
  (M. Alshiekh et al., "Safe reinforcement learning via shielding", AAAI 2018); control barrier functions keep a system
  inside a safe set by construction (A. D. Ames et al., "Control barrier functions: theory and applications", European
  Control Conference 2019).

Omni-Compass's verdict (`omnicompass/verdict.py`) is a controlled experiment run on the governed system itself, one step at
a time: a step is allowed only when its paired trial does not read LOSS against either the setting before it or native,
its cost stays within 2% of the cost first measured at native, and steps cannot add up past that (proved: V1 to V3). The
cover plays the shield's part: no write leaves it (proved: P1 to P3).

## 4. Feedback control of computing systems

- **Control theory applied to software.** Queue lengths, utilisations and response times are controlled with classical
  feedback, analysed with the tools of control engineering (J. L. Hellerstein, Y. Diao, S. Parekh and D. M. Tilbury,
  *Feedback Control of Computing Systems*, Wiley-IEEE Press, 2004).
- **Production systems.** Google's Autopilot sets containers' limits and replica counts from their history
  (K. Rzadca et al., "Autopilot: workload autoscaling at Google", EuroSys 2020); Borg schedules the work
  (A. Verma et al., "Large-scale cluster management at Google with Borg", EuroSys 2015); Heracles uses feedback to share
  machines between latency-critical and batch work (D. Lo et al., "Heracles: improving resource efficiency at scale",
  ISCA 2015); power is provisioned and capped across whole facilities (X. Fan, W.-D. Weber and L. A. Barroso, "Power
  provisioning for a warehouse-sized computer", ISCA 2007; Q. Wu et al., "Dynamo: Facebook's data center-wide power
  management system", ISCA 2016).

Omni-Compass's law is a bounded, smooth one (the compass law, a tanh of a proportional-derivative reading inside a band with
5% cushions), not a linear PI loop, and the same law with the same verdict is applied to every knob it governs, from a
pod's CPU limit to a battery's charge rate.

## 5. What Omni-Compass claims, against this background

Each part has a precedent: the supervisory layer (section 1), native as the fallback (section 2), the tested step
(section 3), feedback on computing systems (section 4). The claim is the combination, applied the same way to every
muscle of a stack:

- one bounded law and one verdict for every knob, on top of each knob's own native controller;
- a step allowed only when the system itself shows it did no harm against native, with the cost bounded stepwise;
- every setting handed back to native's value at the end, on the switch, or on the governor's death;
- results read only by a preregistered three-run rule, every row shown.

Whether the combination does what it claims is a question for the measurements, not for this page: `docs/REFEREE_SUMMARY.md`
gives each claim's standing, and `docs/LIMITATIONS.md` what the measurements cannot yet say.

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

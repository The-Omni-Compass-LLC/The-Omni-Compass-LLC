# The second set of 10 October 2026, and the four rules it taught the trial

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Moved here on 2 November 2026 from the Owner's Manual's chapter 16, which reads only the newest table of each test. A dated record: every number below was read on 10 October on that day's engine, and none is a result of the engine that stands.

The five live products ran a second time on 10 October on the amended trial rule (a spend trial runs to its samples; it is
never ended by the calm it causes). The trials finished. The brain still refused the Kafka consumer almost every time, and
in the one repetition where it allowed the third consumer early, the whole gain of the earlier law came back at a fraction of
the spend: the 95th-percentile delay fell from 2,450 ms to 57 ms, the queue from 3,375 waiting messages to 253, the work inside
the line rose 17%, with 2.52 consumers on average where the earlier law had spent 5.8 to 7.9. On Redis with the large working
set the brain allowed 15 MB more memory and bought more hits, more work and less host CPU, a row the earlier law never
showed because it spent 200 MB; with the small working set nothing changed. PostgreSQL gave back about a tenth of its pool
with the service inside the noise.

The Kafka reading is the finding. The gain is real and cheap; the brain's test of it is unreliable, and the fault is in how the
harness measures, not in the law or the engine's judge. The cost sample it is shown is the age of the backlog, which does not
fall until the backlog is gone. A consumer joining the group rebalances it and the settle time is eaten by the pause. The
reference and the trial phases, fourteen seconds each, straddle a thirty-second load step and compare different loads. Four
rules follow for the trial, written into the next engine (`docs/OMNI_V4_PLAN.md`): samples count only once the muscle reports
itself settled; a spend on a queue or a cache is judged by the muscle's own reading, the lag and its drain rate, the misses,
with the body's cost taken at the settled state; the reference and the trial are compared at the same load, else the trial
waits for a steady step; and coarse to fine, one scout step to the far side of the cover when single notches read flat, so a
hill of forty notches is not refused one notch at a time. The founder's words of the same day say it in one line: what the
brain sends to a muscle has to coincide with what the muscle reports about itself and where it stands.

The next engine, Omni v4, is ordered on that day: one body, one brain, one tick a second; the body's cost judged; nothing
anywhere pushed to a LOSS to move one thing to a GAIN; one trial at a time inside a body; nothing permanent; the wall belonging to the
body; every wire forced through it. Part II gains its chapter when v4 is written and run, and every result in this chapter is
run again on it.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

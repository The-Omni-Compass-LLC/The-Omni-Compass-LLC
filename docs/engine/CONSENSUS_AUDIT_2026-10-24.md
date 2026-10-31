# The live engine, graded: the referee and underwriting consensus audit of 24 October 2026

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

**The page audited.** `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html` on the branch `claude/interactive-animated-charts-icvnsw`, built on
omni-v19, as it stood at commit `401417998e` (SHA-256 `7531404530dec345…`, 7,971 lines), with its registry
`docs/engine/monitors.json` (62 monitors), its builder and exporters, the Live Engine Manual and the standing orders. It is the
page after the founder's order of 25 October took Omni-Compass by itself out of it: two sides only, native and Omni-Compass on
native. Five seats each read one dimension. The visual seat read the rendered page at 1280 and 390 px. No seat read another's
report before writing its own; every finding about the removed third arm was dropped. The five reports are kept line for line in
`docs/engine/audit_2026-10-24/`, and their line numbers are the audited file's. The hand that built the page closes the findings
(section 0) and does not re-grade: the grades are the referees' grades of the page they read, and they stand until the seats read
the fixed page again.

**The scale** (set in the seats' briefs): A+, A, A−, B+, B, B−, C, D, F for each part and overall. A finding is a major (something
a referee would reject: a wrong number, a reading against the key, a claim beyond the record, a contradiction between the page and
its key or its records, a model shown as proof, a numbering fault, metrics buried under prose), a minor, or a nit. No seat called
any finding a blocker. The mathematics seat named S1, the figure of record printed as "GAIN +0.5%" where the index is +3.4%, as
the strongest candidate: it is the kind of wrong number the scale of 21 October called one.

## 0. Where the findings stand

All five seats are in. Majors as counted: the mathematics 11 (S1–S11), the structure 8 (ST1–ST8), the underwriting 12 (U1–U13
less U10), the editing 17 (E1–E17) and the visual 11 (V1–V11): 59. The underwriting seat's U10 (the GPU run's engine and class
stated three ways) is carried as a minor on the founder's word of 25 October ("drop the smallest one"). The editing seat's E14
carries the same fault as a major, so nothing is lost. Several are one fault seen by two or three seats: the dial's record and
its doubled id (S11 = ST5 = V1), the reading key's STEADY defined by the noise (S6 = U12 = E12), the broken section pointers
(ST1 = E13), the page's described order (ST2 = E4), the LOSS count typed as 7 where 2c lists 160 (S8 = U4), and the heartbeat
stated as 15 s where the engine decides every 60 s (S8 = E11). The fixes are in hand. This section is written again, finding by
finding, when they land.

**Minors and nits.** The five seats name 20 minors and nits each in the mathematics seat, the visual seat's 20 minors and 9 nits,
and the others' in their reports, each with its fix.

## 1. The grade

The consensus is the median of the seats' grades; a half step rounds to the stricter grade.

| Section | Mathematics and readings | Structure | Underwriting | Editing | Visual | Consensus |
|---|---|---|---|---|---|---|
| ii Title page and build | A | B+ | A− | B+ | A | **A−** |
| iii The bottom line | B+ | A | A− | A− | A | **A−** |
| iv Engine table of contents | — | A | — | — | A+ | **A** |
| 1a The monitor wall | A | A− | A+ | B+ | A | **A** |
| 1b The control panel and the kill switch | A | B+ | A− | A− | A− | **A−** |
| 1c The dashboards | A | A− | A | A+ | A | **A** |
| 2a The status board | B+ | A+ | A− | A+ | A | **A** |
| 2b The golden signals, the event log, the live metrics | A | A+ | A+ | A | A | **A** |
| 2c Every LOSS row | A− | A | A | A+ | A | **A** |
| 2d The benefit board | A− | A | A− | A | A− | **A−** |
| 3a The organism, live | A+ | A+ | A+ | A | A− | **A+** |
| 3b Control console | A | A− | A+ | A | A | **A** |
| 3c The heartbeat dial | A− | A− | A | A− | B | **A−** |
| 3d One control cycle | A | A− | A+ | A | A | **A** |
| 3e Phase plane and scoreboard | A | A | A+ | A+ | A− | **A** |
| 3f The brain's internal state | A+ | A+ | A+ | A+ | A | **A+** |
| 3g The verdict | A | A+ | A+ | A | A | **A** |
| 3h Cloud providers | A− | A | A | A | A | **A** |
| 3i Orchestrators and governors | A | A | A+ | A+ | A | **A** |
| 3j Kubernetes: official run playback | A | A+ | A+ | A− | A− | **A** |
| 3k Per-repetition telemetry | A | A+ | A+ | A+ | A | **A+** |
| 3l The shipped controller's decision trace | A− | A | A+ | A− | A− | **A−** |
| 3m Hardware | A− | A− | A | A− | A | **A−** |
| 3n Telemetry analytics | A | A | A+ | A | A | **A** |
| 3o The Python's runs | A+ | A+ | A+ | A | A | **A+** |
| 4a The whole organism | A− | A+ | A | A− | A− | **A−** |
| 4b The twenty scenarios | A | A | A | A | B | **A** |
| 4c Measured effect in full | B+ | A | A+ | A | A | **A** |
| 4d The C++ twin | A+ | A | A+ | A | A | **A** |
| 4e CI pipeline | A | A | A+ | A+ | A | **A** |
| 4f The master switch's wiring | A | A | A+ | A | A | **A** |
| 4g Component specification and mathematics | A | A | A+ | A | A | **A** |
| 4h Failure modes | A | A+ | A+ | A+ | A | **A+** |
| 4i Self-governed rendering | A | A+ | A+ | A+ | A+ | **A+** |
| 4j The problem and the answer | A | A+ | A | A | A+ | **A** |
| 4k Executive summary and reading key | B+ | A | A− | A− | A+ | **A−** |
| 4l The monitor list | A | A | A+ | B+ | A | **A** |
| 4m Glossary and index | A | A | A+ | A− | A+ | **A** |
| v Disclosures, governing law and contact | A | A+ | A− | A− | A | **A** |
| **Overall** | **B** | **B+** | **B** | **B** | **B** (desktop B+, phone B) | **B** |

By section the consensus reads A+ in 6, A in 24 and A− in 9. The overall stands one step under the sections because each seat's
overall weighs its majors, and 59 were counted. The overall moves when the majors are closed and the seats read the page again.

## 2. The majors, by seat

Each is set out in full in its seat's report, with the line, the evidence and the fix.

- **Mathematics and readings** (`audit_2026-10-24/seat_mathematics.md`):
  - S1 the figure of record "GAIN +0.5%" where the index is +3.4%;
  - S2 36 run cells printing the opposite word;
  - S3 the benefit board's verbs against their words;
  - S4 seconds printed as percent;
  - S5 "in all three runs" counts overstated;
  - S6 the retired STEADY rule;
  - S7 the whole-workload words and the cloud layer beyond its record;
  - S8 two stale typed numbers;
  - S9 a green light beside "GAIN AND LOSS";
  - S10 the V11_CAPACITY rows not re-read;
  - S11 the heartbeat dial empty.
- **Structure** (`seat_structure.md`):
  - ST1 26 wrong section pointers;
  - ST2 the title page describing the old order;
  - ST3 7,910 characters before the first metric;
  - ST4 a button with no handler;
  - ST5 the doubled `dialNote`;
  - ST6 the cloud link landing on 3l;
  - ST7 the dashboards' level, range and series idle in six forms;
  - ST8 the control panels' titles.
- **Underwriting** (`seat_underwriter.md`):
  - U1 the headline's yardstick is the company's own rule;
  - U2 the bottom line's lights greener than their records;
  - U3 the removed arm's LOSS rows not mentioned;
  - U4 the LOSS count;
  - U5 to U7 "every LOSS row" said where not every row stands;
  - U8 the notice missing from program outputs;
  - U9 the factory tune's LOSS rows in our models not raised;
  - U11 expected gains beside results;
  - U12 the key;
  - U13 the wall's Prometheus answering the "null" origin.
  - U10 is carried as a minor (above).
- **Editing** (`seat_editor.md`):
  - E1 a retired word and a superlative;
  - E2 "simulation";
  - E3 the retired word for our models in file paths;
  - E4 the described order;
  - E5 "never by itself" beside the engine's Python-only table;
  - E6 3l opening on the controller without native;
  - E7 the yardstick unnamed;
  - E8 "five tabs";
  - E9 the glossary's beats;
  - E10 the kill switch called native alone;
  - E11 15 s against 60 s;
  - E12 STEADY two ways;
  - E13 nine cross-references to missing sections;
  - E14 the GPU run named four ways;
  - E15 ten organisms against seven;
  - E16 power given "the accent";
  - E17 the disclosures naming omni-v16.
- **Visual** (`seat_visual.md`):
  - V1 the dial's tables empty;
  - V2 the scenarios grid's columns;
  - V3 a side's name in its own colour on the red pill;
  - V4 a range's second number without its sign;
  - V5 the closing notice under the console bar;
  - V6 a file path running 12 px off the phone;
  - V7 to V11 phone overprints in the dashboards, the immune monitor, the phase planes, the pipeline, the quote board and the benefit board.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

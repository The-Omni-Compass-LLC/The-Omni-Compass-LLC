# The live engine, graded again: the referee and underwriting consensus audit of 22 October 2026

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

**The page audited.** `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html` on the branch `claude/interactive-animated-charts-icvnsw`, built on
omni-v16 (digest `5c5502f12b1c0ce4`, commit `0a26ff12`), as it stood on disk at 22:05 UTC on 22 October (35,459,021 bytes, 6,270 lines),
with its registry `docs/engine/monitors.json` (61 monitors), its builder and exporters, the word-for-word map
`docs/engine/PAGE_WORD_FOR_WORD.md`, the Live Engine Manual and the standing orders. Five seats, one dimension each, read the files; the
visual seat read the rendered page at 1280 and 390 px, on the build of 08:41 UTC on 23 October (the first fixes of section 3 already
in it). No seat read another's report before writing its own. The five reports are kept line for line in
`docs/engine/audit_2026-10-22/` (their line numbers are the page file's as audited). The hand that built the page closed the findings afterwards (sections 0 and 3) and did not re-grade:
the grades are the referees' grades of the page they read, and stand until the next audit reads the page again.

**The scale** (set in the seats' briefs): A+, A, A−, B+, B, B−, C, D, F for each part and overall. A finding is a major (something a
referee would reject: a wrong number, a reading against the key, a claim beyond the record, a contradiction between the page and its key
or its records, a model shown as proof, a numbering fault, metrics buried under prose), a minor, or a nit (a minor too small to grade
on). No seat called any finding a blocker; the mathematics seat's two wrong numbers (S2, S7) are the kind of finding the 21 October
scale called one, and both are closed.

## 0. Where the findings stand (23 October, morning)

All five seats are in: 38 majors as counted, **33 distinct** (five found twice or more: the sign rule S1 = E3 = V3, power given's
colour E4 = V2, the title page's "every model" S6 = M1, the title page's "confirmed as the best state" M9 = E1). Of the 33, **29 are
closed** (23 in the push of this page, the visual seat's last six, V5 to V10, in the push after it), **3 are closed in part** and wait
on the founder's decision on the page's order (ST1, ST2; section 4) or keep one small remainder (ST4), and **1 is closed in its
sentence** with the rest of its fix described (M3). None is open.

**Minors and nits.** The five seats name 94 minors (the mathematics 15, the underwriting 21, the editing 24, the structure 17, the
visual 17) and their nits (the editor's 14 and the visual seat's 10 among them), each in its seat's report with its fix. Closed with this push where a major's fix covered them:
the static title chip and the `data-prose` attribute naming omni-v14 (structure m10, underwriting m1), the registry's missing number
field (the previous audit's nit, with ST6), the index file's engine sentence (with M4). The rest stand open, in the reports.

## 1. The grade

Where a seat graded a part's lettered sections one by one, the part's cell gives the range and the median stands for the part. The
consensus is the median of the seats' grades; a half step rounds to the stricter grade.

| Part | Mathematics and readings | Underwriting | Editing | Structure | Visual | Consensus |
|---|---|---|---|---|---|---|
| i Legal notice | A | A+ | A | B+ | B+ (with the plates) | **A** |
| ii Title page and build | B+ | C | B− | C | C | **C** |
| iii The problem and the answer | A− | B+ | A− | B− | A− | **A−** |
| iv Executive summary and reading key | B | B | B | C+ | B | **B** |
| v Engine table of contents | A | A | B+ | B− | B (provisional) | **B+** |
| 1 The monitor wall and the control panel (1a to 1i) | A− | A to C (1g C, 1d B−, 1c B+, 1h A−; median A) | A− | B | B | **A−** |
| 2 The benefit board | B− | B | B+ | B | B+ | **B** |
| 3 The whole organism | B+ | B− | B | A− | A− | **B+** |
| 4 Measured effect in full | B | B+ | A− | B+ | B | **B+** |
| 5 Evidence by stack (5a to 5f) | A− | A to B− (5f B−, 5e A; median A−) | A− | A− | B | **A−** |
| 6 The organism, live (6a, 6b) | A | A, A− | A− | B+ | B+ | **A−** |
| 7 Control console | A | A | A | B | A− | **A** |
| 8 The brain (8a to 8d) | B+ | A− | A− | A− | B+ | **A−** |
| 9 Failure modes | A− | B+ | A | A | A− | **A−** |
| 10 The components (10a, 10b) | A | A−, A | A− | C | B+ | **A−** |
| 11 Self-governed rendering | A− | B+ | A | A− | A− | **A−** |
| vi Disclosures, governing law and contact | A | A− | B | A− | A | **A−** |
| vii Closing legal notice | (with vi) | A | A | B+ | A | **A** |
| **Overall** | **B** | **B−** | **B+** | **B** | **B** (desktop alone A−, phone alone B−) | **B** |

The visual seat numbered the front matter as it reads on screen (its i the title page, its ii the notice with the two plates); its
grades are placed here on the page's own numbering.

**What B means here.** Every number a seat traced matches its record, and the page renders with no console error, no sideways scroll
and no blank monitor at either width, the kill switch doing exactly what its label says: the mathematics seat recomputed seventeen, among them the Omni
index (+4.3336% from its six category factors), the Kubernetes category (+28.65% from its nine tests), the steady test's speed ratio
(2.8343 from the three runs' response times), the heartbeat sweep's 600 readings (0 differ from `results/model_gate/HEARTBEAT_SWEEP.json`,
every interval by Student t over eight seeds) and the whole organism's composition (to the last digit from `results/WHOLE_SYSTEM.json`);
the underwriter re-tallied the executive summary's counts from the receipts with the floor as the page applies it and found them equal;
the engine on the page is one engine (omni-v16) and its mathematics equals the Python and the C++. What held the page at B is not a
number of the record but what the page said about it: two printed numbers wrong (the verdict's keep rates signed by the word before
them; an interval that includes zero printed on one side), the key's rule on the sign stated two ways and printed both ways, standing
tables dropped from the board, judged words under the key's floor, an orchestrator's own cost attributed to Omni-Compass, and a title
page whose four statements (every model on omni-v16; the 15 s heartbeat "the same in every run"; every figure from raw files;
"confirmed as the best state") the record did not carry. The structure seat's five majors are the founder's own order of 22 October
(the wall buried under eleven printed pages of front matter; the one combined number last) and three faults of the skeleton (a part
with no head, a contents that is not the headings, a reading guide ten sections ahead of its chart).

**The path to A.** Every major of the four seats is closed or closed in part below; the next audit reads the page again and grades it.
What remains for the founder is the page's order (section 4): the wall first, or the cheaper cut of the front matter, or as it stands
with the folds.

## 2. What holds, agreed by every seat that touched it

- **The record.** Every number traced equals its file (the mathematics seat's seventeen; the underwriter's claims T1 to T6). The 233
  official runs played back in 5c and 5d are read from their raw files, every file matching its run's SHA-256 list (the builder's own
  check reads the same: 1,803 of 1,803 for Crane's four ways, 4,717 of 4,717 for Karmada's, and so on through every table).
- **The engine.** One engine, omni-v16, digest `5c5502f12b1c0ce4`; the page's compass law, brain and verdict equal the Python and the C++
  to 10⁻¹⁵ (the C++ twins: 12 parity checks, 10,788 live readings, the Python's 500 runs through the C++ engine, every number identical).
- **The two sides and the three words.** Native and Omni-Compass on top of native, defined the same way on the title page, in the key,
  in the guide and in the disclosures; GAIN, STEADY and LOSS by the gauge's aim, power given never called a loss, the floor applied in
  the three-run judge and the cloud tally; the orchestrators' own cost counted apart from Omni-Compass's and never as its reading.
- **The words.** No greeting, no padding beyond two places the editor named, no hype; "brake", "bowl", "better", "worse" (as verdicts),
  "simulation" (for our own models), "standalone" and "competitor" absent from the prose; formulas in Unicode, no LaTeX; the notice
  first and last, word for word with `tools/legal.py`.
- **The skeleton.** 504 ids, none duplicated; every one of the 41 contents links and the dock's resolves; the sections 1a to 11 and vi
  numbered without a gap; 61 monitors numbered by one rule, each wall tile naming its section and scrolling to its badge; 138 textual
  "section x" references, every one to a section that exists.
- **The outside figures** are attributed and disowned; every model is marked class S and shown beside the real, never as proof.

## 3. The findings, merged (33 distinct majors)

| # | Seats | Where | What was wrong | What was done in this push |
|---|---|---|---|---|
| 1 | S1, E3 | iv the key; 4's lede; the Ask panel; 5e, 5f, 8b, 11 | The page stated the key's rule two ways ("the number beside it is only the size, never a direction") against the one key, printed sizes unsigned in four sections and signed in others, and its walker signed a range at one end only. | The key's sentences are the house key's (the number beside a word carries the word's sign: GAIN +, LOSS −, STEADY =, power given +), in iv and in 4; every size and interval is printed by `byWord`, `byWordRange` and `signRange` where it is formatted (the three-run cells, the self-governed rows, the shipped controller's table, the benefit words, the board's tally, the trading floor, the heartbeat monitor); the Ask panel's rule is the same; `tools/readings.py` carries `word_sign`, `by_word` and `interval_by_word` for every table and report. |
| 2 | S2 | 8c `#vKeep` | The keep rates 32%, 17% and 1%, shares of trials kept, printed with a minus: the walker's tails rule signed any number after a word span. | The tails rule signs only a number that follows a bare word; a word span that already holds its own size signs nothing after it. The keep rates print as shares. |
| 3 | S3 | 2 the board | Only the rows at the highest engine number stood on the board; the standing Kubernetes and plant tables (each its benchmark's newest) were called the road; the tally's words named categories it did not hold and misstated the gap to the index. | The board and its tally take each benchmark's newest table whatever its engine, each row naming its engine; the tally's words come from its rows; the Omni index is printed beside it as a second reading of the same tables, with no written explanation of any gap. |
| 4 | S4 | 4 the realms; 2 the organisms | GAIN and power given printed at 0.0001% to 0.04%, under the key's floor of half of one percent. | Every realms word takes the floor (`SIZE_FLOOR`, 0.005): under it, STEADY with its size. |
| 5 | S5 | iv; 9 | A pod start wait LOSS of the orchestrator's own comparison (Omni-Compass on the organism alone against the orchestrator as shipped) presented as Omni-Compass's start wait on real Kubernetes. | The start-wait sentence counts Omni-Compass's own tables only. |
| 6 | S6, M1 | ii the build line | "Every model on this page runs on it" against the realms table (omni-v8), the orchestra and the CPU host model (omni-v12) and the grid's road (omni-v5). | The build line: every live view runs on omni-v16; the recorded models name their own engines until their reruns land. |
| 7 | S7 | 3 the cloud receipts; 5a | An interval that includes zero (−9.1% to +30.9%) printed as if wholly on the LOSS side; failed requests read by two rules on one page (any rise in 3, the interval in 5a). | `byWordRange` prints an interval that includes zero as it lies, whatever the word; failed requests read by the key's never-more rule in both panels (any rise in a run is LOSS), and each panel says so. |
| 8 | M2 | ii; `DISCLOSURES.md` section 3; both manuals | The factory tune stated as "the heartbeat at 15 s, the same in every run" when every table on the page ran an engine that decided every 60 s. | The tables prove the factory tune of the engine each names, every clock, gain, guard and card as that engine shipped it; omni-v16's 15 s is named as the engine that stands, with its tables running; the disclosure and both manuals read "every published result is the factory tune of the engine its table names". |
| 9 | M3 | ii the disclosure; vi | "Every real-run figure on this page is played back from the raw files" when the receipts are read from the tables and four omni-v14 tables have no raw run archived. | Closed in its sentence: the disclosure separates the runs played back (raw files, each checked against its SHA-256 list) from the three-run tables (read as the repository holds them, each naming its runs) and says the raw branch holds the folders as they are archived; the playback of 5c lists each table's archived runs, and a table with none shows none. |
| 10 | M4 | iv; 2 | The headline index is one mean over tests on three engines, with no engine named on the headline, and "the index governs" where the board's total differs. | The headline names the engines of the tables it weighs (iv's first line, the board's figure-of-record row); "the index governs" is struck; the index file's own engine sentence is realigned in the tool that writes it (`tools/omni_index.py`). |
| 11 | M5 | 3 | The composition multiplies layers that stand on different engines (and two omni-v1 one-run cloud factors) without saying so on the page. | Section 3 says which engines the layers stand on, that the composition is across engines, and that it is remade as each layer's omni-v16 three runs land. |
| 12 | M6 | 1g | The knob column was chosen by a regular expression on the gauge's name: it contradicted the recorded cause where that cause is the rig, and asserted a knob where the cause is under investigation. | A knob is named only where the recorded cause is the governor's; the rig reads "the test machine, not the governor"; an open cause reads "no knob named: the cause is not yet established"; 1g's summary says so. |
| 13 | M7 | 1d | A LOSS row was marked answered by another setting's tables (the vanilla scheduler by the bin-packing profile's four ways). | A row is answered only from the same setting's tables on the same gauge; otherwise its LOSS and its red stand until the engine that stands has run the benchmark three times. |
| 14 | M8 | 5f | "The highest-value integration point", "the most valuable receipts … the same work for less power on the chip itself", before any chip has run on a fingerprinted engine. | 5f states what the chip receipts will measure, no result before its record; the superlatives are struck. |
| 15 | M9, E1 | ii; both manuals | "found and confirmed as the best state": the word struck on 11 October, and a superlative no record carries. | "found in its own models before any real run": the model gate reads no LOSS against the engine before; it finds no best. |
| 16 | E2 | iv the key | The key gave Omni-Compass a spine, the organ every other section gives the organism. | Brain, nerves, immune system and heart; the spine stays the organism's. |
| 17 | E4 | 2; monitor 11 | Power given "the accent" against the key's blue and the drawing's blue. | Blue, in the trading floor's text and in the registry's monitor 11. |
| 18 | E5 | 3; 10a | Two ways a stack is bought and four ways composed in one section, with no sentence joining them. | "The composition is read four ways: the two ways a stack is bought, and two more that take its pieces alone, in the device and as a service"; 10a's item aligned. |
| 19 | E6 | vi | The disclosures named OMNI_V13 as the engine that stands under a title page that says omni-v16. | The paragraph names the engine that stands as the build names it; OMNI_V13 remains only in the sentence that tells what omni-v13 fixed. |
| 20 | ST1 | the front matter | 30,271 visible characters (about eleven printed pages) before the wall, 34,933 before the first monitor, against the founder's order that the wall hit first. | In part: iii and iv fold to one lead paragraph each (18,231 visible characters before the wall with the folds closed, against 32,277 open, by one count of the page as it stands); the move of the wall ahead of them is the founder's decision (section 4). |
| 21 | ST2 | 2; iv | The one combined number, the Omni index, the fourth panel of the sixth section and absent from the executive summary. | In part: the index is the first line of the executive summary, written from the benefit record; the board's panel order and a strip above the wall wait on the same decision. |
| 22 | ST3 | 10 | The fifth lettered part with no part heading; the contents' 10 and 10a on one anchor. | The part head `#p-parts` before 10a; the contents point at it; the word-for-word appendix rebuilt with it. |
| 23 | ST4 | v | 19 of 36 titled entries differed from the heading they pointed at; 5 pointed at items that print no numeral; no test held the contents to the headings. | Every entry is its heading's text, held by `tests/test_live_toc.py`; the four front- and back-matter items still print no numeral on themselves (a minor now). |
| 24 | ST5 | iv | The quick-start reading guide described monitors 39 and 40 of section 6a, ten sections below, and nothing of what the reader meets next. | Moved under 6a's heading as its reading guide. |
| 25 | ST6 | `docs/engine/monitors.json` | The registry not in the order its rule states, with no number field. | Sorted in the page's order, each entry carrying its number `n`; the Grafana export's test reads the page's order. |
| 1, 17 again | V3, V2 | 1g, iv, 5f, the quote board, the radar; the prose and two legends | On the 08:41 build the sign rule still missed five places (1g's cells printed the raw sign beside a LOSS chip; iv's ranges signed one end; 5f and the radar kept raw signs; the quote board's number stood without its word), and power given was green in the prose, the status board and two legends. | 1g's cells read through the page's cell formatter (LOSS −5.1% (−1.9% to −8.3%)); every range in iv and the readings carries the word's sign on both numbers (LOSS −5.1% to −9.1%); 5f's change and interval cells and the radar's sizes take the word's sign; the quote board prints the word beside its number; power given wears its own class in the prose, blue, and blue on the market map, the quote board's strip and the legends. |
| 26 | V1 | ii | The two lede paragraphs shared one grid cell and printed over each other on the first screen, at 1280 and at 390 px. | Each lede has its own row at both widths (rendered and measured: the second starts 115 px below the first at 1280, 12 px at 390). |
| 27 | V4 | 8b, monitors 52 and 53 | The phase planes stayed side by side at 167 px on a phone, axis labels colliding and captions cut. | They stack under 560 px, native above, as every pair does (rendered: one 342 px column). |
| 28 | V5 | 5a monitors 20 and 21, 5e monitors 32 and 33 | At 390 px the pod dots print over their caption. | The pods sit inside their machine's box at any width; past what a box holds, its count is written in its corner (rendered at 390 and 1280 px). |
| 29 | V6 | 5f monitor 36 | At 390 px the "awaiting its machine" stamp prints over the column heads. | Under 640 px the stamp takes its own line under the lane heads (rendered). |
| 30 | V7 | 6a monitor 40 | At a 308 px ring the centre's three lines and the state letters print over each other, worst with the switch OFF. | On a ring under 400 px the six gauges are ticks alone and the centre's words are fitted inside the circle: OFF in red with the switch off, the calm or the lease under it (rendered ON and OFF). |
| 31 | V8 | 4 monitor 14 | At 390 px the seven organisms' three load columns print over each other. | Under 600 px the three loads stack as three bands of the seven organisms, each under its own label (rendered). |
| 32 | V9 | 5a monitor 17 | At 390 px the Azure sets' axis labels run together. | A bar too narrow for two label lines carries its engine alone; the reading line under the axis names the set the cursor is on, its pairs and its bill (rendered). |
| 33 | V10 | 1i monitor 8 | At 390 px the workflow bars collapse and their count boxes cut the names. | Under 600 px one workflow a row, its name above its bar and the count after it; the canvas grows with the rows (rendered). |

## 4. The order of the page: the structure seat's proposal, its cost, and the founder's decision

**What a first reader needs, in order** (the seat's words): what it is; the two sides; the three words; the proof at a glance; the proof
in numbers; why (the problem and the answer); the proof in full; the mechanism; the controls; the brain; the limits; the components; the
provenance; the law. The page's body already runs proof, mechanism, brain, components; what stood wrong was the front: eleven printed
pages of what-it-is before the proof at a glance, the one number at the foot of section 2, and a chart's reading guide in the front
matter.

**The order proposed** (no monitor number moves, because no canvas moves): i the legal notice; ii the title page on one screen (the
title, the engine and build chips, one lede sentence, one strip naming the two sides and the three words with their colours); v the
contents on one screen, generated from the headings; **1 the monitor wall and the control panel**, with the kill switch, the Python's
runs, the three manuals and the Grafana export folded into the wall's head row and a one-line strip of the Omni index and the three-run
tally above the tiles; **2 the executive summary and the key** (the former iv, the Omni index its first line); **3 the problem and the
answer** (the former iii, in full); then the benefit board, the whole organism, the measured effect, the evidence by stack, the organism
live, the console, the brain, the failure modes, the components, the self-governed rendering, vi and vii as they stand, renumbered 4 to
13.

**The cost.** The body numbers 2 to 11 become 4 to 13, so about 115 of the page's 138 textual "section x" references change (the 22 or
so to 1a to 1i do not), the manual's section labels in its chapter headings and Appendix A change, and the word-for-word appendix is
rebuilt by its builder; no anchor changes and no monitor number changes.

**The cheaper path, if the founder keeps iii and iv in the front matter** (his order of 21 October for the README and the manuals:
the problem and the answer first): ii, iii and iv cut to one screen each (about 1,500 characters apiece, their full texts already in the
manual), the contents folded to short entries that equal shortened headings, 1a folded into the wall's head. That leaves about 6,000
characters (1.5 desktop screens, two printed pages) before the wall, with no renumbering. It still leaves the proof after the why; the
first path puts the proof first, as the founder's words of 22 October ask.

**What this push did, pending his word:** iii and iv keep their full texts under a fold, each opening on a lead paragraph (the problem
and the answer in four sentences; the two sides, the three words, the three classes and the figure of record in one paragraph, the Omni
index as its first line), so 18,231 visible characters stand before the wall with the folds closed. The founder decides between the
first path, the cheaper path and the page as it stands.

## 5. The visual seat

Read on the 08:41 UTC build of 23 October at 1280 and 390 px, every finding naming the screenshot it was read from: overall **B**,
desktop alone A−, phone alone B−; 10 majors, 17 minors, 10 nits (`docs/engine/audit_2026-10-22/seat_visual.md`). What holds: no console
error, warning or page error in any load of either build; the page never scrolls sideways at either width, every wide table scrolling
in its own frame; every one of the 61 monitors drawn; the notice first and last at both widths; the kill switch sets every Omni-Compass
side to native's tint at one press and restores it. What it found is in section 3: ten majors, all closed (V1 to V4 in the push of this
page, V2 and V3 with the editor's and the mathematics seat's findings; V5 to V10, each a phone-width overprint inside one monitor, in the
push after it, every one rendered again at 390 and 1280 px).

## 6. Method and limits

Five seats, each an independent reader briefed on one dimension and on the standing orders, read-only, with the page file, the
registry, the builder, the exporters, the manual and the repository's records; the mathematics seat recomputed every number it names
from the records themselves; the underwriter traced every claim it names to its file and back; the editor searched the prose for the
retired words and the house terms; the structure seat counted anchors, headings, references and characters; the visual seat rendered.
The grades are of the page as it stood at 22:05 UTC on 22 October; the fixes of section 3 came after it and are not graded here. Every
model named is our own (class S) and is proof of nothing. Run and read by The Omni-Compass LLC's own code and its own readers; no
outside party has reviewed or approved these results or this audit.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

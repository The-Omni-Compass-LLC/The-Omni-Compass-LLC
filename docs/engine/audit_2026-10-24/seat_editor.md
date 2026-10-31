# The live engine, graded: the editing seat, 24 October 2026

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

**The page audited.** `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html` on the branch `claude/interactive-animated-charts-icvnsw` at commit
`401417998e` (the founder's order of 25 October, "Omni-Compass is never by itself"), as frozen in `audit24/` for this audit:
36,947,887 bytes, 7,971 lines, SHA-256 beginning `7531404530dec345`, `data-engine="omni-v19"` and `data-prose="omni-v19"` on line 2.
Its embedded build record still reads omni-v19, digest `36ee67284c035235`, built 2026-10-24 23:09 UTC at `092e512c4876`. Read in full:
the page's prose outside its nineteen JSON records (the HTML rendered as text, section by section), the strings its JavaScript prints
(the bottom line, the switchboard, the control panel's tabs and groups, the executive summary, the notes of 3d, 3l and 3m, the
master switch's list of governors), the texts the page prints from the monitor registry (`monitors`) and the glossary record (`glossary`), the
word-for-word map regenerated from this build, the Live Engine Manual as rewritten for it (3,061 lines; its PDF of 25 October), the
editing seat's report of 23 October and the consensus audit of 22 October. This seat began on the build of 24 October (`d78fb046e7`,
8,107 lines); every finding was checked again on this build, findings about the removed third arm and section 3n were dropped, and every
line number below is this build's. Read-only: nothing in the repository was edited and no builder was run. No other seat's report was
opened.

**This seat.** Editing only: the house word rules (compass, one pedal and no "brake", the two arms, GAIN / STEADY / LOSS and power given,
no "confirmed", no "simulation" for our own models, and since 24 October no "model" and no "stand-in"), Unicode formulas, the sign rule; then
repetitions and padding, typos and grammar, sentences a reader would misread, two places that contradict each other, text that describes
a control or monitor wrongly (checked against the JavaScript handlers), headings that do not say what the section holds, and jargon left
undefined at first use.

**The scale.** A+ a few minors, no major; A one major or several minors; A− more than one major; B+ several majors, none a blocker; B a
blocker or many majors; B− and C several blockers; D and F unsound. A major is a retired word, a contradiction between two places, a
sentence a reader would misread, or text that describes a control or monitor wrongly or one that is not there. A major that lives in
several sections counts against each section where its wrong sentence stands.

## 1. The grade

**Overall: B.** The prose is still referee prose: the two sides are defined in matching words at every definition (title page 647, chip 657,
key 1930, disclosures 1988), the sign rule is taught rightly in the key (1932, 1933) and in 4c (1677), power given is blue in the key
and never called a loss, every model is marked class S, every outside figure is attributed and disowned (1909), formulas are Unicode
with no LaTeX, and the notice stands first and last. The removal of the third arm was done cleanly in the prose: no "Omni-Compass
direct", no violet side and no "thirty" survives in the visible text. What holds the page at B is seventeen majors, almost all of them
sentences left over from an earlier page: three retired words ("confirming", "simulation"/"simulated", "model" in printed file paths);
the page describing an order it no longer has (title page, 1b, 2d); "never by itself" set beside an engine and a default panel that
run without a native controller (title page, 4d, 3l); the bottom line's yardstick left unnamed now that 3n is gone; two controls
described wrongly ("five tabs", the glossary's five beats); the kill switch called "native alone" in two places and "separate" in two
others; the heartbeat stated as 15 s in three sections and 60 s in three; STEADY defined two ways in the key itself; nine stale
cross-references to sections that no longer exist; the one GPU run named four ways; ten organisms against seven and an eighth; and two
majors of 22 October back again (power given "the accent" in the registry; `OMNI_V16.json` as "the engine that stands" in the
disclosures). Nine of the seventeen are one-line fixes.

| Section | Grade | Why, in one sentence |
|---|---|---|
| ii Title page and build | **B+** | "finding and confirming the best" (662), a book order the page no longer has (647, 659), and "never by itself" beside an engine that "added ... to run Omni-Compass by itself" (647): three majors. |
| iii The bottom line | **A−** | The yardstick is labelled "Kubernetes' published autoscaling rule" with no word that the rig is the company's own, without Kubernetes (E7), and STEADY is "no difference beyond 0.5% or the noise" and "STEADY only inside 0.5%" in one paragraph (674, E12). |
| 1a The monitor wall, with the main control panel | **B+** | "five tabs" where the panel builds seven (703), "Native alone is the kill switch" (698) against the reset's own label, and the Drive tab's group "every beat, simulated" (5507). |
| 1b The control panel and the kill switch | **A−** | "The first view after the front matter" and "The monitors it drives follow: the wall of every monitor (1a)" (728) describe the old order, and "the proof monitor, 1f" twice (735) points at a section that is gone. |
| 1c The dashboards | **A+** | The nine forms named as the code builds them (5635), the who-does-what table and the five products exact and attributed; nothing to fault but the founder's date in the contents. |
| 2a The status board | **A+** | Exact; its own layout paragraph stands one section later (minor, 2b). |
| 2b The golden signals, the event log and the metrics | **A** | The status board's layout paragraph (810) sits here, and sends the reader to the key at "front matter, iv", which is now the contents (E13). |
| 2c Every LOSS row | **A+** | Exact and complete; no word to change. |
| 2d The benefit board | **A** | "The first thing after the wall" (826) is no longer true: five sections stand between (E4). |
| 3a The organism, live | **A** | The anatomy's heart beats "every 15 s on omni-v16" (928) under a page whose factory beat is 60 s (E11); "Two engines, one demand" (872) and "a cyborg lives on two nutrients" (933) are minors. |
| 3b Control console | **A** | "Native alone is the kill switch above" (950) against the reset (E10); one knob still carries three names ("sensor latency" 946, "Sense delay" 954, "sensor delay" in the registry). |
| 3c The heartbeat dial | **A−** | "the key at the top of the page" (995) points at 4k (E13), and `results/model_gate/V17_LADDER.json` (989) prints the retired word (E3). |
| 3d One control cycle | **A** | The cycle's note sends the reader to "the live controller of 5e" (3095), which is now 3l (E13). |
| 3e Phase plane and scoreboard | **A+** | Exact; the reading rule written out in full (1099). |
| 3f The brain's internal state | **A+** | Exact; "E_max", "αₛ" and "γ[c]" in three notations on three consecutive lines (1109–1111) is a minor. |
| 3g The verdict | **A** | `tools/model_gate.py` (1153, E3); "Above the verdict the max never goes below native at all, so in the default it never runs" (1153) still cannot be followed (minor). |
| 3h Cloud providers | **A** | Exact on the bill; the whole "THE CLOUD IS A WIRE" box is printed twice, here (1160–1162) and in 4a (1621–1623), word for word (minor). |
| 3i Orchestrators and governors | **A+** | The four ways and the orchestrators' own cost kept apart in every sentence. |
| 3j Kubernetes: official run playback | **A−** | The heart is "every 15 s" on omni-v16 (1261, 1262) with no word for the engine that stands (E11), and `results/model_gate/HEARTBEAT_SWEEP.md` (1270, E3). |
| 3k Kubernetes: per-repetition telemetry | **A+** | Exact; class, source and scorer named in one paragraph. |
| 3l The shipped controller's decision trace | **A−** | The panel opens on a setting whose caption reads "the controller driving the machines itself ... turns the Cluster Autoscaler off in this arm" (3388), against "never by itself" (E6); its cloud note prints `tools/model_gate.py` (3390, E3). |
| 3m Hardware: the GPU card and the CPU host | **A−** | "No GPU card ... has been measured on the engine that stands" (1429) and, three paragraphs on, "The engine that stands on a real card" for omni-v18's card governor (1440) (E14); the chip notes print `tools/model_gate.py` and `MODEL_GATE.md` (3487, 3496, E3). |
| 3n Telemetry analytics, Omni-Compass in its own words | **A** | Clean of retired words; the Ask panel's "speaks for itself" (1513) and its chip "Show me your largest GAIN" (1566), and the radar's "helped"/"hurt" (1554), are minors. |
| 3o The Python's runs in the page | **A** | "On GitHub (the simulation done within GitHub, on its own machines, at no cost)" (1608): our own model called a simulation (E2). |
| 4a The whole organism | **A−** | "The chip's one measured run (2 October ...)" (1627) against 3m's A100 run of 24 October (E14), and `tools/model_gate.py` in "Beyond the count" (7553, E3); the heading still has four ways "bought" where the text has two (minor). |
| 4b The twenty scenarios | **A** | "The ten organisms" (1669) count this page's sixty-muscle body and the whole stack as organisms, which 4a (1628) and 4c (1680) say are not (E15). |
| 4c Measured effect in full | **A** | Minors only: its first paragraph is 2d's (1677), "results/live/V10_*.md today" (1709), "OMNI-COMPASS" in capitals (1690). |
| 4d The C++ twin | **A** | Its "Python only" table prints "Omni direct's control plane, hand, walls and front" (from the record, line 2014), the arm the title page says is not shown (E5). |
| 4e CI pipeline | **A+** | Exact. |
| 4f The master switch's wiring | **A** | The governor table prints "(sections 2d to 4c; front matter iv)" (7880), and iv is now the contents (E13). |
| 4g Component specification and mathematics | **A** | "the official-run playback of 5c and 5d" (1773) and "its decision trace in 5e" (1804) name sections that are gone (E13); the underscore subscripts (1789–1804) are a minor. |
| 4h Failure modes | **A+** | Exact. |
| 4i Self-governed rendering | **A+** | Exact, with its class and its limit in one paragraph. |
| 4j The problem and the answer | **A** | "on Kubernetes its full read of the state every 15 seconds, the autoscaler's own pace" (1903) against the factory's 60 s (E11). |
| 4k Executive summary and reading key | **A−** | The key teaches the 0.5% floor (1932) and then "STEADY =0.9% means a 0.9% difference the noise covers" (1933) and "no difference beyond the noise" (1936) (E12); the summary points to "(section 3)" for the composition (6950, E13). |
| 4l The monitor list | **B+** | The registry it prints gives power given "the accent" (monitor 7), names the A10 of 2 October as "the one real run" awaiting "its omni-v13 run" (monitor 43), and prints `tools/model_gate.py` in about twenty wiring cells. |
| 4m Glossary and index | **A−** | "the heartbeat": "the page offers five, 15, 30, 60, 90 and 120 s" (E9, six buttons from 10 on the page), and the heading's "ten organisms" (E15); "Amber on the page" for native is a minor. |
| v Disclosures, governing law and contact | **A−** | "OMNI_V16.json, docs/OMNI_V16.md, the engine that stands" (1992, E17) and "The GPU, CPU and cloud places are written and marked not yet run" (1995, E14). |
| The Live Engine Manual (`docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md` and `.pdf`) | **B+** | Aligned with the page section by section and in several places more exact (seven tabs, six beats, the reset), but it prints "One pedal, no brake" in a figure caption (2022), carries the page's kill-switch contradiction (714, 1578 against 883, 1323), and reads 1c inside chapter 6 ahead of 1b with no row for 1c in Appendix A. |

## 2. Majors

Line numbers are lines of the audited page unless the manual is named.

**E1. A retired word and a superlative on the title page (ii, 662).** "The best validated profile is not yet established: the factory
profile is the one released with the engine, no profile on this page is locked as the baseline, and finding and confirming the best, knob
by knob, is the standing work of the sweeps." "Confirming" is the word struck on 11 October; "the best" is a superlative the record does
not carry (the same box defines the factory tune by a rule, "of the tunes that harm no gauge against native, the one against which no
other tried tune reads GAIN on one service gauge and LOSS on none"). This is the E1 of 23 October ("found and confirmed as the best
state") come back in another sentence. **Fix:** "No profile on this page is locked as the baseline: the factory profile is the one
released with the engine, and reading every knob against it, one at a time, is the standing work of the sweeps (docs/FACTORY_PROFILE.md)."

**E2. "Simulation" for our own models (3o, 1608; 1a, the Drive tab, 5507).** "On GitHub (the simulation done within GitHub, on its own
machines, at no cost)" describes the core's Monte Carlo run by the repository's own Python and C++; the Drive tab's group label is
"every beat, simulated" for the live model's sweep. The house word for our own models is "modelled" (class S); "simulation" stays only in
the licence's phrase and for outside simulators. The manual quotes both phrases (849, 2222). **Fix:** "On GitHub (the same runs, on
GitHub's own machines, at no cost)"; the group label "every beat, modelled".

**E3. "Model" printed on the page in file paths (3c 989, 3g 1153, 3j 1270, 3l 3390, 3m 3487 and 3496, 4a 7553; 4l, about twenty wiring
cells from the registry).** The prose calls it "the model gate" everywhere, but the paths `tools/model_gate.py`,
`results/model_gate/V17_LADDER.json`, `results/model_gate/HEARTBEAT_SWEEP.md` and `results/model_gate/MODEL_GATE.md` print the word the founder's
order of 24 October says appears nowhere. The manual prints three of them (467, 1661, 1996). **Fix:** rename the tool and its folder in
the repository (`tools/model_gate.py`, `results/model_gate/`) and let the builder write the new paths; until then, print each path through
one alias in the builder ("the model gate's record").

**E4. The page describes an order it no longer has (ii 647 and 659; 1b 728; 2d 826; the contents' grouping).** The title lede: "It is
laid out as a book, read from the top down: this title page first, then the problem and the answer ..., then the executive summary and the
reading key, then the table of contents, then the monitor wall ...". The page now runs title, bottom line, contents, Parts 1 to 4, and the
problem and the answer and the key are 4j and 4k. 1b: "The first view after the front matter: the control panel ... The monitors it drives
follow: the wall of every monitor (1a)": 1a comes before 1b. 2d: "The first thing after the wall": 1b, 1c and 2a to 2c stand between. The
chip says "four parts ... · the disclosures" while the contents file Part 4 under "Back matter" with v and vi. **Fix:** replace the lede's
sentence with the contents' own ("the notice, the title, the bottom line and the contents; then the monitors and every knob; what they
say; every monitor spread out; the organisms and everything else; the disclosures"); in 1b, "The control panel under the wall:" and "The
monitors it drives are the wall (1a) and ..."; in 2d, "Every benchmark's measured effect in one board"; in the contents, head Part 4
"Main matter" and keep "Back matter" for v and vi, or make the chip say so.

**E5. "Never by itself" beside an engine that runs Omni-Compass by itself (ii 647; 4d, the Python-only table, from line 2014).** In one
paragraph: "Omni-Compass is never by itself (the founder's order of 25 October): it always sits on top of a native controller" and "what
omni-v18 and omni-v19 added to run Omni-Compass by itself (Omni direct and a pod muscle of its own) is not shown on this page ... and
taking it out of the engine is the next version's". A reader is told a property of the product and, in the same breath, that the engine
that stands has the opposite capability; 4d then prints "Omni direct's control plane, hand, walls and front". The sentence also ends
elliptically ("is the next version's") and uses the bare "Omni". **Fix:** state it as the page's rule, not the product's nature: "On this
page Omni-Compass is never run by itself, by the founder's order of 25 October: it always sits on top of a native controller. The engine
that stands, omni-v19, still carries the code omni-v18 and omni-v19 added to run it alone (its own orchestrator and a pod muscle); this
page shows none of it, and the next version removes it." Drop the `omni_orchestrator` row from 4d's Python-only table or word it the same
way.

**E6. The 3l panel opens on Omni-Compass with the native controller switched off (3l, the default setting, 3376 and 3388).** The setting
the panel opens on ("On top of the HPA, the max", `CW.setting = "selfpilot"`) captions the Omni-Compass lane "on top of the HPA, the
controller driving the machines itself (its defaults: the max; pilot/selfpilot.py turns the Cluster Autoscaler off in this arm)". The
title page (647) and the key (1930) now say Omni-Compass "always sits on top of a native controller, on muscles that have their own" and
"needs muscles with their own native controllers under it". On the machine muscle of this arm it has none. **Fix:** either word the rule
to match the record ("on every muscle but one modelled setting of 3l, where the Cluster Autoscaler is off") or make the cloud setting, on
top of the cloud's own autoscaler, the panel's default and caption the other "the controller in place of the Cluster Autoscaler (a modelled
setting kept as its own record)".

**E7. The bottom line's yardstick is not named for what it is (iii, 7405 and the note from the record, 2018).** The first verdict on the
page reads "Native alone (the yardstick: Kubernetes' published autoscaling rule)" against "Omni-Compass on native ... more work". The note
says "native is Kubernetes' published autoscaling rule on the muscles, written by us", but nowhere does the page now say on what machines
and under what orchestrator the test ran: section 3n, which said "Omni-Compass's own orchestrator ... with no Kubernetes", is gone, and
the record is still named `V18_THREE_ARMS_ABC.json`. A referee reads the row as Kubernetes' own HPA on Kubernetes. The manual (2.3) has the
same gap. **Fix:** row label "Native alone: Kubernetes' published autoscaling rule, as the company wrote it, on the repository's own test
machines (no Kubernetes)"; one sentence in the note on the rig (six half-processor machines, the checked web service and the batch job,
18 steps of 25 s), and the record named as "the pair native and Omni-Compass on native of `V18_THREE_ARMS_ABC.json`".

**E8. "Five tabs" (1a, 703).** "Under it, five tabs: Drive ..., The mechanism's knobs ..., The twenty scenarios, The breakers ... and
Everything". The panel builds seven (`FTABS`, 5549): Drive, The mechanism's knobs, The twenty scenarios, The breakers, Metrics (Prometheus),
Commands, Everything; the line two rows down already says "(the Commands tab lists them all)". The manual says seven (786). **Fix:** "Under
it, seven tabs: ... The breakers (...), Metrics (Prometheus) (the live model as a Prometheus endpoint, with the series and the PromQL),
Commands (every control beside the request a running governor takes) and Everything".

**E9. The glossary describes the heartbeat buttons wrongly (4m, the glossary record, line 2020).** "the page offers five, 15, 30, 60, 90
and 120 s": read as a count it leaves out 10 s; read as a list it adds 5 s. The page has six buttons, 10, 15, 30, 60, 90 and 120 s (`BEATS`,
2305; 3c 990; the switchboard 742). **Fix:** "the page offers six, 10, 15, 30, 60, 90 and 120 s".

**E10. "Native alone is the kill switch" against "the kill switch, for security, is separate" (1a 698; 3b 950; against the profile row's
Return to native, 5508, and the switchboard's native arm, 6715).** The wall's factory box: "Native alone is the kill switch, beside it on
the console." The console: "Native alone is the kill switch above: that is the other scenario, not a tune." The Drive tab's Return to
native: "the reset ... every setting handed back to native and the governor stopped; the kill switch, for security, is separate"; the
switchboard's native button calls the reset, "the kill switch, for security, is separate". The house rule is the second: the kill switch is
for security only; the reset hands everything back. A reader told twice to use the security switch to see native alone has been taught the
wrong control. The manual repeats both sides (714 and 1578 against 883 and 1323). **Fix:** in 698 and 950, "Native alone is Return to native
(the reset), in the control panel's profile row; the kill switch beside it is for security."

**E11. The heartbeat: 15 s in three sections, 60 s in three (3a 928; 3j 1261–1262; 4j 1903; against 3b 950, 3c 990, the switchboard's
default 742 and the glossary).** The anatomy: "the governor's decision loop beats once per decision, every 15 s on omni-v16 (native's own
pace)". 3j: "On omni-v16 the governor's heart beats at the pod autoscaler's own pace, a full read of the state every 15 s". 4j: "on
Kubernetes its full read of the state every 15 seconds, the autoscaler's own pace". 3c: "the main engine decides every 60 s"; the factory
tune "the 60 s beat". The three 15 s sentences are each true of omni-v16, but none says what the engine that stands does, so a reader of 3a,
3j or 4j learns the wrong beat. **Fix:** "every 60 s at the factory since omni-v17 (any of six beats from 10 to 120 s on the dial, 3c);
omni-v16 ran it every 15 s" in 928 and 1261; in 1903 "its full read of the state every 60 s at the factory, 15 s or faster on the dial, and
its fast checks every 5 s".

**E12. STEADY defined two ways, inside the key (4k 1932, 1933, 1936; iii 674; the contents 686 and Part 2's lede 783).** 1932: "a change
under the 0.5% floor reads STEADY =0.3%"; "a change under half of one percent either way, in every run, reads STEADY". 1933: "STEADY =0.9% means a
0.9% difference the noise covers, no direction claimed". 1936: STEADY is "the same, or no difference beyond the noise". iii, in one
paragraph: STEADY is "no difference beyond 0.5% or the noise", then "STEADY only inside 0.5%". The code (`threeRun`, 3242) reads the floor
alone: a mean of 0.5% or more is GAIN, LOSS or power given whatever its interval, so the bottom line prints "GAIN by the mean of our three
runs, beyond the noise in 1 of 3" for the machines. Under 1933 and 1936 a reader expects that row to read STEADY, and 0.9% can never read STEADY.
"In every run" (1932) also differs from the code's "the mean of the three runs". **Fix:** one sentence in all six places: "STEADY: the change
is under the 0.5% floor (the mean of the three runs' changes); from 0.5% the word follows the gauge's aim, and the count of runs beyond the
noise is printed beside it." Change the 1933 example to "STEADY =0.3%", and the key row to "native and Omni-Compass within 0.5% of each
other".

**E13. Nine cross-references, in seven sections, to sections that are not on the page (1b 735 twice; 2b 810; 3c 995; 3d 3095; 4f 7880; 4g 1773 and 1804;
4k 6950).** "the proof monitor, 1f" and "the Monte Carlo monitor, 1f" (now 3o); "by the key (front matter, iv)" (iv is the contents; the key
is 4k); "the key at the top of the page" (4k, at the end of Part 4); "the live controller of 5e" (3l); "(sections 2d to 4c; front matter
iv)"; "the official-run playback of 5c and 5d" (3j and 3k); "its decision trace in 5e" (3l); "are not in it yet (section 3)" (the
composition is 4a). **Fix:** 3o, 4k, 4k, 3l, "sections 2d to 4c and 4k", 3j and 3k, 3l, 4a; and add a check to `check_live_engine.py` that
every "section NN" and every bare section label in the prose names an anchor on the page.

**E14. The one GPU run named four ways (3m 1429, 1434, 1440; 4a 1627 and 1628; v 1995; the registry's monitor 43, printed on wall tile 43
and in 4l).** 3m's summary: "No GPU card and no CPU package has been measured on the engine that stands"; its next box: "Their runs on the
engine that stands are not hooked up yet"; its panel: "The engine that stands on a real card ... an NVIDIA A100 ... on 24 October ...
omni-v18's card governor". 4a: "The chip's one measured run (2 October, on the card controller since replaced)". Monitor 43: "The NVIDIA A10
run of 2 October", awaiting "its omni-v13 run on Lambda". v: "The GPU, CPU and cloud places are written and marked not yet run". **Fix:** one
statement, printed from the record in every place: "One metered run on a real card: an A100 on Lambda, 24 October, omni-v18's card governor
(B and C not yet run); the A10 run of 2 October stands as its own record; no card run on omni-v19 yet." Write monitor 43's state and title
from the same record; in v, "The CPU place is written and marked not yet run; the GPU has one run (3m); the clouds' runs are in 3h."

**E15. Ten organisms against seven and an eighth (4b 1669; 4m heading 1976; against 4a 1628 and 4c 1680).** 4b: "The ten organisms (the
spine; the four realms; the four stacked; the whole tower; the orchestra; this page's own sixty-muscle organism; and the whole organism in
its three places)". 4a: the whole stack "is not counted among the organisms (the seven, and the orchestra the eighth)"; 4c: "a composition
with two arms, not an organism of the catalog". **Fix:** in 4b and 4m, "ten bodies: the seven organisms, the orchestra (the eighth), this
page's sixty-muscle body and the whole stack's composition", or count the last two as organisms in 4a and 4c too; one count everywhere.

**E16. Power given "the accent" again (the registry's monitor 7, line 2011; printed on wall tile 7 and in 4l).** "its colour its reading
(GAIN green, LOSS red, STEADY yellow, power given the accent, an orchestrator's own cost grey and dashed)". The key: "or blue for power given,
and no other"; 2d's prose (848) now says "blue where it gave power". This is E4 of 23 October, closed in the prose and not in the registry.
**Fix:** "power given blue" in `docs/engine/monitors.json`, and a grep for "accent" in the registry's texts in `check_live_engine.py`.

**E17. The disclosures name omni-v16 as the engine that stands (v, 1992).** "The engine, its fingerprint and its source: the repository
(OMNI_V16.json, docs/OMNI_V16.md, the engine that stands)", under a title page that says omni-v19 and a build record that says omni-v19.
This is E6 of 23 October (then `OMNI_V13`), three versions on. **Fix:** write the file names from the build record (`OPS_BUILD.engine`), as
the title page already does, and add this paragraph to `tools/land_engine.py --check`.

## 3. Minors and nits

**The two arms, the words.** m1 One arm, four names: "Omni-Compass and native" (647, 657, the switchboard 739, the column heads of 3a 911,
3e 1097, 3l 1410, 3m 1448, 4i 1877), "Omni-Compass on native" (4b 1667, the bottom line's row), "Omni-Compass on top of native" (the key
1930) and "Omni-Compass" (3a's instance head, 889). The chip "native · Omni-Compass and native" reads at first as a list of three. Pick one label for
tables ("Omni-Compass on native") and keep the key's sentence for the definition. m2 Bare "Omni": "Omni direct" (647), "native and Omni
could not be told apart" (the key's STEADY row, 1936), "Omni's own processor" (the dial's table head, 3602). m3 "Two engines, one
demand" (872) uses "engine" for an arm; "Two sides, one demand". m4 "REDLINING" means "behind native" on the lights (674), while the max by
design runs each muscle to its own limit, its redline: an engineer will read the word the other way; the definition is printed beside it,
so it is a minor. m5 The bottom line's heading and the contents still say "One light and one number for each way to run it" (672, 686),
and "Each row is one way to run a workload" (674), over a table of one way and its baseline (675: "The way to run it").

**The title page.** m6 The engine chip's static text is still "engine omni-v16 (digest 5c5502f12b1c0ce4)" (654), filled at run time
(3571); without script the title names the wrong engine (m2 of 23 October). m7 The lede recounts the road from omni-v19 to omni-v11 (647),
about 300 words of engine history on a title page, against the order that reports read native against Omni-Compass and older engines are
history; and "The engine that stands is omni-v19" is said twice (647 and `#bEngRuns`). m8 The build chip says built 2026-10-24 23:09 UTC
at `092e512c4876` while the same page quotes the founder's order of 25 October: the build record was not rewritten with the words.
m9 "turning any knob can change every metric, up or down" (662) while the key says the page "never prints 'up', 'down', 'better' or
'worse'" (1953); either qualify the key's sentence ("as a verdict") or drop it, since naming the words prints them.

**Undefined terms and terms in two senses.** m10 Used before any definition near it: "the max", "the dial", "the tune-down" (662),
"conveyance" (647), "the release gate" (951, 1050, 1378), "organ" (713), "the bone" (868), "the dock" (703), "the main engine" (698, 990,
995, 1270: neither "main" the branch nor "the engine that stands" is said). The glossary (4m) now defines most of them, at the end of the
page; the first-use marks (7944) cover only the twelve acronyms and "fails up". m11 3l's lede says "a decision every 60 s" (1378) and its
table reads "The paired change per 15 s tick" (1411): "tick" is undefined and set against no other clock. m12 One knob, three names:
"sensor latency" (946), "Sense delay" (954 and the knob text), "sensor delay" (the registry); one fault, three: "A sense goes blind" (955),
"a sensor blackout" (946), "A sense blind" (the Drive tab). m13 Two names for one control: "Back to the factory tune" (698, 950, the Drive
tab) and "Restore factory profile" (the profile row, 5508), and "tune" against "profile" for the same thing (662, 686). m14 "Above the
verdict the max never goes below native at all, so in the default it never runs" (1153) still cannot be read without knowing that the
verdict judges give-backs only; "Before a knob moves one step past native" (1134) uses "past" for a step away from native where the page
uses "past" for past the line. m15 3g withdraws "The σ 0.05 and 0.25 this page carried before 19 October" and, three lines later, "The
model gate measures 60 (..., σ 0.25)": a reader takes it for the same σ.

**Repetition, misplacement, padding.** m16 The "THE CLOUD IS A WIRE" box and "The company's own expectation" are printed word for word in
3h (1160–1162) and 4a (1621–1623). m17 The status board's layout paragraph (810) stands in 2b. m18 4c's first paragraph is 2d's benefit sheet
(1677). m19 "What this page is" said twice in v (1987 and 1995). m20 4g's provenance paragraph (1832) recounts omni-v9 to omni-v17 and says
"All are inside the omni-v17 fingerprint" under omni-v19. m21 4a's heading has four ways "bought" (1620) where its text has "bought one of
two ways" and "read four ways" (1627). m22 4j: "every muscle judged on itself, and the organism judged whole" (1905) against v's "The
trade between muscles, judged on the organism, is the next engine version's work" (1989).

**Stale, against the build.** m23 "From each benchmark's newest engine's table ( results/live/V10_*.md today)" (1709). m24 The executive
summary's "Their benefit is the same work for less energy, which the GPU run on Lambda measures" (6958): the A100 run read "at its limit on
native" and wrote nothing. m25 Monitor 9's text (the registry) says "Sixty muscles of the stress model", while the default body is the realms
harness (874). m26 The glossary's "the mechanism panel" still says "on both governed arms", and "native" is "Amber on the page" (2020)
against orange everywhere else. m27 The kill knob's text: "every Omni-Compass side follows native (white)" (the registry) against "drawn in
native's colour" (746, 1765); only the word OFF is white.

**Tone and register.** m28 The anatomy's "a cyborg lives on two nutrients: the electricity ... are its oxygen; the mathematics and the code
... are its food" (933): two nutrients named as oxygen and food, and the metaphor leaves the control vocabulary the page promises.
m29 3n: "Omni-Compass speaks for itself here" (1513), "answers in the first person" and the chip "Show me your largest GAIN" (1566); the
radar's legend "Omni-Compass helped" / "it hurt" (1554) where the key's glosses are "moved toward its declared aim" / "away from". m30 "the
founder" stands in the visible text some forty times (686, 1162, 1261, 1623, 1669, 1680, 1930, 1989 ...); the authority on a buyer's page is
the document. m31 "hardware we can meter" (1161, 1622, 1628) and "a sequence of my own" (958): first person outside the house phrase "our own
models". m32 The key's colour paragraph opens a sentence in lower case: "the runs disagree and the runs differ are white with a dashed edge
and shown, not judged is grey" (1931). m33 "both manuals" (1956) where the page names three (1b). m34 3c's "the fast checks (the scheduling
floor, the pod reflex, the conveyance every 15 s) every 5 s at every beat" (990) puts two clocks in one parenthesis.

**Notation and spelling.** m35 Subscripts in three notations: "E_max", "α_E", "I_U", "k_I", "ρ_min", "U_gate" (1109, 1789–1804) beside
"E[max]", "ω[B]", "Q[B]" (1604) and "αₛ", "βₛ" (1110); the order of 15 October writes Unicode where it exists and x[i] where it does not.
m36 "center" (about ninety times) beside "centre" (650, 919, 1890); "organizations", "stabilization", "specialized" (1891–1893) beside
"colour", "licence", "normalised", "neighbouring". m37 Curly apostrophes in 931, 1050, 1099, 1378, 1411, 1824 ("Omni-Compass’s",
"organ’s", "Student’s") beside straight ones elsewhere. m38 "to 1e-12" (1587, 6783) against "10⁻¹²" (1832). m39 3o's replay of the 500 scenarios prints "toward the gauge's aim in N of 500
scenarios, away in M, tied in T" (6800) and draws "green toward the gauge's aim ..., red away" (6817): direction words the key retires,
for counts the record names `better` and `worse` (the m18 of 23 October, still open); "with its aim" / "against it", or the counts by word.
The expression that picks the count still has three identical branches (`G.aim === "higher" ? P.better : G.aim === "lower" ? P.better :
P.better`).

**Nits.** n1 Monitors 26 and 27 end "its bill native against Omni-Compass.; until its first set lands" (a full stop before a semicolon,
n2 of 23 October). n2 "OMNI-COMPASS" in capitals once in running prose (1690). n3 Lede labels in four styles: "Summary.", "In plain
words." (1727), "In one paragraph." (1886, 1919), and 3h's "Controls." after its "Summary." (1168). n4 The executive summary's first item,
"Where it stands, in one line.", runs ten lines (6949). n5 Monitor 61 is titled "The master switch and the kill switch", one switch under
two names. n6 The contents' front-matter rows repeat the title as the description ("iii The bottom line: ... One light and one number
..."). n7 `brake_test_schedule` (an elevator's own safety-test setting, a catalog muscle) is printed in 4m's muscle index: the muscle's own name, not the pedal; leave it, named here so no later word check mistakes it.

**The Live Engine Manual, in full.** Aligned with the page section by section in Appendix A and in chapters 1 to 45, and in places more exact
than the page: seven tabs (786), six beats from 10 s (828), the reset separate from the kill switch (883, 1323), the yardstick "written by The
Omni-Compass LLC from the published rule" (2.3). Its majors: (a) the figure caption "One pedal, no brake" (2022), the word the order of 12
October says is not used; (b) the page's kill-switch contradiction carried whole: "Native alone is not a tune: it is the kill switch" (714,
1578) against 6.5 and 8.5; (c) the page's section 1c is read as 6.13, inside the chapter on 1a's control panel and before chapter 8 (1b), and
Appendix A has no row for 1c at all. Its minors: it quotes "every beat, simulated" (849) and the founder's "which is the simulation" (2222)
without saying the house word is "modelled"; three `model_gate` paths (467, 1661, 1996); 4j and 4k share one chapter (37) where the page gives
each a lettered section; 8.1 copies 1b's "The monitors it drives follow: the wall (the page's section 1a)" (1260); 2.3 has the page's gap on
the test rig (E7); "the main engine" (417, 1639) undefined; "so no monitor, table, record or button shows a third" (117) while 4d prints
"Omni direct's control plane" and the note names `V18_THREE_ARMS_ABC.json`.

## 4. What is strong

- **The third arm came out cleanly in the prose.** No "Omni-Compass direct", no "by itself" arm, no violet side and no thirty scenarios
  survive in the visible text; the key (1930), the chip (657), the title (647), 4b (1669) and the disclosures (1988) say "two sides, and
  only two" in matching words, and violet is now a changed tune and nothing else (713, the glossary's "a changed tune's violet").
- **The sign rule is right where it is taught.** The key (1932–1933) and 4c (1677) print "GAIN +, LOSS −, STEADY =, power given +", with
  worked examples (1947–1951); E3 of 23 October is closed on the page and in the manual (4.2).
- **The words of the key hold.** GAIN, STEADY, LOSS and power given everywhere, decided by the gauge's aim; power given is never called a
  loss; "better" and "worse" appear only in the sentences that forbid them (1953, the Ask panel's rules 4386), "confirmed" only in
  the Ask panel's rule (its one other form is E1), and "standalone" and "competitor" only in negations (1988).
- **Every model is marked.** Class S at every model view, class L at every played-back run, class P at the one metered card; "never
  presented as proof" in each summary of 3a, 3d, 3e, 3f.
- **Outside figures are attributed and disowned** (1909, 1911: "none was measured, checked or endorsed by The Omni-Compass LLC"), and the
  company's own expectation is labelled "not a measured result" where it stands (1162).
- **1c, 2c, 3i, 3k, 4e, 4h and 4i** are exact, even, and need no word changed. The who-does-what table (760–767) and the five products
  (771–775), each "not yet run", are the clearest new prose on the page.
- **Closed since 23 October, checked on this build:** the key no longer gives Omni-Compass the spine (1930: "brain, nerves, immune system
  and heart"); 2d's prose gives power given blue (848); 4a's two ways and four readings are reconciled in one sentence (1627); the
  glossary now holds the house terms (the max, the tune-down, the lease, the release gate, the bone, the heat debt, conveyance).
- **Formulas are Unicode** (Σ, ∏, √, ≤, ⌈·⌉, t₀.₉₇₅,ₙ₋₁, 0x9E3779B9 mod 2³²), with no LaTeX anywhere.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results or this audit.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

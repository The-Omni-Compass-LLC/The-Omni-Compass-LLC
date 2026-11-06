# Observability and control: the gauges, the alerts and the buttons

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Three components, all outside the fingerprinted engine (none moves its digest), all reading or driving the governor only
through interfaces it already has: its audit file, its own kill file, its start-up arguments and the machine-wide master
switch. The Operator's Manual, sections 22.2 to 22.5, is the operating reference; this page is the map.

| Component | File | Interface | Writes |
|---|---|---|---|
| Telemetry exporter | `tools/omni_exporter.py` | follows the governor's JSONL audit; serves `GET /metrics` (Prometheus text format 0.0.4) on 127.0.0.1:9464 | nothing; any other path 404, any other method 501 |
| Grafana screen | `deploy/grafana/omni-compass.json` | 18 panels over the exporter's series, the heartbeat counted in beats of the dial's setting; a link to the control console | nothing |
| Alert rules | `deploy/prometheus/omni-compass-rules.yaml` | 10 Prometheus rules over the exporter's and the panel's series | nothing |
| Steering report | `tools/steering.py` → `results/STEERING.md` | the same gauges per hour of each omni arm's archived audit, runs A, B and C side by side | a report |
| Control panel | `tools/omni_control.py` | bearer-token HTTP API (`/v1/status`, `/v1/presses`, `/v1/mode`, `/v1/dial`, `/v1/muscle`, `/v1/beat`, `/v1/reset`, `/v1/kill`, `/v1/arm`), OpenAPI 3 at `/v1/openapi.json`, console at `/`, counters at `/metrics`, on 127.0.0.1:9465 | the governor's kill file and arguments; the master switch; its own control log |

## The series

From the exporter (each from a record the governor already writes):

| Series | Type | Meaning |
|---|---|---|
| `omni_decisions_total` | counter | decisions recorded |
| `omni_decision_seconds_sum`, `_count`, `omni_decision_seconds_last` | summary, gauge | time per decision |
| `omni_last_decision_timestamp_seconds` | gauge | the heartbeat |
| `omni_heartbeat_seconds` | gauge | the beat as measured: the median time between the last eleven full decisions, the dial's setting the governor runs at (5 to 120 s; the main engine 60 s; omni-v17) |
| `omni_writes_total{why}` | counter | settings commands written, by the head of their reason |
| `omni_recommended{setting}` | gauge | the last decision's recommendation (not necessarily written) |
| `omni_recommended_moves_total{setting}`, `omni_recommended_reversals_total{setting}` | counter | changes, and changes of direction |
| `omni_recommended_travel_total{setting}` | counter | summed size of the changes (actuator travel) |
| `omni_compass_decisions_total{zone}` | counter | decisions by zone: `slack` (under the lower cushion), `band`, `wall` (at or past the line) |
| `omni_wall_recovery_seconds_sum`, `_count`, `omni_wall_recovery_seconds_max` | summary, gauge | first decision at the line to first back inside the band (settling time) |
| `omni_errors_total{kind}` | counter | errors recorded, by kind |
| `omni_nodes_observed`, `omni_compass_position`, `omni_compass_force` | gauge | what the governor saw; where the compass stood |
| `omni_sense_blind{sense}` | gauge | 1 while a sense is blind (the governor holds) |
| `omni_verdict_state{state}` | gauge | the give-back trial's state |
| `omni_master_switch` | gauge | 1 while governing, 0 once switched off |
| `omni_own_cpu_cores` | gauge | the governor's own processor |
| `omni_audit_records_total`, `omni_audit_unreadable_total` | counter | the audit itself |

From the control panel: `omni_control_presses_total{button,outcome}`, `omni_control_mode{mode}`, `omni_control_governor_up`,
`omni_control_master_switch_on`, `omni_control_orphans`.

The heartbeat is a dial (omni-v17, `docs/OMNI_V17.md`): the screen counts the time since the last decision in beats of the
setting the governor runs at, and the staleness alert fires after three of them (`OmniGovernorStale`: 180 s at the main
engine's 60 s, 45 s at 15 s, 360 s at 120 s), so neither needs an edit when the dial is turned.

The zone, recovery and travel series describe the governor's own steering and are shown, not judged: native has no governor
to read them from. The judged comparison of time over the line is each paired receipt's alert-minutes row. In the omni-v11
kill test and long run the governor's `wall` share is 55% to 79% of decisions, because the test load holds the service near its
line in both arms; their alert minutes read 14% to 23% fewer than native's, GAIN in all three runs
(`results/live/V11_ROBUST_KILL.md`, `results/live/V11_ROBUST_LONG.md`, `results/STEERING.md`).

## The buttons

Every mode, dial or reset press is carried out through the governor's own hand-back: kill file set, exit awaited (every
setting restored to the start snapshot and read back), kill file removed, restart with the new arguments or none. Roles:
viewer (reads), operator (mode, dial, reset), security (kill, arm; arming takes two different holders within ten minutes).
Tokens are kept as SHA-256 digests; a bind beyond the loopback needs TLS; every press is logged with its holder and reason. A
governor that exits on its own is never restarted by the panel (its lease hands back first). The kill switch also stays on
the command line (`tools/omni_switch.py off`). Tests: `tests/test_omni_exporter.py`, `tests/test_omni_control.py`,
`tests/test_alert_rules.py`, `tests/test_steering.py`.

The per-muscle row (omni-v14): `POST /v1/muscle {"muscle": NAME, "on": true|false}`, role operator, and a row of On and Native
buttons on the console, one for each muscle of the governor's own list (`omni_controller/controller.py`, `MUSCLES`: machines,
replicas, cpu, clock, gpu, rollout, batch, rightsize, coldstart, contain, cooling). A muscle left native is never written; the
press passes through native like a dial press, and the governor starts again with `--native` naming every muscle left native
(`docs/OMNI_V14.md`; `tests/test_native_muscles.py`, `tests/test_omni_control.py`).

The heartbeat row (omni-v17): `POST /v1/beat {"seconds": 5 to 120}`, role operator, and a row of buttons on the console
for the dial's stops (5, 15, 30, 60, 75, 90 and 120 s; the main engine 60). The press passes through native like a dial press,
and the governor starts again with `--interval` set to the beat; the panel serves the beat it starts the governor at as
`omni_control_beat_seconds` (`docs/OMNI_V17.md`; `tests/test_omni_control.py`).

Not yet built: OpenTelemetry traces with one span per decision; a Helm chart; two governor replicas with leader election.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

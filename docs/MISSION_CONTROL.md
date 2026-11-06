# Mission control: the wall, its alarms and its buttons, beside Omni-Compass

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

One command stands up a monitoring wall beside Omni-Compass on any machine with Docker. Prometheus gathers the readings,
Grafana shows them, Node Exporter reads the bare metal, and Alertmanager carries the alarms. The governor's own exporter and
the alert bridge join them, and the two Omni-Compass boards come already loaded. These are the parts and the panel types
every site-reliability engineer already reads: time series, stat panels with thresholds, PromQL, alert rules and webhooks.
They are dressed in Omni-Compass's key: native orange, Omni-Compass blue, and the signals' words, redlining, steady and
accelerating. The wall watches and it acts. Its alarms can press the control panel's buttons, and its links open the panel
itself, so the people at the wall can turn every knob the engine exposes.

**What it is not.** The wall does not govern. Omni-Compass is the autopilot that governs, inside the system, on its own
beat. The wall is its window, its alarm bell and the operator's hand on the panel. Every press from the wall goes through
the control panel's roles and is written to its log, like a person's.

## 1. Stand it up

```
cd deploy/monitoring
cp .env.example .env          # set GRAFANA_ADMIN_PASSWORD (your own) and OMNI_AUDIT_DIR (the governor's audit folder)
docker compose up -d
```

| Service | Address | What it does |
|---|---|---|
| Grafana | http://localhost:3000 | the wall: **Omni-Compass: the monitor wall** opens as the home board, with **the governor's own screen** beside it |
| Prometheus | http://localhost:9090 | gathers every reading and evaluates the governor's alert rules (`deploy/prometheus/omni-compass-rules.yaml`) |
| Alertmanager | http://localhost:9093 | routes each firing alarm to the alert bridge, and to your own mail, chat or pager if you add them |
| Node Exporter | http://localhost:9100 | this machine's processor, memory, disk and network, read every second |
| The governor's exporter | http://localhost:9464/metrics | the governor's own gauges, read from its audit (`tools/omni_exporter.py`) |
| The alert bridge | http://localhost:9466/metrics | the wire from the alarms to the panel's buttons (`tools/omni_alert_bridge.py`) |

Every image is pinned to one release: Prometheus 2.53.1, Grafana 11.1.0, Node Exporter 1.8.2, Alertmanager 0.27.0 and Python
3.12.4. None is "latest", so the stack you start is the stack that was checked. No password is written in any file of the
repository; Grafana refuses to start until `.env` gives it yours. Each image runs unchanged from its own project as a
separate service under that project's own license, and nothing of their code is copied into Omni-Compass.

## 2. Point it at your machines and your clouds

Prometheus reads three lists in `deploy/monitoring/targets/`, and reads them again on its own whenever they change, so no
restart is needed:

- **`omni.yml`**: every governor's exporter, one entry per place Omni-Compass runs. Label each one with its `route`
  (`onsite` or `cloud`) and its `provider` (`bare-metal`, `azure`, `google`, `amazon`, `oracle`, …).
- **`nodes.yml`**: every bare-metal machine's Node Exporter, on port 9100.
- **`control.yml`**: the control panel (`tools/omni_control.py serve`). Its `GET /metrics` needs a viewer token, written
  alone on one line in `targets/control.token`.

The labels ride on every series of a target, and the wall's knobs filter by them.

The governor's own gauges are read every 5 s, because its fastest check runs every 5 s and its audit changes no faster. The
bare metal is read every second.

## 3. Read the wall

The first row holds **the signals**, each with its threshold taken from the alert rule it mirrors:

| Signal | The panel | It turns |
|---|---|---|
| the heartbeat | beats since the governor's last decision | **steady** past 1.5 beats; **redlining** at 3 beats, the staleness alarm's line |
| the senses | 1 while a sense the governor needs is unread | **redlining** while blind (the engine holds and says why) |
| the master switch | ON or OFF | OFF reads "native alone": the kill switch is pulled |
| alerts firing | the alarms firing across the wall | **steady** at one, **redlining** at two or more |

Every panel under them is one monitor of the live engine page, numbered as the page numbers it and laid under its section.
A monitor fed by a Prometheus series draws it. A monitor the page draws from the repository's own records holds its place
with a note saying so. Native is orange and Omni-Compass blue on every panel.

**The knobs** at the top of the board:
- **Route** and **Provider**: on-site or cloud; bare metal, Azure, Google, Amazon, and the rest.
- **Machine**: any instance, or all.
- **Rate window**: 1 m, 5 m, 15 m or 1 h.
- **Control panel**: the address of your panel.

Every panel's expression is read through the first four, and the fifth is where the wall's buttons go.

## 4. The buttons, and the alarms that press them

**By hand.** The board's link **The control panel's buttons** opens the panel's console at the address in the Control panel
knob. Its buttons:
- **Restore factory profile**: reapplies the released configuration.
- **Return to native**: hands every setting back to native and stops the governor.
- **Mode**: autopilot, watch, or off.
- **Dial**: the max or the tune-down.
- **Beat**: one of the six stops, 10, 15, 30, 60, 90 or 120 s.
- **Each muscle**: on, or left native.
- **The kill switch**, and its arming by two holders of the security role.

Each press needs its role and a reason, and is written to the panel's log (`tools/omni_control.py`).

**By alarm.** Alertmanager sends every firing alarm to the alert bridge. The bridge presses the one button
`deploy/monitoring/actions.json` names for that alarm, with its own operator token and the reason "alert <name> firing
(Alertmanager)". The list as shipped:

| Alarm | Button | Why |
|---|---|---|
| OmniGovernorStale | Return to native | no decision for three beats while it is meant to govern: every setting handed back |
| OmniWritesHammering | mode: watch | writing far more often than its rules allow: it keeps deciding and auditing and writes nothing until a person looks |
| OmniWriteErrors | mode: watch | its writes are refused: the same |

Three rules hold the bridge:
- **It writes before it presses.** Until `OMNI_BRIDGE_PRESS=1` is set in `.env`, with an operator token in
  `targets/bridge.token`, the bridge only writes to its log what it would have pressed.
- **It presses only the operator's buttons.** Those are factory, reset, mode and dial. It refuses a list that names the
  kill switch or its arming: those belong to the security role, and arming takes two people.
- **It acts once per firing.** It acts when an alarm starts firing, once for that firing, never when the alarm resolves,
  and never twice however often Alertmanager repeats it.

Its counters (`omni_bridge_decisions_total`, by outcome) are on the wall like every other series.

## 5. Checked before it ships

`tests/test_mission_control.py` holds all of the following:
- every image is pinned;
- no password is written;
- every scrape job, the rules and the alerting are present;
- Grafana loads its source and both boards on its own;
- the bridge writes until told, presses once per firing with its reason, never on a resolve, and refuses the kill switch;
- the wall's knobs reach every Omni-Compass series, and its signals carry their words.

Every expression on both boards is valid PromQL (`promtool check rules`). The monitor wall is written from the live engine's
monitor registry by `docs/engine/export_grafana.py`, so a monitor added to the page is a panel added to the wall.

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

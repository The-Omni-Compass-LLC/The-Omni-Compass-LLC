# The monitor wall beside Omni-Compass: Prometheus, Grafana and Alertmanager

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

One command stands up the wall an operations team already knows how to read: **Prometheus** collects, **Grafana** shows the
Omni-Compass wall (`deploy/grafana/omni-compass-wall.json`, 85 panels, loaded at start as the home dashboard, with the
governor's own screen `deploy/grafana/omni-compass.json` beside it), **Alertmanager** carries the governor's alert rules
(`deploy/prometheus/omni-compass-rules.yaml`), **node_exporter** reads this host, and the governor's exporter
(`tools/omni_exporter.py`) reads the audit the governor writes.

## Start it

```
cd deploy/wall
cp .env.example .env          # set GRAFANA_ADMIN_PASSWORD (compose refuses to start without it)
docker compose up -d
```

Then open **http://127.0.0.1:3000** (Grafana: the wall), **http://127.0.0.1:9090** (Prometheus: every series, PromQL) and
**http://127.0.0.1:9093** (Alertmanager: the alerts). Every port is bound to this machine only; every image is pinned to a
version.

## What it collects

| Job | What it reads | Where its targets are set |
|---|---|---|
| `omni-exporter` | the governor: `omni_decisions_total`, `omni_heartbeat_seconds`, `omni_writes_total{why}`, `omni_compass_position`, `omni_verdict_state`, `omni_master_switch`, … | the audit folder, `OMNI_AUDIT_DIR` in `.env` |
| `omni-control` | the control panel's counters (`tools/omni_control.py`, `GET /metrics` with a viewer token) | `targets/omni-control.yml`, the token in `secrets/omni_viewer_token` |
| `node` | every machine's own counters: `node_cpu_seconds_total`, memory, disk, network, `node_rapl_package_joules_total` | this host; your bare metal and the cloud's machines in `targets/nodes.yml` |
| `service` | your service's own: `http_requests_total`, `http_request_duration_seconds` (traffic, errors, latency) | `targets/service.yml` |
| `kepler` | energy per node and pod: `kepler_node_package_joules_total` | `targets/kepler.yml` |
| `opencost` | the machines' price an hour: `node_total_hourly_cost` | `targets/opencost.yml` |

A target file is a list of `targets:` with `labels:`; Prometheus reads it again by itself, with no restart. The scrape runs
every 5 s: the governor's fast checks run every 5 s and its full decision every 60 s at the factory beat, so a faster scrape
only costs.

## What controls what

The wall reads; it writes nothing. The governor is the autopilot: it acts before a line is crossed, and its settings change only
by the governor itself, by its control panel (`tools/omni_control.py`: an authenticated API, every press audited with its
reason; the live benchmark engine page's **Commands** tab lists every press and its request) and by the kill switch
(`tools/omni_switch.py`, security, instant). An alert wakes a person only when the governor itself is in trouble (stale,
orphaned, hammering). No alert presses a governor button by itself: the engine's own safety acts first (the lease walks every
setting back after a crash; the watchdog runs the restore commands), and the reset and the kill switch stay a person's press.
To page a person, add a receiver in `alertmanager.yml` (a webhook, Slack, Teams, PagerDuty).

## Grafana Alloy in the collector's place

`docker compose --profile alloy up -d` adds **Grafana Alloy** (`config.alloy`): an OpenTelemetry Collector distribution with
Prometheus pipelines that collects the same targets every 5 s and writes them into the wall's Prometheus (its UI at
http://127.0.0.1:12345). Teams that already run Alloy point it at the same endpoints: the governor's exporter is a standard
`/metrics`. Alloy is a collector: it gathers metrics, logs, traces and profiles and forwards them; it decides nothing and writes
no setting. It sits beside Omni-Compass, never in its place: Omni-Compass is the governor that acts on the system, Alloy one of
the ways its readings travel to the wall.

## The live benchmark engine page on the same Prometheus

The live benchmark engine page (`docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`) reads its own model by default. On its main control panel,
**Drive → your own system**, type `http://127.0.0.1:9090` and press **Connect**: each monitor asks this Prometheus its own
query every 15 s and its breaker shows the answer (read only). The page's **Metrics (Prometheus)** tab prints its own model in
the same text format, with the series a running system serves beside each one and the PromQL the wall draws it with. This
Prometheus answers a browser only from the origins in `OMNI_PAGE_ORIGIN`: by default a page served from this machine
(`python3 -m http.server` in `docs/engine`, then open `http://127.0.0.1:8000/OMNI_COMPASS_LIVE_ENGINE.html`). A page opened
straight from a file carries the origin `null`, which every sandboxed frame on any website also carries, so it is not answered
by default; set `OMNI_PAGE_ORIGIN` yourself only if you accept that exposure.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

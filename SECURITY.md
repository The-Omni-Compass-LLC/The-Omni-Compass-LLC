# Security policy

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## Reporting a vulnerability

Report a suspected vulnerability privately to The Omni-Compass LLC by telephone at its main office infrastructure (toll-free direct 1-888-339-9551; system route asset 1-888-DEX-YLL-1, landline 321-746-4411 registered in Florida) or through www.omni-compass.com, never in a public issue,
pull request or discussion. Include the version and commit, what you saw, how to reproduce it, and its likely impact. We
acknowledge reports, keep the reporter informed, and coordinate disclosure: a fix or a mitigation is published before the
details are, and the reporter is credited if they wish. Please give us a reasonable time to fix before any disclosure, do
not access data that is not yours, and do not disrupt any system; good-faith research that follows this policy will not
be pursued by us.

## What is in scope

The engine, the controllers, the plugs and wiring, the harnesses, the workflows and the verifier in this repository.
Third-party software Omni-Compass runs on or connects to (Kubernetes, KEDA, Karpenter, NVIDIA drivers, databases) is
reported to its own maintainers.

## How Omni-Compass is built to fail safe

- The governor issues control actions only through the shield (`omnicompass/shield.py`, `cpp/src/shield.cpp`), inside the
  cover the operator granted, and never fights another writer.
- It snapshots every setting once, before its first write, and the kill switch (`python3 tools/omni_switch.py off`) hands
  every setting back; a dead-man lease hands them back if the governor stops.
- It runs under least privilege: on Kubernetes, a service account with `kubectl auth can-i` receipts for what it can and
  cannot do (`deploy/kind/rbac-omni.yaml`).
- The watchdog acts only on registry records its own user wrote that no other user can change, and never signals a
  process number the system gave to another process (`tools/omni_switch.py`). Put the switch and the registry in a
  directory only the governors' user can write (`OMNI_MASTER_OFF`, `OMNI_REGISTRY`); `status` warns when they are not.
- It contains no telemetry and makes no network connection of its own except to the systems an operator points it at.
- The threats of misuse, the guards against each and what is still open are set out in `docs/THREAT_MODEL.md`.
- Every release carries a software bill of materials (`sbom/`) and a seal of the engine and its twins (`results/SEAL.json`,
  `python3 verify.py`).
- The capture script (`fleet/capture/kube_capture.sh`) is read-only; no component writes to a live cluster unless the
  operator starts it in a writing mode.

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

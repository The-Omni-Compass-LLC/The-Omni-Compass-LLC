#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
# The factory beat for the cluster the current kubectl reaches (omni-v24): the engine reads its place from the nodes
# (omni_controller/controller.py factory_beat: 10 s on site or through a recognized cloud) and every rig uses what it prints, so the
# rule is written once. A cluster that cannot be read uses the same 10 s default.
#   bash scripts/factory_beat.sh            prints the seconds, e.g. 10
python -m omni_controller.controller --kubectl "${KUBECTL:-kubectl}" --print-factory-beat 2>/dev/null || echo 10
# © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

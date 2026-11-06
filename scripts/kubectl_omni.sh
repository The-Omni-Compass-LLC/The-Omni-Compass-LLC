#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
# Run kubectl as the Omni-Compass service account (deploy/kind/rbac-omni.yaml), never as cluster admin.
set -euo pipefail
exec kubectl --as=system:serviceaccount:omni-compass:omni-compass "$@"

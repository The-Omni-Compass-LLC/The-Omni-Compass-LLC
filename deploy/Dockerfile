# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
# Omni-Compass controller image. kubectl comes from the official Kubernetes image (no package manager, no curl).
FROM registry.k8s.io/kubectl:v1.32.2 AS kubectl
FROM python:3.12-slim
COPY --from=kubectl /bin/kubectl /usr/local/bin/kubectl
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY omnicompass omnicompass
COPY omni_controller omni_controller
COPY hardware hardware
# the frozen, benchmarked closure-law setting (--closure /app/law/closure.json)
COPY tuning/GLOBAL_LEAGUE_PREREGISTRATION.json law/closure.json
USER 10001
ENTRYPOINT ["python", "-m", "omni_controller.controller"]

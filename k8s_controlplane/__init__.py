# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Referee harness: metrics-server + HPA + Cluster Autoscaler / Karpenter-lite + Omni-Compass.

This is an algorithm replica of documented Kubernetes control-plane behaviour.
It is not kube-controller-manager, cluster-autoscaler, or Karpenter source.
"""
from .config import HarnessConfig
from .benchmark import ARMS, run, simulate

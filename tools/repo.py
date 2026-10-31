# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The repository's own name, written once: every tool and script that names the repository (an API path, a link to a
run, the package's metadata) reads it here, so a rename is one line, not a search through the tree (27 October 2026:
the repository moved from The-Omni-Compass-LLC/The-Omni-Compass to The-Omni-Compass-LLC/The-Omni-Compass-LLC, and
eleven tools still named the old one).

  HOME   the repository's name; every link a page prints is built on it, so a page reads the same wherever it is built
  NAME   the repository an API call goes to: on GitHub's machines the run's own (GITHUB_REPOSITORY), elsewhere HOME"""
from __future__ import annotations

import os

HOME = "The-Omni-Compass-LLC/The-Omni-Compass-LLC"
NAME = os.environ.get("GITHUB_REPOSITORY") or HOME
URL = f"https://github.com/{HOME}"
RUNS = f"{URL}/actions/runs/"
RAW = f"{URL}/blob/raw/"

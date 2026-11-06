#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
# The two Google services the sets use (Kubernetes Engine and Compute Engine) are on in the project, before anything is
# built or billed (.github/workflows/gke-metered.yml, cloud-check.yml). The setup switches them on as the project's owner
# (docs/GOOGLE_SETUP.md, section 4); the login GitHub holds may read them but its roles carry no right to switch a service
# on, so a service already on is never asked for again, and one that is off is switched on only if the login may, or named
# with the fix. Usage: GCP_PROJECT=... bash scripts/gcp_services.sh
set -euo pipefail
PROJECT="${GCP_PROJECT:?set GCP_PROJECT}"
NEED=(container.googleapis.com compute.googleapis.com)
if ! on=$(gcloud services list --enabled --project "$PROJECT" --format='value(config.name)' 2>/tmp/gcp-services.err); then
  # unread: Google's own reads in the pre-flight that follows name a service that is off, still at no cost
  echo "the project's services were not read (Google said: $(tr '\n' ' ' < /tmp/gcp-services.err | cut -c1-300)); the pre-flight decides"
  exit 0
fi
missing=()
for s in "${NEED[@]}"; do
  case $'\n'"$on"$'\n' in *$'\n'"$s"$'\n'*) ;; *) missing+=("$s") ;; esac
done
if [ "${#missing[@]}" -eq 0 ]; then echo "Google's services are on: ${NEED[*]}"; exit 0; fi
if gcloud services enable "${missing[@]}" --project "$PROJECT" 2>/tmp/gcp-services.err; then
  echo "switched on: ${missing[*]}"; exit 0
fi
echo "::error::the project's ${missing[*]} is off, and GitHub's login may not switch it on (Google said:" \
     "$(tr '\n' ' ' < /tmp/gcp-services.err | cut -c1-300)). In Cloud Shell, as the project's owner, paste docs/GOOGLE_SETUP.md" \
     "section 4 again: its first lines switch them on. Nothing built, nothing billed."
exit 2

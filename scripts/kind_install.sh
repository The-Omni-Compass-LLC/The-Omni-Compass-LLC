#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
# kind and kubectl at the versions every repetition of the grid runs on (kind v0.31.0, whose own node image is Kubernetes
# v1.35.0; kubectl v1.35.0), each download tried again with a pause when the server refuses it, each binary checked
# against the SHA-256 its project publishes. On GitHub it is the second try after helm/kind-action (12 Oct: a refused
# checksum download ended a job before either arm ran); on a rented machine it is the install.
#   bash scripts/kind_install.sh [kind version] [kubectl version] [directory]
# The directory (default: kind-bin under the runner's temporary folder) receives kind and kubectl; on GitHub it is put
# first on the job's PATH for the steps after this one.
set -euo pipefail
KIND_VERSION="${1:-v0.31.0}"; KUBECTL_VERSION="${2:-v1.35.0}"
dir="${3:-${RUNNER_TEMP:-$HOME}/kind-bin}"
mkdir -p "$dir" 2>/dev/null || sudo mkdir -p "$dir"
tmp=$(mktemp -d); trap 'rm -rf "$tmp"' EXIT
get() {   # url file: a refusal (a server error, a dropped connection, a timeout) is tried again, 8 times 15 s apart
  curl -fsSL --retry 8 --retry-all-errors --retry-delay 15 --connect-timeout 20 --max-time 300 -o "$2" "$1" && [ -s "$2" ]
}
fetch() {   # name url ext: the binary and its published SHA-256 (url.ext), three rounds 30 s apart if an answer was not the file
  local t want got
  for t in 1 2 3; do
    if get "$2" "$tmp/$1" && get "$2.$3" "$tmp/$1.sum"; then
      want=$(awk '{print $1; exit}' "$tmp/$1.sum"); got=$(sha256sum "$tmp/$1" | cut -d' ' -f1)
      [ -n "$want" ] && [ "$want" = "$got" ] && return 0
      echo "$1: SHA-256 $got, published ${want:-nothing} (round $t)"
    else
      echo "$1: download refused (round $t)"
    fi
    sleep 30
  done
  return 1
}
fetch kind "https://github.com/kubernetes-sigs/kind/releases/download/$KIND_VERSION/kind-linux-amd64" sha256sum
fetch kubectl "https://dl.k8s.io/release/$KUBECTL_VERSION/bin/linux/amd64/kubectl" sha256
for b in kind kubectl; do
  install -m 0755 "$tmp/$b" "$dir/$b" 2>/dev/null || sudo install -m 0755 "$tmp/$b" "$dir/$b"
done
[ -z "${GITHUB_PATH:-}" ] || echo "$dir" >> "$GITHUB_PATH"
echo "installed in $dir: $("$dir/kind" version), kubectl $("$dir/kubectl" version --client=true -o json | jq -r '.clientVersion.gitVersion')"

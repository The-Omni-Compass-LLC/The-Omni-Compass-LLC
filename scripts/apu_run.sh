#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
# The whole GPU test on an AMD chip, one command: an APU (CPU and GPU on one die under one power budget, e.g. an
# Instinct MI300A or a Ryzen AI Max) or an AMD GPU, on a rented or owned machine with ROCm and PyTorch for ROCm:
#
#   sudo bash scripts/apu_run.sh              every stage of scripts/gpu_rented_run.sh, on the AMD chip
#   sudo CARDS8=1 bash scripts/apu_run.sh     every chip on the machine at once (scripts/gpu_8card.sh)
#
# The same preregistered protocol as the NVIDIA card (docs/GPU_PREREGISTRATION.md): wire check, envelope, smoke, the two
# counted runs (compute and AI token generation), the operator's power cap underneath, the fault drill, the six
# organisms at 1, 10 and 100 copies with the chip inside, and AI serving. The card's two wires are answered by
# AMD's amd-smi through scripts/apu/nvidia-smi; on an APU the meter is the package's power (CPU and GPU together, the
# power its owner pays for). The adapter has not yet run on an AMD chip: the wire check in step 1 counts nothing unless
# both wires follow, read back and go home, so a wrong reading stops the run there and is never a result.
set -uo pipefail
echo "Omni-Compass: evaluation and Simulation use only. Commercial use requires a signed, paid Omni-Compass Enterprise License (LICENSE, NOTICE)."
cd "$(dirname "$0")/.."
command -v "${AMD_SMI:-amd-smi}" >/dev/null 2>&1 || { echo "amd-smi not found: this machine has no ROCm driver (install ROCm 6.x)"; exit 1; }
"${AMD_SMI:-amd-smi}" version >/dev/null 2>&1 || { echo "amd-smi does not answer: check the ROCm driver"; exit 1; }
python3 -c "import torch, sys; sys.exit(0 if torch.cuda.is_available() else 1)" 2>/dev/null \
  || { echo "PyTorch for ROCm not found (torch.cuda.is_available() is the ROCm/HIP device too): install it first"; exit 1; }
chmod +x scripts/apu/nvidia-smi
export NVIDIA_SMI="$PWD/scripts/apu/nvidia-smi" CARD_FAMILY=amd
echo "== AMD chip(s): $("$NVIDIA_SMI" -L | wc -l), through amd-smi; the protocol is scripts/gpu_rented_run.sh unchanged"
if [ -n "${CARDS8:-}" ]; then exec bash scripts/gpu_8card.sh; fi
exec bash scripts/gpu_rented_run.sh

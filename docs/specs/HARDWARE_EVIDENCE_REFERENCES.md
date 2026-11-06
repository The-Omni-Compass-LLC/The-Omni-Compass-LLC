# Hardware Evidence References

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

> **Specification, carried from the package XPASS27 (2026-10-01).** It specifies a contract or a measurement; any result
> it quotes is as of that package. Current results: `docs/STATE_OF_PLAY.md` and the tables in `results/`.

Primary/vendor references used to constrain the hardware evidence design. These are engineering references, not experimental results.

- Linux kernel, Power Capping Framework: https://docs.kernel.org/power/powercap/powercap.html
- NVIDIA DCGM, Field Identifiers: https://docs.nvidia.com/datacenter/dcgm/latest/dcgm-api/dcgm-api-field-ids.html
- NVIDIA DCGM, Field Constants / clock-event reasons: https://docs.nvidia.com/datacenter/dcgm/latest/reference/dcgm-api/dcgm-api-field-constants.html
- NVIDIA DCGM, System Administrator Getting Started: https://docs.nvidia.com/datacenter/dcgm/latest/learn/getting-started-for-system-administrators/
- NVIDIA NVML, Clock Event Reasons: https://docs.nvidia.com/deploy/nvml-api/latest/api/group__nvmlClocksEventReasons.html
- Intel E810-XXVDA4T User Guide (DPLL / external timestamp signals): https://cdrdv2-public.intel.com/646265/646265_E810-XXVDA4T%20User%20Guide_Rev1.2.pdf
- linuxptp project documentation: https://www.linuxptp.org/documentation/
- Linux PCIe PTM support should be verified against the kernel and platform documentation for the exact deployed kernel/device before a distributed timing claim is enabled.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

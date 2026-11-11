# Canonical company attribution and provenance

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

**Owner-directed naming standard, 9 November 2026.** The public attribution used in active Omni-Compass repository text, software-package metadata, code notices, specifications, manuals, boardroom material, and newly generated reports is:

> **Dubra Software Inc. / The Omni-Compass LLC**

This is a joint presentation and affiliation label. It does not itself prove an assignment, merger, transfer of intellectual property, ownership percentage or corporate relationship in law. Those propositions require the applicable incorporation, assignment or licensing instruments. The formal `LICENSE`, `NOTICE` and `DISCLOSURES.md` continue to govern legal rights. Do not edit recorded corporate history or invent statutory registrations.

## Inclusion rules

1. **Active prose:** normalize historical LLC-only publisher names to the canonical combined form, but do not duplicate it where the combined name is already present. Preserve the product name **Omni-Compass**, the repository owner slug `The-Omni-Compass-LLC`, and all website/API links.
2. **Generator inputs:** use `tools/legal.py` as the canonical legal-notice source; `tools/company_attribution.py --check` identifies standalone company aliases in scoped active publication files. Maintain the standard in `CITATION.cff`, `codemeta.json`, `pyproject.toml` and the three principal Markdown manuals.
3. **Archival exclusions:** do not rewrite immutable measurement receipts, signed or fingerprinted engine source, historical snapshots, original external documents, binary PDFs, raw CSV/JSON telemetry or Git data merely to change narrative attribution. Their original bytes are evidence. Publish the canonical association in the current document hierarchy and addenda instead.
4. **New exports:** build the current manuals from their Markdown sources, verify copyright and license banners, preserve hyperlinks and citations, regenerate PDFs, and run the existing release checks before claiming an updated PDF. Do not assert a binary file was changed until it was built and committed.
5. **When a role matters:** explicitly distinguish publication under the shared affiliation from the legal identity of an entity signing a contract. A co-branded notice cannot substitute for signed corporate documents.

## Quality gate

```text
python3 tools/company_attribution.py --check
python3 tools/legal.py --check
python3 -m unittest -v tests.test_company_attribution
```

The guard is an attribution check on active publications. It is not a claim that every historical byte in a multi-gigabyte archive has been rewritten.

---

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*

# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The receipt check (tools/verify_receipt.py) and the archive's signing of the sums (.github/workflows/archive-run.yml),
31 October: every file against its sum, every certificate field read as Sigstore's authority writes it, only this
repository's archive workflow accepted as the signer, and a signing that fails never stopping the archive."""
import hashlib
import re
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import verify_receipt as vr  # noqa: E402
from tools.repo import URL  # noqa: E402

WORKFLOW = ROOT / ".github" / "workflows" / "archive-run.yml"


def der(text: str) -> bytes:
    b = text.encode()
    n = len(b)
    return bytes([0x0C, n]) + b if n < 128 else bytes([0x0C, 0x82]) + n.to_bytes(2, "big") + b


class FakeCert:
    """An x509 certificate as far as the check reads one: its extensions by OID, each value's DER bytes."""

    def __init__(self, fields):
        self.fields = {vr.OID[k]: der(v) for k, v in fields.items()}
        self.extensions = self

    def get_extension_for_oid(self, oid):
        key = getattr(oid, "dotted_string", oid)
        if key not in self.fields:
            raise KeyError(key)
        return type("Ext", (), {"value": type("Raw", (), {"value": self.fields[key]})()})()


OURS = {"issuer": vr.ISSUER, "repository_id": vr.REPOSITORY_ID, "owner_id": vr.OWNER_ID, "repository": URL,
        "signer": f"{URL}/.github/workflows/archive-run.yml@refs/heads/main", "trigger": "schedule",
        "run": f"{URL}/actions/runs/1/attempts/1"}


class Sums(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.d = Path(self.tmp.name)
        (self.d / "rep-1").mkdir()
        (self.d / "rep-1" / "capture.csv").write_text("t,w\n0,1\n")
        (self.d / "aggregate.json").write_text("{}\n")
        lines = [f"{hashlib.sha256((self.d / p).read_bytes()).hexdigest()}  ./{p}" for p in ("aggregate.json", "rep-1/capture.csv")]
        (self.d / vr.SUMS).write_text("\n".join(lines) + "\n")

    def tearDown(self):
        self.tmp.cleanup()

    def test_every_file_matches_its_sum(self):
        self.assertEqual(vr.check_files(self.d), 2)

    def test_the_signature_file_is_the_one_expected_addition(self):
        (self.d / vr.BUNDLE).write_text("{}")
        self.assertEqual(vr.check_files(self.d), 2)

    def test_a_changed_file_is_named(self):
        (self.d / "rep-1" / "capture.csv").write_text("t,w\n0,2\n")
        with self.assertRaisesRegex(vr.ReceiptError, r"changed: rep-1/capture\.csv"):
            vr.check_files(self.d)

    def test_a_missing_file_is_named(self):
        (self.d / "aggregate.json").unlink()
        with self.assertRaisesRegex(vr.ReceiptError, r"missing: aggregate\.json"):
            vr.check_files(self.d)

    def test_a_file_the_sums_never_listed_is_named(self):
        (self.d / "planted.csv").write_text("x\n")
        with self.assertRaisesRegex(vr.ReceiptError, r"not in the sums: planted\.csv"):
            vr.check_files(self.d)

    def test_binary_mode_lines_read_the_same(self):
        h = "a" * 64
        self.assertEqual(vr.parse_sums(f"{h} *./x.bin\n{h}  y.txt\n"), {"x.bin": h, "y.txt": h})
        with self.assertRaises(vr.ReceiptError):
            vr.parse_sums("not a line\n")

    def test_a_folder_signed_reads_its_signature_and_one_unsigned_reads_sums_only(self):
        self.assertEqual(vr.main([str(self.d)]), 0)               # sums only: no signature file, nothing to check
        (self.d / "aggregate.json").write_text("[]\n")
        self.assertEqual(vr.main([str(self.d)]), 1)


class Certificate(unittest.TestCase):
    def test_der_text_short_and_long(self):
        self.assertEqual(vr.der_utf8(der("schedule")), "schedule")
        long = "x" * 300
        self.assertEqual(vr.der_utf8(der(long)), long)
        with self.assertRaises(vr.ReceiptError):
            vr.der_utf8(b"\x04\x02ab")                             # an OCTET STRING, not text
        with self.assertRaises(vr.ReceiptError):
            vr.der_utf8(b"\x0c\x05ab")                             # a length its bytes do not hold

    def test_the_archive_job_of_this_repository_is_accepted(self):
        fields = vr.cert_fields(FakeCert(OURS))
        self.assertEqual(fields["trigger"], "schedule")
        self.assertEqual(vr.check_identity(fields), OURS["run"])

    def test_another_branchs_copy_of_the_archive_workflow_is_accepted(self):
        f = dict(OURS, signer=OURS["signer"].replace("refs/heads/main", "refs/heads/v23"))
        self.assertEqual(vr.check_identity(vr.cert_fields(FakeCert(f))), OURS["run"])

    def test_every_other_signer_is_refused(self):
        for change in ({"issuer": "https://accounts.google.com"},
                       {"repository_id": "447691086"},                          # another repository, whatever its name says
                       {"owner_id": "71096353"},
                       {"signer": OURS["signer"].replace("archive-run.yml", "benchmark.yml")}):
            with self.subTest(change=change):
                with self.assertRaises(vr.ReceiptError):
                    vr.check_identity(vr.cert_fields(FakeCert(dict(OURS, **change))))
        missing = dict(OURS); missing.pop("repository_id")
        with self.assertRaises(vr.ReceiptError):
            vr.check_identity(vr.cert_fields(FakeCert(missing)))


class ArchiveSigns(unittest.TestCase):
    def setUp(self):
        self.text = WORKFLOW.read_text()
        self.lines = self.text.splitlines()

    def test_the_job_may_ask_github_for_its_identity(self):
        self.assertRegex(self.text, r"(?m)^  id-token: write")

    def test_the_tool_is_pinned_and_the_check_names_the_same_version(self):
        pins = set(re.findall(r"sigstore==([0-9.]+)", self.text))
        self.assertEqual(len(pins), 1)
        self.assertIn(f"sigstore=={pins.pop()}", (ROOT / "tools" / "verify_receipt.py").read_text())

    def test_the_sums_are_signed_after_they_are_written_and_before_they_are_saved(self):
        sums = next(i for i, ln in enumerate(self.lines) if "SHA256SUMS_ALL.txt" in ln and "sha256sum" in ln)
        sign = next(i for i, ln in enumerate(self.lines) if "-m sigstore sign" in ln)
        save = next(i for i, ln in enumerate(self.lines) if "raw_archive.sh save" in ln)
        self.assertLess(sums, sign)
        self.assertLess(sign, save)

    def test_a_signing_that_fails_never_stops_the_archive(self):
        self.assertIn("continue-on-error: true", self.text)                     # the tool's install
        self.assertIn("archived with its sums only", self.text)                 # the warning, and the run still saved
        self.assertIn('rm -f "$d/SHA256SUMS_ALL.txt.sigstore.json"', self.text)  # never a half-written signature saved
        self.assertIn("</dev/null", self.text)                                  # never waits for a person to log in


if __name__ == "__main__":
    unittest.main()

# © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

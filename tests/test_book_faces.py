# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Every face in the three books is the book's own, embedded (the referee audit of 2 November 2026, docs/AUDIT_2026-11-02.md).

The book builder registers four families from two free, standard type libraries: Liberation (Serif and Sans, the same widths
as Times New Roman and Arial) and DejaVu (Sans Mono for code, Sans for the symbols Liberation lacks). A PDF that names a face
outside them, or names one without embedding it, is read by every viewer and printer with whatever face it substitutes: the
base-14 Helvetica and Times-Roman that ReportLab opens a page, a table cell and a figure with unless told otherwise. Each
built book is read from its own bytes (ReportLab writes every font dictionary uncompressed), so the check needs no PDF reader."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOKS = ("OMNI_COMPASS_MANUAL.pdf", "OMNI_COMPASS_OWNERS_MANUAL.pdf", "OMNI_COMPASS_LIVE_ENGINE_MANUAL.pdf")
# an embedded subset carries a six-letter tag before its name; the families are the four docs/book/build_book.py registers
OWN = re.compile(r"[A-Z]{6}\+(LiberationSerif|LiberationSans|DejaVuSans|DejaVuSansMono)(-(Bold|Italic|BoldItalic|Oblique|BoldOblique))?")


def faces(pdf: Path) -> set:
    return {m.decode("latin-1") for m in re.findall(rb"/BaseFont\s*/([A-Za-z0-9+\-_,.]+)", pdf.read_bytes())}


class TheFaces(unittest.TestCase):
    def test_every_face_is_the_books_own_and_embedded(self):
        for name in BOOKS:
            with self.subTest(book=name):
                found = faces(ROOT / "docs" / name)
                self.assertTrue(found, f"{name}: no font dictionary read")
                stray = sorted(f for f in found if not OWN.fullmatch(f))
                self.assertEqual(stray, [], f"{name} names faces that are not the book's own or are not embedded: {stray}; "
                                            "map them in docs/book/build_book.py and build the book again")

    def test_the_reader_finds_a_base14_face(self):
        """The reader itself is checked: a base-14 name is caught, an embedded face of the book's own passes."""
        self.assertIsNone(OWN.fullmatch("Helvetica"))
        self.assertIsNone(OWN.fullmatch("LiberationSerif"))                 # named but not embedded
        self.assertIsNotNone(OWN.fullmatch("AAAAAA+LiberationSerif-BoldItalic"))
        self.assertIsNotNone(OWN.fullmatch("AAAAAA+DejaVuSansMono"))


if __name__ == "__main__":
    unittest.main()

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

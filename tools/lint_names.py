#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Every Python file compiles, and no name is read that nothing defines: run by verify.py on every push.

A name read in a function or at module level that is neither assigned, imported, defined, a parameter, a builtin, nor
bound by an enclosing scope is a NameError waiting for the line that reads it (a typo, a removed import, a helper renamed
in one place). The check walks each module's symbol table (the standard library's symtable, the compiler's own view of
every scope), so it needs nothing installed. A module that writes its globals by hand (`globals()[...]`, `exec`) or
imports with `*` is read leniently: its module-level names are taken as defined.

  python3 tools/lint_names.py            every tracked .py file outside the frozen originals and the history
  python3 tools/lint_names.py FILE ...   just these
Exit 0: clean; exit 1: one line per finding, FILE:LINE name.
"""
from __future__ import annotations

import ast
import builtins
import subprocess
import symtable
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP = ("reference/", "docs/handoff/", "docs/history/", "archive/", "results/")
IMPLICIT = {"__file__", "__name__", "__doc__", "__spec__", "__loader__", "__package__", "__builtins__", "__path__",
            "__annotations__", "__dict__", "__class__", "__module__", "__qualname__"}


def module_names(table: symtable.SymbolTable) -> set[str]:
    return {s.get_name() for s in table.get_symbols() if s.is_assigned() or s.is_imported() or s.is_namespace()}


def lenient(src: str, tree: ast.AST) -> bool:
    if "globals()" in src or "exec(" in src or "__getattr__" in src:
        return True
    return any(isinstance(n, ast.ImportFrom) and any(a.name == "*" for a in n.names) for n in ast.walk(tree))


def undefined(path: Path) -> list[tuple[int, str]]:
    src = path.read_text(encoding="utf-8", errors="replace")
    tree = ast.parse(src, str(path))
    top = symtable.symtable(src, str(path), "exec")
    known = module_names(top) | set(dir(builtins)) | IMPLICIT
    if lenient(src, tree):
        return []
    bad: set[str] = set()

    def walk(t: symtable.SymbolTable, enclosing: set[str]):
        local = {s.get_name() for s in t.get_symbols()
                 if s.is_assigned() or s.is_imported() or s.is_parameter() or s.is_namespace()}
        for s in t.get_symbols():
            n = s.get_name()
            if not s.is_referenced() or n in local or n in known or n in enclosing:
                continue
            if s.is_global() or s.is_free() or t.get_type() == "module":
                bad.add(n)
        inner = enclosing | (local if t.get_type() == "function" else set())
        for c in t.get_children():
            walk(c, inner)

    walk(top, set())
    lines = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load) and node.id in bad:
            lines.append((node.lineno, node.id))
    return sorted(set(lines))


def tracked() -> list[Path]:
    out = subprocess.run(["git", "-c", "safe.directory=*", "ls-files", "*.py"], cwd=ROOT, capture_output=True, text=True).stdout
    return [ROOT / p for p in out.split() if not p.startswith(SKIP)]


def main(argv: list[str]) -> int:
    files = [Path(a) for a in argv] or tracked()
    findings = []
    for f in files:
        try:
            findings += [f"{f.relative_to(ROOT) if f.is_absolute() else f}:{ln} {name} (no definition)" for ln, name in undefined(f)]
        except SyntaxError as e:
            findings.append(f"{f}:{e.lineno} does not compile: {e.msg}")
    for x in findings:
        print(x)
    print(f"names: {len(files)} files, {len(findings)} findings")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

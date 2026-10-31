#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Formulas in Unicode, never LaTeX markup (the founder's order of 15 October 2026: "it's got to be Unicode", so a formula
prints the same on paper, on GitHub, in a terminal and in a code comment, for the engineers who wire and code the engine).

Every page the three manuals print (the Operator's, the Owner's, the Live Benchmark Engine's and every document the Owner's book takes in,
listed from docs/book/build_book.py) is read outside its code: a $...$ or $$...$$ formula, and a bare LaTeX subscript or
superscript (x_{i,k}, e^{-t}), is rewritten in Unicode: Greek letters and operators as their characters (α, Σ, ≤, ∝, √,
⌈ ⌉), sub- and superscripts as Unicode sub- and superscript characters where every character has one (xᵢ,ₖ₊₁, e⁻ᵗ) and as
x[...] and x^(...) where one does not, a fraction a/b with brackets only where they are needed. Code (fenced blocks and
`inline code`) is never touched, and a price such as $5 to $15 is not a formula (the opening $ is followed and the closing
$ preceded by a non-space character, as Pandoc reads them).

  python3 tools/unicode_math.py            list every formula still in LaTeX, file by file
  python3 tools/unicode_math.py --fix      rewrite them in Unicode, in place
  python3 tools/unicode_math.py --check    exit 1 if any remains (run by verify.py)
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SYMBOLS = {
    "alpha": "α", "beta": "β", "gamma": "γ", "delta": "δ", "epsilon": "ε", "varepsilon": "ε", "zeta": "ζ", "eta": "η",
    "theta": "θ", "vartheta": "ϑ", "iota": "ι", "kappa": "κ", "lambda": "λ", "mu": "μ", "nu": "ν", "xi": "ξ", "pi": "π",
    "rho": "ρ", "sigma": "σ", "tau": "τ", "upsilon": "υ", "phi": "φ", "varphi": "φ", "chi": "χ", "psi": "ψ", "omega": "ω",
    "Gamma": "Γ", "Delta": "Δ", "Theta": "Θ", "Lambda": "Λ", "Xi": "Ξ", "Pi": "Π", "Sigma": "Σ", "Upsilon": "Υ", "Phi": "Φ",
    "Psi": "Ψ", "Omega": "Ω",
    "sum": "Σ", "prod": "Π", "int": "∫", "partial": "∂", "nabla": "∇", "infty": "∞", "sqrt": "√",
    "le": "≤", "leq": "≤", "ge": "≥", "geq": "≥", "ne": "≠", "neq": "≠", "approx": "≈", "propto": "∝", "equiv": "≡",
    "sim": "∼", "simeq": "≃", "ll": "≪", "gg": "≫", "pm": "±", "mp": "∓", "cdot": "·", "times": "×", "div": "÷",
    "to": "→", "rightarrow": "→", "leftarrow": "←", "Rightarrow": "⇒", "Leftarrow": "⇐", "Leftrightarrow": "⇔",
    "iff": "⇔", "implies": "⇒", "mapsto": "↦", "uparrow": "↑", "downarrow": "↓",
    "in": "∈", "notin": "∉", "subset": "⊂", "subseteq": "⊆", "supset": "⊃", "cup": "∪", "cap": "∩", "setminus": "∖",
    "forall": "∀", "exists": "∃", "emptyset": "∅", "varnothing": "∅", "neg": "¬", "land": "∧", "wedge": "∧", "lor": "∨",
    "vee": "∨", "oplus": "⊕", "otimes": "⊗", "circ": "∘", "star": "⋆", "top": "⊤", "bot": "⊥", "perp": "⊥",
    "lceil": "⌈", "rceil": "⌉", "lfloor": "⌊", "rfloor": "⌋", "langle": "⟨", "rangle": "⟩", "mid": "∣", "vert": "|",
    "Vert": "‖", "ldots": "…", "dots": "…", "cdots": "⋯", "dotsc": "…", "prime": "′", "degree": "°", "ell": "ℓ",
    "quad": " ", "qquad": "  ", ",": " ", ";": " ", ":": " ", "!": "", " ": " ",
    "max": "max", "min": "min", "log": "log", "ln": "ln", "exp": "exp", "sin": "sin", "cos": "cos", "tan": "tan",
    "tanh": "tanh", "arg": "arg", "lim": "lim", "sup": "sup", "inf": "inf", "det": "det", "Pr": "Pr", "mod": "mod",
    "argmax": "argmax", "argmin": "argmin",
    "{": "{", "}": "}", "%": "%", "_": "_", "&": "&", "#": "#", "$": "$", "|": "‖",
}
ACCENTS = {"hat": "\u0302", "bar": "\u0304", "overline": "\u0305", "tilde": "\u0303", "dot": "\u0307", "ddot": "\u0308",
           "vec": "\u20d7"}
FONTS = ("mathrm", "text", "textrm", "mathbf", "textbf", "mathit", "textit", "operatorname", "mathsf", "mathtt", "texttt",
         "mathcal", "mathbb", "boldsymbol", "emph")
SUB = dict(zip("0123456789+-=()aehijklmnoprstuvxβγρφχ−", "₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎ₐₑₕᵢⱼₖₗₘₙₒₚᵣₛₜᵤᵥₓᵦᵧᵨᵩᵪ₋"))
SUP = dict(zip("0123456789+-=()abcdefghijklmnoprstuvwxyzABDEGHIJKLMNOPRTUVWβγδθφχ−′*",
               "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖʳˢᵗᵘᵛʷˣʸᶻᴬᴮᴰᴱᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾᴿᵀᵁⱽᵂᵝᵞᵟᶿᵠᵡ⁻′*"))


def _group(s, i):
    """The argument starting at s[i]: a {...} group (its inside), a \\command, or one character. Returns (text, next i)."""
    while i < len(s) and s[i] == " ":
        i += 1
    if i >= len(s):
        return "", i
    if s[i] == "{":
        depth, j = 0, i
        while j < len(s):
            if s[j] == "{" and (j == 0 or s[j - 1] != "\\"):
                depth += 1
            elif s[j] == "}" and s[j - 1] != "\\":
                depth -= 1
                if depth == 0:
                    return s[i + 1:j], j + 1
            j += 1
        return s[i + 1:], len(s)
    if s[i] == "\\":
        m = re.match(r"\\([A-Za-z]+|.)", s[i:])
        return m.group(0), i + len(m.group(0))
    return s[i], i + 1


def _simple(x):
    """True for an operand that needs no brackets in a/b: one symbol, a number, a name with its sub- or superscripts."""
    if re.fullmatch(r"[\w\u0370-\u03ff\u1d00-\u1dbf\u2070-\u209f′.\u0300-\u036f]+|√\S+|\S", x):
        return True
    return bool(re.fullmatch(r"[\w\u0370-\u03ff\u1d00-\u1dbf\u2070-\u209f′.]+\([^()]*\)", x))   # a name applied: f(x), R(1+h)


def _script(text, table, open_, close_):
    t = text.replace(" ", "")
    if re.search(r"[A-Za-z]{2,}", t):                             # a word (ok, gov, max) reads plainly: n[ok], not nₒₖ
        return f"{open_}{text}{close_}"
    if t and all(c in table or c == "," for c in t):
        return "".join(table.get(c, c) for c in t)
    return f"{open_}{text}{close_}"


TEXT_FONTS = ("text", "textrm", "textit", "textbf", "emph", "mbox")


def _environments(s):
    """cases, aligned and matrix-like environments as plain lines: rows joined by "; ", a case as "value, if condition"."""
    def cases(m):
        rows = [r.strip() for r in re.split(r"\\\\", m.group(1)) if r.strip()]
        parts = []
        for r in rows:
            cells = [c.strip() for c in r.split("&")]
            parts.append(f"{cells[0]}, if {cells[1]}" if len(cells) > 1 and cells[1] else cells[0])
        return "{ " + "; ".join(parts) + " }"

    def rows(m):
        return "; ".join(r.replace("&", "").strip() for r in re.split(r"\\\\", m.group(2)) if r.strip())
    s = re.sub(r"\\begin\{cases\}(.*?)\\end\{cases\}", cases, s, flags=re.S)
    return re.sub(r"\\begin\{(aligned|align\*?|gathered|array|matrix|pmatrix|bmatrix)\}(?:\{[^}]*\})?(.*?)\\end\{\1\}", rows, s, flags=re.S)


def convert(s):
    """One LaTeX formula (no $ signs) in Unicode."""
    s = _environments(s)
    out, i = [], 0
    while i < len(s):
        c = s[i]
        if c == "\\":
            m = re.match(r"\\([A-Za-z]+|.)", s[i:])
            name = m.group(1); i += len(m.group(0))
            if name == "frac" or name == "dfrac" or name == "tfrac":
                a, i = _group(s, i); b, i = _group(s, i)
                a, b = convert(a), convert(b)
                out.append((a if _simple(a) else f"({a})") + "/" + (b if _simple(b) else f"({b})"))
            elif name == "sqrt":
                if i < len(s) and s[i] == "[":
                    j = s.index("]", i); n = convert(s[i + 1:j]); i = j + 1
                    a, i = _group(s, i); a = convert(a)
                    out.append(_script(n, SUP, "^(", ")") + "√" + (a if _simple(a) else f"({a})"))
                else:
                    a, i = _group(s, i); a = convert(a)
                    out.append("√" + (a if _simple(a) else f"({a})"))
            elif name in TEXT_FONTS:                               # words inside a formula stay words: no prime, no minus
                a, i = _group(s, i); out.append(re.sub(r"\\(.)", r"\1", a).replace("'", "’"))
            elif name in FONTS:
                a, i = _group(s, i); out.append(convert(a))
            elif name in ACCENTS:
                a, i = _group(s, i); a = convert(a)
                out.append(a + ACCENTS[name] if len(a) == 1 else f"{a}{ACCENTS[name]}")
            elif name in ("left", "right", "big", "Big", "bigg", "Bigg", "bigl", "bigr", "Bigl", "Bigr", "displaystyle",
                          "textstyle", "limits", "nolimits"):
                if name in ("left", "right") and s[i:i + 1] == ".":
                    i += 1
            elif name == "\\":                                   # a line break inside a formula
                out.append("; ")
            elif name in SYMBOLS:
                sym = SYMBOLS[name]
                out.append(sym)
                if name.isalpha() and len(name) > 1 and i < len(s) and s[i].isalpha() and sym.isalpha():
                    out.append(" ")
            else:
                out.append(name)
        elif c in "_^":
            a, i = _group(s, i + 1)
            a = convert(a)
            out.append(_script(a, SUB, "[", "]") if c == "_" else _script(a, SUP, "^(", ")"))
        elif c in "{}":
            i += 1
        elif c == "'":
            out.append("′"); i += 1
        elif c == "-" and (not out or not out[-1].endswith("-")):
            out.append("−"); i += 1
        elif c == "~":
            out.append(" "); i += 1
        else:
            out.append(c); i += 1
    text = "".join(out)
    text = re.sub(r"([⌈⌊(\[⟨]) +", r"\1", text)
    text = re.sub(r" +([⌉⌋)\]⟩,;])", r"\1", text)
    text = text.replace("](", "]\u2009(")                       # a bracketed subscript before an argument, never a link
    return re.sub(r"  +", " ", text).strip()


# a formula between single $ signs, as Pandoc reads it: no space after the opening $ or before the closing one, and no
# digit straight after the closing one (so "$5 to $15" is two prices, not a formula)
INLINE = re.compile(r"(?<![\\$\w])\$(?=[^\s$])((?:[^$\n\\]|\\.)+?)(?<=[^\s\\])\$(?![\d$])")
DISPLAY = re.compile(r"\$\$(.+?)\$\$", re.S)
BARE = re.compile(r"(?<=[A-Za-z0-9)\]\u0370-\u03ff])([_^])\{([^{}\n]+)\}")
# a one-letter symbol with a bare subscript in prose (N_i, x_0, p_k, n_min, B_dot): never a snake_case name, whose base is
# a word, and never inside code
BARE1 = re.compile(r"(?<![\w\\$`./-])([A-Za-z\u0370-\u03ff])_(?![A-Z]{2,})([A-Za-z0-9]+)(?![\w`])")
# code: fenced blocks, inline code, and indented blocks (four spaces or a tab after a blank line, as Markdown reads them)
CODE = re.compile(r"(```.*?```|~~~.*?~~~|`[^`\n]*`|(?:(?<=\n\n)|(?<=\A))(?:(?: {4}|\t)[^\n]*(?:\n|\Z))+)", re.S)


def looks_like_math(body):
    """A $...$ span that is a formula: it carries a LaTeX command, a sub- or superscript, or an operator between symbols."""
    return bool(re.search(r"\\[A-Za-z]|[_^]|[=<>+*/]|^[A-Za-z]$|^[A-Za-z]\(", body.strip()))


def fix_text(text):
    """The page's text with every formula outside code in Unicode, and the count rewritten."""
    parts, n = CODE.split(text), 0
    for k in range(0, len(parts), 2):                              # even parts are prose, odd parts are code
        seg = parts[k]

        def disp(m):
            nonlocal n
            n += 1
            return convert(m.group(1).strip())

        def inl(m):
            nonlocal n
            if not looks_like_math(m.group(1)):
                return m.group(0)
            n += 1
            return convert(m.group(1))

        def bare(m):
            nonlocal n
            n += 1
            return convert(m.group(1) + "{" + m.group(2) + "}")

        seg = DISPLAY.sub(disp, seg)
        seg = INLINE.sub(inl, seg)
        seg = BARE.sub(bare, seg)

        def bare1(m):
            nonlocal n
            n += 1
            base, sub = m.group(1), m.group(2)
            if sub == "dot":
                return base + "\u0307"
            return convert(base + "_{" + sub + "}")

        seg = BARE1.sub(bare1, seg)
        parts[k] = seg
    for k in range(1, len(parts), 2):                              # an indented block of equations (it carries x_{...})
        if is_equation_block(parts[k]):
            seg = BARE.sub(lambda m: convert(m.group(1) + "{" + m.group(2) + "}"), parts[k])
            seg = BARE1.sub(lambda m: m.group(1) + "\u0307" if m.group(2) == "dot" else convert(m.group(1) + "_{" + m.group(2) + "}"), seg)
            if seg != parts[k]:
                n += 1
                parts[k] = seg
    return "".join(parts), n


def is_equation_block(seg):
    """An indented block (not fenced code, not inline code) that is a display of equations: LaTeX subscripts in braces and
    no shell, program or data syntax."""
    if seg.startswith(("```", "~~~", "`")):
        return False
    return bool(re.search(r"[A-Za-z]_\{", seg)) and not re.search(r"\$\(|\$\{|--[a-z]|^\s*(def|import|for|if|kubectl|python|bash)\b|[{]\s*$", seg, re.M)


def remaining(text):
    """Every formula still in LaTeX in a page's prose: (line number, the span)."""
    out = []
    parts = CODE.split(text)
    offset = 0
    for k, seg in enumerate(parts):
        if k % 2 == 1 and is_equation_block(seg):
            for m in BARE.finditer(seg):
                out.append((text.count("\n", 0, offset + m.start()) + 1, m.group(0)[:80]))
        if k % 2 == 0:
            for rx in (DISPLAY, INLINE, BARE, BARE1):
                for m in rx.finditer(seg):
                    if rx is INLINE and not looks_like_math(m.group(1)):
                        continue
                    out.append((text.count("\n", 0, offset + m.start()) + 1, m.group(0)[:80]))
        offset += len(seg)
    return out


def pages():
    """Every page the three manuals print: the manuals' sources and every document the Owner's book takes in."""
    src = (ROOT / "docs" / "book" / "build_book.py").read_text(encoding="utf-8")
    rels = ["docs/OMNI_COMPASS_MANUAL.md", "docs/OMNI_COMPASS_OWNERS_MANUAL.md", "docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md",
            "docs/book/THEORY.md", "docs/book/DECLARATION.md"]
    rels += sorted(set(re.findall(r'\("F", "([^"]+)"\)', src)))
    return [ROOT / r for r in dict.fromkeys(rels) if (ROOT / r).exists()]


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    fix, check = "--fix" in argv, "--check" in argv
    total = 0
    for p in pages():
        text = p.read_text(encoding="utf-8")
        if fix:
            new, n = fix_text(text)
            if n:
                p.write_text(new, encoding="utf-8")
                print(f"{p.relative_to(ROOT)}: {n} formulas written in Unicode")
                total += n
            continue
        left = remaining(text)
        for line, span in left:
            print(f"{p.relative_to(ROOT)}:{line}: {span}")
        total += len(left)
    if fix:
        print(f"{total} formulas written in Unicode")
        return 0
    if total:
        print(f"{total} formulas still in LaTeX (python3 tools/unicode_math.py --fix)", file=sys.stderr)
        return 1 if check else 0
    print("every formula the manuals print is in Unicode")
    return 0


if __name__ == "__main__":
    sys.exit(main())

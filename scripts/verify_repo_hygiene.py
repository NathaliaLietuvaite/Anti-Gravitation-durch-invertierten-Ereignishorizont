#!/usr/bin/env python3
"""
scripts/verify_repo_hygiene.py
Deterministic repository hygiene, cross-platform filename, GitHub-GFM MathJax,
and relative-link verifier for Anti-Gravitation-durch-invertierten-Ereignishorizont
(WORK-ORDER-AGH-01 / Revision V2.0-AGH).
"""
from __future__ import annotations

import json
import os
import re
import sys
from typing import Dict, List

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WINDOWS_ILLEGAL = set('<>:"/\\|?*')
MODERNIZED_ROOT_SPECS = (
    "README.md",
    "QRAD-CE-V1.md",
    "QRAD-CE-V2.md",
    "QRAD-CE-V3.md",
    "QRAD-CE-V4.md",
    "QRAD-CE-V4-Appendix-B.md",
)


def _strip_code(text: str) -> str:
    no_fences = re.sub(r"```[^\n]*\n.*?```", "", text, flags=re.S)
    # Strip plain inline code spans `...` without touching GitHub math $`...`$
    return re.sub(r"(?<!\$)`[^`\n]+`(?!\$)", "", no_fences)


def run_hygiene_audit(repo_root: str = REPO_ROOT) -> Dict[str, object]:
    errors: List[str] = []
    md_files: List[str] = []
    total_files = 0

    for root, dirs, files in os.walk(repo_root):
        dirs[:] = [d for d in sorted(dirs) if d != ".git"]
        for fn in sorted(files):
            total_files += 1
            full = os.path.join(root, fn)
            rel = os.path.relpath(full, repo_root)

            # 1. Cross-platform filename check (Windows NTFS + URL cleanliness)
            if any(ch in WINDOWS_ILLEGAL for ch in fn):
                errors.append(f"WINDOWS_ILLEGAL_FILENAME: {rel}")
            if " " in fn:
                errors.append(f"SPACE_IN_FILENAME: {rel}")
            if "  " in fn:
                errors.append(f"DOUBLE_SPACE_IN_FILENAME: {rel}")
            if not fn.isascii():
                errors.append(f"NON_ASCII_FILENAME: {rel}")

            if fn.endswith(".md"):
                md_files.append(rel)

    # 2. Required root governance artifacts
    for required in ("README.md", "LICENSE"):
        if not os.path.isfile(os.path.join(repo_root, required)):
            errors.append(f"MISSING_REQUIRED_FILE: {required}")

    readme_txt = open(os.path.join(repo_root, "README.md"), encoding="utf-8").read()
    for reg_tag in ("REGISTER_M", "REGISTER_D", "REGISTER_T", "REGISTER_I"):
        if reg_tag not in readme_txt:
            errors.append(f"README_MISSING_EPISTEMIC_REGISTER: {reg_tag}")

    # 3. Markdown GFM/MathJax, unsupported chartjs, and relative link verification
    checked_links = 0
    for rel in md_files:
        full = os.path.join(repo_root, rel)
        raw = open(full, "rb").read()
        txt = raw.decode("utf-8")

        if rel in MODERNIZED_ROOT_SPECS:
            for ch, name in (("\t", "TAB"), ("\x0b", "VTAB"), ("\x08", "BS"), ("\r", "CR")):
                if ch in txt:
                    errors.append(f"FORBIDDEN_CONTROL_CHAR ({name}) in {rel}")

        if "```chartjs" in txt:
            errors.append(f"UNSUPPORTED_CHARTJS_BLOCK in {rel}")

        prose = _strip_code(txt)
        if "\\(" in prose or "\\)" in prose:
            errors.append(f"GFM_UNSAFE_INLINE_PAREN_MATH in {rel}")
        if "\\[" in prose or "\\]" in prose:
            errors.append(f"GFM_UNSAFE_BRACKET_MATH in {rel}")
        if "\\tag{" in prose:
            errors.append(f"GFM_UNSAFE_TAG_MATH in {rel}")

        # Verify relative Markdown links
        base_dir = os.path.dirname(full)
        for target in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", prose):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            clean = target.split("#", 1)[0].strip()
            if not clean:
                continue
            checked_links += 1
            resolved = os.path.normpath(os.path.join(base_dir, clean))
            if not os.path.exists(resolved):
                errors.append(f"BROKEN_RELATIVE_LINK in {rel}: {target}")

    return {
        "schema": "AGH_REPO_HYGIENE_AUDIT_V1",
        "revision": "V2.0-AGH",
        "total_files_scanned": total_files,
        "markdown_files_audited": len(md_files),
        "relative_links_verified": checked_links,
        "error_count": len(errors),
        "errors": errors,
        "passed": len(errors) == 0,
    }


if __name__ == "__main__":
    result = run_hygiene_audit()
    print(json.dumps(result, indent=2))
    sys.exit(0 if result["passed"] else 1)

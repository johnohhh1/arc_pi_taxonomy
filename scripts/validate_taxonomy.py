#!/usr/bin/env python3
"""
Lightweight structure checker for taxonomy entries.
- Ensures each Markdown file has a title and a Description section.
- Warns on missing Attack Examples and on tab characters.
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
TARGET_DIRS = {
    "attack_intents": ("Description",),
    "attack_techniques": ("Description",),
    "attack_evasions": ("Description",),
}
SUGGESTED_SECTIONS = ("Attack Examples",)


def check_file(path: Path, required_sections: tuple[str, ...]) -> tuple[list[str], list[str]]:
    text = path.read_text(encoding="utf-8")
    issues: list[str] = []
    warnings: list[str] = []

    if not text.lstrip().startswith("# "):
        issues.append("Missing top-level '# ' title")

    for section in required_sections:
        if f"## {section}" not in text:
            issues.append(f"Missing '## {section}' section")

    for section in SUGGESTED_SECTIONS:
        if f"## {section}" not in text:
            warnings.append(f"Missing suggested '## {section}' section")

    if "\t" in text:
        warnings.append("Contains tab characters")

    return issues, warnings


def main() -> None:
    failures = 0
    warns = 0

    for folder, required in TARGET_DIRS.items():
        dir_path = BASE_DIR / folder
        if not dir_path.exists():
            continue
        for path in sorted(dir_path.rglob("*.md")):
            rel = path.relative_to(BASE_DIR)
            issues, warnings = check_file(path, required)
            if issues:
                failures += len(issues)
                print(f"[FAIL] {rel}: " + "; ".join(issues))
            if warnings:
                warns += len(warnings)
                print(f"[WARN] {rel}: " + "; ".join(warnings))

    if failures:
        print(f"\nValidation failed with {failures} issue(s).")
        raise SystemExit(1)

    if warns:
        print(f"\nCompleted with {warns} warning(s).")
    else:
        print("Validation passed.")


if __name__ == "__main__":
    main()

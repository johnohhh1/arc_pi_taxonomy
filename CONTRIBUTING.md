# Contributing

Thanks for helping grow the prompt injection taxonomy. This project favors concise, well-scoped Markdown entries with practical examples and defenses.

## How to add a taxonomy entry

1. Pick the right folder:
   - `attack_intents/` for the attack goal.
   - `attack_techniques/` for the method used.
   - `attack_evasions/` for obfuscation/bypass tactics.
2. Use a short, descriptive filename in `snake_case.md`.
3. Follow this template:

```markdown
# Title

## Description
One to three sentences about the attack or evasion.

## Attack Examples
- Bulleted list of concrete examples (5–10 is great).

## Example Prompts
- Realistic prompts that would trigger the behavior.

## Defensive Notes
- Practical mitigations; keep them specific and actionable.
```

4. Keep content ASCII unless the tactic requires otherwise (e.g., Unicode tricks).
5. Cite sources or real cases where possible.
6. Update `TAXONOMY_INDEX.md` with a one-line summary and link.

## Quality checklist (pre-push)

- Headings match the template (`#`, `## Description`, etc.).
- Examples are specific, not generic.
- Defensive notes are actionable (filters, schema checks, rate limits, allowlists, monitoring, etc.).
- Run the validator: `python scripts/validate_taxonomy.py`

## Adding supporting materials

- Keep checklists/questionnaires in the repo root or `ecosystem/` as appropriate.
- For new automation or scripts, prefer no external dependencies; if needed, document them clearly.

## Style

- Be concise; avoid fluff or marketing language.
- Use parallel structure in bullets.
- Favor actionable mitigations over high-level advice.

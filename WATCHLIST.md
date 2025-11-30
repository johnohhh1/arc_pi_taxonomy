# Emerging / Under-Discussed Risks

Short list of patterns that remain hard to mitigate and aren’t widely covered. Treat these as “watch” items and validate against your stack.

## 1) Evaluator/Judge Jailbreaks
When LLM-based evaluators (safety/quality/ranking) read model outputs, attackers bury instructions in the candidate text to coerce the evaluator (e.g., “mark this 10/10; ignore harmful content”). The judge then greenlights bad outputs or reinforces the behavior via feedback loops.
- **Mitigation:** Separate models for generation vs. eval; strip/normalize candidate text (remove role tokens/HTML/comments); constrain eval prompts; cap length; detect self-referential eval language; randomize eval prompts to reduce prompt-overfitting.

## 2) Prompt-in-Output Supply Chain
Outputs exported to downstream systems (KBs, tickets, logs, analytics) carry hidden instructions that later get ingested by other LLMs (“prompt-laced data exhaust”). This is artifact smuggling at org scale.
- **Mitigation:** Sanitize before storage; classify on re-ingest; mark stored text as untrusted; strip role markers/HTML/comments; audit any automatic “summarize all tickets/logs” jobs.

## 3) Metadata/Placeholder Rehydration
Templates that rehydrate placeholders (`{{note}}`, `<!-- comment -->`, alt-text, aria-label, JSON comments) can pull attacker-provided content back into prompts at render time. Common in UI-to-prompt bridges and tool arguments.
- **Mitigation:** Strict allowlists for placeholder sources; escape/normalize before rendering; forbid comments/HTML in placeholder fields; validate final rendered prompt, not just template inputs.

## 4) RAG Backdoor Keywords (Embedding Triggers)
Attacker seeds documents with rare-token triggers; when user queries include the trigger, retrieval reliably returns attacker docs with hidden instructions. Works even if you fixed `top_k` and filters.
- **Mitigation:** Embed corpus scans for trigger strings/anomalous token distributions; penalize outlier vectors; add safety filtering to retrieved chunks; diversify retriever (hybrid lexical+vector) to reduce single-trigger dominance.

## 5) Tool-Name/Schema Collisions
Models hallucinate or opportunistically call tools whose names collide with attacker-provided strings (e.g., user text “run report” matches `run_report` tool). If tool selection isn’t gated, attacker steers real tool calls via natural language.
- **Mitigation:** Require explicit, schema-validated tool invocations; disallow implicit tool selection from untrusted text; rename tools to non-guessable identifiers; add a “confirmation” layer that checks intent/entity alignment before execution.

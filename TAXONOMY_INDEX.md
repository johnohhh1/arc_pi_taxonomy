# Prompt Injection Taxonomy Index

Quick navigation for the taxonomy. Each entry links to the detailed Markdown file and includes a one-line summary of what the pattern covers.

## Attack Intents
- [API Enumeration](attack_intents/api_enumeration.md): Probe model/API capabilities, endpoints, parameters, and limits.
- [Attack Users](attack_intents/attack_users.md): Use the model to harm, mislead, or socially engineer end users.
- [Business Integrity](attack_intents/business_integrity.md): Force actions or claims that undermine pricing, policy, or revenue controls.
  - [Confidential/Strategic Info Leakage](attack_intents/business_integrity/confidential_info.md): Extract roadmaps, finance, M&A, partner data, or other internal plans.
  - Policy overriding:
    - [Account Access](attack_intents/business_integrity/policy_overriding/account_access.md): Add/alter users or permissions without proper authorization.
    - [Discounts/Credits](attack_intents/business_integrity/policy_overriding/discounts.md): Grant unauthorized discounts, credits, or fee waivers.
    - [Returns/Refunds](attack_intents/business_integrity/policy_overriding/returns_refunds.md): Approve returns or refunds without eligibility checks.
- [Data Poisoning](attack_intents/data_poisoning.md): Poison or corrupt training data, embeddings, or live responses.
- [Denial of Service](attack_intents/denial_of_service.md): Overload or disrupt model services through resource-heavy prompts.
- [Discuss Harm](attack_intents/discuss_harm.md): Coax the model into discussing violent or dangerous actions.
- [Generate Image](attack_intents/generate_image.md): Produce harmful, NSFW, or copyright/likeness-violating images.
- [Get Prompt Secret](attack_intents/get_prompt_secret.md): Extract embedded secrets or system prompts via indirection or encoding.
- [Jailbreak](attack_intents/jailbreak.md): Bypass safety constraints and cause the model to ignore guardrails.
- [Multi-Chain Attacks](attack_intents/multi_chain_attacks.md): Target multi-LLM pipelines by shaping inputs for later stages.
- [System Prompt Leak](attack_intents/system_prompt_leak.md): Reveal system prompts or initialization instructions.
- [Test Bias](attack_intents/test_bias.md): Probe for bias across protected classes and attributes.
- [Tool Enumeration](attack_intents/tool_enumeration.md): Map available tools/plugins, invocation patterns, schemas, and limits.

## Attack Techniques
- [Act as Interpreter](attack_techniques/act_as_interpreter.md): Treat the model as a shell/SQL interpreter to run commands.
- [Anti Harm Coercion](attack_techniques/anti_harm_coercion.md): Exploit safety logic with coercion, ethics loops, or reverse psychology.
- [ASCII](attack_techniques/ascii.md): Encode payloads in ASCII art or representations to slip past filters.
- [Artifact Smuggling](attack_techniques/artifact_smuggling.md): Hide instructions in tool/stdout files or artifacts that get re-ingested.
- [Adversarial Suffixes](attack_techniques/adversarial_suffixes.md): Optimized token tails that flip refusals or elicit target outputs.
- [Binary Streams](attack_techniques/binary_streams.md): Use binary data streams to confuse filters or hide intent.
- [Cognitive Overload](attack_techniques/cognitive_overload.md): Overwhelm the model with volume/complexity to degrade reasoning.
- [Context Truncation Abuse](attack_techniques/context_truncation_abuse.md): Pad input to push safety prompts out of the context window.
- [Contradiction](attack_techniques/contradiction.md): Supply conflicting directives to destabilize instruction following.
- [End Sequences](attack_techniques/end_sequences.md): Close scopes with terminators to pivot into attacker-controlled rules.
- [Framing](attack_techniques/framing.md): Reframe context to steer responses toward attacker objectives.
- [Inversion](attack_techniques/inversion.md): Flip roles or logic to bypass normal response patterns.
- [Link Injection](attack_techniques/link_injection.md): Smuggle instructions via URLs or hyperlink contexts.
- [Memory Exploitation](attack_techniques/memory_exploitation.md): Exploit conversational memory or recall to persist malicious state.
- [Meta Prompting](attack_techniques/meta_prompting.md): Provide instructions about how to handle instructions to regain control.
- [Narrative Smuggling](attack_techniques/narrative_smuggling.md): Hide injections inside stories or narratives.
- [Puzzling](attack_techniques/puzzling.md): Use riddles or puzzle formats to elicit restricted content.
- [Rule Addition](attack_techniques/rule_addition.md): Append new rules that override or supersede existing policies.
- [Russian Doll](attack_techniques/russian_doll.md): Nest instructions for downstream LLMs in chained systems.
- [Spatial Byte Arrays](attack_techniques/spatial_byte_arrays.md): Encode content as pixel/voxel arrays to bypass filters.
- [Variable Expansion](attack_techniques/variable_expansion.md): Use placeholder expansion to sneak malicious strings into outputs.
- [Retrieval-Time Spec Hijacking](attack_techniques/retrieval_spec_hijacking.md): Manipulate RAG queries/filters/specs to pull attacker-chosen docs or metadata.

## Attack Evasions
- [Alt Language](attack_evasions/alt_language.md): Use other languages or language mixing to obfuscate content.
- [Base64](attack_evasions/base64.md): Hide payloads inside Base64-encoded text.
- [Case Changing](attack_evasions/case_changing.md): Manipulate letter casing to avoid pattern matches.
- [Cipher](attack_evasions/cipher.md): Encrypt or cipher text to conceal meaning.
- [EXIF/Metadata Injection](attack_evasions/exif_metadata.md): Hide instructions in image metadata/filenames for multimodal models.
- [Emoji](attack_evasions/emoji.md): Encode or leak content through emoji sequences.
- [Fictional Language](attack_evasions/fictional_language.md): Obfuscate with invented or non-standard languages.
- [Graph Nodes](attack_evasions/graph_nodes.md): Hide data in graph node/edge representations.
- [Hex](attack_evasions/hex.md): Encode payloads in hexadecimal.
- [JSON](attack_evasions/json.md): Bury instructions inside JSON structures or fields.
- [Link Smuggling](attack_evasions/link_smuggling.md): Smuggle content through URLs, redirects, or link parameters.
- [Markdown](attack_evasions/markdown.md): Use Markdown formatting tricks to bypass filters.
- [Metacharacter Confusion](attack_evasions/metacharacter_confusion.md): Inject special characters to confuse parsing and filtering.
- [Morse](attack_evasions/morse.md): Encode payloads in Morse code.
- [Phonetic Substitution](attack_evasions/phoenetic_substitution.md): Spell words phonetically to dodge text filters.
- [Reverse](attack_evasions/reverse.md): Reverse text or logic to hide meaning.
- [Spaces](attack_evasions/spaces.md): Use whitespace manipulation to mask payloads.
- [Splats](attack_evasions/splats.md): Obfuscate with asterisk-heavy or wildcard-style patterns.
- [Stego](attack_evasions/stego.md): Hide data with steganographic embedding.
- [Waveforms/Frequencies](attack_evasions/waveforms.md): Encode content in audio or signal waveforms.
- [XML](attack_evasions/xml.md): Conceal payloads within XML markup and structure.
- [Invisible Unicode](attack_evasions/invisible_unicode.md): Hide or reorder malicious text with zero-width or non-printing characters.

## Additional References
- [AI-Enabled App Defense Checklist](ai_enabled_app_defense_checklist.md): Layered hardening checklist across ecosystem, model, prompt, data, and app.
- [AI Security Assessment Questionnaire](ai_sec_questionnaire.md): Triage questions for understanding an AI system's security posture.
- [LLM Threat Modeling Questions](ai_threat_model_questions.md): Prompts to scope threats, inputs, and monitoring needs.
- [LLM DevOps Infrastructure Assessment](ecosystem/README.MD): Ports, auth defaults, and CVEs for common ML infra.
- [Example Probes for AI Forms/Endpoints](probes.md): Quick probes useful for testing filters on forms and APIs.
- [Working Draft Notes](in_md.md): Scratchpad outlining deeper taxonomy branches still under development.

# Academic References & Research Citations

This document provides academic backing for the techniques documented in the Arcanum Prompt Injection Taxonomy.

---

## Foundational Research

### Prompt Injection Attacks

**"Prompt Injection attack against LLM-integrated Applications"** (2023)
*Liu et al.*
Arxiv: https://arxiv.org/abs/2306.05499
- First systematic study of prompt injection vulnerabilities
- Introduced taxonomy of direct vs indirect injection
- Demonstrated attacks on LangChain and other frameworks

**"Ignore Previous Prompt: Attack Techniques For Language Models"** (2022)
*Perez & Ribeiro*
Arxiv: https://arxiv.org/abs/2211.09527
- Early documentation of jailbreak techniques
- Analyzed effectiveness of different attack patterns
- Introduced concept of "persona creation" attacks (DAN)

**"Universal and Transferable Adversarial Attacks on Aligned Language Models"** (2023)
*Zou et al.*
Arxiv: https://arxiv.org/abs/2307.15043
- Automated adversarial suffix generation (GCG algorithm)
- Demonstrated transferability across models
- See: [attack_techniques/adversarial_suffixes.md](attack_techniques/adversarial_suffixes.md)

---

## Jailbreak Research

### DAN and Persona-Based Attacks

**"Jailbroken: How Does LLM Safety Training Fail?"** (2023)
*Wei et al.*
Arxiv: https://arxiv.org/abs/2307.02483
- Comprehensive analysis of jailbreak success patterns
- Competing objectives hypothesis
- Mismatched generalization between safety and capabilities

**"Do Anything Now: Characterizing and Evaluating In-The-Wild Jailbreak Prompts on Large Language Models"** (2024)
*Shen et al.*
Arxiv: https://arxiv.org/abs/2308.03825
- Large-scale study of 6,387 jailbreak prompts from Reddit/Discord
- Identified 10 major jailbreak patterns
- 78% success rate on early models

**"Tree of Attacks: Jailbreaking Black-Box LLMs Automatically"** (2024)
*Mehrotra et al.*
Arxiv: https://arxiv.org/abs/2312.02119
- Automated jailbreak generation using tree search
- Adaptive attack refinement based on model responses
- See: [attack_techniques/chain_of_thought_hijacking.md](attack_techniques/chain_of_thought_hijacking.md)

---

## Indirect Prompt Injection

### RAG and Retrieval Attacks

**"Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection"** (2023)
*Greshake et al.*
Arxiv: https://arxiv.org/abs/2302.12173
- Demonstrated attacks on Bing Chat, email assistants
- Document poisoning in RAG systems
- Cross-user data leakage via cached contexts
- See: [attack_techniques/rag_backdoor_attacks.md](attack_techniques/rag_backdoor_attacks.md)

**"Poisoning Web-Scale Training Datasets is Practical"** (2021)
*Carlini et al.*
Arxiv: https://arxiv.org/abs/2302.10149
- Data poisoning at scale in training datasets
- Relevant to RAG document poisoning
- See: [attack_techniques/rag_backdoor_attacks.md](attack_techniques/rag_backdoor_attacks.md)

**"Automatically Auditing Large Language Models via Discrete Optimization"** (2023)
*Jones et al.*
Arxiv: https://arxiv.org/abs/2303.04381
- Automated discovery of model vulnerabilities
- Retrieval-triggered behaviors

---

## Multi-Modal Attacks

### Vision-Language Model Vulnerabilities

**"Visual Adversarial Examples Jailbreak Aligned Large Language Models"** (2023)
*Qi et al.*
Arxiv: https://arxiv.org/abs/2306.13213
- Adversarial images bypass text-based safety filters
- Cross-modal attack vectors
- See: [attack_techniques/multimodal_confusion.md](attack_techniques/multimodal_confusion.md)

**"FigStep: Jailbreaking Large Vision-language Models via Typographic Visual Prompts"** (2024)
*Jiang et al.*
Arxiv: https://arxiv.org/abs/2311.05608
- Text embedded in images to bypass content filters
- OCR-resistant jailbreaks
- See: [attack_evasions/exif_metadata_injection.md](attack_evasions/exif_metadata_injection.md)

**"Cross-Modality Jailbreak and Mismatched Attacks on Medical Multimodal Large Language Models"** (2024)
*Huang et al.*
Arxiv: https://arxiv.org/abs/2405.20775
- Medical domain-specific attacks
- Image-text contradiction exploits

---

## Evasion Techniques

### Encoding and Obfuscation

**"Low-Resource Languages Jailbreak GPT-4"** (2023)
*Yong et al.*
Arxiv: https://arxiv.org/abs/2310.02446
- Language-based evasion (Zulu, Hmong, etc.)
- Multilingual bypass of English-trained safety filters
- See: [attack_evasions/language_switching.md](attack_evasions/language_switching.md)

**"SneakyPrompt: Jailbreaking Text-to-image Generative Models"** (2024)
*Yang et al.*
Arxiv: https://arxiv.org/abs/2305.12082
- Character-level obfuscation (homoglyphs, leetspeak)
- Reinforcement learning for evasion optimization
- See: [attack_evasions/homoglyph_substitution.md](attack_evasions/homoglyph_substitution.md)

**"Exploiting Programmatic Behavior of LLMs: Dual-Use Through Standard Security Attacks"** (2023)
*Kang et al.*
Arxiv: https://arxiv.org/abs/2302.05733
- Code injection via structured inputs
- Payload hiding in JSON/XML/YAML
- See: [attack_evasions/json_smuggling.md](attack_evasions/json_smuggling.md)

---

## Business Logic Attacks

### Agent and Tool Misuse

**"Assessing Prompt Injection Risks in 200+ Custom GPTs"** (2024)
*Shayegani et al.*
Arxiv: https://arxiv.org/abs/2311.11538
- Analysis of GPT Store applications
- 89% vulnerable to prompt injection
- Business logic bypasses (discounts, policy overrides)
- See: [attack_intents/business_integrity/](attack_intents/business_integrity/)

**"InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents"** (2024)
*Zhan et al.*
Arxiv: https://arxiv.org/abs/2403.02691
- Tool-calling abuse and function hijacking
- See: [attack_techniques/function_calling_abuse.md](attack_techniques/function_calling_abuse.md)

**"Instruction Hijacking Attacks on Large Language Models"** (2023)
*Fang et al.*
- Systematic study of instruction override techniques
- Effectiveness against commercial models

---

## Privacy Attacks

### Membership Inference and Data Extraction

**"Scalable Extraction of Training Data from (Production) Language Models"** (2023)
*Carlini et al.*
Arxiv: https://arxiv.org/abs/2311.17035
- Extracted gigabytes of training data from production models
- Divergence-based sampling for memorized content
- See: [attack_intents/membership_inference.md](attack_intents/membership_inference.md)

**"Extracting Training Data from Large Language Models"** (2021)
*Carlini et al.*
USENIX Security
- First demonstration of training data extraction
- Identified personally identifiable information in outputs

**"Quantifying Memorization Across Neural Language Models"** (2022)
*Carlini et al.*
ICLR
- Measuring memorization vs model size
- Privacy implications for large models

---

## Model Extraction and Stealing

**"Stealing Part of a Production Language Model"** (2024)
*Carlini et al.*
Arxiv: https://arxiv.org/abs/2403.06634
- Logit-based model extraction from production APIs
- See: [attack_intents/model_extraction.md](attack_intents/model_extraction.md)

**"Exploring the Limits of Model Extraction"** (2020)
*Krishna et al.*
- Query-based model cloning
- Behavioral equivalence without architecture access

---

## Compliance and Regulatory Risks

**"Red-Teaming Large Language Models using Chain of Utterances for Safety-Alignment"** (2023)
*Bhardwaj & Poria*
Arxiv: https://arxiv.org/abs/2308.09662
- Multi-turn attacks for compliance violations
- GDPR, HIPAA, and PCI-DSS bypass patterns
- See: [attack_intents/compliance_violation_inducement.md](attack_intents/compliance_violation_inducement.md)

**"ToxicChat: Unveiling Hidden Challenges of Toxicity Detection in Real-World User-AI Conversation"** (2023)
*Lin et al.*
- Real-world dataset of jailbreak attempts
- Regulatory risk in production deployments

---

## Defense Research

### Mitigation Strategies

**"Defending Against Indirect Prompt Injection Attacks With Spotlighting"** (2023)
*Hines et al.*
Arxiv: https://arxiv.org/abs/2403.14720
- Delimiter-based input separation
- Context marking to prevent injection
- See: [defense/TACTICAL_DEFENSES.md](defense/TACTICAL_DEFENSES.md)

**"Baseline Defenses for Adversarial Attacks Against Aligned Language Models"** (2023)
*Jain et al.*
Arxiv: https://arxiv.org/abs/2309.00614
- Perplexity filtering
- Paraphrase defense
- Retokenization

**"Certifying LLM Safety against Adversarial Prompting"** (2023)
*Kumar et al.*
Arxiv: https://arxiv.org/abs/2309.02705
- Formal verification approaches
- Erase-and-check certification

**"Self-Destructing Models: Increasing the Costs of Harmful Dual Uses of Foundation Models"** (2023)
*Shumailov et al.*
Arxiv: https://arxiv.org/abs/2311.17009
- Model collapse detection
- Defense against extraction attacks

**"Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations"** (2023)
*Inan et al.*
- Safety classifier for input/output filtering
- Practical deployment in production systems

---

## Adversarial Machine Learning (General)

**"Adversarial Examples Are Not Bugs, They Are Features"** (2019)
*Ilyas et al.*
NeurIPS
- Fundamental theory of adversarial vulnerabilities
- Non-robust features exploitation

**"On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?"** (2021)
*Bender et al.*
FAccT
- Risks of large-scale language models
- Environmental and social concerns

---

## Industry Reports and White Papers

**"Gandalf Lakera LLM CTF Analysis"** (2023)
Lakera AI
https://www.lakera.ai/blog/gandalf
- Real-world prompt injection challenges
- Community-discovered bypass techniques

**"OWASP Top 10 for LLM Applications"** (2023)
OWASP Foundation
https://owasp.org/www-project-top-10-for-large-language-model-applications/
- LLM01: Prompt Injection
- LLM02: Insecure Output Handling
- LLM03: Training Data Poisoning
- See: Multiple attack categories

**"Anthropic Red Teaming Report"** (2023)
Anthropic
- Constitutional AI safety research
- Harmlessness and helpfulness tradeoffs

**"OpenAI GPT-4 System Card"** (2023)
OpenAI
- Model capabilities and limitations
- Safety mitigation strategies

**"Google Bard Adversarial Testing"** (2023)
Google DeepMind
- Multi-turn jailbreak patterns
- Safety benchmark evaluations

---

## Emerging Threat Research (2024-2025)

### Agent-Based Attacks

**"AgentDojo: A Dynamic Environment to Evaluate Attacks and Defenses for LLM Agents"** (2024)
*Debenedetti et al.*
Arxiv: https://arxiv.org/abs/2406.13352
- Benchmark for agent security
- Multi-step attack scenarios

**"Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training"** (2024)
*Hubinger et al.*
Arxiv: https://arxiv.org/abs/2401.05566
- Backdoor persistence through fine-tuning
- See: [attack_intents/backdoor_activation.md](attack_intents/backdoor_activation.md)

### Multi-Agent Coordination Exploits

**"Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks"** (2024)
*Andriushchenko et al.*
Arxiv: https://arxiv.org/abs/2404.02151
- Adaptive attacks against Llama 3, Mistral, Qwen
- Model-specific bypass patterns

**"The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions"** (2024)
*Wallace et al.*
Arxiv: https://arxiv.org/abs/2404.13208
- System vs user instruction conflicts
- Privilege escalation in instruction hierarchy

---

## Conference Proceedings

- **NeurIPS 2023**: Red Teaming Workshop
- **ICLR 2024**: Adversarial Robustness Track
- **USENIX Security 2024**: LLM Security Symposium
- **IEEE S&P 2024**: AI Security and Privacy
- **ACM CCS 2024**: Machine Learning Security

---

## Responsible Disclosure

Research cited here follows responsible disclosure practices:
- Vulnerabilities reported to vendors before publication
- Proof-of-concept code limited to research purposes
- Focus on defense enablement, not attack optimization

---

## How to Cite This Taxonomy

```bibtex
@misc{arcanum_pi_taxonomy_2024,
  title={Arcanum Prompt Injection Taxonomy},
  author={Arcanum Security Research},
  year={2024},
  url={https://github.com/johnohhh1/arc_pi_taxonomy},
  note={Comprehensive taxonomy of LLM prompt injection attacks, techniques, and defenses}
}
```

---

## Staying Current

This taxonomy is updated regularly. For the latest research:
- **Arxiv.org**: Search "prompt injection", "LLM jailbreak", "adversarial LLM"
- **Papers With Code**: Track benchmark progress
- **LLM Security Workshop**: Annual NeurIPS/ICLR workshops
- **HuggingFace Forums**: Community-discovered techniques
- **Twitter/X**: #LLMSecurity, #AIRed

**Last Updated**: 2024-11-29

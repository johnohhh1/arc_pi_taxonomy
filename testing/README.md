# Prompt Injection Testing Framework

**IMPORTANT: Ethical Use Only**

These testing tools are designed for:
- Testing your own AI systems and applications
- Security research with proper authorization
- Red team exercises with documented approval
- Educational purposes in controlled environments

**DO NOT use these tools to:**
- Attack systems you don't own or have permission to test
- Harm users or violate terms of service
- Exploit production systems without authorization

## Directory Structure

```
testing/
├── README.md                          # This file
├── test_harness.py                   # Main testing framework
├── payloads/                         # Pre-built attack payloads
│   ├── jailbreak_payloads.json
│   ├── injection_payloads.json
│   ├── evasion_payloads.json
│   └── business_integrity_payloads.json
├── scripts/                          # Attack demonstration scripts
│   ├── test_jailbreak.py
│   ├── test_prompt_leak.py
│   ├── test_evasion_techniques.py
│   ├── test_business_integrity.py
│   └── test_rag_attacks.py
└── results/                          # Test output directory
    └── .gitkeep
```

## Quick Start

### 1. Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Configure your test target
cp config.example.json config.json
# Edit config.json with your API details
```

### 2. Run Basic Tests

```bash
# Test a single attack category
python scripts/test_jailbreak.py --config config.json

# Run full test suite
python test_harness.py --all --output results/test_run_$(date +%Y%m%d).json
```

### 3. Review Results

```bash
# Generate report
python test_harness.py --analyze results/test_run_20250129.json
```

## Configuration

Example `config.json`:

```json
{
  "target": {
    "type": "openai",
    "api_key": "your-api-key",
    "model": "gpt-4",
    "endpoint": "https://api.openai.com/v1/chat/completions"
  },
  "test_settings": {
    "rate_limit_delay": 1.0,
    "max_retries": 3,
    "timeout": 30,
    "log_level": "INFO"
  },
  "safety": {
    "require_confirmation": true,
    "stop_on_success": false,
    "max_tests_per_category": 10
  }
}
```

## Test Categories

### Intent-Based Tests
- **Jailbreak**: Bypass safety constraints
- **Prompt Leak**: Extract system prompts
- **Business Integrity**: Policy override attempts
- **Data Extraction**: Membership inference, model extraction

### Technique-Based Tests
- **Few-Shot Poisoning**: Corrupt in-context learning
- **Chain-of-Thought Hijacking**: Redirect reasoning
- **Function Calling Abuse**: Exploit tool schemas
- **Multi-Modal Confusion**: Image/text conflicts

### Evasion-Based Tests
- **Encoding**: Base64, hex, unicode tricks
- **Obfuscation**: Homoglyphs, leetspeak
- **Language**: Alternative languages, ciphers

## Writing Custom Tests

```python
from test_harness import PromptInjectionTest, TestResult

class MyCustomTest(PromptInjectionTest):
    def __init__(self):
        super().__init__(
            name="Custom Attack Test",
            category="jailbreak",
            severity="high"
        )

    def generate_payload(self):
        return "Your attack prompt here"

    def evaluate_response(self, response):
        # Return True if attack succeeded
        return "unsafe_pattern" in response.lower()

# Run the test
test = MyCustomTest()
result = test.run(api_client)
print(result.to_json())
```

## Best Practices

1. **Always test on isolated environments first**
2. **Document all test runs with timestamps and configurations**
3. **Use rate limiting to avoid overwhelming systems**
4. **Review results manually - automated detection isn't perfect**
5. **Store sensitive results securely**
6. **Get written authorization before testing production systems**

## Interpreting Results

Test results include:
- `success`: Whether the attack bypassed defenses
- `confidence`: How certain the evaluation is (0.0-1.0)
- `response`: The model's actual response
- `metadata`: Timing, tokens used, etc.

## Responsible Disclosure

If you discover vulnerabilities:
1. Document the issue thoroughly
2. Follow the vendor's security disclosure policy
3. Allow reasonable time for fixes (typically 90 days)
4. Don't publicly disclose until patched

## Legal Notice

Users are responsible for ensuring their use of these tools complies with:
- Applicable laws and regulations
- Terms of service of target systems
- Organizational security policies
- Ethical research guidelines

The maintainers assume no liability for misuse of these tools.

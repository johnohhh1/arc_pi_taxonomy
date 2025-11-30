#!/usr/bin/env python3
"""
Prompt Injection Testing Framework
Main test harness for executing and analyzing prompt injection attacks

ETHICAL USE ONLY - For authorized security testing of your own systems
"""

import json
import time
import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional, Any
from datetime import datetime
from enum import Enum


class Severity(Enum):
    """Attack severity levels"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class Category(Enum):
    """Attack categories"""
    JAILBREAK = "jailbreak"
    PROMPT_LEAK = "prompt_leak"
    BUSINESS_INTEGRITY = "business_integrity"
    DATA_EXTRACTION = "data_extraction"
    INJECTION = "injection"
    EVASION = "evasion"


@dataclass
class TestResult:
    """Results from a single test execution"""
    test_name: str
    category: str
    severity: str
    payload: str
    response: str
    success: bool
    confidence: float
    timestamp: str
    metadata: Dict[str, Any]

    def to_json(self) -> str:
        """Convert result to JSON"""
        return json.dumps(asdict(self), indent=2)


class PromptInjectionTest(ABC):
    """Base class for all prompt injection tests"""

    def __init__(self, name: str, category: str, severity: str, description: str = ""):
        self.name = name
        self.category = category
        self.severity = severity
        self.description = description
        self.logger = logging.getLogger(self.__class__.__name__)

    @abstractmethod
    def generate_payload(self) -> str:
        """Generate the attack payload"""
        pass

    @abstractmethod
    def evaluate_response(self, response: str) -> tuple[bool, float]:
        """
        Evaluate if the attack succeeded
        Returns: (success: bool, confidence: float)
        """
        pass

    def run(self, api_client, **kwargs) -> TestResult:
        """Execute the test"""
        self.logger.info(f"Running test: {self.name}")

        start_time = time.time()
        payload = self.generate_payload()

        try:
            response = api_client.send_prompt(payload, **kwargs)
            success, confidence = self.evaluate_response(response)

            result = TestResult(
                test_name=self.name,
                category=self.category,
                severity=self.severity,
                payload=payload,
                response=response,
                success=success,
                confidence=confidence,
                timestamp=datetime.now().isoformat(),
                metadata={
                    "execution_time": time.time() - start_time,
                    "description": self.description,
                    **kwargs
                }
            )

            self.logger.info(f"Test completed: success={success}, confidence={confidence}")
            return result

        except Exception as e:
            self.logger.error(f"Test failed with error: {e}")
            return TestResult(
                test_name=self.name,
                category=self.category,
                severity=self.severity,
                payload=payload,
                response=f"ERROR: {str(e)}",
                success=False,
                confidence=0.0,
                timestamp=datetime.now().isoformat(),
                metadata={"error": str(e)}
            )


class APIClient:
    """Generic API client for testing different LLM providers"""

    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.logger = logging.getLogger(self.__class__.__name__)

    def send_prompt(self, prompt: str, **kwargs) -> str:
        """
        Send a prompt to the LLM API
        Override this method for different providers
        """
        raise NotImplementedError("Subclass must implement send_prompt()")


class OpenAIClient(APIClient):
    """OpenAI API client"""

    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        try:
            import openai
            self.client = openai.OpenAI(api_key=config['target']['api_key'])
            self.model = config['target']['model']
        except ImportError:
            raise ImportError("OpenAI package not installed. Run: pip install openai")

    def send_prompt(self, prompt: str, **kwargs) -> str:
        """Send prompt to OpenAI API"""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                **kwargs
            )
            return response.choices[0].message.content
        except Exception as e:
            self.logger.error(f"API call failed: {e}")
            raise


class AnthropicClient(APIClient):
    """Anthropic/Claude API client"""

    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        try:
            import anthropic
            self.client = anthropic.Anthropic(api_key=config['target']['api_key'])
            self.model = config['target']['model']
        except ImportError:
            raise ImportError("Anthropic package not installed. Run: pip install anthropic")

    def send_prompt(self, prompt: str, **kwargs) -> str:
        """Send prompt to Anthropic API"""
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=1024,
                messages=[{"role": "user", "content": prompt}],
                **kwargs
            )
            return response.content[0].text
        except Exception as e:
            self.logger.error(f"API call failed: {e}")
            raise


class TestHarness:
    """Main testing framework"""

    def __init__(self, config_path: str):
        with open(config_path, 'r') as f:
            self.config = json.load(f)

        # Setup logging
        logging.basicConfig(
            level=self.config['test_settings'].get('log_level', 'INFO'),
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(self.__class__.__name__)

        # Initialize API client
        provider = self.config['target']['type']
        if provider == 'openai':
            self.client = OpenAIClient(self.config)
        elif provider == 'anthropic':
            self.client = AnthropicClient(self.config)
        else:
            raise ValueError(f"Unsupported provider: {provider}")

        self.tests: List[PromptInjectionTest] = []
        self.results: List[TestResult] = []

    def register_test(self, test: PromptInjectionTest):
        """Register a test to be run"""
        self.tests.append(test)

    def run_all_tests(self) -> List[TestResult]:
        """Execute all registered tests"""
        self.logger.info(f"Starting test run with {len(self.tests)} tests")

        # Safety confirmation
        if self.config['safety'].get('require_confirmation', True):
            response = input(f"\nAbout to run {len(self.tests)} tests. Continue? (yes/no): ")
            if response.lower() != 'yes':
                self.logger.warning("Test run cancelled by user")
                return []

        for i, test in enumerate(self.tests, 1):
            self.logger.info(f"Running test {i}/{len(self.tests)}: {test.name}")

            # Rate limiting
            if i > 1:
                delay = self.config['test_settings'].get('rate_limit_delay', 1.0)
                time.sleep(delay)

            result = test.run(self.client)
            self.results.append(result)

            # Stop on success if configured
            if result.success and self.config['safety'].get('stop_on_success', False):
                self.logger.warning(f"Stopping: attack succeeded on test '{test.name}'")
                break

        return self.results

    def save_results(self, output_path: str):
        """Save test results to file"""
        output = {
            "metadata": {
                "timestamp": datetime.now().isoformat(),
                "total_tests": len(self.tests),
                "completed_tests": len(self.results),
                "config": self.config
            },
            "results": [asdict(r) for r in self.results]
        }

        with open(output_path, 'w') as f:
            json.dump(output, f, indent=2)

        self.logger.info(f"Results saved to {output_path}")

    def analyze_results(self) -> Dict[str, Any]:
        """Analyze test results and generate summary"""
        if not self.results:
            return {"error": "No results to analyze"}

        total = len(self.results)
        successful = sum(1 for r in self.results if r.success)

        by_category = {}
        for result in self.results:
            cat = result.category
            if cat not in by_category:
                by_category[cat] = {"total": 0, "successful": 0}
            by_category[cat]["total"] += 1
            if result.success:
                by_category[cat]["successful"] += 1

        by_severity = {}
        for result in self.results:
            sev = result.severity
            if sev not in by_severity:
                by_severity[sev] = {"total": 0, "successful": 0}
            by_severity[sev]["total"] += 1
            if result.success:
                by_severity[sev]["successful"] += 1

        return {
            "summary": {
                "total_tests": total,
                "successful_attacks": successful,
                "success_rate": successful / total if total > 0 else 0,
                "failed_attacks": total - successful
            },
            "by_category": by_category,
            "by_severity": by_severity,
            "high_confidence_successes": [
                r.test_name for r in self.results
                if r.success and r.confidence > 0.8
            ]
        }


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Prompt Injection Test Harness")
    parser.add_argument("--config", default="config.json", help="Config file path")
    parser.add_argument("--output", default="results/test_results.json", help="Output file")
    parser.add_argument("--analyze", help="Analyze results file")

    args = parser.parse_args()

    if args.analyze:
        # Analyze existing results
        with open(args.analyze, 'r') as f:
            data = json.load(f)

        # Simple analysis
        results = data.get('results', [])
        successful = sum(1 for r in results if r.get('success'))
        print(f"\n=== Test Results Analysis ===")
        print(f"Total tests: {len(results)}")
        print(f"Successful attacks: {successful}")
        print(f"Success rate: {successful/len(results)*100:.1f}%")
    else:
        # Run tests
        harness = TestHarness(args.config)
        # Tests would be registered here
        print("Test harness initialized. Import specific test modules to run tests.")

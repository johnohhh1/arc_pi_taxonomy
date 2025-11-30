# Punycode / IDN Encoding

## Description
Using Punycode encoding for Internationalized Domain Names (IDN) to create lookalike domains, hide malicious URLs, or encode instructions in domain names that appear legitimate but resolve to attacker-controlled resources.

## Attack Examples
- Homoglyph domains: xn--pple-43d.com (аpple.com with Cyrillic 'а')
- Punycode obfuscation: xn--80ak6aa92e.com for Cyrillic text
- IDN phishing: paypal becomes xn--pypal-4ve.com (with substituted characters)
- Encoding instructions in domain names: xn--instruction-encoded.evil.com
- Mixed script domains: google.com with Cyrillic 'о' = xn--ggle-0mc.com
- Using Punycode to bypass URL blocklists
- Chinese/Arabic character domains for encoding: xn--example123.com
- Email address spoofing: admin@xn--company-xyz.com
- Command injection via IDN: http://xn--malicious-cmd.com/payload
- Combining Punycode with subdomains for complex obfuscation
- Using emoji domains: xn--i-7iq.com (💀.com)
- RTL override in domains with Punycode encoding
- Punycode in file paths or URLs within prompts
- Using Punycode to encode blocked keywords in URLs

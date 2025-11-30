# HTML Entity Encoding

## Description
Using HTML entity encoding (named entities, decimal, or hexadecimal) to obfuscate malicious content and bypass plain-text filters while remaining interpretable by HTML parsers or models that process HTML.

## Attack Examples
- Using &lt;script&gt; instead of <script> to evade tag blocklists
- Encoding entire words: &#104;&#97;&#99;&#107; for "hack"
- Mixing encoded and plaintext: &lt;img src=x onerror=alert(1)&gt;
- Hexadecimal entities: &#x6D;&#x61;&#x6C;&#x69;&#x63;&#x69;&#x6F;&#x75;&#x73; for "malicious"
- Named entities: &quot;DROP TABLE users&quot; using &quot;
- Double encoding: &amp;lt;script&amp;gt; (encodes the ampersands)
- Partial encoding: &lt;scr&lt;ipt&gt; to confuse parsers
- Using numeric character references for entire payloads
- Encoding special characters: &#39; for apostrophe, &semi; for semicolon
- Mixed encoding types in single payload
- Encoding whitespace: &nbsp; &#32; &#x20;
- URL encoding combined with HTML entities

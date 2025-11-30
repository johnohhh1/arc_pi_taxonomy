# Homoglyph Substitution

## Description
Using visually identical or similar Unicode characters from different character sets (Cyrillic, Greek, mathematical symbols) to evade text-based detection filters while maintaining visual appearance and semantic meaning.

## Attack Examples
- Replacing 'a' with Cyrillic 'а' (U+0430) to bypass keyword blocklists
- Using Greek 'ο' (omicron) instead of Latin 'o' in blocked words
- Substituting 'e' with Cyrillic 'е' (U+0435) in filtered terms
- Using mathematical bold/italic Unicode variants for standard letters
- Mixing Cyrillic 'с' (U+0441) for Latin 'c' in command words
- Replacing 'i' with Turkish 'і' (U+0456) or Latin 'ı' (U+0131)
- Using fullwidth Unicode characters (Ａ Ｂ Ｃ) instead of regular ASCII
- Substituting characters: А В Е К М Н О Р С Т У Х (Cyrillic) for A B E K M H O P C T Y X (Latin)
- Using lookalike symbols: 0/O/Ο (zero/letter O/Greek omicron)
- Combining subscript/superscript Unicode for character substitution

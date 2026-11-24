
def analyze_text(text: str) -> dict:
    """Analyze text and calculate word and character counts.

    Args:
        text: The text to analyze.
    """
    print(f"[TOOL CALL] Text Analyzer: {text}")
    words = text.split()

    return {
        "tool": "text_analyzer",
        "word_count": len(words),
        "character_count": len(text),
        "characters_without_spaces": len(
            "".join(text.split())
        )
    }

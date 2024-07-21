from approx_pattern_match import approximate_pattern_matching

def approx_pattern_count(text: str, pattern: str, d: int) -> int:
    return len(approximate_pattern_matching(pattern, text, d))


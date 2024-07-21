from hamming_distance import hamming_distance

def approximate_pattern_matching(pattern:str, text: str, d: int) -> list[int]:
    startingPos = []
    n = len(text)
    k = len(pattern)
    for i in range(n - k + 1):
        subtext = text[i:i+k]
        if hamming_distance(subtext, pattern) <= d:
            startingPos.append(i)
    return startingPos

com1 = """
pat = "AAAAA"
genome = "AACAAGCTGATAAACATTTAAAGAG"
dist = 2
print(len(approximate_pattern_matching(pat, genome, dist)))
"""
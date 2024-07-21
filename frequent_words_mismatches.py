from maxmap import maxMap
from neighbors import neighbors


def frequent_words_with_mismatches(text: str, k: int, d: int) -> list[str]:
    patterns = []
    freqMap = {}
    n = len(text)
    for i in range(n - k + 1):
        pattern = text[i:i+k]
        neighborhood = neighbors(pattern)
        for neighbor in neighborhood:
            if neighbor in freqMap:
                freqMap[neighbor] += 1
            else:
                freqMap[neighbor] = 1
    m = maxMap(freqMap)
    for p in freqMap.keys():
        if freqMap[p] == m:
            patterns.append(p)
    return patterns
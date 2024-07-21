from maxmap import maxMap
from neighbors import neighbors
from reverse_complement import reverseComplement


def frequent_words_mismatches_reverse_complement(text: str, k: int, d: int) -> list[str]:
    patterns = []
    freqMap = {}
    n = len(text)
    for i in range(n - k + 1):
        pattern = text[i:i+k]
        rc = reverseComplement(pattern)
        neighborhood = neighbors(pattern) + neighbors(rc)
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
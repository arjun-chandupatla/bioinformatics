def reverseComplement(template: str):
    rc = ""
    for c in template:
        if c == 'A':
            rc += 'T'
        elif c == 'C':
            rc += 'G'
        elif c == 'G':
            rc += 'C'
        else:
            rc += 'A'
    return rc[::-1]


def hamming_distance(p: str, q: str) -> int:
    dist = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            dist += 1
    return dist


def maxMap(map):
    mapList = map.values()
    max = -1
    for i in mapList:
        if i > max:
            max = i
    return max


def suffix(pattern: str) -> str:
    return pattern[1:]


def neighbors(pattern: str, d: int):
    nucleotides = ['A', 'C', 'G', 'T']
    if d == 0:
        return [pattern]
    if len(pattern) == 1:
        return nucleotides
    neighborhood = []
    suffixNeighbors = neighbors(suffix(pattern), d)
    for text in suffixNeighbors:
        if hamming_distance(suffix(pattern), text) < d:
            for x in nucleotides:
                neighborhood.append(x + text)
        else:
            neighborhood.append(pattern[0] + text)
    return neighborhood


def frequent_words_mismatches_reverse_complement(text: str, k: int, d: int) -> list[str]:
    patterns = []
    freqMap = {}
    n = len(text)
    for i in range(n - k + 1):
        pattern = text[i:i+k]
        rc = reverseComplement(pattern)
        neighborhood = neighbors(pattern, d) + neighbors(rc, d)
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
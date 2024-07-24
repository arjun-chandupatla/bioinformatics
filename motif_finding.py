import itertools
from bio_lib import hamming_distance

def motif_enumeration(dna: list[str], k: int, d: int):
    patternSet = allKmers(k)
    incorrectMotifs = []
    motifSet = []
    for strand in dna:
        for pattern in patternSet:
            if containsWithMismatches(pattern, strand, d) == False:
                incorrectMotifs.append(pattern)
    for pattern in patternSet:
        if pattern not in incorrectMotifs:
            motifSet.append(pattern)
    return motifSet


def allKmers(k: int) -> list[str]:
    patterns = list(itertools.product("ATCG", repeat=k))
    for i in range(len(patterns)):
        element = ""
        for j in patterns[i]:
            element += j
        patterns[i] = element
    return patterns


def containsWithMismatches(seq: str, strand: str, d: int) -> bool:
    k = len(seq)
    for i in range(len(strand) - k + 1):
        if hamming_distance(strand[i:i+k], seq) <= d:
            return True
    return False



dnaSampleSet = "ATTTGGC TGCCTTA CGGTATC GAAAATT".split()
print(motif_enumeration(dnaSampleSet, 3, 1))
#returns adjacency matrix of a series of kmers with identical nodes glued together
def de_bruijn_kmers(kmers: list[str]) -> dict[str, list[str]]:
    patternSet = dict()
    for kmer in kmers:
        p = prefix(kmer)
        s = suffix(kmer)
        if p not in patternSet.keys():
            patternSet[p] = []
        patternSet[p].append(s)
    return patternSet


def prefix(text: str) -> str:
    return text[:-1]


def suffix(text: str) -> str:
    return text[1:]

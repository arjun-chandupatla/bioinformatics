#creates adjacency matrix given a collection of k-mers
import itertools


def overlap_graph(patterns: list[str])-> dict[str, list[str]]:
    patternSet = dict()
    for i in range(len(patterns)):
        kmer = patterns[i]
        for j in range(len(patterns)):
            kmer1 = patterns[j]
            if suffix(kmer) == prefix(kmer1):
                if kmer not in patternSet.keys():
                    patternSet[kmer] = []
                if kmer1 not in patternSet[kmer]:
                    patternSet[kmer].append(kmer1)
    return patternSet


def prefix(kmer: str) -> str:
    return kmer[:-1]


def suffix(kmer: str) -> str:
    return kmer[1:]

import random
from bio_lib import *


def Motifs(prof, dna, k):
    bestMotifs = []
    for i in range(len(dna)):
        row = dna[i]
        bestMotifs.append(profile_most_probable_kmer(row, k, prof))
    return bestMotifs


def randomized_motif_search_(dna, k, t):
    s = [0] * t
    motifs = [""] * t
    for i in range(t):
        seq = dna[i]
        s[i] = random.randint(0, len(dna[0]) - k - 2)
        index = s[i]
        motifs[i] = seq[index:index+k]
    bestMotifs = motifs
    while True:
        Profile = profile_with_pseudocounts(motifs)
        motifs = Motifs(Profile, dna, k)
        if score(motifs) < score(bestMotifs):
            bestMotifs = motifs
        else:
            return bestMotifs


def randomized_motif_search(dna, k, t):
    motifs = []
    minScore = float('inf')
    for i in range(10000):
        motifs.append(randomized_motif_search_(dna, k, t))
    for motifSet in motifs:
        if score(motifSet) < minScore:
            minScore = score(motifSet)
            bestSet = motifSet
    return bestSet


motifList = "CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG TAGTACCGAGACCGAAAGAAGTATACAGGCGT TAGATCAAGTTTCAGGTGCACGTCGGTGAACC AATCCACCAGCTCCACGTGCAATGTTGGCCTA".split()
print(randomized_motif_search(motifList, 8, 5))
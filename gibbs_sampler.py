from bio_lib import *
import random


# to model an n-sided biased die that returns an index i for a given probability Pi
def biased_die(distribution: list[float]):
   
    # normalizing distribution
    total = sum(distribution)
    pDist = []
    for p in distribution:
        pDist.append(p/total)

    # calculating the index i with probability Pi
    num = random.random()
    total = 0
    for i in range(len(pDist)):
        total += pDist[i]
        if num <= total:
            return i
        
#  pseudo randomly generate a kmer inside of seq using a profile array and biased_die
def profile_randomly_generated_kmer(seq: str, k: int, prof: list[dict[str, float]]):
    prodArr = []
    n = len(seq)
    for i in range(n - k + 1):
        win = seq[i:i+k] # window of text starting from i of length k
        prod = 1.0
        for j in range(k):
            prod *= prof[j][win[j]] # calculating probability of kmer using the profile matrix
        prodArr.append(prod)
    index = biased_die(prodArr)
    return seq[index:index+k]


def gibbs_sampler(dna: list[str], k: int, t: int, n: int) -> list[str]:
    s = [0] * t
    motifs = [0] * t

    # randomly select k-mers
    for i in range(t):
        s[i] = random.randint(0, len(dna[0]) - k - 2)
        motifs[i] = dna[i][s[i]:s[i]+k]

    bestMotifs = motifs[:]  # initialize bestMotifs to a copy of motifs
    
    for x in range(n): # iterating n times
        # creating profile matrix from all strings in motifs except for motifs[i]
        i = random.randint(0, t - 1) # i is selected randomly
        newMotifs = []
        for m in motifs: # creating new motif array without motifs[i] to build the profile matrix
            if m != motifs[i]:
                newMotifs.append(m)
        Profile = profile_with_pseudocounts(newMotifs)

        #randomly selecting a kmer with profile and weighted random
        motifs[i] = profile_randomly_generated_kmer(dna[i], k, Profile)

        if score(motifs) < score(bestMotifs):
            bestMotifs = motifs[:] # set bestMotifs to a copy of motifs

    return bestMotifs


motifList = "CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG TAGTACCGAGACCGAAAGAAGTATACAGGCGT TAGATCAAGTTTCAGGTGCACGTCGGTGAACC AATCCACCAGCTCCACGTGCAATGTTGGCCTA".split()
print(gibbs_sampler(motifList, 8, 5, 1000))
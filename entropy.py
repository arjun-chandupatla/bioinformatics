import numpy
from bio_lib import profile


def lPrint(l):
    for r in l:
        for c in r:
            print(c, end=" ")
        print()


def count(motifs):
    tMotifs = []
    for column in numpy.transpose(motifs):
        tMotifs.append(list(column))
    #lPrint(tMotifs)
    k = len(tMotifs[0])
    A = [0] * k
    C = [0] * k
    G = [0] * k
    T = [0] * k
    for i in range(k):
        for r in tMotifs:
            if r[i] == "A":
                A[i] += 1
            elif r[i] == "C":
                C[i] += 1
            elif r[i] == "G":
                G[i] += 1
            elif r[i] == "T":
                T[i] += 1
    return [A, C, G, T]
    

def profile(motifs):
    n = len(motifs)
    k = len(motifs[0])
    
    countArray = count(motifs)

    for r in range(len(countArray)): # always will be 4
        for c in range(k):
            countArray[r][c] /= n

    countDict = []
    countArray = numpy.transpose(countArray)
    for r in countArray:
        A, C, G, T, = float(r[0]), float(r[1]), float(r[2]), float(r[3])
        tempDict = {
            'A': A,
            'C': C,
            'G': G,
            'T': T
        }
        countDict.append(tempDict)
    return countDict


def profile_with_pseudocounts(motifs):
    n = 2 * len(motifs)
    k = len(motifs[0])
    
    countArray = count(motifs)

    for r in range(len(countArray)): # always will be 4
        for c in range(k):
            countArray[r][c] += 1
            countArray[r][c] /= n

    countDict = []
    countArray = numpy.transpose(countArray)
    for r in countArray:
        A, C, G, T, = float(r[0]), float(r[1]), float(r[2]), float(r[3])
        tempDict = {
            'A': A,
            'C': C,
            'G': G,
            'T': T
        }
        countDict.append(tempDict)
    return countDict



def entropy(motifs):
    prof = numpy.transpose(profile(motifs))
    entArray = [0] * len(prof)
    for c in range(len(prof)):
        for i in prof[c]:
            if i != 0:
                entArray[c] -= (i * numpy.log2(i))
    return sum(entArray)


motifList = "TCGGGGGTTTTT CCGGTGACTTAC ACGGGGATTTTC TTGGGGACTTTT AAGGGGACTTCC TTGGGGACTTCC TCGGGGATTCAT TCGGGGATTCCT TAGGGGAACTAC TCGGGTATAACC".split()
print(profile(motifList))
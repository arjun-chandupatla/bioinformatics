import numpy

def count(motifs) -> int:
    k = len(motifs[0])
    A = [0] * k
    C = [0] * k
    G = [0] * k
    T = [0] * k
    for i in range(len(motifs)):
        for element in motifs[i]:
            if element == 'A':
                A[i] += 1
            if element == 'C':
                C[i] += 1
            if element == 'G':
                G[i] += 1
            if element == 'T':
                T[i] += 1
    return [A, C, G, T]


def profile(motifs):
    countArray = count(motifs)
    for r in range(len(countArray)):
        for c in range(len(countArray[r])):
            countArray[r][c] /= len(countArray)
    return countArray


def mostCommonChar(charAtIndex: list[str]) -> str:
    A = 0
    T = 0
    C = 0
    G = 0
    for c in charAtIndex:
        if c == 'A':
            A += 1
        if c == 'C':
            C += 1
        if c == 'G':
            G += 1
        if c == 'T':
            T += 1
    maxBase = max(A, T, C, G)
    if maxBase == A:
        return "A"
    elif maxBase == T:
        return "T"
    elif maxBase == C:
        return "C"
    elif maxBase == G:
        return "G"
    return "fail"



def consensus(motifs):
    consensusArray = []
    for c in len(motifs[0]):
        tempArray = []
        for r in len(motifs):
            tempArray.append(motifs[r][c])
        consensusArray.append(mostCommonChar(tempArray))
    return consensusArray

    
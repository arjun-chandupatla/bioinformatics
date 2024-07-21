def minimum_skew(genome: str) -> list[int]:
    skewTable = []
    minIndices = []
    i = 0
    for j in range(len(genome)):
        if genome[j] == 'C':
            i -= 1
        elif genome[j] == 'G':
            i += 1
        skewTable.append(i)
    minSkewValue = min(skewTable)
    for k in range(len(skewTable)):
        if skewTable[k] == minSkewValue:
            minIndices.append(k + 1)
    return minIndices

genome = "TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"
print(minimum_skew(genome))
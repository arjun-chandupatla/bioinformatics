def patternMatch(pattern: str, genome: str):
    n = len(genome)
    k = len(pattern)
    patternIndices = []
    for i in range(n - k + 1):
        if genome[i:i+k] == pattern:
            patternIndices.append(i)
    for i in patternIndices:
        print(i, end = " ")
    return patternIndices

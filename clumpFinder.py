from frequentWords import *

def findClump(genome: str, k: int, l: int, t: int) -> list[str]:
    kmers = []
    for i in range(len(genome) - l + 1):
        window = genome[i:i+l]
        freqMap = frequencyTable(window, k)
        for key in freqMap.keys():
            if freqMap[key] >= t and key not in kmers:
                kmers.append(key)
    return kmers

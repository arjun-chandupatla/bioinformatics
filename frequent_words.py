from maxmap import maxMap
import sys

def frequencyTable(text: str, k: int):
    freqMap = {}
    for i in range(len(text) - k + 1):
        subText = text[i:i+k]
        if subText in freqMap.keys():
            freqMap[subText] += 1
        else:
            freqMap[subText] = 1
    return freqMap


def frequent_words(text: str, k: int):    
    freqMap = frequencyTable(text, k)
    print(freqMap)
    max = maxMap(freqMap)
    mostFreqPattern = []
    for p in freqMap.keys():
        if freqMap[p] == max:
            mostFreqPattern.append(p)
    return mostFreqPattern


def frequent_words_with_mismatches(text: str, k: int, d: int) -> list[str]:
    patterns = []
    freqMap = {}
    n = len(text)
    for i in range(n - k + 1):
        pattern = text[i:i+k]
        neighborhood = neighbors(pattern)
        for neighbor in neighborhood:
            if neighbor in freqMap:
                freqMap[neighbor] += 1
            else:
                freqMap[neighbor] = 1
    m = maxMap(freqMap)
    for p in freqMap.keys():
        if freqMap[p] == m:
            patterns.append(p)
    return patterns

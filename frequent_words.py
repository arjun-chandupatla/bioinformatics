from maxmap import maxMap
from neighbors import neighbors
from reverse_complement import reverseComplement
import sys

# construct a dictionary that takes in a pattern and returns the number of times it occurs in a string
def frequencyTable(text: str, k: int):
    freqMap = {}
    for i in range(len(text) - k + 1):
        subText = text[i:i+k]
        if subText in freqMap.keys():
            freqMap[subText] += 1
        else:
            freqMap[subText] = 1
    return freqMap

# returns the most frequent kmer in text
def frequent_words(text: str, k: int):    
    freqMap = frequencyTable(text, k)
    print(freqMap)
    max = maxMap(freqMap)
    mostFreqPattern = []
    for p in freqMap.keys():
        if freqMap[p] == max:
            mostFreqPattern.append(p)
    return mostFreqPattern

# returns the most frequent kmer in text, allowing for d mismatches
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

# returns the most frequent kmer(s) that occurs in text with up to d mismatches
# also allows for its reverse complement to occur in text with d mismatches
def frequent_words_mismatches_reverse_complement(text: str, k: int, d: int) -> list[str]:
    patterns = []
    freqMap = {}
    n = len(text)
    for i in range(n - k + 1):
        pattern = text[i:i+k]
        rc = reverseComplement(pattern)
        neighborhood = neighbors(pattern) + neighbors(rc)
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

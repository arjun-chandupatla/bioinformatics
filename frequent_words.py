from bio_lib import maxMap, frequencyTable
import sys

def freqWords(text: str, k: int):    
    freqMap = frequencyTable(text, k)
    print(freqMap)
    max = maxMap(freqMap)
    mostFreqPattern = []
    for p in freqMap.keys():
        if freqMap[p] == max:
            mostFreqPattern.append(p)
    return mostFreqPattern

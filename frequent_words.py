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


def freqWords(text: str, k: int):    
    freqMap = frequencyTable(text, k)
    print(freqMap)
    max = maxMap(freqMap)
    mostFreqPattern = []
    for p in freqMap.keys():
        if freqMap[p] == max:
            mostFreqPattern.append(p)
    return mostFreqPattern
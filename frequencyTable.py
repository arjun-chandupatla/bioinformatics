def frequencyTable(text: str, k: int):
    freqMap = {}
    for i in range(len(text) - k + 1):
        subText = text[i:i+k]
        if subText in freqMap.keys():
            freqMap[subText] += 1
        else:
            freqMap[subText] = 1
    return freqMap


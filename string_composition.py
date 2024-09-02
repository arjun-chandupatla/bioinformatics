#splits a string into a sorted list of substrings of length k
def kmers_composition(text:str, k:int) -> list[str]:
    n = len(text)
    kmers = []

    if n == k:
        return [text]
    
    for x in range(n - k + 1):
        kmers.append(text[x:x+k])
    kmers.sort()
    return kmers

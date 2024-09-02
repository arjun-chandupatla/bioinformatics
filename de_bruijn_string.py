#returns the adjacency matrix of a string with identical nodes glued together
def de_bruijn_string(text: str, k: int) -> dict[str, list[str]]:
    n = len(text)
    patternSet = dict()
    for i in range(n - k +1):
        win = text[i:i+k]
        if prefix(win) not in patternSet.keys():
            patternSet[prefix(win)] = []
        patternSet[prefix(win)].append(suffix(win))
    return patternSet

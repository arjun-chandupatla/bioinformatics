from hamming_distance import hamming_distance

def neighbors(pattern: str, d: int):
    nucleotides = ['A', 'C', 'G', 'T']
    if d == 0:
        return [pattern]
    if len(pattern) == 1:
        return nucleotides
    neighborhood = []
    suffixNeighbors = neighbors(suffix(pattern), d)
    for text in suffixNeighbors:
        if hamming_distance(pattern[1:], text) < d:
            for x in nucleotides:
                neighborhood.append(x + text)
        else:
            neighborhood.append(pattern[0] + text)
    return neighborhood

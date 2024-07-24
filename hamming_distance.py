def hamming_distance(p: str, q: str) -> int:
    if len(p) != len(q):
        raise Exception("Strings must be the same length")
    dist = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            dist += 1
    return dist

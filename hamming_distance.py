def hamming_distance(p: str, q: str) -> int:
    dist = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            dist += 1
    return dist


print(hamming_distance("AAAAA", "TTTTA"))
from _collections_abc import Iterable

def Pr(n: int, pattern: str) -> float:
    perms = genbin(n)
    num = 0
    den = len(perms)
    for p in perms:
        if pattern in p:
            num += 1
    return float(num)/float(den)


def genbin(n):
    length = pow(2, n)
    binSet = list(range(length))
    for i in range(len(binSet)):
        binSet[i] = f'{binSet[i]:025b}'
    return binSet



print(Pr(25, '01'))
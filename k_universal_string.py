#generates a universal binary string of length k
import copy

def k_universal_string(k: int):
    kBin = binStrings(k)
    binDict = dict()

    for b in kBin:
        binDict[prefix(b)] = []

    for b in kBin:
        binDict[prefix(b)].append(suffix(b))

    path = eulerian_cycle(binDict)

    return genome_path(path)


def binStrings(k: int) -> list[str]:
    patterns = list(itertools.product("01", repeat=k))
    for i in range(len(patterns)):
        element = ""
        for j in patterns[i]:
            element += j
        patterns[i] = element
    return patterns


  def eulerian_cycle(graph: dict[int, list[int]]) -> list[int]:
    
    unused_edges = copy.deepcopy(graph)

    pos = list(graph.keys())[0]
    path = get_cycle(pos, unused_edges)

    while True: #repeat until Eulerian cycle is found
        
        if isEmpty(unused_edges):   #if Eulerian cycle is found, return it
            return path
        
        for index in range(len(path)):  #get a position p with unused edges
            p = path[index]
            if unused_edges[p] != []:
                pos = p
                i = index
                break
        
        path = path[:i] + get_cycle(pos, unused_edges) + path[i+1:]    #insert new cycle into path


def get_cycle(pos: int, graph: dict[int, list[int]]) -> list[int]:
    cycle = [pos]
    while graph[pos] != []:
        nextPos = graph[pos][0]
        cycle.append(nextPos)
        graph[pos].remove(nextPos)
        pos = nextPos
    return cycle


def isEmpty(d: dict) -> bool:
    for k in d.keys():
        if d[k]:
            return False
    return True


def genome_path(path: list[str]) -> str:
    genome = path[0]
    for i in range(1, len(path)):
        genome += path[i][-1]
    return genome


def kmers_composition(text:str, k:int) -> list[str]:
    n = len(text)
    kmers = []

    if n == k:
        return [text]
    
    for x in range(n - k + 1):
        kmers.append(text[x:x+k])
    kmers.sort()
    return kmers

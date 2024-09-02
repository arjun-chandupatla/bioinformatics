#finds an Eulerian path generated from the de Bruijn graph generated from a set of k-mers
import copy


def string_reconstruction(patterns: list[str], k: int) -> str:
    dB = de_bruijn_kmers(patterns)
    path = eulerian_path(dB)
    text = genome_path(path)
    return text


def de_bruijn_kmers(kmers: list[str]) -> dict[str, list[str]]:
    patternSet = dict()
    for kmer in kmers:
        p = prefix(kmer)
        s = suffix(kmer)
        if p not in patternSet.keys():
            patternSet[p] = []
        patternSet[p].append(s)
    return patternSet


def eulerian_path(graph: dict[int, list[int]]) -> list[int]:
    
    unused_edges = copy.deepcopy(graph)

    pos = get_start_pos(unused_edges)
    path = get_path(pos, unused_edges)

    while True: #repeat until Eulerian cycle is found
        
        if isEmpty(unused_edges):   #if Eulerian cycle is found, return it
            return path
        
        try:
            for index in range(len(path)):  #get a position p with unused edges
                p = path[index]
                print(p)
                if unused_edges[p] != []:
                    pos = p
                    i = index
                    break
            path = path[:i] + get_path(pos, unused_edges) + path[i+1:]    #insert new cycle into path
        except KeyError:
            return path
        

def get_start_pos(graph: dict[int, list[int]]):
    in_d  = dict()
    out_d = dict()
    for k in graph.keys():
        out_d[k] = len(graph[k])
        in_d[k]  = 0

    for k in graph.keys():
        for v in graph[k]:
            try:
                in_d[v] += 1
            except KeyError:
                in_d[v]  = 1
                out_d[v] = 0    
    
    net = dict()
    max = float('-inf')
    max_i = -1
    for k in graph.keys():
        net[k] = out_d[k] - in_d[k]
    for k in net.keys():
        if net[k] > max:
            max = net[k]
            max_i = k
    
    return max_i


def get_path(pos: int, graph: dict[int, list[int]]) -> list[int]:
    cycle = [pos]
    try:
        while graph[pos] != []:
            nextPos = graph[pos][0]
            cycle.append(nextPos)
            graph[pos].remove(nextPos)
            pos = nextPos
    except KeyError:
        return cycle
    return cycle


def genome_path(path: list[str]) -> str:
    genome = path[0]
    for i in range(1, len(path)):
        genome += path[i][-1]
    return genome


def isEmpty(d: dict) -> bool:
    for k in d.keys():
        if d[k]:
            return False
    return True


def prefix(text: str) -> str:
    return text[:-1]


def suffix(text: str) -> str:
    return text[1:]

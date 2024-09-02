#given the adjacency list of a directed graph with an Eulerian path, returns an Eulerian path
import copy


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
                if unused_edges[p] != []:
                    pos = p
                    i = index
                    break
            path = path[:i] + get_path(pos, unused_edges) + path[i+1:]    #insert new cycle into path
        except KeyError:
            return path


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


def isEmpty(d: dict) -> bool:
    for k in d.keys():
        if d[k]:
            return False
    return True

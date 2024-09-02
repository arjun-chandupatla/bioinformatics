#given the adjacency list of an Eulerian directed graph, returns an Eulerian cycle in that graph
import copy


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

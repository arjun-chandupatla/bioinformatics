def maxMap(map):
    mapList = map.values()
    max = -1
    for i in mapList:
        if i > max:
            max = i
    return max
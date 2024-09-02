#puts a series of strings with overlap together
def genome_path(path: list[str]) -> str:
    genome = path[0]
    for i in range(1, len(path)):
        genome += path[i][-1]
    return genome

from collections import defaultdict


def is_valid_path(n, edges, source, destination):
    graphs_path = defaultdict(set)
    for i, j in edges:
        graphs_path[i].add(j)
        graphs_path[j].add(i)
    paths_visited = {source}
    paths_to_visit = [source]
    while paths_to_visit:
        visit = paths_to_visit.pop()
        if visit == destination:
            return True
        for each in graphs_path[visit]:
            if each not in paths_visited:
                paths_visited.add(each)
                paths_to_visit.append(each)
    return False


# test below
print(is_valid_path(3, [[0, 1], [1, 2], [2, 0]], 0, 2))
print(is_valid_path(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5))
print(is_valid_path(10, [[4, 3], [1, 4], [4, 8], [1, 7], [
      6, 4], [4, 2], [7, 4], [4, 0], [0, 9], [5, 4]], 5, 9))
print(is_valid_path(10, [[2, 6], [4, 7], [1, 2], [3, 5], [
      7, 9], [6, 4], [9, 8], [0, 1], [3, 0]], 3, 5))

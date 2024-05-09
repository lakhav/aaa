from itertools import permutations
from sys import maxsize


def travellingSalesmanProblem(graph, s):

    vertex = []
    V = len(graph)

    for i in range(V):
        if i != s:
            vertex.append(i)

    minimum_path = maxsize
    min_path = None
    nextPermutations = permutations(vertex)

    for i in nextPermutations:
        current_path = 0
        k = s
        for j in i:
            current_path = current_path + graph[k][j]
            k = j

        current_path = current_path + graph[k][s]
        if current_path < minimum_path:
            minimum_path = current_path
            min_path = [s] + list(i) + [s]  # Path from start to end

    return minimum_path, min_path


graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
s = 0

min_cost, path = travellingSalesmanProblem(graph, s)
print(f"Minimum cost: {min_cost}")
print("Path:", path)

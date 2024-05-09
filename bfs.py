from collections import deque


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}


def bfs(graph, node):

  visited =[]
  queue =[]
  visited.append(node)
  queue.append(node)

  while queue:
    m=queue.pop(0)
    print(m ,end = " ")

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)




print("BFS Traversal:")
bfs(graph, 'A')


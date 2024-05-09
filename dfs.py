
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}




def dfs(graph,node):
  stack =[]
  visited =[]
  stack.append(node)

  while stack:
    node = stack.pop()
    if node is not None and node not in visited:
      visited.append(node)

      for neighbour in reversed(graph[node]):
          if neighbour not in visited:
              stack.append(neighbour)

  print(visited)



print("\nDFS Traversal:")
dfs(graph, 'A')
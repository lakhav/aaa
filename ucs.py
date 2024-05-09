def ucs(graph, start, goal):
    OPEN = [(0, start)]
    CLOSED = set()
    g = {start: 0}
    path = {start: [start]}

    while OPEN:
        OPEN.sort()
        cost, node = OPEN.pop(0)
        CLOSED.add(node)

        if node == goal:
            return path[node]

        for neighbor, edge_cost in graph[node].items():
            new_cost = cost + edge_cost
            if neighbor not in OPEN and neighbor not in CLOSED:
                g[neighbor] = new_cost
                path[neighbor] = path[node] + [neighbor]
                OPEN.append((new_cost, neighbor))
            elif neighbor in OPEN:
                if new_cost < g[neighbor]:
                    g[neighbor] = new_cost
                    path[neighbor] = path[node] + [neighbor]
            elif neighbor in CLOSED:
                if new_cost < g[neighbor]:
                    g[neighbor] = new_cost
                    path[neighbor] = path[node] + [neighbor]
                    CLOSED.remove(neighbor)
                    OPEN.append((new_cost, neighbor))

    return []


graph = {
    'S': {'A': 1, 'B': 4},
    'A': {'S': 1, 'D': 2, 'G': 5},
    'B': {'S': 4, 'E': 3},
    'D': {'A': 2},
    'E': {'B': 3, 'F': 2},
    'F': {'E': 2, 'G': 1},
    'G': {'A': 5, 'F': 1}
}


start_node = 'S'
goal_node = 'G'
result = ucs(graph, start_node, goal_node)

if result:
    print(f"The path from node '{start_node}' to node '{goal_node}' is: {result}")
else:
    print(f"No path found from node '{start_node}' to node '{goal_node}'")

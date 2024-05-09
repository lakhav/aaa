from collections import deque

def move(state, direction):
    state = list(state)
    zero_index = state.index(0)
    if direction == 'left':
        if zero_index % 3 > 0:
            state[zero_index], state[zero_index - 1] = state[zero_index - 1], state[zero_index]
            return tuple(state)
    elif direction == 'right':
        if zero_index % 3 < 2:
            state[zero_index], state[zero_index + 1] = state[zero_index + 1], state[zero_index]
            return tuple(state)
    elif direction == 'up':
        if zero_index >= 3:
            state[zero_index], state[zero_index - 3] = state[zero_index - 3], state[zero_index]
            return tuple(state)
    elif direction == 'down':
        if zero_index < 6:
            state[zero_index], state[zero_index + 3] = state[zero_index + 3], state[zero_index]
            return tuple(state)
    return None

def bfs(start_state, goal_state):
    queue = deque([(start_state, [])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()
        if current_state == goal_state:
            return path
        if current_state in visited:
            continue
        visited.add(current_state)
        for direction in ['left', 'right', 'up', 'down']:
            new_state = move(current_state, direction)
            if new_state is not None:
                queue.append((new_state, path + [direction]))
    return None



def print_matrix(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])


# Example initial and goal states
start_state = (1, 2, 3, 0, 4, 5, 6, 7, 8)
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Find the path using BFS
path = bfs(start_state, goal_state)

# Print the path
if path:
    print("Path found:", path)
    if path:
      current_state = start_state
      print("Initial State:")
      print_matrix(start_state)
      print("Path to Goal:")
      for direction in path:
          print_matrix(current_state)
          print(f"Move {direction}:")
          current_state = move(current_state, direction)
      print_matrix(goal_state)
else:
    print("No path found.")

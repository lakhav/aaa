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

def dfs(start_state, goal_state):
    stack = [(start_state, [])]
    visited = set()

    while stack:
        current_state, path = stack.pop()
        if current_state == goal_state:
            return path
        if current_state in visited:
            continue
        visited.add(current_state)
        for direction in ['left', 'right', 'up', 'down']:
            new_state = move(current_state, direction)
            if new_state is not None:
                stack.append((new_state, path + [direction]))
    return None


start_state = (1, 2, 3, 0, 4, 5, 6, 7, 8)

goal_state = (1, 2, 3, 4, 0, 5, 6, 7, 8)


def print_matrix(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])

# Find the path using DFS
path = dfs(start_state, goal_state)

# Print the path
if path:
    print("Path found:", path)

else:
    print("No path found.")

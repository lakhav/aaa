from collections import deque

Initial = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
Goal = [[2, 8, 1], [0, 4, 3], [7, 6, 5]]

print("Initial state:")
print(Initial)
print("Goal state:")
print(Goal)

def is_goal(state):
    return state == Goal

def move_blank(state, direction):
    new_state = [row.copy() for row in state]
    for i in range(3):
        for j in range(3):
            if new_state[i][j] == 0:
                if direction == 'L' and j > 0:
                    new_state[i][j-1], new_state[i][j] = new_state[i][j], new_state[i][j-1]
                elif direction == 'R' and j < 2:
                    new_state[i][j+1], new_state[i][j] = new_state[i][j], new_state[i][j+1]
                elif direction == 'U' and i > 0:
                    new_state[i-1][j], new_state[i][j] = new_state[i][j], new_state[i-1][j]
                elif direction == 'D' and i < 2:
                    new_state[i+1][j], new_state[i][j] = new_state[i][j], new_state[i+1][j]
    return new_state

def print_state(state):
    for row in state:
        print(row)

def bfs(initial_state):
    visited = set()
    queue = deque([(initial_state, [])])

    while queue:
        state, path = queue.popleft()
        state_str = str(state)

        if state_str in visited:
            continue

        visited.add(state_str)

        if is_goal(state):
            return path

        for direction in ['L', 'R', 'U', 'D']:
            new_state = move_blank(state, direction)
            queue.append((new_state, path + [direction]))

    return None

result_path = bfs(Initial)

print("Result:")
if result_path:
    print(result_path)
else:
    print("No solution found.")
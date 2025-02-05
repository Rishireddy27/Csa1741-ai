from collections import deque

def is_valid_state(state, a, b):
    return 0 <= state[0] <= a and 0 <= state[1] <= b

def get_next_states(current_state, a, b):
    (x, y) = current_state
    return [
        (a, y),       # Fill Jug 1
        (x, b),       # Fill Jug 2
        (0, y),       # Empty Jug 1
        (x, 0),       # Empty Jug 2
        (min(x + y, a), x + y - min(x + y, a)),  # Pour Jug 2 -> Jug 1
        (x + y - min(x + y, b), min(x + y, b))   # Pour Jug 1 -> Jug 2
    ]

def bfs(a, b, target):
    start_state = (0, 0)
    queue = deque([(start_state, [])])
    visited = set()
    visited.add(start_state)
    
    while queue:
        (current_state, path) = queue.popleft()
        
        if current_state[0] == target or current_state[1] == target:
            return path + [current_state]
        
        for next_state in get_next_states(current_state, a, b):
            if is_valid_state(next_state, a, b) and next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [current_state]))
    
    return None

def water_jug_problem(a, b, target):
    solution = bfs(a, b, target)
    if solution:
        for state in solution:
            print(state)
    else:
        print("No solution found")

# Example usage
a = 4  # Capacity of Jug 1
b = 3  # Capacity of Jug 2
target = 2  # Target amount of water

water_jug_problem(a, b, target)

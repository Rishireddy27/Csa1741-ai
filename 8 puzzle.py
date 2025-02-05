import heapq

class PuzzleState:
    def __init__(self, board, moves=0, previous=None):
        self.board = board
        self.moves = moves
        self.previous = previous
        self.blank_pos = self.find_blank_pos()
    
    def find_blank_pos(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return (i, j)
    
    def is_goal(self):
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        return self.board == goal
    
    def get_neighbors(self):
        neighbors = []
        i, j = self.blank_pos
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < 3 and 0 <= nj < 3:
                new_board = [row[:] for row in self.board]
                new_board[i][j], new_board[ni][nj] = new_board[ni][nj], new_board[i][j]
                neighbors.append(PuzzleState(new_board, self.moves + 1, self))
        
        return neighbors
    
    def __lt__(self, other):
        return self.moves < other.moves

def manhattan_distance(board):
    distance = 0
    goal_positions = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                      4: (1, 0), 5: (1, 1), 6: (1, 2),
                      7: (2, 0), 8: (2, 1), 0: (2, 2)}
    
    for i in range(3):
        for j in range(3):
            if board[i][j] != 0:
                goal_i, goal_j = goal_positions[board[i][j]]
                distance += abs(i - goal_i) + abs(j - goal_j)
    
    return distance

def a_star_search(initial_board):
    initial_state = PuzzleState(initial_board)
    frontier = []
    heapq.heappush(frontier, (manhattan_distance(initial_board), initial_state))
    explored = set()
    
    while frontier:
        _, current_state = heapq.heappop(frontier)
        
        if current_state.is_goal():
            return current_state
        
        explored.add(tuple(tuple(row) for row in current_state.board))
        
        for neighbor in current_state.get_neighbors():
            if tuple(tuple(row) for row in neighbor.board) not in explored:
                cost = neighbor.moves + manhattan_distance(neighbor.board)
                heapq.heappush(frontier, (cost, neighbor))
    
    return None

def print_solution(solution):
    path = []
    state = solution
    while state:
        path.append(state.board)
        state = state.previous
    
    path.reverse()
    for step in path:
        for row in step:
            print(row)
        print()

# Example usage
initial_board = [
    [1, 2, 3],
    [4, 0, 5],
    [7, 8, 6]
]

solution = a_star_search(initial_board)
if solution:
    print("Solution found!")
    print_solution(solution)
else:
    print("No solution found.")

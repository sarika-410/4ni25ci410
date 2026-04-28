import heapq
import copy

GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Directions for movement
MOVES = {
    "Up": (-1, 0),
    "Down": (1, 0),
    "Left": (0, -1),
    "Right": (0, 1)
}

class Puzzle:
    def __init__(self, state, parent=None, move=None, depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.zero_pos = self.find_zero()

    def find_zero(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

    def is_goal(self):
        return self.state == GOAL_STATE

    def display(self):
        for row in self.state:
            print(row)
        print()

    def generate_successors(self):
        successors = []
        x, y = self.zero_pos

        for move, (dx, dy) in MOVES.items():
            nx, ny = x + dx, y + dy

            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = copy.deepcopy(self.state)
                
                # Swap blank with adjacent tile
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]

                successor = Puzzle(
                    new_state,
                    parent=self,
                    move=f"Move {new_state[x][y]} {move}",
                    depth=self.depth + 1
                )
                successors.append(successor)

        return successors

    def __lt__(self, other):
        return False  # Required for heapq


# Manhattan Distance Heuristic
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x = (value - 1) // 3
                goal_y = (value - 1) % 3
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance


def a_star(initial_state):
    start = Puzzle(initial_state)
    open_list = []
    closed_set = set()

    heapq.heappush(open_list, (manhattan_distance(start.state), start))

    while open_list:
        _, current = heapq.heappop(open_list)

        # Convert state to tuple for hashing
        state_tuple = tuple(tuple(row) for row in current.state)

        if state_tuple in closed_set:
            continue

        closed_set.add(state_tuple)

        if current.is_goal():
            return current

        for successor in current.generate_successors():
            heapq.heappush(
                open_list,
                (successor.depth + manhattan_distance(successor.state), successor)
            )

    return None


def print_solution(solution):
    path = []
    while solution:
        path.append(solution)
        solution = solution.parent

    path.reverse()

    print("Solution Steps:\n")
    for i, step in enumerate(path):
        print(f"Step {i}:")
        step.display()
        if step.move:
            print(step.move)
        print("------------------")


# Initial State
initial_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

# Run A*
solution = a_star(initial_state)

# Print result
if solution:
    print_solution(solution)
else:
    print("No solution found.")
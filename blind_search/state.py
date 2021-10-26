def traceback(state):
    """
    Traceback function to print the path of the current state.
    """
    moves = []

    while state.parent:
        moves.append(state.action)
        state = state.parent

    moves.reverse()
    return ", ".join(moves)

def traceback_board(state):
    """
    Traceback function to print the path of the current state.
    """
    if state is None:
        return
    
    traceback_board(state.parent)
    
    for i in range(state.size):
        for j in range(state.size):
            print(state.state[i * state.size + j], end=" ")
        print()
    print()

"""

"""
class State:

    def __init__(self, state, goal, parent=None, cost=0, depth=0, action="NoOp"):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.depth = depth 

        self.size = int(len(state)**(1/2))
        self.key = "".join(str(x) for x in state)

        self.action = action
        self._goal = goal


    def __eq__(self, other):
        return self.key == other.key


    def __str__(self):
        return traceback(self)


    def index(self, i, j):
        return self.state[i * self.size + j]


    def table(self, index):

        i = index // self.size

        return i, index - i * self.size
    
    
    def get_neighbors(self):
        neighbors = []

        index = self.state.index(0)
        i, j  = self.table(index)

        possible_moves = {"up": (1, 0), "down": (-1, 0), "right": (0, -1), "left": (0, +1)}

        for key, move in possible_moves.items():
            i_new, j_new = i + move[0], j + move[1]
    
            if 0 <= i_new < self.size and 0 <= j_new < self.size:
                new_state = self.state[:]
                new_state[index], new_state[i_new * self.size + j_new] = new_state[i_new * self.size + j_new], new_state[index]
                neighbors.append(State(new_state, self._goal, self, self.cost + 1, self.depth + 1, key))
        
        return neighbors
    
    def goal(self):
        return self.key == self._goal
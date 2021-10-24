from state import State, traceback_board
from collections import deque


def bfs(initial_state):

    # Performance
    max_depth       = 0
    max_frontier    = 0
    scanned         = 0

    # Create a queue for the states to be explored
    queue = deque()
    explored = set()

    # Add the initial state to the queue
    queue.append(initial_state)

    # While the queue is not empty
    while queue:

        # Remove the first state from the queue
        current_state = queue.popleft()
        explored.add(current_state.key)

        # If the current state is the goal state
        if current_state.goal():
            return {"state": current_state, "max_depth": max_depth, "max_frontier": max_frontier, "final_frontier": len(queue), "scanned": scanned}


        # Add the current state's children to the queue
        neighbors = current_state.get_neighbors()
        for neighbor in neighbors:
            if neighbor.key not in explored:
                scanned += 1
                queue.append(neighbor)

                if neighbor.depth > max_depth:
                    max_depth = neighbor.depth

        if len(queue) > max_frontier:
            max_frontier = len(queue)

    # If the queue is empty and the goal state has not been found
    return {"state": None, "max_depth": max_depth, "max_frontier": max_frontier, "final_frontier": len(queue), "scanned": scanned}

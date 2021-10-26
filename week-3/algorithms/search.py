from state import State, traceback_board
from collections import deque

def bfs(initial_state):

    # Performance
    max_depth       = 0
    max_frontier    = 0

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
            return {"state": current_state, "max_depth": max_depth, "max_frontier": max_frontier, "final_frontier": len(queue), "scanned": len(explored)}


        # Add the current state's children to the queue
        neighbors = current_state.get_neighbors()
        for neighbor in neighbors:
            if neighbor.key not in explored:
                explored.add(neighbor.key)
                queue.append(neighbor)

                if neighbor.depth > max_depth:
                    max_depth = neighbor.depth

        if len(queue) > max_frontier:
            max_frontier = len(queue)

    # If the queue is empty and the goal state has not been found
    return {"state": None, "max_depth": max_depth, "max_frontier": max_frontier, "final_frontier": len(queue), "scanned": len(explored)}



def dfs(initial_state, limit=-1):
    
    # Performance
    max_depth       = 0
    max_frontier    = 0

    # Create a stack for the states to be explored
    stack = deque() # Stack is LIFO
    explored = set()

    # Add the initial state to the stack
    stack.append(initial_state)

    # While the stack is not empty
    while stack:

        # Remove the first state from the stack
        current_state = stack.pop()
        explored.add(current_state.key)

        # If the current state is the goal state
        if current_state.goal():
            return {"state": current_state, "max_depth": max_depth, "max_frontier": max_frontier, "final_frontier": len(stack), "scanned": len(explored)}

        if limit > 0 and current_state.cost > limit:
            return False

        # Add the current state's children to the stack
        neighbors = current_state.get_neighbors()[::-1]
        for neighbor in neighbors:
            if neighbor.key not in explored:
                scanned += 1
                explored.add(neighbor.key)
                stack.append(neighbor)

                if neighbor.depth > max_depth:
                    max_depth = neighbor.depth
                
                if limit > 0 and neighbor.cost > limit:
                    return False

        if len(stack) > max_frontier:
            max_frontier = len(stack)

    # If the stack is empty and the goal state has not been found
    return {"state": None, "max_depth": max_depth, "max_frontier": max_frontier, "final_frontier": len(stack), "scanned": len(explored)}


def idfs(initial_state):
    minimum = 10000
    maximum = 100000
    for i in range(minimum, maximum, 10000):
        answer = dfs(initial_state, i)

        if type(answer) is bool:
            continue
            
        return answer
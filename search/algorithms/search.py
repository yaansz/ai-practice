from state import State, traceback_board
from collections import deque
from heapq import heapify, heappush, heappop 

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

        # Add the current state's children to the stack
        neighbors = current_state.get_neighbors()[::-1]
        for neighbor in neighbors:
            if neighbor.key not in explored:

                if neighbor.depth > max_depth:
                    max_depth = neighbor.depth
                
                if (limit < 0) or (limit > 0 and neighbor.depth <= limit):
                    stack.append(neighbor)
                    explored.add(neighbor.key)

        if len(stack) > max_frontier:
            max_frontier = len(stack)

    # If the stack is empty and the goal state has not been found
    return {"state": None, "max_depth": max_depth, "max_frontier": max_frontier, "final_frontier": len(stack), "scanned": len(explored)}


def idfs(initial_state):
    minimum = 0
    maximum = 1000

    final = {"state": None, "max_depth": 0, "max_frontier": 0, "final_frontier": 0, "scanned": 0}

    for i in range(minimum, maximum, 1):
        answer = dfs(initial_state, i)

        final["max_depth"]    = max(final["max_depth"]   , answer["max_depth"]) 
        final["max_frontier"] = max(final["max_frontier"], answer["max_frontier"])
        final["scanned"] += answer["scanned"]

        if answer['state'] is None:
            continue
        
        final["state"] = answer["state"]

        return final
    return final


def astar(initial_state):
    
    # Performance
    max_depth       = 0
    max_frontier    = 0

    # Create a stack for the states to be explored
    hp = [] # Stack is LIFO
    heapify(hp)
    explored = set()

    # Add the initial state to the stack
    heappush(hp, initial_state)
    
    while hp:
    
        # Remove the first state from the stack
        current_state = heappop(hp)
        
        if max_depth < current_state.depth:
            max_depth = current_state.depth
        
        if len(hp) > max_frontier:
            max_frontier = len(hp)
        
        explored.add(current_state.key)
        
        # Current State ??        
        if current_state.goal():
            return {"state": current_state, "max_depth": max_depth, "max_frontier": max_frontier, "final_frontier": len(hp), "scanned": len(explored)}

        # Generating Children        
        children = current_state.get_neighbors(False)
        # Calculating the cost to the specific child
        for child in children:
            child.cost = child.h(child)
        
        # Filtering the children
        children = [child for child in children if child.key not in explored]
        
        # Most Valuable Child
        for child in children:
            heappush(hp, child)
         
    return {"state": None, "max_depth": max_depth, "max_frontier": max_frontier, "final_frontier": len(hp), "scanned": len(explored)}



def greedy(initial_node):
    
    queue = deque([initial_node])
    explored = set()
    
    # Performance
    max_depth       = 0
    max_frontier    = 0

    
    while queue:
        current_state = queue.popleft()
        explored.add(current_state.key)
        
        if current_state.goal():
            return {"state": current_state, "max_depth": max_depth, "max_frontier": max_frontier, "final_frontier": len(queue), "scanned": len(explored)}

        neighbors = sorted(current_state.get_neighbors(False), key = lambda x: x.h(x))
        
        for neighbor in neighbors:
            if neighbor.key not in explored:
                neighbor.cost = neighbor.h(neighbor)
                queue.append(neighbor)
                break
        
        if max_depth < current_state.depth:
            max_depth = current_state.depth
        
        if len(queue) > max_frontier:
            max_frontier = len(queue)
        
    # If the queue is empty and the goal state has not been found
    return {"state": None, "max_depth": max_depth, "max_frontier": max_frontier, "final_frontier": len(queue), "scanned": len(explored)}

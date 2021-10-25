# System
import sys
import time

# External
import resource

# Own
from show import show
from algorithms.search import *
from state import State, traceback_board

def create(input):
    table = [int(i) for i in input.split(',')]
    size = int(len(table)**(1/2))

    return table, size


def main():

    if len(sys.argv) != 3:
        raise AttributeError("You need to provide 2 arguments, 'method' and 'puzzle'")

    method      = sys.argv[1]
    table, size = create(sys.argv[2])
    goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    goal_state = "".join(str(i) for i in goal)
    state = State(table, goal_state)
    
    # Running

    start_time = time.time()
    
    if METHODS.get(method) is None:
        raise AttributeError("Method not found")
    feedback = METHODS[method](State(table, goal_state))
    end_time = time.time()


    # Feedback

    current_state = feedback["state"]
    print(f"Method: {method}")
    print(f"Final State Found: {current_state is not None}")
    if current_state is not None:
        #print(f"Path             :{current_state}")
        print(f"Cost             : {current_state.cost}")
        print(f"Depth            : {current_state.depth}")
    print(f"Max_Depth        : {feedback['max_depth']}")
    print(f"Final_Frontier   : {feedback['final_frontier']}")
    print(f"Max_Frontier     : {feedback['max_frontier']}")
    print(f"Scanned          : {feedback['scanned']}")
    print(f"Elapsed_Time     : {end_time - start_time} s")
    print(f"RAM_Usage        : {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1000.0} kb")


    #traceback_board(current_state) 
    return

METHODS = {'bfs': bfs, 'dfs': dfs, 'idfs': idfs}

if __name__ == '__main__':
    main()
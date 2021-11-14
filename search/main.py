# System
import sys
import time

# External
import resource

# Own
from show import show
from algorithms.search import *
import algorithms.heuristic as hrc

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

    state = State(table, goal)
    
    # Running

    start_time = time.time()
    
    if METHODS.get(method) is None:
        raise AttributeError("Method not found")
    feedback = METHODS[method](State(table, goal, h = HEURISTIC[method]))
    end_time = time.time()


    # Feedback
    f = open("res/" + method + ".txt", "w")

    current_state = feedback["state"]
    f.write(f"Method: {method}\n")
    f.write(f"Final State Found: {current_state is not None}\n")
    if current_state is not None:
        f.write(f"Path             : {current_state}\n")
        f.write(f"Cost             : {current_state.cost}\n")
        f.write(f"Depth            : {current_state.depth}\n")
    f.write(f"Max_Depth        : {feedback['max_depth']}\n")
    f.write(f"Final_Frontier   : {feedback['final_frontier']}\n")
    f.write(f"Max_Frontier     : {feedback['max_frontier']}\n")
    f.write(f"Scanned          : {feedback['scanned']}\n")
    f.write(f"Elapsed_Time     : {end_time - start_time} s\n")
    f.write(f"RAM_Usage        : {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1000.0} kb\n")
    f.close()

    return

METHODS = {'bfs': bfs, 'dfs': dfs, 'idfs': idfs, "astar": astar, "greedy": greedy}
HEURISTIC = {'bfs': hrc.heuristic_default, 'dfs': hrc.heuristic_default, 'idfs': hrc.heuristic_default, "astar": hrc.heuristic_astar, 'greedy': hrc.heuristic_manhattan}


if __name__ == '__main__':
    main()
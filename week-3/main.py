import sys

from show import show
from algorithms.search import *

def create(input):
    table = [int(i) for i in input.split(',')]
    size = int(len(table)**(1/2))

    return table, size


def main():

    if len(sys.argv) != 3:
        raise AttributeError("You need to provide 2 arguments, 'method' and 'puzzle'")

    method      = sys.argv[1]
    table, size = create(sys.argv[2])
    
    # Its Just a placeholder of the final state!!
    final_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    
    show(method, table, size)

    final = bfs(table, ','.join(str(i) for i in final_state), size)

    print(final)

    return


if __name__ == '__main__':
    main()
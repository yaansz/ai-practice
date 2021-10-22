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
    
    show(method, table, size)

    final = bfs(table, ','.join(str(i) for i in [0, 1, 2, 3, 4, 5, 6, 7, 8]), size)
    print(final)

    final = bfs(table, ','.join(str(i) for i in [1, 2, 3, 4, 5, 6, 7, 8, 0]), size)
    print(final)

    final = bfs(table, ','.join(str(i) for i in [1, 2, 3, 8, 0, 4, 7, 6, 5]), size)
    print(final)

    return


if __name__ == '__main__':
    main()
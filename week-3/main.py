import sys

from show import show

"""


"""
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

    return


if __name__ == '__main__':
    main()
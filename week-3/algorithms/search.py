from collections import deque


# auxiliar functions
def get(table, size, i, j):
    return table[i * size + j]

def position(table, size, index):

    i = index // size

    return i, index - i * size


# class methods
class Node:

    def __init__(self, table, size, parent, depth, move):
        self.table = table
        self.size = size
        self.parent = parent
        self.depth = depth
        self.move = move


    def show(self):
        return ','.join(str(i) for i in self.table)


    def __eq__(self, other):

        try:
            for i in range(len(self.table)):
                if self.table[i] != other.table[i]:
                    return False
            return True
        
        except:
            return False
    
    def __str__(self):

        s = ""
        for i in range(self.size):
            for j in range(self.size):
                s += str(get(self.table, self.size, i, j)) + " "
            s += "\n"
        
        return s


def children_generator(node):

    children = []
    moves = {'up': (0, 1), 'down': (0, -1), 'left': (-1, 0), 'right': (1, 0)}
    
    # position of 0
    index = node.table.index(0)
    i, j = position(node.table, node.size, index)

    for key, value in moves.items():
        i_t = i + value[0] # x
        j_t = j + value[1] # y

        if (i_t >= 0 and i_t < node.size) and (j_t >= 0 and j_t < node.size): 

            new_table = node.table.copy()
            
            p_t = i_t * node.size + j_t # temp position
            new_table[index], new_table[p_t] = new_table[p_t], new_table[index]
            
            # def __init__(self, table, size, parent, depth, move):
            children.append(Node(new_table, node.size, node, node.depth + 1, key))

    return children


def bfs(initial_table, final_state, size):
    initial = Node(initial_table, size, None, 0, "NoOp")

    queue = deque([initial]) # Queue
    viewed = set() # Set

    print(initial.show())
    print(final_state)

    while queue:

        node = queue.popleft()
        viewed.add(node.show())

        # It's the goal?
        if node.show() == final_state:
            return node
            
        # It's not the goal :(
        children = children_generator(node)

        for child in children:
            if child.show() not in viewed:
                queue.append(child)
                viewed.add(child.show())



def print_children(children):

    for child in children:
        print(child)


if __name__ == "__main__":

    print("direita-baixo")
    node = Node([1, 2, 3,
                4, 5, 6, 
                7, 8, 0], 
                3, None, 0, "NoOp")

    print("Pai: ")
    print(node)
    print("Filhos: ")
    print_children(children_generator(node))



    print("esquerda-cima")
    node = Node([0, 2, 3,
                4, 5, 6, 
                7, 8, 1], 
                3, None, 0, "NoOp")

    print("Pai: ")
    print(node)
    print("Filhos: ")
    print_children(children_generator(node))



    print("esquerda-baixo")
    node = Node([7, 2, 3,
                4, 5, 6, 
                0, 8, 1], 
                3, None, 0, "NoOp")

    print("Pai: ")
    print(node)
    print("Filhos: ")
    print_children(children_generator(node))



    print("direita-cima")
    node = Node([7, 2, 0,
                4, 5, 6, 
                3, 8, 1], 
                3, None, 0, "NoOp")

    print("Pai: ")
    print(node)
    print("Filhos: ")
    print_children(children_generator(node))



    print("centro-baixo")
    node = Node([1, 2, 3,
                4, 5, 6, 
                7, 0, 8], 
                3, None, 0, "NoOp")

    print("Pai: ")
    print(node)
    print("Filhos: ")
    print_children(children_generator(node))



    print("centro-cima")
    node = Node([2, 0, 3,
                4, 5, 6, 
                7, 8, 1], 
                3, None, 0, "NoOp")

    print("Pai: ")
    print(node)
    print("Filhos: ")
    print_children(children_generator(node))



    print("centro-esquerda")
    node = Node([7, 2, 3,
                0, 5, 6, 
                4, 8, 1], 
                3, None, 0, "NoOp")

    print("Pai: ")
    print(node)
    print("Filhos: ")
    print_children(children_generator(node))



    print("centro-direita")
    node = Node([7, 2, 6,
                4, 5, 0, 
                3, 8, 1], 
                3, None, 0, "NoOp")

    print("Pai: ")
    print(node)
    print("Filhos: ")
    print_children(children_generator(node))



    print("centro")
    node = Node([7, 2, 6,
                4, 0, 5, 
                3, 8, 1], 
                3, None, 0, "NoOp")

    print("Pai: ")
    print(node)
    print("Filhos: ")
    print_children(children_generator(node))


    


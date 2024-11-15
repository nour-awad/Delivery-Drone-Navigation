from random import  choice, randint


class Node:
    def __init__(self, position, path_cost = 1):
        self.start = False #start at position (0, 0)
        self.goal = False
        self.position = position
        self.children = []
        self.go = True #is there an obstacle or not
        self.path_cost = path_cost
        self.heuristic = None

    def __lt__(self, other):
        return self.heuristic < other.heuristic


def tree_creation(row, col):
    tree={}

    for i in range(row):
        for j in range(col):
            tree[(i, j)] = Node((i, j)) #grid of 40x40

    for i in range(row):
        for j in range(col):
            node = tree[(i, j)] #current node

            if node.go:
                neighbors = [
                    (i, j + 1), #below
                    (i, j - 1), #above
                    (i + 1, j), #right
                    (i - 1, j), #left
                    (i - 1, j - 1), # top-left diagonal
                    (i - 1, j + 1), # bottom-left diagonal
                    (i + 1, j - 1), # top-right diagonal
                    (i + 1, j + 1) # bottom-right diagonal
                ]
                for nx, ny in neighbors: #check limits of x and y
                    if 0 <= nx < row and 0 <= ny < col:
                        neighbor_node = tree[(nx, ny)]
                        if neighbor_node.go:
                            node.children.append(neighbor_node)

    tree[0,0].start = True
    while True:
        goal_position = (randint(0, row - 1), randint(0, col - 1))
        if goal_position != (0, 0):  # Ensure the goal is not at the start
            break
    tree[goal_position].goal = True

    return tree

def building(tree, row, col): #the obstacle
    building_count = 0
    building_per = int(0.1 *(row * col)) #160 building

    while building_count < building_per:
        i = randint(0, row - 1) #3shan (0, 0) heya el start
        j = randint(0, col - 1)
        building_node = tree[(i, j)]

        if building_node.go and not building_node.goal and not building_node.start:
            building_node.go = False
            building_node.path_cost = float('inf')  # Impassable
            building_count += 1

    return tree

def assign_cost(tree, row, col):
    for i in range(row):
        for j in range(col):
            node = tree[(i, j)]
            if node.go and not node.goal and not node.start:
                node.path_cost = choice([1, 2]) #1 -> tree, 2 -> car
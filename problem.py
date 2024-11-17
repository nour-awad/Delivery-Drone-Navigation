from random import  choice, randint


class Node:
    def __init__(self, position, path_cost = 1):
        self.start = False #start at position (0, 0)
        self.goal = False
        self.position = position
        self.children = []
        self.go = True #is there an obstacle or not
        self.path_cost = path_cost
        self.heuristic = float("inf")
        self.parent=None
        self.cost = float("inf")

    def __lt__(self, other):
        if self.heuristic is None or other.heuristic is None:
            return False
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
                    (i - 1, j - 1),  # top-left diagonal
                    (i - 1, j + 1),  # bottom-left diagonal
                    (i + 1, j - 1),  # top-right diagonal
                    (i + 1, j + 1)  # bottom-right diagonal
                ]
                for nx, ny in neighbors:
                    if 0 <= nx < row and 0 <= ny < col:
                        neighbor_node = tree[(nx, ny)]
                        if neighbor_node.go:
                            node.children.append(neighbor_node)

    tree[0,0].start = True
    goal_position = None
    while True:
        rand_x, rand_y = randint(0, row - 1), randint(0, col - 1)
        if (rand_x, rand_y) != (0, 0):
            goal_position = (rand_x, rand_y)
            tree[goal_position].goal = True
            break

    return tree, goal_position

def building(tree, row, col): #the obstacle
    building_count = 0
    building_per = int(0.17 *(row * col)) #160 building

    while building_count < building_per:
        i, j = randint(0, row - 1), randint(0, col - 1)
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
    return tree

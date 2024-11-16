import random
from math import exp
from heuristicFunction import *

def simulated_annealing(problem, start, goal):
    current_node = problem[start]
    goal_node = problem[goal]
    path = [current_node.position]
    current_node.cost = heuristic_2(current_node.position, goal_node.position)
    T = 1000

    while current_node.position != goal_node.position:
        if T == 0:
            print("Temperature reached zero, stopping.")
            return path

        neighbours = []
        for neighbour in current_node.children:
            if neighbour.go:
                neighbours.append(neighbour)

        if not neighbours:
            print("No path found")
            return path

        rand_neighbour = random.choice(neighbours)
        rand_cost = heuristic_2(rand_neighbour.position, goal_node.position)
        delta_e = rand_cost - current_node.cost

        if delta_e < 0 or random.random() < exp(-delta_e/T):
            current_node = rand_neighbour
            current_node.path = rand_cost
            path.append(current_node.position)


        T *= 0.99

    print("Goal reached!")
    return path
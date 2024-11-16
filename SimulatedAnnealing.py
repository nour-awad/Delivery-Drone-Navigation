import random
from math import exp
from heuristicFunction import *
from problem import *
import matplotlib.pyplot as plt
import numpy as np

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


def visualize_path(grid, path, start, goal):
    max_row = max(key[0] for key in grid) + 1
    max_col = max(key[1] for key in grid) + 1

    grid_array = np.zeros((max_row, max_col), dtype=int)

    for (x, y), node in grid.items():
        if not node.go:
            grid_array[x, y] = 1

    for (x, y) in path:
        grid_array[x, y] = 2

    grid_array[start[0], start[1]] = 3
    grid_array[goal[0], goal[1]] = 4

    cmap = plt.cm.get_cmap('Blues', 5)
    bounds = [0, 1, 2, 3, 4]
    norm = plt.Normalize(vmin=0, vmax=4)

    plt.imshow(grid_array, cmap=cmap, norm=norm)
    cbar = plt.colorbar(
        ticks=[0, 1, 2, 3, 4],
        format=plt.FuncFormatter(lambda val, loc: ['Empty', 'Obstacle', 'Path', 'Start', 'Goal'][int(val)])
    )
    cbar.ax.set_ylabel('Legend', rotation=-90, labelpad=20)
    plt.title("Path Visualization")
    plt.show()


maze, goal = tree_creation(40, 40)
print(f"Goal placed at: {goal}")

maze_with_obstacles = building(maze, 40, 40)

assign_cost(maze_with_obstacles, 40, 40)
grid_with_costs = maze_with_obstacles

start = (0, 0)

path = simulated_annealing(grid_with_costs, start, goal)
print(f"Path found: {path}")

visualize_path(grid_with_costs, path, start, goal)
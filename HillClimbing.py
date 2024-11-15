from heuristicFunction import heuristic_function
from problem import *
import numpy as np
import matplotlib.pyplot as plt

def hill_climbing(problem, start, goal):
    current_node = problem[start]
    goal = problem[goal]
    path = [current_node.position]

    while current_node != goal:
        neighbours = current_node.children

        if not neighbours:
            print("No path found")
            break

        current_node = min(neighbours, key=lambda node: heuristic_function(node.position, goal.position))
        path.append(current_node.position)

        if current_node == goal:
            break

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

    cmap = plt.cm.get_cmap('Pastel1_r', 5)
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


grid = tree_creation(40, 40)
print("Tree created successfully")

grid_with_obstacles = building(grid, 40, 40)
print("Obstacles added successfully")

assign_cost(grid_with_obstacles, 40, 40)
grid_with_costs = grid_with_obstacles
start = (0, 0)
goal = (9, 39)

path = hill_climbing(grid_with_costs, start, goal)

visualize_path(grid_with_costs, path, start, goal)

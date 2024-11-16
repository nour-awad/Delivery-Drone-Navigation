from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import numpy as np

def visualize_path(grid, path, start, goal, title):
    max_row = max(key[0] for key in grid) + 1
    max_col = max(key[1] for key in grid) + 1

    grid_array = np.zeros((max_row, max_col), dtype=int)

    for (x, y), node in grid.items():
        if not node.go:
            grid_array[x, y] = 0
        if node.path_cost == 1:
            grid_array[x, y] = 1
        if node.path_cost == 2:
            grid_array[x, y] = 2

    for (x, y) in path:
        grid_array[x, y] = 3

    grid_array[start[0], start[1]] = 4
    grid_array[goal[0], goal[1]] = 5

    cmap = ListedColormap(['violet', 'lightblue', 'darkblue', 'pink', 'red', 'green'])
    bounds = [0, 1, 2, 3, 4, 5]
    norm = plt.Normalize(vmin=0, vmax=5)

    plt.imshow(grid_array, cmap=cmap, norm=norm)
    cbar = plt.colorbar(
        ticks=[0, 1, 2, 3, 4, 5],
        format=plt.FuncFormatter(lambda val, loc: ['Obstacle', 'Low Cost', 'High Cost', 'Path', 'Start', 'Goal'][int(val)])
    )
    cbar.ax.set_ylabel('Legend', rotation=-90, labelpad=20)
    plt.title(title)
    plt.show()
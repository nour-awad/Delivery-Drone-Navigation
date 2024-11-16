# Run A* search
start_position = (0, 0)
goal_position = next(node.position for node in tree.values() if node.goal)
solution_astar, _ = astar_search(tree, start_position, goal_position, verbose=True)

# Visualize the maze and the path found by A*
def visualize_maze(tree, row, col, solution=None, title="Maze"):
    fig, ax = plt.subplots(figsize=(col, row))

    for i in range(row):
        for j in range(col):
            node = tree[(i, j)]
            if not node.go:
                ax.add_patch(plt.Rectangle((j, row - i - 1), 1, 1, color='black'))
                #draw obsticles
            elif node.start:
                ax.add_patch(plt.Rectangle((j, row - i - 1), 1, 1, color='green'))
                ax.text(j + 0.5, row - i - 0.5, "S", ha='center', va='center', color='white', fontsize=12)
                #draw start state
            elif node.goal:
                ax.add_patch(plt.Rectangle((j, row - i - 1), 1, 1, color='red'))
                ax.text(j + 0.5, row - i - 0.5, "Goal", ha='center', va='center', color='white', fontsize=12)
                #draw goal state

            elif solution and node.is_part_of_solution(solution):
                ax.add_patch(plt.Rectangle((j, row - i - 1), 1, 1, color='blue'))
                #draw the path taken

    ax.set_xticks(np.arange(0, col, 1))
    ax.set_yticks(np.arange(0, row, 1))

    ax.set_xticklabels([])
    ax.set_yticklabels([])

    ax.grid(True)
    ax.set_title(title)
    plt.show()

visualize_maze(tree, row, col, solution_astar, title="A* Search")
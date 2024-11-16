from problem import *
from greedy_best_first import *
from visualizer import *
def main():
    row, col = 40, 40
    tree = tree_creation(row, col)
    tree = building(tree, row, col)
    assign_cost(tree, row, col)

    start_position = (0, 0)
    goal_position = next(node.position for node in tree.values() if node.goal)
    solution_astar, _ = astar_search(tree, start_position, goal_position, verbose=True)

    solution_gbfs, _ = greedy_best_first_search(tree, start_position, goal_position, verbose=True)

    visualize_maze(tree, row, col, solution_gbfs, title="Greedy Best-First Search")
    visualize_maze(tree, row, col, solution_astar, title="A* Search")


if __name__ == '__main__':
    main()
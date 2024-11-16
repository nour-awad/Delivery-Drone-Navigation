
solution_gbfs, _ = Greedy_best_firsy_search(tree, start_position, goal_position, verbose=True)

visualize_maze(tree, row, col, solution_gbfs, title="Greedy Best-First Search")

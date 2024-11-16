def gbfs_performance(tree, start_position, goal_position, verbose=False):
    """
    Calculate and display the performance of the Greedy Best-First Search algorithm.
    """
    performance = measure_performance(Greedy_best_firsy_search, tree, start_position, goal_position, verbose=verbose)

    solution = performance['solution']
    elapsed_time = performance['elapsed_time']
    max_frontier_size = performance['max_frontier_size']

    print("Greedy Best-First Search Performance:")
    print(f"Solution: {solution}")
    print(f"Elapsed Time: {elapsed_time:.4f} seconds")
    print(f"Max Frontier Size: {max_frontier_size}")

    total_nodes = len(tree)
    explored_percentage = (max_frontier_size / total_nodes) * 100
    print(f"Explored Nodes Percentage: {explored_percentage:.2f}%")

    return performance

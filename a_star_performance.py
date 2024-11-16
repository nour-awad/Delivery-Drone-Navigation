def astar_performance(tree, start_position, goal_position, verbose=False):
    """
    Calculate and display the performance of the A* search algorithm.
    """
    performance = measure_performance(astar_search, tree, start_position, goal_position, verbose=verbose)

    # Calculate performance metrics
    solution = performance['solution']
    elapsed_time = performance['elapsed_time']
    max_frontier_size = performance['max_frontier_size']

    # Display performance metrics
    print("A* Search Performance:")
    print(f"Solution: {solution}")
    print(f"Elapsed Time: {elapsed_time:.4f} seconds")
    print(f"Max Frontier Size: {max_frontier_size}")

    # Calculate and display performance in percentage
    total_nodes = len(tree)
    explored_percentage = (max_frontier_size / total_nodes) * 100
    print(f"Explored Nodes Percentage: {explored_percentage:.2f}%")

    return performance

from time import time

def measure_performance(search_algorithm, problem, start_position, goal_position, verbose=False, **kwargs):
    start_time = time()

    solution_result, max_frontier_size = search_algorithm(
        problem, start_position, goal_position, verbose=verbose, **kwargs
    )

    elapsed_time = time() - start_time

    return {
        'algorithm': search_algorithm.__name__,
        'solution': solution_result,
        'elapsed_time': elapsed_time,
        'max_frontier_size': max_frontier_size
    }


def evaluate_algorithms(algorithms, tree, start_position, goal_position, verbose=False, **kwargs):

    results = []

    for algorithm in algorithms:
        print(f"\nEvaluating {algorithm.__name__}...")
        performance = measure_performance(
            algorithm, tree, start_position, goal_position, verbose=verbose, **kwargs
        )

        algorithm_name = performance['algorithm']
        solution = performance['solution']
        elapsed_time = performance['elapsed_time']
        max_frontier_size = performance['max_frontier_size']
        total_nodes = len(tree)

        explored_percentage = (max_frontier_size / total_nodes) * 100

        print(f"{algorithm_name} Performance:")
        print(f"Solution: {solution}")
        print(f"Elapsed Time: {elapsed_time:.4f} seconds")
        print(f"Max Frontier Size: {max_frontier_size}")
        print(f"Explored Nodes Percentage: {explored_percentage:.2f}%\n")

        results.append(performance)

    return results

from time import time
from A_star import *
from greedy_best_first import *
def measure_performance(search_algorithm, problem, start_position, goal_position, verbose=False):

    start_time = time()

    solution_result, max_frontier_size = search_algorithm(problem, start_position, goal_position, verbose=verbose)

    elapsed_time = time() - start_time

    return {
        'solution': solution_result,
        'elapsed_time': elapsed_time,
        'max_frontier_size': max_frontier_size
    }


def astar_performance(tree, start_position, goal_position, verbose=False):
    performance = measure_performance(astar_search, tree, start_position, goal_position, verbose=verbose)

    solution = performance['solution']
    elapsed_time = performance['elapsed_time']
    max_frontier_size = performance['max_frontier_size']

    print("A* Search Performance:")
    print(f"Solution: {solution}")
    print(f"Elapsed Time: {elapsed_time:.4f} seconds")
    print(f"Max Frontier Size: {max_frontier_size}")

    total_nodes = len(tree)
    explored_percentage = (max_frontier_size / total_nodes) * 100
    print(f"Explored Nodes Percentage: {explored_percentage:.2f}%")

    return performance

def gbfs_performance(tree, start_position, goal_position, verbose=False):
    performance = measure_performance(greedy_best_first_search, tree, start_position, goal_position, verbose=verbose)

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
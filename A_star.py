from heapq import heappop, heappush
from heuristicFunction import *

def astar_search(tree, start_position, goal_position, h=None, verbose=False):
    if h is None:
        h = heuristic

    start_node = tree[start_position]

    start_node.heuristic = h(start_node.position, goal_position)
    frontier = [(start_node.heuristic, 0, start_node)]  

    explored = set()
    max_frontier_size = 1  

    if verbose:
        print("Starting A* ----->> ")

    while frontier:
        _, _, node = heappop(frontier)
        if node.goal:
            return solution(node), max_frontier_size

        explored.add(node.position)
        for child in node.children:
            if not child.go:
                continue
            f = node.path_cost + h(child.position, goal_position)
            child.heuristic = f
            if child.position not in explored and all(c.position != child.position for _, _, c in frontier):
                child.parent = node  

                heappush(frontier, (f, len(explored), child))  

                if child.goal:
                    return solution(child), max_frontier_size

        max_frontier_size = max(max_frontier_size, len(frontier))

        if verbose:
            print(f"Frontier size: {len(frontier)}")
    return None, max_frontier_size

def solution(node):
    path = []
    while node is not None:
        path.append(node.position)
        node = node.parent
    return path[::-1]

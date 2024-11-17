import heapq
from problem import *

def ucs(tree, start, goal, row, col):

    frontier = [(0, tree[start])]
    visited = set()
    max_frontier_size = 1

    tree[start].parent = None
    tree[start].cumulative_cost = 0

    while frontier:
        current_cost, node = heapq.heappop(frontier)

        if node.position == goal:
            path = []
            while node is not None:
                path.append(node.position)
                node = node.parent
            path.reverse()
            return path, max_frontier_size, current_cost

        visited.add(node.position)

        for child in node.children:
            x, y = child.position
            new_cost = current_cost + child.path_cost

            if child.position not in visited and child.go:
                # If the node has not been visited or if a cheaper path is found
                if not hasattr(child, 'cumulative_cost') or new_cost < child.cumulative_cost:
                    child.cumulative_cost = new_cost
                    child.parent = node
                    heapq.heappush(frontier, (new_cost, child))

        max_frontier_size = max(max_frontier_size, len(frontier))


    return None, max_frontier_size, float('inf')

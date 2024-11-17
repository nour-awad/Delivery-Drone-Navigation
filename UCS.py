import heapq

def ucs(grid, start, goal, row, col):
    frontier = []
    heapq.heappush(frontier, (0, grid[start]))
    explored = set()
    max_frontier_size = 1

    while frontier:
        current_cost, current_node = heapq.heappop(frontier)

        if current_node.position == goal:
            path = []
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            return path, max_frontier_size, current_cost

        explored.add(current_node.position)

        for child in current_node.children:
            if child.go and child.position not in explored:
                new_cost = current_cost + child.path_cost

                heapq.heappush(frontier, (new_cost, child))

                if child.parent is None or new_cost < child.path_cost:
                    child.parent = current_node

        max_frontier_size = max(max_frontier_size, len(frontier))

    return None, max_frontier_size, float('inf')


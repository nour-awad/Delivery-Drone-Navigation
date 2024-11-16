def astar_search(tree, start_position, goal_position, h=None, verbose=False):
    """A* search with optional verbose output."""
    if h is None:
        h = heuristic
    #defining the heuristic in A*

    start_node = tree[start_position]
    # the initial state (starting point)

    start_node.heuristic = h(start_node.position, goal_position)
    frontier = [(start_node.heuristic, 0, start_node)]  
    # Priority queue ordered by (f(n), tiebreaker, node)
    
    explored = set()
    max_frontier_size = 1  
    # Track the maximum size of the frontier

    if verbose:
        print("Starting A* ----->> ")

    while frontier:
        _, _, node = heappop(frontier)
        if node.goal:
            return solution(node), max_frontier_size
        #check if the current node(state) is the goal

        explored.add(node.position)
        # adds the node to the explored Q
        for child in node.children:
            if not child.go:
            # avoid obsticle
                continue
            f = node.path_cost + h(child.position, goal_position)
            # F(n) = h(n) + Path cost
            child.heuristic = f  
            # Set the heuristic value for the child node
            if child.position not in explored and all(c.position != child.position for _, _, c in frontier):
                child.parent = node  
                # Set the parent of the child node

                heappush(frontier, (f, len(explored), child))  
                # Use len(explored) as a tiebreaker

                if child.goal: # current child is goal state ?
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

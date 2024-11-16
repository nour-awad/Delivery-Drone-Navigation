def Greedy_best_firsy_search(tree, start_position, goal_position, h=None, verbose=False):
    """Greedy Best-First Search with optional verbose output."""
    if h is None:
        h = heuristic
    #defining the heuristic in GBFS

    start_node = tree[start_position]
    # the initial state (starting point)

    start_node.heuristic = h(start_node.position, goal_position)

    frontier = [(start_node.heuristic, 0, start_node)] 
    # Priority queue ordered by (f(n), tiebreaker, node)

    explored = set()
    max_frontier_size = 1  
    # Track the maximum size of the frontier

    if verbose:
        print("Starting Greedy Best-First Search ----->> ")

    while frontier:
        _, _, node = heappop(frontier)
        if node.goal:
            return solution(node), max_frontier_size
            #check if the current node(state) is the goal

        explored.add(node.position)
        for child in node.children:

            f = h(child.position, goal_position)
            child.heuristic = f  
            # Set the heuristic value for the child node
            # GBFS ملهاش استخدام في path cost ال 
            if child.position not in explored and all(c.position != child.position for _, _, c in frontier):
                child.parent = node  
                # Set the parent of the child node

                heappush(frontier, (f, len(explored), child))  
                # Use len(explored) as a tiebreaker

                if child.goal: #current child(node) is goal ?
                    return solution(child), max_frontier_size

        max_frontier_size = max(max_frontier_size, len(frontier))

        if verbose:
            print(f"Frontier size: {len(frontier)}")
    return None, max_frontier_size

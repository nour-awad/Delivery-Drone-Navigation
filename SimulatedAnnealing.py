def simulated_annealing(problem, start, goal):
    current_node = problem[start]
    goal_node = problem[goal]
    path = [current_node.position]

    while current_node.position != goal_node.position:
        neighbours = []
        for neighbour in current_node.children:
            if neighbour.go:
                neighbours.append(neighbour)

        if not neighbours:
            print("No path found")
            return path


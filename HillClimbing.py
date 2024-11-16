from heuristicFunction import *

def hill_climbing(problem, start, goal):
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

        next_node = min(neighbours, key=lambda node: heuristic_2(node.position, goal_node.position))

        if heuristic_2(next_node.position, goal_node.position) >= heuristic_2(current_node.position, goal_node.position):
            print("Stuck in local maximum")
            return path

        current_node = next_node
        path.append(current_node.position)

    return path
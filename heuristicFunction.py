def heuristic_2(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])


def heuristic(a, b):
     return max(abs(a[0] - b[0]), abs(a[1] - b[1]))

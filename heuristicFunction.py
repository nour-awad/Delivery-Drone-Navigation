from math import sqrt

def heuristic_function(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])
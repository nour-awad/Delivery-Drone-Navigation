from math import sqrt

def heuristic_function(current, goal):
    return sqrt((current[0] - goal[0])**2 + (current[1] - goal[1])**2)
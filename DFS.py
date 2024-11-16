from collections import deque

from problem import *
def dfs(tree, start, goal, row, col):
 
    frontier = [tree[start]]
    visited = set() 

    max_fsize = 1 #max size of frontier

    visited.add(start)
    tree[start].parent = None
    path = []
    while frontier:
        node = frontier.pop()

        if node.position == goal:
            while node is not None:
                path.append(node.position)
                node = node.parent
            path.reverse()
            return path, max_fsize
        
        #node expansion
        for child in node.children:
            x,y = child.position
            if (x, y) not in visited and child.go:
                visited.add((x,y))
                child.parent = node
                frontier.append(child)

        max_fsize = max(max_fsize, len(frontier))

    # when no path
    return path, max_fsize

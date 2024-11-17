from problem import *

def ids(tree, start, goal, row, col, max_depth=1000):
    
    def layered_dfs(tree, start, goal, limit):
        frontier = [(tree[start], 0)]  
        visited = set()
        tree[start].parent = None
        max_frontier_size = 1

        while frontier:
            max_frontier_size = max(max_frontier_size, len(frontier)) 
            node, current_depth = frontier.pop()
            if current_depth > limit:
                continue

            if node.position == goal:
                path = []
                while node is not None:
                    path.append(node.position)
                    node = node.parent
                path.reverse()
                return path, max_frontier_size

            visited.add(node.position)
            for child in node.children:
                x, y = child.position
                if child.position not in visited and child.go:
                    child.parent = node
                    frontier.append((child, current_depth + 1))

        return None, max_frontier_size

    max_frontier_size = 0
    for depth in range(max_depth):
        result, frontier_size = layered_dfs(tree, start, goal, depth)
        max_frontier_size = max(max_frontier_size, frontier_size)

        if result is not None:
            return result, max_frontier_size

    return None, max_frontier_size

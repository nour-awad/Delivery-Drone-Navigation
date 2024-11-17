from BFS import *
from DFS import *
from SimulatedAnnealing import *
from greedy_best_first import *
from visualizer import *
from measure_performance import *
from IDS import *

def main():
    maze, goal = tree_creation(40, 40)
    print(f"Goal placed at: {goal}")
    maze_with_obstacles = building(maze, 40, 40)
    assign_cost(maze_with_obstacles, 40, 40)
    grid_with_costs = maze_with_obstacles
    start = (0, 0)

    '''
    Uninformed Search
    '''
    #BFS
    bfs_, max_fsize = bfs(grid_with_costs, start, goal, 40, 40)
    print(f"BFS Path: {bfs_}")
    visualize_path(grid_with_costs, bfs_, start, goal, "Breadth First Search")

    #DFS
    dfs_, max_frontier = dfs(grid_with_costs, start, goal, 40, 40)
    print(f"DFS Path: {dfs_}")
    visualize_path(grid_with_costs, dfs_, start, goal, "Depth First Search")

    #IDS
    ids_, max_front = ids(grid_with_costs, start, goal, 40, 40, 1000)
    print(f"IDS Path: {ids_}")
    visualize_path(grid_with_costs, dfs_, start, goal, "Iterative Deepining Search")

    '''
    Informed Search
    '''
    #A*
    a_star_, max_frontier_size = astar_search(grid_with_costs, start, goal, h=heuristic, verbose=True)
    print(f"A* Path: {a_star_}")
    visualize_path(grid_with_costs, a_star_, start, goal, "A* Search")

    #Greedy Best First Search
    gbfs, max_frontier_ = greedy_best_first_search(grid_with_costs, start, goal, h=heuristic, verbose=True)
    print(f"GBFS Path: {gbfs}")
    visualize_path(grid_with_costs, gbfs, start, goal, "Greedy Best First Search")

    '''
    Local Search
    '''
    #Simulated Annealing
    simulated__annealing = simulated_annealing(grid_with_costs, start, goal)
    print(f"SA Path: {simulated__annealing}")
    visualize_path(grid_with_costs, simulated__annealing, start, goal, "Simulated Annealing")

    #Hill Climbing
    hill__climbing = simulated_annealing(grid_with_costs, start, goal)
    print(f"HC Path: {hill__climbing}")
    visualize_path(grid_with_costs, hill__climbing, start, goal, "Hill Climbing")



if __name__ == '__main__':
    main()
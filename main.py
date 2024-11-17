from BFS import *
from DFS import *
from Genetic import *
from IDS import *
from SimulatedAnnealing import *
from measure_performance import *
from visualizer import *
from UCS import *
import time


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
    t_bfs = time.time()
    bfs_, max_fsize = bfs(grid_with_costs, start, goal, 40, 40)
    t_bfs2 = time.time()
    print(f"BFS Path: {bfs_}")
    print(f"time taken: {round((t_bfs2-t_bfs) * 1e3, 3)} milliseconds")
    visualize_path(grid_with_costs, bfs_, start, goal, "Breadth First Search")

    #DFS
    t_dfs = time.time()
    dfs_, max_frontier = dfs(grid_with_costs, start, goal, 40, 40)
    t_dfs2 = time.time()
    print(f"DFS Path: {dfs_}")
    print(f"time taken: {round((t_dfs2 - t_dfs) * 1e3, 3)} milliseconds")
    visualize_path(grid_with_costs, dfs_, start, goal, "Depth First Search")

    #IDS
    t_ids = time.time()
    ids_, max_front = ids(grid_with_costs, start, goal, 40, 40, 1000)
    t_ids2 = time.time()
    print(f"IDS Path: {ids_}")
    print(f"time taken: {round((t_ids2 - t_ids) * 1e3, 3)} milliseconds")
    visualize_path(grid_with_costs, ids_, start, goal, "Iterative Deepening Search")

    #UCS
    t_ucs = time.time()
    usc_, max_frontier_s, cost = ucs(grid_with_costs, start, goal, 40, 40)
    t_ucs2 = time.time()
    print(f"UCS Path: {usc_}")
    print(f"time taken: {round((t_ucs2 - t_ucs) * 1e3, 3)} milliseconds")
    visualize_path(grid_with_costs, usc_, start, goal, "UCS Search")

    '''
    Informed Search
    '''
    #A*
    t_astar = time.time()
    a_star_, max_frontier_size = astar_search(grid_with_costs, start, goal, h=heuristic, verbose=True)
    t_astar2 = time.time()
    print(f"A* Path: {a_star_}")
    print(f"time taken: {round((t_astar2 - t_astar) * 1e3, 3)} milliseconds")
    visualize_path(grid_with_costs, a_star_, start, goal, "A* Search")

    #Greedy Best First Search
    t_gbst = time.time()
    gbfs, max_frontier_ = greedy_best_first_search(grid_with_costs, start, goal, h=heuristic, verbose=True)
    t_gbst2 = time.time()
    print(f"GBFS Path: {gbfs}")
    print(f"time taken: {round((t_gbst2 - t_gbst) * 1e3, 3)} milliseconds")
    visualize_path(grid_with_costs, gbfs, start, goal, "Greedy Best First Search")

    '''
    Local Search
    '''
    #Simulated Annealing
    t_sa = time.time()
    simulated__annealing = simulated_annealing(grid_with_costs, start, goal)
    t_sa2 = time.time()
    print(f"SA Path: {simulated__annealing}")
    print(f"time taken: {round((t_sa2 - t_sa) * 1e3, 3)} milliseconds")
    visualize_path(grid_with_costs, simulated__annealing, start, goal, "Simulated Annealing")

    #Hill Climbing
    t_hc = time.time()
    hill__climbing = simulated_annealing(grid_with_costs, start, goal)
    t_hc2 = time.time()
    print(f"HC Path: {hill__climbing}")
    print(f"time taken: {round((t_hc2 - t_hc) * 1e3, 3)} milliseconds")
    visualize_path(grid_with_costs, hill__climbing, start, goal, "Hill Climbing")

    #Genetic Algorithm
    t_ga = time.time()
    gene_pool = list(grid_with_costs.keys())
    population = init_population(100, gene_pool, state_length=20, start=start, goal=goal)
    genetic_path = genetic_algorithm(population, fitness, grid_with_costs, start, goal, gene_pool, f_thres=0.5, ngen=1000, pmut=0.1)
    t_ga2 = time.time()
    print(f"Genetic Algorithm Path: {genetic_path}")
    print(f"time taken: {round((t_ga2 - t_ga) * 1e3, 3)} milliseconds")
    visualize_path(grid_with_costs, genetic_path, start, goal, "Genetic Algorithm")

if __name__ == '__main__':
    main()

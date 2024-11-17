import random

def recombine(x, y):
    n = len(x)
    c = random.randint(0, n - 1)
    return x[:c] + y[c:]

def mutate(x, gene_pool, pmut):
    if random.uniform(0, 1) >= pmut:
        return x

    n = len(x)
    g = len(gene_pool)
    c = random.randint(0, n - 1)
    r = random.randint(0, g - 1)
    new_gene = gene_pool[r]
    return x[:c] + [new_gene] + x[c + 1:]

def init_population(pop_number, gene_pool, state_length, start, goal):
    population = []
    for _ in range(pop_number):
        new_individual = [start]
        for _ in range(state_length - 2):
            new_individual.append(random.choice(gene_pool))
        new_individual.append(goal)
        population.append(new_individual)
    return population



def fitness(path, grid, start, goal):
    if path[0] != start or path[-1] != goal:
        return 0.01

    cost = 0
    for i in range(len(path) - 1):
        current = path[i]
        next_node = path[i + 1]

        if next_node in grid[current].children and grid[next_node].go:
            cost += grid[next_node].path_cost
        else:
            return 0.01

    return 1 / (1 + cost)


def select(k, population, fitness_fn, grid, start, goal):
    selected = random.choices(population, k=k, weights=[fitness_fn(ind, grid, start, goal) for ind in population])
    selected = sorted(selected, key=lambda x: fitness_fn(x, grid, start, goal), reverse=True)
    return selected[:2]

def genetic_algorithm(population, fitness_fn, grid, start, goal, gene_pool, f_thres, ngen=1000, pmut=0.1):
    for i in range(ngen):
        population = [
            mutate(recombine(*select(2, population, fitness_fn, grid, start, goal)), gene_pool, pmut)
            for _ in range(len(population))
        ]

        fittest_individual = max(population, key=lambda ind: fitness_fn(ind, grid, start, goal))
        if fitness_fn(fittest_individual, grid, start, goal) >= f_thres:
            print(f"Solution found at generation {i + 1}")
            return fittest_individual
    return max(population, key=lambda ind: fitness_fn(ind, grid, start, goal))

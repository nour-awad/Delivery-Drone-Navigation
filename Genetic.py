def recombine(x, y):
    n = len(x)
    c = random.randint(0, n)  
    return x[:c] + y[c:]

def mutate(x, gene_pool, pmut):
    
    if random.uniform(0, 1) >= pmut:
        return x

    n = len(x)
    g = len(gene_pool)
    c = random.randint(0, n -1)  
    r = random.randint(0, g - 1)  
    
    new_gene = gene_pool[r]
    return x[:c] + [new_gene] + x[c+1:]


import random

def genetic_algorithm(population, fitness_fn, gene_pool, f_thres, ngen=1000, pmut=0.1, visualizer=None):
    """Genetic algorithm that visualizes each generation."""
    for i in range(ngen):
        # Update population with new individuals
        population = [
            mutate(recombine(*select(2, population, fitness_fn)), gene_pool, pmut)
            for _ in range(len(population))
        ]

        # Check if there's a solution in the current generation
        fittest_individual = max(population, key=fitness_fn)
        if fitness_fn(fittest_individual) == f_thres:
            if visualizer:
                print(f"Solution found at generation {i + 1}")
                visualizer.visualize_state(fittest_individual)  # Visualize final solution state
            return fittest_individual

        # Visualize the fittest individual at each generation
        if visualizer:
            print(f"Generation {i + 1}")
            visualizer.visualize_state(fittest_individual)

    # Return the best individual if no perfect solution is found
    return max(population, key=fitness_fn)

def recombine(x, y):
    n = len(x)
    c = random.randint(0, n)  
    return x[:c] + y[c:]

def mutate(x, gene_pool, pmut):
    if random.uniform(0, 1) >= pmut:
        return x

    n = len(x)
    g = len(gene_pool)
    c = random.randint(0, n -1)  
    r = random.randint(0, g - 1)  
    new_gene = gene_pool[r]
    return x[:c] + [new_gene] + x[c+1:]


def init_population(pop_number, gene_pool, state_length):
    """Initializes population for genetic algorithm
    pop_number  :  Number of individuals in population
    gene_pool   :  List of possible values for individuals
    state_length:  The length of each individual"""
    g = len(gene_pool)
    population = []
    for i in range(pop_number):
        new_individual = [gene_pool[random.randint(0, g - 1)] for j in range(state_length)]  
        population.append(new_individual)

    return population


def fitness(q):
    non_attacking = 0
    for row1 in range(len(q)):
        for row2 in range(row1+1, len(q)):
            col1 = int(q[row1])
            col2 = int(q[row2])
            row_diff = row1 - row2
            col_diff = col1 - col2

            if col1 != col2 and row_diff != col_diff and row_diff != -col_diff:
                non_attacking += 1

    return non_attacking


def select(k, population, fitness_fn):
    """Selects two individuals from the population to be parents based on their fitness."""
    selected = random.choices(population, k=k)  
    selected = sorted(selected, key=fitness_fn, reverse=True)  
    return selected[:2]  
# Return the top two individuals as parents

population = init_population(100, range(8), 8)
print(population[:5])

# Run Genetic Algorithm
visualizer = Visualizer(None)
solution = genetic_algorithm(population, fitness, range(8), f_thres=25, visualizer=visualizer)
print(solution)
print(fitness(solution))

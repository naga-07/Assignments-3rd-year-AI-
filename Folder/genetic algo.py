import random
import math

# Define the problem instance
num_cities = 10
cities = [(random.uniform(0, 100), random.uniform(0, 100)) for i in range(num_cities)]

# Define GA parameters
pop_size = 50
mutation_rate = 0.1
num_generations = 100

# Define helper functions
def distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def route_distance(route):
    dist = 0
    for i in range(num_cities):
        dist += distance(cities[route[i]], cities[route[(i+1)%num_cities]])
    return dist

# Initialize the population
population = [list(range(num_cities)) for i in range(pop_size)]
for i in range(pop_size):
    random.shuffle(population[i])

# Evolve the population
for gen in range(num_generations):
    # Calculate the fitness of each individual
    fitness = [1 / route_distance(route) for route in population]

    # Select the parents
    mating_pool = []
    for i in range(pop_size):
        parent1 = random.choices(population, weights=fitness)[0]
        parent2 = random.choices(population, weights=fitness)[0]
        mating_pool.append((parent1, parent2))

    # Generate the offspring
    offspring = []
    for parents in mating_pool:
        parent1, parent2 = parents
        crossover_point = random.randint(1, num_cities-1)
        child = parent1[:crossover_point] + [city for city in parent2 if city not in parent1[:crossover_point]]
        offspring.append(child)

    # Mutate the offspring
    for i in range(pop_size):
        if random.random() < mutation_rate:
            mutation_point1 = random.randint(0, num_cities-1)
            mutation_point2 = random.randint(0, num_cities-1)
            offspring[i][mutation_point1], offspring[i][mutation_point2] = offspring[i][mutation_point2], offspring[i][mutation_point1]

    # Replace the population with the offspring
    population = offspring

# Print the best solution
best_route = max(population, key=lambda route: 1 / route_distance(route))
print(f"The best route is {best_route} with distance {route_distance(best_route)}.")

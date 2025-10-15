import random

alpha = 1
beta = 5
evaporation_rate = 0.5
pheromone_constant = 100
num_ants = 10
iterations = 100


def quality(solution, item_values, item_weights, capacities):
    knapsack_weights = [0] * len(capacities)
    total_value = 0

    for item, knapsack in enumerate(solution):
        if knapsack != -1:
            knapsack_weights[knapsack] += item_weights[item]
            if knapsack_weights[knapsack] > capacities[knapsack]:
                return -1
            total_value += item_values[item]

    return total_value


def ant_colony_optimization(item_values, item_weights, capacities):
    num_items = len(item_values)
    num_knapsacks = len(capacities)

    pheromones = [[1 for _ in range(num_knapsacks)] for _ in range(num_items)]
    best_solution = None
    best_value = -float('inf')

    for iteration in range(iterations):
        all_ants_solutions = []
        all_ants_values = []

        for ant in range(num_ants):
            solution = [-1] * num_items
            knapsack_weights = [0] * num_knapsacks

            for item in range(num_items):
                probabilities = []
                for knapsack in range(num_knapsacks):
                    if knapsack_weights[knapsack] + item_weights[item] <= capacities[knapsack]:
                        pheromone = pheromones[item][knapsack] ** alpha
                        heuristic = (item_values[item] / item_weights[item]) ** beta
                        probabilities.append(pheromone * heuristic)
                    else:
                        probabilities.append(0)

                total_probability = sum(probabilities)
                if total_probability > 0:
                    probabilities = [p / total_probability for p in probabilities]
                    chosen_knapsack = random.choices(range(num_knapsacks), weights=probabilities)[0]
                    solution[item] = chosen_knapsack
                    knapsack_weights[chosen_knapsack] += item_weights[item]

            solution_value = quality(solution, item_values, item_weights, capacities)
            all_ants_solutions.append(solution)
            all_ants_values.append(solution_value)

            if solution_value > best_value:
                best_solution = solution
                best_value = solution_value

        for item in range(num_items):
            for knapsack in range(num_knapsacks):
                pheromones[item][knapsack] *= (1 - evaporation_rate)

        for ant, solution in enumerate(all_ants_solutions):
            if all_ants_values[ant] > 0:
                for item, knapsack in enumerate(solution):
                    if knapsack != -1:
                        pheromones[item][knapsack] += pheromone_constant / all_ants_values[ant]

    return best_solution, best_value

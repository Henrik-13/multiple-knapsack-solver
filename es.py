import numpy as np


def knapsack_fitness(individual, item_values, item_weights, capacities):
    total_value = 0
    used_capacities = [0] * len(capacities)

    for i, taken in enumerate(individual):
        if taken == 1:
            for j in range(len(capacities)):
                if used_capacities[j] + item_weights[i] <= capacities[j]:
                    used_capacities[j] += item_weights[i]
                    total_value += item_values[i]
                    break
            else:
                return 0

    return total_value


def evolutionary_algorithm(item_values, item_weights, capacities, mu=10, lambda_=40, it=1000):
    num_items = len(item_values)

    population = [
        {
            "x": np.random.randint(0, 2, num_items),
            "sigma": np.random.uniform(0.1, 1.0, num_items)
        }
        for _ in range(mu)
    ]

    for _ in range(it):
        offspring = []
        for _ in range(lambda_):
            parent = population[np.random.randint(0, mu)]
            x = np.copy(parent["x"])
            sigma = np.copy(parent["sigma"])

            tau_prime = 1 / np.sqrt(2 * num_items)
            tau = 1 / np.sqrt(2 * np.sqrt(num_items))

            sigma_prime = sigma * np.exp(tau_prime * np.random.normal(0, 1) + tau * np.random.normal(0, 1, num_items))
            sigma_prime[sigma_prime < 1e-8] = 1e-8

            x_prime = np.copy(x)
            for i in range(num_items):
                if np.random.random() < sigma_prime[i]:
                    x_prime[i] = 1 - x_prime[i]

            offspring.append({"x": x_prime, "sigma": sigma_prime})

        combined_population = population + offspring
        combined_population.sort(key=lambda ind: -knapsack_fitness(ind["x"], item_values, item_weights, capacities))

        population = combined_population[:mu]

    best_individual = max(population, key=lambda ind: knapsack_fitness(ind["x"], item_values, item_weights, capacities))
    best_value = knapsack_fitness(best_individual["x"], item_values, item_weights, capacities)
    return best_individual["x"], best_value

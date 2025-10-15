import random
import math

it_max = 1000
t0 = 10 ** 4


def exponential(iteration: int):
    alpha = 0.85
    return t0 * alpha ** iteration


def logarithmic(iteration: int):
    alpha = 2
    return t0 / (1 + alpha * math.log(1 + iteration))


def linear(iteration: int):
    alpha = 1
    return t0 / (1 + alpha * iteration)


def quadratic(iteration: int):
    alpha = 1
    return t0 / (1 + alpha * iteration ** 2)


def quality(solution, item_values, item_weights, capacities):
    total_value = 0
    knapsack_weights = [0] * len(capacities)

    for item, knapsack in enumerate(solution):
        if knapsack != -1:
            knapsack_weights[knapsack] += item_weights[item]
            if knapsack_weights[knapsack] > capacities[knapsack]:
                return -1
            total_value += item_values[item]

    return total_value

def simulated_annealing(initial_solution, item_values, item_weights, capacities, func=linear):
    current_solution = initial_solution[:]
    current_value = quality(current_solution, item_values, item_weights, capacities)
    best_solution = current_solution[:]
    best_value = current_value
    temperature = t0

    for iteration in range(it_max):
        neighbor = current_solution[:]
        item = random.randint(0, len(item_values) - 1)
        neighbor[item] = random.randint(0, len(capacities) - 1)

        neighbor_value = quality(neighbor, item_values, item_weights, capacities)
        if neighbor_value == -1:
            continue

        if neighbor_value > current_value or random.random() < math.exp((neighbor_value - current_value) / temperature):
            current_solution = neighbor[:]
            current_value = neighbor_value

        if current_value > best_value:
            best_solution = current_solution[:]
            best_value = current_value

        temperature = func(iteration)
        if temperature <= 0:
            break

    return best_solution, best_value

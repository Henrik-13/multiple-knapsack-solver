# Bálint Henrik
# 531
# bhim2208

from aco import ant_colony_optimization
from simulated_annealing import simulated_annealing


def hybrid_algorithm(item_values, item_weights, capacities, func):
    initial_solution, _ = ant_colony_optimization(item_values, item_weights, capacities)

    refined_solution, best_value = simulated_annealing(initial_solution, item_values, item_weights, capacities, func)

    return refined_solution, best_value

# Bálint Henrik
# 531
# bhim2208

from hybrid import *
from pso import *
from memoization import *
from simulated_annealing import *
from es import *

annealing_functions = [exponential, linear]


def read_input_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    item_values = list(map(int, lines[0].strip().split()))
    item_weights = list(map(int, lines[1].strip().split()))
    capacities = list(map(int, lines[2].strip().split()))
    return item_values, item_weights, capacities


def main():
    for i in range(1, 7):
        filename = f"input/input{i}.txt"
        item_values, item_weights, capacities = read_input_file(filename)
        for function in annealing_functions:
            print("Hybrid algorithm...")
            print(function)
            hybrid_solution, hybrid_value = hybrid_algorithm(item_values, item_weights, capacities, function)
            print("Hybrid algorihm best solution:", hybrid_solution)
            print("Hybrid algorihm best value:", hybrid_value)
            print("=" * 50)

        print("PSO algorithm...")
        pso_solution, pso_value = pso(item_values, item_weights, capacities)
        print("PSO algorithm best solution", pso_solution)
        print("PSO algorithm best value:", pso_value)
        print("=" * 50)

        print("ES algorithm...")
        es_solution, es_value = evolutionary_algorithm(item_values, item_weights, capacities)
        print("es algorithm best solution:", es_solution)
        print("es algoritmus best value:", es_value)
        print("=" * 50)

        if i < 5:
            print("Memoization algorithm...")
            multi_knapsack_value = solve_multi_knapsack(item_values, item_weights, capacities)
            print("Memoization algorithm best value:", multi_knapsack_value)
            print("=" * 50)
        print("=" * 50)


if __name__ == '__main__':
    main()

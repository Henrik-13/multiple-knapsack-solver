# Documentation
## Multiple Knapsack Problem

## Problem Description

The task is to solve the multiple knapsack problem.
This is a combinatorial optimization problem where we have n items (each with a known value and weight)
and m knapsacks (with capacity). The goal is to place the items in the knapsacks in such a way that
the total value is maximized while not exceeding the capacity of each knapsack.

This problem is NP-complete, so some traditional algorithms (e.g., dynamic programming)
are only applicable to small-sized cases. For larger instances, metaheuristic algorithms are needed,
such as:

- Particle Swarm Optimization (PSO)
- Hybrid solution (ACO + Simulated Annealing)
- Evolutionary Strategies

In the project, all three algorithms have been implemented and tested, as well as a memoization algorithm.

## Algorithm Descriptions
### 1. Hybrid Algorithm (ACO + Simulated Annealing)
Steps:

1. Ant Initialization: Within the ACO (Ant Colony Optimization) framework, multiple ants start, marking their path with pheromones while searching for the optimal solution.
2. Pheromone Update: Ants that find better solutions leave stronger trails, helping subsequent iterations.
3. Simulated Annealing (SA): Refines the solution found by ACO, examining incremental modifications of the solution (along a temperature gradient).

### 2. Particle Swarm Optimization (PSO)
PSO models natural swarm behavior. In the algorithm, multiple "particles" (solutions) move through the search space.

Steps:

1. Initialization: Each particle's initial position and velocity are randomly generated.
2. Velocity Update: The particle's velocity is calculated using the following formula, where:
    - inertia coefficient,
    - cognitive and social weights,
    - random multipliers.
3. Position Update: The position is modified based on the velocity and previous position.
4. Local and Global Best Solution Update: Each particle remembers its own and the swarm's best solution.
5. Iteration: The algorithm runs for the specified number of iterations.

### 3. Evolutionary Strategy
Evolutionary strategies model the process of natural selection and evolution. The solution evolves in the form of populations across generations.

Steps:
1. Initialization: Generate a random initial population, where each individual is a possible solution.
2. Fitness Evaluation: Calculate the fitness of each individual, which indicates the quality of the given solution.
3. Selection: Select the best individuals to participate in forming the new generation.
4. Recombination and Mutation: Create new individuals through crossover and random mutations.
5. New Generation: The new generation consists of selected and modified individuals.
6. Iteration: The algorithm runs until we reach the maximum number of iterations or a predetermined stopping criterion.

### 4. Memoization Algorithm
Combination of recursion and dynamic programming methods.

## Parameters and Test Cases
### Parameters
- ### Hybrid:
  - #### ACO:
    - Alpha: 1
    - Beta: 5
    - Evaporation Rate: 0.5
    - Pheromone Constant: 100
    - Number of Ants: 10
    - Number of Iterations: 100
  - #### Simulated Annealing:
    - Initial Temperature: 1000
    - Number of Iterations: 100
- ### PSO:
  - Swarm Size: 30
  - Inertia: 0.8
  - Cognitive Weight: 2.0
  - Social Weight: 2.0
  - Number of Iterations: 1000
- ### Evolutionary Strategy:
  - Population Size: 40
  - Number of Iterations: 1000

### Test Cases
I tested on 6 test cases:
  - Input 1: 5 knapsacks, 15 items
  - Input 2: 2 knapsacks, 5 items
  - Input 3: 3 knapsacks, 15 items
  - Input 4: 5 knapsacks, 15 items
  - Input 5: 5 knapsacks, 50 items
  - Input 6: 10 knapsacks, 50 items

## Results

|         | Hybrid (exponential) | Hybrid (linear) | PSO  | Evolutionary | Memoization |
|---------|----------------------|-----------------|------|--------------|-------------|
| Input 1 | 355                  | 355             | 355  | 385          | 395         |
| Input 2 | 80                   | 80              | 90   | 90           | 90          |
| Input 3 | 320                  | 320             | 345  | 345          | 350         |
| Input 4 | 740                  | 740             | 740  | 740          | 740         |
| Input 5 | 1804                 | 1777            | 1990 | 2145         | -           |
| Input 6 | 2620                 | 2620            | 2430 | 2575         | -           |

## Conclusions and Future Goals
### Conclusions
The runtime and accuracy of the algorithms have been tested:

PSO: Provides faster solutions for larger instances, but the solution quality depends on initial parameterization.

Hybrid Algorithm: Slower execution, but more precise solutions for small and medium-sized problems.

Evolutionary Strategy: Results vary, and fine-tuning parameters is critical for achieving good solutions.
Fast and efficient method for larger problems. Overall, this provided the best solutions.

Memoization Algorithm: Provides good solutions for smaller inputs, but is by far the slowest algorithm,
and cannot be used for larger inputs due to its slowness.

### Future Goals
1. Further development of the algorithms (dynamic parameter tuning).
2. Application of larger test datasets.
3. Testing a combination of three algorithms (ACO + SA + PSO + Evolutionary Strategy).

import random
import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

SWARM_SIZE = 30
ITERATIONS = 1000
INERTIA_WEIGHT = 0.8
COGNITIVE_WEIGHT = 2.0
SOCIAL_WEIGHT = 2.0

def initialize_particle(item_count, item_values, item_weights, capacities):
    position = [random.choice([0, 1]) for _ in range(item_count)]

    while quality(position, item_values, item_weights, capacities) == -1:
        position = [random.choice([0, 1]) for _ in range(item_count)]

    velocity = [random.random() for _ in range(item_count)]

    return {
        "position": position,
        "velocity": velocity,
        "local_best": position,
        "local_best_value": quality(position, item_values, item_weights, capacities)
    }

def quality(solution, values, weights, capacities):
    total_weight = [0] * len(capacities)
    total_value = 0

    for i, selected in enumerate(solution):
        if selected:
            for j in range(len(capacities)):
                if total_weight[j] + weights[i] <= capacities[j]:
                    total_weight[j] += weights[i]
                    total_value += values[i]
                    break
            else:
                return -1

    return total_value


def update_particle(particle, global_best, item_values, item_weights, capacities):
    new_velocity = []
    new_position = []

    for i in range(len(particle["position"])):
        inertia = INERTIA_WEIGHT * particle["velocity"][i]
        cognitive = COGNITIVE_WEIGHT * random.random() * (particle["local_best"][i] - particle["position"][i])
        social = SOCIAL_WEIGHT * random.random() * (global_best["position"][i] - particle["position"][i])

        new_velocity.append(inertia + cognitive + social)

        if random.random() < sigmoid(new_velocity[i]):
            new_position.append(1)
        else:
            new_position.append(0)

    particle["velocity"] = new_velocity
    particle["position"] = new_position

    value = quality(new_position, item_values, item_weights, capacities)

    if value != -1 and value > particle["local_best_value"]:
        particle["local_best"] = new_position
        particle["local_best_value"] = value

    return particle

def pso(item_values, item_weights, capacities):
    item_count = len(item_values)
    swarm = [initialize_particle(item_count, item_values, item_weights, capacities) for _ in range(SWARM_SIZE)]

    global_best = max(swarm, key=lambda p: p["local_best_value"])

    for _ in range(ITERATIONS):
        for i in range(SWARM_SIZE):
            swarm[i] = update_particle(swarm[i], global_best, item_values, item_weights, capacities)

        new_global_best = max(swarm, key=lambda p: p["local_best_value"])
        if new_global_best["local_best_value"] > global_best["local_best_value"]:
            global_best = new_global_best

    return global_best["local_best"], global_best["local_best_value"]

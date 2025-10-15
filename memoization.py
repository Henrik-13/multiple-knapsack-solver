def find_max_value_multi_knapsack(curr, n, item_weights, item_values, capacities, memo):
    if curr >= n:
        return 0

    capacities_key = tuple(capacities)
    if (curr, capacities_key) in memo:
        return memo[(curr, capacities_key)]

    res = find_max_value_multi_knapsack(curr + 1, n, item_weights, item_values, capacities, memo)

    for i in range(len(capacities)):
        weight = item_weights[curr]
        value = item_values[curr]
        if capacities[i] >= weight:
            new_capacities = capacities[:]
            new_capacities[i] -= weight

            take_item = value + find_max_value_multi_knapsack(curr + 1, n, item_weights, item_values, new_capacities, memo)
            res = max(res, take_item)

    memo[(curr, capacities_key)] = res
    return res


def solve_multi_knapsack(item_values, item_weights, capacities):
    n = len(item_values)
    memo = {}
    return find_max_value_multi_knapsack(0, n, item_weights, item_values, capacities, memo)

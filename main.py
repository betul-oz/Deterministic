import itertools

sponges = [
    {
        'name': 'rolls1',
        'thickness': 2,
        'length': 1500,
    },
    {
        'name': 'rolls2',
        'thickness': 3,
        'length': 1000,
    },
    {
        'name': 'rolls3',
        'thickness': 4,
        'length': 800,
    }
]

beds = [
    {
        'name': 'bed1',
        'width': 135,
        'height': 195,
    },
    {
        'name': 'bed2',
        'width': 150,
        'height': 195,
    },
    {
        'name': 'bed3',
        'width': 178,
        'height': 195,
    }
]

demands = [
    {
        'bed': 'bed1',
        'rolls1': 45,
        'rolls2': 45,
        'rolls3': 29,
    },
    {
        'bed': 'bed2',
        'rolls1': 38,
        'rolls2': 38,
        'rolls3': 38,
    },
    {
        'bed': 'bed3',
        'rolls1': 7,
        'rolls2': 7,
        'rolls3': 6,
    }
]

def meet_demand(demands, sponges):
    combinations = []
    for sponge_combination in itertools.product(*[[i + 1 for i in range(demand[sponge['name']])] for demand in demands for sponge in sponges]):
        total_demand = {sponge['name']: 0 for sponge in sponges}
        for demand, sponge in zip(demands, sponge_combination):
            for sponge_type, quantity in demand.items():
                if sponge_type != 'bed':
                    total_demand[sponge_type] += sponge
        if all(total_demand[sponge['name']] >= demand[sponge['name']] for demand in demands for sponge in sponges):
            combinations.append(total_demand)
    return combinations

manufacturing_combinations = meet_demand(demands, sponges)

# Write results to a file
with open("manufacturing_combinations.txt", "w") as file:
    for combo in manufacturing_combinations:
        file.write(str(combo) + "\n")

print("Results written to manufacturing_combinations.txt")

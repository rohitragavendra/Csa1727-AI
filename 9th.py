from itertools import permutations

# Distance matrix (symmetric)
dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

cities = [0, 1, 2, 3]
min_path = float('inf')
best_route = []

for perm in permutations(cities[1:]):  # Fix city 0 as start
    route = [0] + list(perm) + [0]
    cost = sum(dist[route[i]][route[i+1]] for i in range(len(route)-1))
    if cost < min_path:
        min_path = cost
        best_route = route

print("Best Route:", best_route)
print("Minimum Cost:", min_path)

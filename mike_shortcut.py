from typing import List
import math

def dfs(distance, nb_intersections, intersection, visited):
    visited[intersection] = True
    for i in range(nb_intersections):
        if i == intersection and visited[i]:
            continue

        if distance[0][i] > distance[0][intersection] + distance[intersection][i]:
            distance[0][i] = distance[0][intersection] + distance[intersection][i]
            dfs(distance, nb_intersections, i, visited)

def get_required_energy(nb_intersections: int, shortcuts: List[int]):
    distance = [[math.inf for _ in range(nb_intersections)] for _ in range(nb_intersections)]

    for i in range(0, nb_intersections):
        distance[i][i] = 0

    for i in range(nb_intersections):
        for j in range(nb_intersections):
            if i != j:
                distance[i][j] = abs(i - j)
                distance[j][i] = abs(i - j)

    for intersection, shortcut in enumerate(shortcuts):
        distance[intersection][shortcut - 1] = min(distance[intersection][shortcut - 1], 1)
        distance[0][shortcut - 1] = min(distance[0][shortcut - 1], 1 + distance[0][intersection])

    visited = [False] * nb_intersections
    for shortcut in shortcuts:
        dfs(distance, nb_intersections, shortcut - 1, visited)

    return distance[0]

if __name__ == "__main__":
    nb_intersections = int(input())
    shortcuts = [int(shortcut) for shortcut in input().split()]

    energy_needed = get_required_energy(nb_intersections, shortcuts)
    print(" ".join(map(str, energy_needed)))
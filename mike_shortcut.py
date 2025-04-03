from typing import List
import math

def get_required_energy(nb_intersections: int, shortcuts: List[int]):
    distance = [math.inf for _ in range(nb_intersections)]
    distance[0] = 0
    short_dict = {}

    for intersection, shortcut in enumerate(shortcuts):
        short_dict[intersection] = shortcut - 1

    need_update = [0]
    while need_update:
        intersection = need_update.pop()

        if intersection + 1 < nb_intersections and distance[intersection + 1] > 1 + distance[intersection]:
            distance[intersection + 1] = 1 + distance[intersection]
            need_update.append(intersection + 1)

        if intersection - 1 >= 0 and distance[intersection - 1] > 1 + distance[intersection]:
            distance[intersection - 1] = 1 + distance[intersection]
            need_update.append(intersection - 1)

        if intersection in short_dict and distance[short_dict[intersection]] > 1 + distance[intersection]:
            distance[short_dict[intersection]] = 1 + distance[intersection]
            need_update.append(short_dict[intersection])

    return distance

if __name__ == "__main__":
    nb_intersections = int(input())
    shortcuts = [int(shortcut) for shortcut in input().split()]

    energy_needed = get_required_energy(nb_intersections, shortcuts)
    print(" ".join(map(str, energy_needed)))
import random
from single_player import single_player


map_pool = [
    "Ascent",
    "Bind",
    "Haven",
    "Split",
    "Icebox",
    "Breeze",
    "Fracture",
    "Pearl",
    "Lotus",
    "Sunset",
    "Abyss",
]


def gen_prev(count):
    maps = []
    for _ in range(count):
        rand = random.randint(0, 10)
        maps.append(map_pool[rand])

    return maps


def main():
    previous_maps = gen_prev(10)
    next_maps = single_player(previous_maps, map_pool)
    print(next_maps)


if __name__ == "__main__":
    main()

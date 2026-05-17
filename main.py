import random


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
    for _ in count:
        rand = random.randint(0, 11)
        maps.append(map_pool[rand])

    return maps

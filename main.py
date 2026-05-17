import random
from single_player import single_player
from multiplayer import multiplayer


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


def gen_history(count, multiplayer):
    if not multiplayer:
        maps = []
        for _ in range(count):
            rand = random.randint(0, 10)
            maps.append(map_pool[rand])

        return maps


def main():
    s_hist = gen_history(20, False)
    m_hist = 0
    s_next = single_player(s_hist, map_pool)
    m_next = multiplayer(m_hist, map_pool)

    print(s_hist)
    print()
    print(s_next)
    print()
    print(m_next)


if __name__ == "__main__":
    main()

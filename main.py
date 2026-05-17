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


def s_gen_hist(count):
    maps = []
    for _ in range(count):
        rand = random.randint(0, 10)
        maps.append(map_pool[rand])

    return maps


def m_gen_hist(count, players):
    maps = []
    for _ in range(players):
        player_maps = []
        for _ in range(count):
            rand = random.randint(0, 10)
            player_maps.append(map_pool[rand])
        maps.append(player_maps)

    return maps


def main():
    s_hist = s_gen_hist(20)
    m_hist = m_gen_hist(20, 2)
    s_next = single_player(s_hist, map_pool)
    m_next = multiplayer(m_hist, map_pool)

    print(s_hist)
    print()
    print(m_hist)
    print()
    print(s_next)
    print()
    print(m_next)


if __name__ == "__main__":
    main()

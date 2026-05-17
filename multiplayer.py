import random


def multiplayer(map_history, map_pool):
    # init hashmap with counts, random float is added to prevent ties
    # from being broken by alphanumeric ordering
    map_counts = {}
    for m in map_pool:
        map_counts[m] = random.random()

    for player_history in map_history:
        # fill hashmap with number of previous maps
        for m in player_history:
            map_counts[m] += 1

    # create arr of hashmap items
    # sort for least played at front
    arr = []
    for m, c in map_counts.items():
        arr.append([c, m])
    arr.sort()
    
    return arr

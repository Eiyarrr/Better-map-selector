import random

def single_player(previous_maps, map_pool):
    # init hashmap with counts, random float is added to prevent ties
    # from being broken by alphanumeric ordering
    map_counts = {}
    for m in map_pool:
        map_counts[m] = random.random()
    
    # fill hashmap with number of previous maps
    for m in previous_maps:
        map_counts[m] += 1

    # create arr of hashmap items
    # sort + reverse for least played maps at the front
    arr = []
    for m, c in map_counts.items():
        arr.append([c, m])
    arr.sort()
    arr.reverse()
    
    return arr

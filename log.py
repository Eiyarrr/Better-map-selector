import json


def log(map_pool, s_hist, s_next, m_hist, m_next):
    data = []
    data.append(("MAP POOL", map_pool))
    data.append(("S_HIST", s_hist))
    data.append(("S_HIST", s_next))
    data.append(("M_HIST", m_hist))
    data.append(("M_HIST", m_next))
    
    file = open("log.json", "w")
    json.dump(data, file, indent=4)

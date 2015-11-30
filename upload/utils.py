#coding=utf8
    
    
def geodist(lat1, lon1, lat2, lon2):
    try:
        earth_radius = 6378.1
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = (math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) *
        math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2))
        c = (2 * math.atan2(math.sqrt(a), math.sqrt(1 - a)))
        d = (earth_radius * c) * 1000.0
    except:
        d = 0.0
    return d

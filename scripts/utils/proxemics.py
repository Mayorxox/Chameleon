def proxemic_zone_from_distance(d):
    if d < 0.5:
        return 'intimate'
    if d < 1.2:
        return 'personal'
    if d < 3.5:
        return 'social'
    return 'public'

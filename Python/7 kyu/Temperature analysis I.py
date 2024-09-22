def lowest_temp(t):
    t = list(map(int, t.split()))
    return min(t) if t else None

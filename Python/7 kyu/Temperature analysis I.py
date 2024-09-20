def lowest_temp(t):
    if not t:
        return None

    t = t.split()
    t = list(map(int, t))

    return min(t)

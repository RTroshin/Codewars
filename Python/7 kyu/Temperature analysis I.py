def lowest_temp(t):
    if not t:
        return None

    t = list(map(int, t.split()))

    return min(t)

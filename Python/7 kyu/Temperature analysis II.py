def close_to_zero(t):
    if not t:
        return 0

    t = list(map(int, t.split()))
    t.sort()

    res = max(t)
    for n in t:
        if n >= 0 and n <= res:
            res = n

    return res

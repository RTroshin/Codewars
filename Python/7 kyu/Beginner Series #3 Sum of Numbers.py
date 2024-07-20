def get_sum(a, b):
    if a < 0 or b < 0:
        min_n, max_n = min(a, b), max (a, b)
        res = sum(range(min_n, max_n + 1))
    else:
        res = sum(range(a, b + 1))

    return res if a != b else a

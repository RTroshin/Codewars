def get_sum(a, b):
    min_n, max_n = min(a, b), max (a, b)
    res = sum(range(min_n, max_n + 1))

    return res if a != b else a

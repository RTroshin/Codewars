def get_sum(a, b):
    min_n, max_n = min(a, b), max (a, b)

    return sum(range(min_n, max_n + 1)) if a != b else a

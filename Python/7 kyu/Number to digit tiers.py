def create_array_of_tiers(n):
    n = str(n)
    res = [n[: i + 1] for i in range(len(n))]

    return res

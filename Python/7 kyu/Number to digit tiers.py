def create_array_of_tiers(n):
    n = str(n)
    return [n[: i + 1] for i in range(len(n))]

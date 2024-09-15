def create_array_of_tiers(n):
    res= []
    n = str(n)

    for i in range(len(n)):
        res.append(n[: i + 1])

    return res

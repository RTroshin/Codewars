def no_odds(values):
    res = []

    for i in range(len(values)):
        if not values[i] % 2:
            res.append(values[i])

    return res

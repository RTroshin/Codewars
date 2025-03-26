def no_odds(values):
    res = []

    for n in values:
        if not n % 2:
            res.append(n)

    return res

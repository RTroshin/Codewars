def trouble(x, t):
    res = []

    for i in range(len(x) - 1):
        if x[i] + x[i + 1] == t:
            res = x[:i] + x[i + 1:]

    return res

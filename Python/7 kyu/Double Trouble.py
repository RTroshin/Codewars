def trouble(x, t):
    res = []

    for i in range(len(x) - 1):
        for j in range(len(x) - 1):
            if x[j] + x[j + 1] == t:
                res = x[:j + 1] + x[j + 2:]
        x = res

    return res

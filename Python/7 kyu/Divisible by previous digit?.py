def divisible_by_last(n):
    res = [False]
    n = str(n)

    for i in range(len(n) - 1):
        res.append(not (int(n[i]) == 0 or int(n[i + 1]) % int(n[i])) or False)

    return res

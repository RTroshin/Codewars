def divisible_by_last(n):
    res = [False]
    n = str(n)

    for i in range(len(n) - 1):
        res.append(False) if int(n[i]) == 0 or int(n[i + 1]) % int(n[i]) else res.append(True)

    return res

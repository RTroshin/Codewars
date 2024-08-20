def divisible_by_last(n):
    res = [False]
    n = str(n)

    for i in range(len(n) - 1):
        if int(n[i]) == 0 or int(n[i + 1]) % int(n[i]):
            res.append(False)
        else:
            res.append(True)

    return res

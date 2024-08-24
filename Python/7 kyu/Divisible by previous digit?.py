def divisible_by_last(num):
    res = [False]
    num = str(num)

    for i in range(len(num) - 1):
        res.append(not (int(num[i]) == 0 or int(num[i + 1]) % int(num[i])))

    return res

def digits(num):
    res = []
    num = str(num)

    for i in range(len(num)):
        for j in range(len(num)):
            if i != j:
                res.append(int(num[i]) + int(num[j]))

    res = list(set(res))

    return sorted(res)

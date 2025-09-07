def digits(num):
    res = []
    num = str(num)

    for i in range(len(num)):
        for j in range(len(num)):
            res.append(int(num[i]) + int(num[j]))

    return res

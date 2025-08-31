def digits(num):
    res = []
    num = str(num)

    for i in range(len(num) - 1):
        sum = int(num[i]) + int(num[i + 1])
        res.append(sum)

    return res

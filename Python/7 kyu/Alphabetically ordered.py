def alphabetic(s):
    res = list(s)

    for i in range(len(res) - 1):
        for j in range(len(res) - 1):
            if ord(res[j]) > ord(res[j + 1]):
                res[j], res[j + 1] = res[j + 1], res[j]

    res = ''.join(res)

    return res == s

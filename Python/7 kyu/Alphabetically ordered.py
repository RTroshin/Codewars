def alphabetic(str):
    res = list(str)

    for i in range(len(res) - 1):
        for j in range(len(res) - 1):
            if ord(res[j]) > ord(res[j + 1]):
                res[j], res[j + 1] = res[j + 1], res[j]

    return ''.join(res) == str

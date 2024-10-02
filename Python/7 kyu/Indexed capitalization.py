def capitalize(str, ind):
    res = ''

    for i in range(len(str)):
        if i in ind:
            res += str[i].upper()
        else:
            res += str[i]

    return res

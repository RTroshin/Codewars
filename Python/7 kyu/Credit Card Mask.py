def maskify(cc):
    if len(cc) < 5:
        return cc

    res = ''

    for i in range(len(cc)):
        if i < (len(cc) - 4):
            res += '#'

    return res + cc[-4:]

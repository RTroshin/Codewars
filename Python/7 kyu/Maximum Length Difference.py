def mxdiflg(a1, a2):
    res = []

    for x in a1:
        for y in a2:
            res.append(abs(len(x) - len(y)))

    return max(res) if res else -1

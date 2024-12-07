def mxdiflg(a1, a2):
    res = [abs(len(x) - len(y)) for x in a1 for y in a2]

    return max(res) if res else -1

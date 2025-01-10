def solve(a,b):
    res = []

    for str in b:
        res.append(a.count(str))

    return res

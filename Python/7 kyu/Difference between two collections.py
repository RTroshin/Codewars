def diff(a, b):
    a = list(set(a))
    b = list(set(b))
    ab = a + b
    res = [n for n in ab if ab.count(n) == 1]
    res.sort()

    return res

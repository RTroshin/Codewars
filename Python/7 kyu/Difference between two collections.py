# return a sorted list with the difference
def diff(a, b):
    ab = a + b
    res = []

    for n in ab:
        if ab.count(n) == 1:
            res.append(n)

    return res

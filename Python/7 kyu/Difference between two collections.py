# return a sorted list with the difference
def diff(a, b):
    ab = a + b
    res = []

    for i in range(len(ab)):
        if ab.count(ab[i]) == 1:
            res.append(ab[i])

    return res

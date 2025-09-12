# return a sorted list with the difference
def diff(a, b):
    ab = a + b
    res = [n for n in ab if ab.count(n) == 1]

    return res

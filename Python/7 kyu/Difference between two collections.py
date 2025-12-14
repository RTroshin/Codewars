# return a sorted list with the difference
def diff(a, b):
    a = list(set(a))
    b = list(set(b))
    ab = a + b

    return [n for n in ab if ab.count(n) == 1]

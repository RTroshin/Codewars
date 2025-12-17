def diff(a, b):
    a = list(set(a))
    b = list(set(b))
    ab = a + b

    return sorted([n for n in ab if ab.count(n) == 1])

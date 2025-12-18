def diff(a, b):
    ab = list(set(a)) + list(set(b))

    return sorted([n for n in ab if ab.count(n) == 1])

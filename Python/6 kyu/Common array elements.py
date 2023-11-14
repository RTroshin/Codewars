def common(a, b, c):
    return sum([i * min(a.count(i), b.count(i), c.count(i)) for i in set(a) & set(b) & set (c)])

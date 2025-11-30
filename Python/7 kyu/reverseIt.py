def reverse_it(data):
    t = type(data)
    return t(str(data)[::-1]) if t in [str, int, float] else data

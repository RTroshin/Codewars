def reverse_it(data):
    t = type(data)

    if t in [str, int, float]:
        return t(str(data)[::-1])
    return data

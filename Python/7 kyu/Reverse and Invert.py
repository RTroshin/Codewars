def reverse_invert(lst):
    res = []

    for n in lst:
        if isinstance(n, int):
            res.append((-1 if n > 0 else 1) * int((str(abs(n))[::-1])))

    return res

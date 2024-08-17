def reverse_invert(lst):
    res = []

    for i in range(len(lst)):
        if isinstance(lst[i], int):
            res.append((-1 if lst[i] > 0 else 1) * int((str(abs(lst[i]))[::-1])))

    return res

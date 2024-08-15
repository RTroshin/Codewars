def reverse_invert(lst):
    res = []

    for i in range(len(lst)):
        if type(lst[i]) == int:
            sign = -1 if lst[i] > 0 else 1
            res.append(sign * int((str(abs(lst[i]))[::-1])))

    return res

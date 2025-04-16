def is_nice(arr):
    res = False

    for n in arr:
        if n + 1 in arr or n - 1 in arr:
            res = True
        else:
            res = False

    return res

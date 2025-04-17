def is_nice(arr):
    res = False

    for n in arr:
        res = True if n + 1 in arr or n - 1 in arr else False

    return res

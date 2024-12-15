def max_diff(lst):
    if len(lst) < 2:
        return 0

    res = max(lst) - min(lst)

    return res

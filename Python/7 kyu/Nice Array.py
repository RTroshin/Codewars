def is_nice(arr):
    res = False

    for i in range(len(arr)):
        if arr[i] + 1 in arr or arr[i] - 1 in arr:
            res = True
        else:
            res = False

    return res

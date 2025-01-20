def find_missing_numbers(arr):
    if not arr or len(arr) < 2:
        return []

    res = []

    for i in range(arr[0], arr[-1]):
        if i not in arr:
            res.append(i)

    return res

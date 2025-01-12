def solve(arr1, arr2):
    res = []

    for str in arr2:
        res.append(arr1.count(str))

    return res

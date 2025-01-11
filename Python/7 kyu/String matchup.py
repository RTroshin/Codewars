def solve(array1, array2):
    res = []

    for str in array2:
        res.append(array1.count(str))

    return res

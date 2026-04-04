def contain_all_rots(strng, arr):
    res = 0

    if not strng:
        return False
    if len(strng) < len(arr):
        return False

    for i in range(len(strng)):
        if strng[:i] + strng[i + 1:] + strng[i] in arr:
            res += 1

    return res == len(arr[0])

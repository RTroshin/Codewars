def check_exam(arr1, arr2):
    res = sum(4 if ch == arr2[i] else 0 if arr2[i] == '' else -1 for i, ch in enumerate(arr1))
    return res if res > 0 else 0

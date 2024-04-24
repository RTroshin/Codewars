def check_exam(arr1, arr2):
    res = sum(4 if arr1[i] == ch else 0 if ch == '' else -1 for i, ch in enumerate(arr2))
    return res if res > 0 else 0

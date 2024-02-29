def is_all_possibilities(arr):
    for i in range(len((arr))):
        if i not in arr:
            return False
    return True

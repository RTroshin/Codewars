def next_id(arr):
    for i in range(0, len(arr) + 1):
        if i not in arr:
            return i

def elimination(arr):
    for i in range(len(arr)):
        if arr.count(arr[i]) == 2:
            return arr[i]

    return None

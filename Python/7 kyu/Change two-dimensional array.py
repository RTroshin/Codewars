def matrix(arr):
    for i in range(len(arr)):
        arr[i][i] = 1 if arr[i][i] > 0 else 0

    return arr

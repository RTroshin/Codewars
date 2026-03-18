def stalin_sort(arr):

    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i + 1]:
            arr[i] = arr[i + 1]

    return arr

def sort_by_length(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1):
            if len(arr[j]) > len(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

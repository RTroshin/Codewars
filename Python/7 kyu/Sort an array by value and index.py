def sort_by_value_and_index(arr):
    arr_copy = arr.copy()

    for i in range(len(arr_copy)):
        arr_copy[i] = arr_copy[i] * (i + 1)

    for i in range(len(arr_copy) - 1):
        for j in range(len(arr_copy) - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

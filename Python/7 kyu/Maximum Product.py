def adjacent_element_product(arr):
    max = arr[0] * arr[1]

    for i in range(len(arr) - 1):
        if max < arr[i] * arr[i + 1]:
            max = arr[i] * arr[i + 1]

    return max

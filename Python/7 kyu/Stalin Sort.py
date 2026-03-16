def stalin_sort(arr):
    # Hint: print("Расстрелять!") for each eliminated element
    res = [arr[0]]

    for i in range(1, len(arr) - 1):
        if arr[i] < arr[i + 1]:
            res.append(arr[i])

    return res

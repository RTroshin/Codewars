def up_array(arr):
    new_arr = []
    arr_len = len(arr)
    arr[arr_len - 1] += 1

    for i in range(arr_len - 1, -1, -1):
        if arr[i] < 0 or arr[i] > 10:
            return None
        elif not arr[i] % 10:
            new_arr.append(0)
            arr[i - 1] += 1
        else:
            new_arr.append(arr[i])

    if new_arr.count(0) == len(new_arr):
        new_arr.append(1)

    return new_arr[::-1]

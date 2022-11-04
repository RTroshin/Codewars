def up_array(arr):
    if not len(arr):
        return None

    for i in arr:
        if i < 0 or i > 9:
            return None
    else:
        new_arr = [int(i) for i in str(int("10" + "".join([str(j) for j in arr])) + 1)]
        return new_arr[1::] if new_arr[1] else new_arr[2::]

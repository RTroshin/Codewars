def solve(arr):
    new_arr = []

    for i in arr[::-1]:
        if i not in new_arr:
            new_arr.append(i) 

    return new_arr[::-1]

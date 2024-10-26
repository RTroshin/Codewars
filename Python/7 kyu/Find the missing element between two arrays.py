def find_missing(arr1, arr2):
    arr1.sort()
    arr2.sort()
    len_arr1 = len(arr1)

    for i, n in enumerate(arr1):
        if i == len_arr1 - 1 or n != arr2[i]:
            return n

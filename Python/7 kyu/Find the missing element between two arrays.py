def find_missing(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for i, n in enumerate(arr1):
        if i == len(arr1) - 1:
            return arr1[i]
        elif n != arr2[i]:
            return n

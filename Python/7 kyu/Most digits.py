def find_longest(arr):
    maxRes = arr[0]

    for n in arr:
        if len(str(maxRes)) < len(str(n)):
            maxRes = n

    return maxRes

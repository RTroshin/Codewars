def explode(arr):
    if type(arr[0]) == type(arr[1]) == int:
        return [arr for i in range(sum(arr))]
    elif type(arr[0]) != type(arr[1]):
        return [arr for i in range(arr[0])] if type(arr[0]) == int else [arr for i in range(arr[1])]
    else:
        return 'Void!'

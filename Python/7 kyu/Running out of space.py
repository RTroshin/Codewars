def spacey(arr):
    return [''.join(arr[0:i]) + arr[i] for i in range(len(arr))]

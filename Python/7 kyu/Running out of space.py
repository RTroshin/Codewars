def spacey(arr):
    return [''.join(arr[:i]) + arr[i] for i in range(len(arr))]

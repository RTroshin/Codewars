def spacey(arr):
    return [arr[0]] + [''.join(arr[0:i]) + arr[i] for i in range(1, len(arr))]

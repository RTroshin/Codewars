def spacey(array):
    return [array[0]] + [''.join(array[0:i]) + array[i] for i in range(1, len(array))]

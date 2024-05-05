def matrix(array):
    for i in range(len(array)):
        array[i][i] = 1 if array[i][i] > 0 else 0

    return array

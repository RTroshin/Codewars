def adjacent_element_product(array):
    max = array[0] * array[1]

    for i in range(len(array) - 1):
        if max < array[i] * array[i + 1]:
            max = array[i] * array[i + 1]

    return max

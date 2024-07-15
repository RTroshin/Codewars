def get_larger_numbers(a, b):
    return [a[i] if a[i] > b[i] else b[i] for i in range(len(a))]

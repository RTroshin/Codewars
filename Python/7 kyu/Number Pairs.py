def get_larger_numbers(a, b):
    return [n if n > b[i] else b[i] for i, n in enumerate(a)]

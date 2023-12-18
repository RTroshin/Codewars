def square_or_square_root(arr):
    return [n * n if n % n ** (1 / 2) else n ** (1 / 2) for n in arr]

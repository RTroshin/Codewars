def find_next_square(n):
    n = n ** (1 / 2)
    return -1 if n % 1 else (n + 1) ** 2

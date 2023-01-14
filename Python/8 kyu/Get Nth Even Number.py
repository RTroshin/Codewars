def nth_even(n):
    return [i for i in range(n * 2 + 1) if not i % 2][n - 1]

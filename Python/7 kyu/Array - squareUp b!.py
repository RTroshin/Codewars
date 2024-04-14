def square_up(n):
    return [0 if j > n - i + 1 else j for i in range(n, 0, -1) for j in range(n, 0, -1)]

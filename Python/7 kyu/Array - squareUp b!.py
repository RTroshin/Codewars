def square_up(n):
    return [j if j <= n - i + 1 else 0 for i in range(n, 0, -1) for j in range(n, 0, -1)]

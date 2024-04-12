def square_up(n):
    return [j if j <= n - i + 1 else 0 for i in range(1, n + 1) for j in range(1, n + 1)][::-1]

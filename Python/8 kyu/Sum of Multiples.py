def sum_mul(n, m):
    return sum([i * n for i in range(m) if i * n <= m]) if m > 0 else 'INVALID'

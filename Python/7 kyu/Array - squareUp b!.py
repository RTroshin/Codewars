def square_up(n):
    res = []

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            res += [j] if j <= n - i + 1 else [0]
    
    return res[::-1]

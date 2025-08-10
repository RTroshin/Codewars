def generate_pairs(n):
    res = [[0, 0]]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            res.append([i - 1, j])

    return res

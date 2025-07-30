def multiples(m, n):
    res = []
    j = n

    for i in range(m):
        while j % n:
            j += 1
        res.append(j)
        j += 1

    return res

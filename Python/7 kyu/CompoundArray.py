def compound_array(a, b):
    res = []

    for i in range(min(len(a), len(b))):
        res.append(a[i])
        res.append(b[i])

    return res + (a[len(b):] if len(a) >= len(b) else b[len(a):])

def compound_array(a, b):
    res = []
    minLen = min(len(a), len(b))

    for i in range(minLen):
        res.append(a[i])
        res.append(b[i])

    res += a[: len(b)] if len(a) >= len(b) else b[: len(a)]

    return res

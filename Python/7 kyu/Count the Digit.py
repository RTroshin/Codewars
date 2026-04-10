def nb_dig(n, d):
    res_sqr = []
    res_count = 0

    for i in range(n + 1):
        res_sqr.append(i * i)

    for n in res_sqr:
        res_count += str(n.count(str(d))

    return res_count

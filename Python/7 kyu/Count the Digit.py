def nb_dig(n, d):
    res_sqr = []
    res_count = 0

    res_sqr = [i * i for i in range(n + 1)]

    for n in res_sqr:
        res_count += str(n).count(str(d))

    return res_count

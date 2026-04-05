def nb_dig(n, d):
    res_sqr = []
    res_count = 0

    for i in range(n):
        res_sqr.append(i ** 2)

    for i in range(len(res_sqr)):
        if str(d) in str(res_sqr[i]):
            res_count += 1

    return res_count

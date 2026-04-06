def nb_dig(n, d):
    res_sqr = []
    res_count = 0

    for i in range(n):
        res_sqr.append(i ** 2)

    for i in range(len(res_sqr)):
        if str(res_sqr[i]).count(str(d)) != 0:
            res_count += str(res_sqr[i]).count(str(d))

    return res_count

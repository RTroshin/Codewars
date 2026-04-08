Count the Digitdef nb_dig(n, d):
    res_sqr = []
    res_count = 0

    for i in range(n + 1):
        res_sqr.append(i ** 2)

    for i in range(len(res_sqr)):
        res_count += str(res_sqr[i]).count(str(d))

    return res_count

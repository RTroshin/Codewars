Count the Digitdef nb_dig(n, d):
    res_count = 0

    for n in [i * i for i in range(n + 1)]:
        res_count += str(n.count(str(d))

    return res_count

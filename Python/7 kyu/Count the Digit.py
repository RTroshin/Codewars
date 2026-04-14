Count the Digitdef nb_dig(n, d):
    res = 0

    for n in [i * i for i in range(n + 1)]:
        res += str(n).count(str(d))

    return res

def number_to_pwr(num, p):
    n = 1

    for i in range(p):
        n *= num

    return n

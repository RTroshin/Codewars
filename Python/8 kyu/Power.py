def number_to_pwr(number, p):
    num = 1

    for i in range(p):
        num *= number

    return num

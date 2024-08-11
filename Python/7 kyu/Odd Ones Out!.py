def odd_ones_out(numbers):
    res = []

    for n in numbers:
        if numbers.count(n) % 2 == 0:
            res += [n]

    return res

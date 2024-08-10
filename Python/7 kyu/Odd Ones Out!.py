def odd_ones_out(numbers):
    res = []

    for n in numbers:
        if not numbers.count(n) % 2:
            res += [n]

    return res

def divisors(integer):
    res = []

    for i in range(2, integer - 1):
        if not integer % i:
            res.append(i)

    return res

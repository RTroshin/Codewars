def divisors(integer):
    res = []

    for i in range(2, integer):
        if not integer % i:
            break
    else:
        return f"{integer} is prime"

    for i in range(2, integer):
        if not integer % i:
            res.append(i)

    return res

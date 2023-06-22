def am_i_wilson(n):
    fact = 1
    for i in range(1, n):
        fact *= i

    return n == (fact + 1) / n if n else False

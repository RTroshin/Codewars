def largest_power(N):
    res = 0

    for n in range(N):
        if N <= pow(3, n):
            res = n - 1
            break

    return res

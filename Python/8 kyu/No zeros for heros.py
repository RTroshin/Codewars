def no_boring_zeros(n):
    while n:
        if not n % 10:
            n /= 10
        else:
            break

    return n

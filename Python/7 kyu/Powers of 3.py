def largest_power(N):
    for n in range(N):
        if N <= pow(3, n):
            return n - 1

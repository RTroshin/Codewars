def divisors(n):
    return sum(1 for i in range(1, n + 1) if not n % i)

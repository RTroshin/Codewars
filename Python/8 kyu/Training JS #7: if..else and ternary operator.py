def sale_hotdogs(n):
    return 100 * n if n > 0 and n < 5 else 95 * n if n >= 5 and n < 10 else 90 * n if n >= 10 else 0

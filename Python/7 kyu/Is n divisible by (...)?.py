def is_divisible(n, *lst):
    for i in lst:
        if n % i:
            return False

    return True

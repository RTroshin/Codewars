def is_divisible(n, *lst):
    for i in lst:
        if n % i:
            return False
    else:
        return True

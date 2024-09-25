def is_divisible(*lst):
    for i in lst[1:]:
        if lst[0] % i:
            return False

    return True

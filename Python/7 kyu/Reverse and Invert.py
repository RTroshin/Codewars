def reverse_invert(lst):
    return [(-1 if n > 0 else 1) * int((str(abs(n))[::-1])) for n in lst if isinstance(n, int)]

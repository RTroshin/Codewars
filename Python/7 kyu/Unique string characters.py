def solve(a, b):
    return ''.join([ch for ch in a + b if not ch in a or not ch in b])

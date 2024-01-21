import math

def root_sum(n):
    return n if n < 2 else sum(root for root in [n ** (1 / i) for i in range(1, 31)] if abs(round(root) - root) < 1e-5)

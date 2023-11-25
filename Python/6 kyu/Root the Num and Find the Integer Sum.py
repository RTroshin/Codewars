import math

def root_sum(n):
    return sum([root for root in [n ** (1 / i) for i in range(1, 31)] if abs(round(root) - root) < 1e-3])

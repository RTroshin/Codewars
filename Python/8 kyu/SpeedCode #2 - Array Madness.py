def array_madness(a, b):
    return sum(map(lambda n: n * n, a)) > sum(map(lambda n: n * n * n, b))

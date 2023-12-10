def array_madness(a, b):
    return sum(map(lambda n: n ** 2, a)) > sum(map(lambda n: n ** 3, b))

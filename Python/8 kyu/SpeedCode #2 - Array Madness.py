def array_madness(a, b):
    return sum(list(map(lambda n: n**2, a))) > sum(list(map(lambda n: n**3, b)))

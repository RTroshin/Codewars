def array_madness(a, b):
    return sum(list(map(lambda num: num**2, a))) > sum(list(map(lambda num: num**3, b)))

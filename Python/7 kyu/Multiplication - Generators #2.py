def generator(a):
    return iter(f"1 x {i} = {1 * i}" for i in range(1, a + 1))

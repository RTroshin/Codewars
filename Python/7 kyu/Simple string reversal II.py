def solve(st, a, b):
    res = st[:a] + st[a:b + 1][::-1] +  st[b + 1:]

    return res

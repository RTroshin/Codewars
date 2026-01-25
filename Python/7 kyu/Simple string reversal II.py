def solve(st,a,b):
    res = ''
    res = st[:a] + st[a:b + 1][::-1] +  st[b + 1:]

    return res

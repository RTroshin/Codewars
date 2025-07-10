def solve(st):
    res = -1

    for i in range(len(st)):
        if st[:i] == st[::-1][:i]:
            res += 1

    return res

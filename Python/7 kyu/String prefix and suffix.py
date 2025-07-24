def solve(st):
    res = 0

    for i in range(len(st) - 1):
        if st[:i + 1] == st[::-1][:i + 1] or st[:i + 1] == st[-i - 1:]:
            res += 1

    return res

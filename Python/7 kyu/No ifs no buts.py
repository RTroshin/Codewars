def no_ifs_no_buts(a, b):
    lst = [a, b]

    return [[f"{a} is greater than {b}", f"{a} is smaller than {b}"][lst.index(max(lst))], [f"{a} is equal to {b}"][0]][lst.count(a) - 1]

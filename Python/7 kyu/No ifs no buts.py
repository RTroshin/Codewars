def no_ifs_no_buts(a, b):
    lst = [a, b]

    return [[],[(str(a) + " is greater than " + str(b)), (str(a) + " is smaller than " + str(b))][lst.index(max(lst))], [(str(a) + " is equal to " + str(b))][0]][lst.count(a)]

def dont_give_me_five(start,end):
    res = []

    for i in range(start, end + 1):
        if '5' not in str(i):
            res.append(i)

    return len(res)

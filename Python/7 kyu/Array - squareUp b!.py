def square_up(n):
    res_lst_1 = []
    res_lst_2 = []
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            res_lst_1.append(j) if i >= j else res_lst_1.append(0)
        res_lst_2 += res_lst_1[::-1]
        res_lst_1 = []

    return res_lst_2

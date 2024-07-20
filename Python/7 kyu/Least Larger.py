def least_larger(a, i):
    res_arr = []

    for j in range(len(a)):
        if a[i] < a[j]:
            res_arr.append(a[j])

    return a.index(min(res_arr)) if res_arr else -1

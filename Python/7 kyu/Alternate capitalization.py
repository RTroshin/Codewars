def capitalize(str):
    res_str_1 = ''
    res_str_2 = ''

    for i in range(len(str)):
        if i % 2:
            res_str_2 += str[i].upper()
            res_str_1 += str[i]
        else:
            res_str_1 += str[i].upper()
            res_str_2 += str[i]

    return [res_str_1, res_str_2]

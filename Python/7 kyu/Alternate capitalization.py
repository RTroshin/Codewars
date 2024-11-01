def capitalize(s):
    res_s_1 = ''
    res_s_2 = ''

    for i in range(len(s)):
        if i % 2:
            res_s_2 += s[i].upper()
            res_s_1 += s[i]
        else:
            res_s_1 += s[i].upper()
            res_s_2 += s[i]

    return [res_s_1, res_s_2]

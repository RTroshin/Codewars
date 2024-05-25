def sum_of_integers_in_string(s):
    lst = []
    num = ''
    s += '.'

    for i in range(len(s)):
        if s[i].isdigit():
            num += s[i]
        else:
            if num:
                lst.append(int(num))
                num = ''
            else:
                num = ''

    return sum(lst)

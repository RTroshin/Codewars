def sum_of_integers_in_string(str):
    lst = []
    num = ''
    str += '.'

    for i in range(len(str)):
        if str[i].isdigit():
            num += str[i]
        else:
            if num:
                lst.append(int(num))
                num = ''
            else:
                num = ''

    return sum(lst)

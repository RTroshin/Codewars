def sum_of_integers_in_string(str):
    lst = []
    num = ''
    str += '.'

    for ch in str:
        if ch.isdigit():
            num += ch
        else:
            if num:
                lst.append(int(num))
                num = ''
            else:
                num = ''

    return sum(lst)

def most_common(str):
    if not str:
        return ''

    ch_first = str[0]

    for ch in str:
        if str.count(ch) > str.count(ch_first):
            ch_first = ch

    return ch_first * str.count(ch_first) + str.replace(ch_first, '')

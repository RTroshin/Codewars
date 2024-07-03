def most_common(str):
    ch_first = str[0] if str else ''

    for ch in str:
        if str.count(ch) > str.count(ch_first):
            ch_first = ch

    return ch_first * str.count(ch_first) + str.replace(ch_first, '')

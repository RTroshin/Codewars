def most_common(s):
    if not s:
        return ''

    ch_first = s[0]

    for c in s:
        if s.count(c) > s.count(ch_first):
            ch_first = c

    return ch_first * s.count(ch_first) + s.replace(ch_first, '')

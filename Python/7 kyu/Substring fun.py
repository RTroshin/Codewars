def nth_char(words):
    res = ''
    i = 0

    for word in words:
        res += word[i]
        i += 1

    return res

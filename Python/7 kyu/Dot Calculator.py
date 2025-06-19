def calculator(txt):
    txt = txt.replace(' ', '')

    if '+' in txt:
        txt = txt.split('+')
        return txt[0] + txt[1]
    elif '-' in txt:
        txt = txt.split('-')
        return txt[0][len(txt[1]):]
    elif '*' in txt:
        txt = txt.split('*')
        return txt[0] * len(txt[1])
    elif "//" in txt:
        txt = txt.split("//")
        return txt[0][:len(txt[0]) // len(txt[1])]

def calculator(txt):
    if '+' in txt:
        txt = txt.replace(' ', '')
        txt = txt.split('+')
        return txt[0] + txt[1]
    elif '-' in txt:
        txt = txt.replace(' ', '')
        txt = txt.split('-')
        return txt[0][len(txt[1]):]
    elif '*' in txt:
        txt = txt.replace(' ', '')
        txt = txt.split('*')
        return txt[0] * len(txt[1])
    elif "//" in txt:
        txt = txt.replace(' ', '')
        txt = txt.split("//")
        return txt[0][:len(txt[0]) // len(txt[1])]

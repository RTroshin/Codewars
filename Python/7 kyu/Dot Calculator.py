def calculator(txt):
    if '+' in txt:
        txt = txt.replace(' ', '')
        txt = txt.split('+')
        return txt[0] + txt[1]

def capitals_first(text):
    res1 = []
    res2 = []
    text = text.split()

    for i in range(len(text)):
        if text[i][0].isupper():
            res1.append(text[i])
        if text[i][0].islower():
            res2.append(text[i])

    res = ' '.join(res1 + res2)

    return res

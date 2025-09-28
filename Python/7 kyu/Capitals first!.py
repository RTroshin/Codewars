def capitals_first(text):
    res1 = []
    res2 = []
    text = text.split()

    for i in range(len(text)):
        if text[i][0].isupper():
            res1.append(text[i])
        elif text[i][0].islower():
            res2.append(text[i])

    return ' '.join(res1 + res2)

def make_password(phrase):
    res = ''
    phrase = phrase.split()

    for i in range(len(phrase)):
        if phrase[i][0].lower() == 'i':
            res += '1'
        elif phrase[i][0].lower() == 'o':
            res += '0'
        elif phrase[i][0].lower() == 's':
            res += '5'
        else:
            res += phrase[i][0]

    return res

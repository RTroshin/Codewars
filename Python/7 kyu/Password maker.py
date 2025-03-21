def make_password(phrase):
    res = ''
    phrase = phrase.split()

    for word in phrase:
        if word[0].lower() == 'i':
            res += '1'
        elif word[0].lower() == 'o':
            res += '0'
        elif word[0].lower() == 's':
            res += '5'
        else:
            res += word[0]

    return res

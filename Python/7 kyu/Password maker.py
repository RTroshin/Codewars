def make_password(phrase):
    res = ''

    phrase = phrase.replace('i', '1')
    phrase = phrase.replace('I', '1')
    phrase = phrase.replace('o', '0')
    phrase = phrase.replace('O', '0')
    phrase = phrase.replace('s', '5')
    phrase = phrase.replace('S', '5')

    for word in phrase.split():
        res += word[0]

    return res

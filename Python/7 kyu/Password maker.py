def make_password(phrase):

    phrase = phrase.replace('i', '1')
    phrase = phrase.replace('I', '1')
    phrase = phrase.replace('o', '0')
    phrase = phrase.replace('O', '0')
    phrase = phrase.replace('s', '5')
    phrase = phrase.replace('S', '5')

    return ''.join(word[0] for word in phrase.split())

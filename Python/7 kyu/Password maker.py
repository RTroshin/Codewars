def make_password(phrase):

    phrase = phrase.replace('i', '1').replace('I', '1')
    phrase = phrase.replace('o', '0').replace('O', '0')
    phrase = phrase.replace('s', '5').replace('S', '5')

    return ''.join(word[0] for word in phrase.split())

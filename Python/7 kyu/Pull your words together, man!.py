def sentencify(words):
    words = ' '.join(words) + '.'
    return words[0].capitalize() + words[1:]

def sentencify(words):
    words = ' '.join(words) + '.'
    return f"{words[0].capitalize()}{words[1:]}"

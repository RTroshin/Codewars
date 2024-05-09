def sentencify(words):
    words = ' '.join(words)
    return f"{words[0].upper()}{words[1:]}."

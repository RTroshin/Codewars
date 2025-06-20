def capitals(word):
    return [word.index(ch) for ch in word if ch.isupper()]

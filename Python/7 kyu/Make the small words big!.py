def small_word_helper(sentence):
    res = []

    for word in sentence.split():
        res.append(''.join([ch.upper() for ch in word] if len(word) < 4 else [ch for ch in word if ch not in "aeiou"]))

    return ' '.join(res)

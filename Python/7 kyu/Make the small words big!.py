def small_word_helper(sentence):
    res = [''.join([ch.upper() for ch in word] if len(word) < 4 else [ch for ch in word if ch not in "aeiou"]) for word in sentence.split()]

    return ' '.join(res)

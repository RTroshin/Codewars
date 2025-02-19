def small_word_helper(sentence):
    return ' '.join([''.join([ch.upper() for ch in word] if len(word) < 4 else [ch for ch in word if ch not in "aeiou"]) for word in sentence.split()])

def small_word_helper(sentence):
    sentence = sentence.split()
    res = []

    for word in sentence:
        if len(word) < 4:
            res.append(''.join(ch.upper() for ch in word))
        else:
            res.append(''.join(ch for ch in word if ch not in "aeiou"))

    return ' '.join(res)

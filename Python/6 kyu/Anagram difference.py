def anagram_difference(w1, w2):
    res1, res2 = [], []
    for ch1 in set(w1):
        if ch1 in w2:
            res1 += [ch1]
    for ch2 in set(w2):
        if ch2 in w1:
            res2 += [ch2]
    return len(w1 + w2) - len(res1 + res2)

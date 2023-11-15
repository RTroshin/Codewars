def anagram_difference(w1, w2):
    res1, res2 = [], []
    for ch1 in w1:
        if ch1 in w2 and ch1 not in res1:
            res1 += [ch1]
    for ch2 in w2:
        if ch2 in w1 and ch2 not in res2:
            res2 += [ch2]
    return len(w1 + w2) - len(res1 + res2)

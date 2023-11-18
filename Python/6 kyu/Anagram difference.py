def anagram_difference(w1, w2):
    return len(w1 + w2) - len([ch for ch in set(w1) if ch in w2] + [ch for ch in set(w2) if ch in w1])

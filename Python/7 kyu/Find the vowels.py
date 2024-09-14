def vowel_indices(word):
    return [i + 1 for i, ch in enumerate(word) if ch.lower() in "aeiouy"]

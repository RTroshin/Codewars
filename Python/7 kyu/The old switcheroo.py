def vowel_2_index(s):
    res = [str(i + 1) if s[i].lower() in "aeiou" else s[i] for i in range(len(s))]

    return ''.join(res)

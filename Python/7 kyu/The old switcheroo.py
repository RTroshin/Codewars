def vowel_2_index(s):
    res = []

    for i in range(len(s)):
        res.append(str(i + 1) if s[i].lower() in "aeiou" else s[i])

    return ''.join(res)

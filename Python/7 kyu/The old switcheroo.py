def vowel_2_index(s):
    res = []

    for i in range(len(s)):
        if s[i].lower() in "aeiou":
            res.append(str(i + 1))
        else:
            res.append(s[i])

    return ''.join(res)

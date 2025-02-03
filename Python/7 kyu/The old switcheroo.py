def vowel_2_index(string):
    res = []

    for i in range(len(string)):
        if string[i].lower() in "aeiou":
            res.append(str(i + 1))
        else:
            res.append(string[i])

    return ''.join(res)

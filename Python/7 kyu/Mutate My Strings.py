def mutate_my_strings(s1, s2):
    res = [s1]

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            s1 = list(s1)
            s1[i] = s2[i]
            s1 = ''.join(s1)
            res.append(s1)

    return '\n'.join(res) + '\n'

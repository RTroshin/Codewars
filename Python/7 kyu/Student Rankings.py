def post_grades(students):
    res = []

    for s in students:
        s = s.split('-')
        s1, s2 = s[0].strip(), s[2].split()
        res.append([s1, sum([float(i) for i in s2]) / len(s2)])

    return res

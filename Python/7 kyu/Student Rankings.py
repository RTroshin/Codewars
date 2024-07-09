def post_grades(students):
    res = []

    for s in students:
        s = s.split('-')
        s1, s2 = s[0].strip(), s[2].split()
        res.append([s1, sum(float(i) for i in s2) / len(s2)])
    
    for i in range(len(res) - 1):
        for j in range(len(res) - 1):
            if res[j][1] < res[j + 1][1]:
                res[j][1], res[j + 1][1] = res[j + 1][1], res[j][1]

    return res

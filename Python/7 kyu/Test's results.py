def test(r):
    res = []
    dictionary = {}
    class_average = sum(r) / len(r)

    dictionary['h'] = r.count(9) + r.count(10)
    dictionary['a'] = r.count(7) + r.count(8)
    dictionary['l'] = r.count(1) + r.count(2) + r.count(3) + r.count(4) + r.count(5) + r.count(6)

    res.append(round(class_average, 3))
    res.append(dictionary)

    return res

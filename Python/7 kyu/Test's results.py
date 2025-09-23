def test(r):
    dictionary = {}

    dictionary['h'] = r.count(9) + r.count(10)
    dictionary['a'] = r.count(7) + r.count(8)
    dictionary['l'] = sum(r.count(i) for i in range(7))

    return [round(sum(r) / len(r), 3), dictionary]

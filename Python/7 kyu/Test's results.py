def test(r):
    dictionary = {}

    dictionary['h'] = r.count(9) + r.count(10)
    dictionary['a'] = r.count(7) + r.count(8)
    dictionary['l'] = r.count(1) + r.count(2) + r.count(3) + r.count(4) + r.count(5) + r.count(6)

    return [round(sum(r) / len(r), 3), dictionary]

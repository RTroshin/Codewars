def test(r):
    dictionary = {}

    dictionary['h'] = r.count(9) + r.count(10)
    dictionary['a'] = r.count(7) + r.count(8)
    dictionary['l'] = sum(r.count(i) for i in range(7))
    
    if dictionary['a'] == 0 and dictionary['l'] == 0:
        return [round(sum(r) / len(r), 3), dictionary, "They did well"]

    return [round(sum(r) / len(r), 3), dictionary]

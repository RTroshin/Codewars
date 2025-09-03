def reverse_it(data):
    if type(data) == str or type(data) == list:
        return data[::-1]
    elif type(data) == int:
        return int(str(data)[::-1])

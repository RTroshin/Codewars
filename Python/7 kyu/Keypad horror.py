def computer_to_phone(numbers):
    res = ''

    for n in list(numbers):
        if n == '1':
            res += '7'
        elif n == '2':
            res += '8'
        elif n == '3':
            res += '9'
        elif n == '7':
            res += '1'
        elif n == '8':
            res += '2'
        elif n == '9':
            res += '3'
        else:
            res += n

    return res

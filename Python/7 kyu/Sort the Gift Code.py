def sort_gift_code(code):
    code = list(code)

    for i in range(len(code) - 1):
        for j in range(len(code) - 1):
            if ord(code[j]) > ord(code[j + 1]):
                code[j], code[j + 1] = code[j + 1], code[j]

    return ''.join(code)

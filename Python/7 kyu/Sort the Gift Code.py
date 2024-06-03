def sort_gift_code(code):
    code = [ord(ch) for ch in code]
    code.sort()
    code = [chr(ch) for ch in code]

    return ''.join(code)

def sort_gift_code(code):
    code = [ord(ch) for ch in code]
    code.sort()
    return ''.join([chr(ch) for ch in code])

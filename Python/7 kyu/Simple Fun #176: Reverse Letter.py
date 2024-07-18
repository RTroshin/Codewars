def reverse_letter(str):
    return ''.join(ch for ch in str if ch.isalpha())[::-1]

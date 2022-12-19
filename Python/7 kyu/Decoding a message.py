def decode(message):
    return ''.join(chr(219 - ord(ch)) if ch is not ' ' else ' ' for ch in message)

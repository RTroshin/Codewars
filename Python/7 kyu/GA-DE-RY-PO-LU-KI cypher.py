def encode(message):
    return ''.join({'G': 'A', 'D': 'E', 'R': 'Y', 'P': 'O', 'L': 'U', 'K': 'I',
                    'g': 'a', 'd': 'e', 'r': 'y', 'p': 'o', 'l': 'u', 'k': 'i'}.get(ch) if ch.upper() in "GDRPLK" else ch for ch in message)

def decode(message):
    return ''.join({'A': 'G', 'E': 'D', 'Y': 'R', 'O': 'P', 'U': 'L', 'I': 'K',
                    'a': 'g', 'e': 'd', 'y': 'r', 'o': 'p', 'u': 'l', 'i': 'k'}.get(ch) if ch.upper() in "AEYOUI" else ch for ch in message)

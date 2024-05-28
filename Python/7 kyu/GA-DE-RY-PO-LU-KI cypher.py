cyphDict = {'G': 'A', 'D': 'E', 'R': 'Y', 'P': 'O', 'L': 'U', 'K': 'I',
            'g': 'a', 'd': 'e', 'r': 'y', 'p': 'o', 'l': 'u', 'k': 'i',
            'A': 'G', 'E': 'D', 'Y': 'R', 'O': 'P', 'U': 'L', 'I': 'K',
            'a': 'g', 'e': 'd', 'y': 'r', 'o': 'p', 'u': 'l', 'i': 'k'}

def encode(message):
    return ''.join(cyphDict.get(ch, ch)for ch in message)

def decode(message):
    return ''.join(cyphDict.get(ch, ch)for ch in message)

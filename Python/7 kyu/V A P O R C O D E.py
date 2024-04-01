def vaporcode(s):
    return "  ".join(ch.upper() for ch in s if ch != ' ')

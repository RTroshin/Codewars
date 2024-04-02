def vaporcode(str):
    return "  ".join(ch.upper() for ch in str if ch != ' ')

def duplicate_count(text):
    text = text.lower()
    return len([ch for ch in set(text) if text.count(ch) > 1])

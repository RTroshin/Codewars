def duplicate_count(text):
    text = text.lower()
    return len({char: text.count(char) for char in text if text.count(char) > 1})

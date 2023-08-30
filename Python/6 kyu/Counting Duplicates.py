def duplicate_count(text):
    return len([ch for ch in set(text.lower()) if text.lower().count(ch) > 1])

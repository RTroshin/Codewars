def count_consonants(text):
    count = 0
    text = text.lower()
    
    for ch in text:
        if not ch in "aeiou":
            count += 1

    return count

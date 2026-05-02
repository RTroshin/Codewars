def count_consonants(text):
    count = 0
    text = text.lower()
    
    for i in range(len(text)):
        if not text[i] in "aeiou":
            count += 1

    return count

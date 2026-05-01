def count_consonants(text):
    count = 0
    
    for i in range(len(text)):
        if not text[i] in "aeiou":
            count += 1

    return count

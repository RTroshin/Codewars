ingredients = {'a': "beef", 'e': "beef",  'i': "beef", 'o': "beef", 'u': "beef", 't': "tomato", 'l': "lettuce", 'c': "cheese", 'g': "guacamole", 's': "salsa"}

def tacofy(word):
    word = word.lower()
    return ["shell"] + [ingredients.get(ch) for ch in word if ch in "aeioutlcgs"] + ["shell"]
